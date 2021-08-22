#! /usr/bin/python3

"""Replace the real "cum_confirmed_cases" data in a CSV with pure
exponential growth. For each "adm1_name", this finds the first and
last non-empty non-zero entry and replaces the series with exponential
growth that interpolates from the first to the last value.

The purpose is to test whether the method of estimating the impact of
NPI will erroneously find impact when there is none. This erroroneous
impact comes from the use of cumulative confirmed cases instead of
daily confirmed cases to estimate the growth rate.
"""
import argparse
import csv
import datetime
import logging
import math
import sys

from collections import defaultdict

import numpy

#logging.getLogger().setLevel(logging.INFO)

CASES = 'cum_confirmed_cases'
CASES_ORIGINAL = CASES + "_original"


def FindFirstLast(entries):
  """Returns the indices of the first and last non-empty, non-zero rows"""
  first = None
  for i, entry in enumerate(entries):
    if entry[CASES] and float(entry[CASES]) > 0:
      if first is None:
        first = i
      last = i
  return first, last


class Interpolator(object):
  def CumCases(self, day):
    raise NotImplemented()


class ConstantInterpolator(Interpolator):
  def __init__(self, cases):
    self.cases = cases

  def CumCases(self, day):
    return self.cases


class ExponentialInterpolator(Interpolator):
  """Interpolate from first_cases to last_cases using an exponential."""
  def __init__(self, first_cases, last_cases, total_days):
    self.first_cases = first_cases
    self.last_cases = last_cases
    self.total_days = total_days
    self.daily_diff = (math.log(last_cases) - math.log(first_cases)) / total_days

  def CumCases(self, day):
    return math.exp(math.log(self.first_cases) + self.daily_diff * day)


class GeometricInterpolator(Interpolator):
  """Interpolate from first_cases to last_cases using geometric series."""
  def __init__(self, first_cases, last_cases, total_days):
    self.first_cases = first_cases
    self.last_cases = last_cases
    self.total_days = total_days
    logging.info(f"{first_cases}->{last_cases}")
    self.r = self.SolveR()

  def SolveR(self):
    """Solves the polynomial equation (sum(first*r^i)) = last."""
    cum = numpy.poly1d([self.first_cases] * (self.total_days+1))
    p = cum - numpy.poly1d([self.last_cases])
    logging.info(f"Solving\n{p}")
    r, = [r for r in p.roots if not numpy.iscomplex(r) and r.real > 0]
    return r.real

  def CumCases(self, day):
    return self.first_cases * (self.r**(day+1) - 1)/(self.r-1)


def SimulateData(entries, adm_field, cumulative):
  out = []
  for entry in entries:
    entry[CASES_ORIGINAL] = entry[CASES]
  first_index, last_index = FindFirstLast(entries)
  if first_index is None:
    logging.info(f"Skipping {entry[adm1_field]}")
    return entries

  first = entries[first_index]
  first_date = datetime.date.fromisoformat(first['date'])
  first_cases = float(first[CASES])

  last = entries[last_index]
  last_date = datetime.date.fromisoformat(last['date'])
  last_cases = float(last[CASES])

  total_days = (last_date - first_date).days
  if first_cases == last_cases:
    interpolator = ConstantInterpolator(first_cases)
  else:
    interpolator = GeometricInterpolator(first_cases, last_cases, total_days)
    # interpolator = ExponentialInterpolator(first_cases, last_cases, total_days)
  out.extend(entries[0:first_index])
  for entry in entries[first_index:last_index+1]:
    date = datetime.date.fromisoformat(entry['date'])
    index_day = (date-first_date).days
    cases = interpolator.CumCases(index_day)
    if not cumulative:
      if index_day == first_index:
        last_cases = 0
      else:
        last_cases = interpolator.CumCases(index_day - 1)
      cases -= last_cases
    entry[CASES] = str(int(math.floor(cases+.5)))
    logging.info(f"diff {entry[CASES]} {entry[CASES_ORIGINAL]}")
    out.append(entry)

  out.extend(entries[last_index + 1:])

  return out


def Process(entries, adm_field, cumulative):
  adms = defaultdict(lambda: [])
  names = []
  for entry in entries:
    name = entry[adm_field]
    adms[name].append(entry)
    if name not in names:
      names.append(name)
  simulated = []
  for name in names:
    logging.info(f"doing {name}")
    simulated.extend(SimulateData(adms[name], adm_field, cumulative))

  return simulated


def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('--cases', type=str, choices=('cumulative', 'daily'),
                      default='cumulative',
                      help='Output cumulative cases')
  parser.add_argument('in_fn', type=str, nargs=1)
  args = parser.parse_args()

  in_fn, = args.in_fn
  adm_field = "adm1_name" if "adm1" in in_fn else "adm2_name"
  with open(in_fn) as csvfile:
    entries = csv.DictReader(csvfile)
    simulated = Process(entries, adm_field, args.cases == 'cumulative')
    fieldnames = list(entries.fieldnames)
    fieldnames.insert(fieldnames.index(CASES) + 1, CASES_ORIGINAL)
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames,
                            lineterminator="\n")
    writer.writeheader()
    writer.writerows(simulated)

if __name__ == '__main__':
  main(sys.argv)
