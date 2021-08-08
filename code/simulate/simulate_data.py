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
    self.r = self.SolveR()

  def SolveR(self):
    """Solves the polynomial equation (sum(first*r^i)) = last."""
    cum = numpy.poly1d([self.first_cases] * (self.total_days+1))
    p = cum - numpy.poly1d([self.last_cases])
    r, = [r for r in p.roots if not numpy.iscomplex(r) and r.real > 0]
    return r.real

  def CumCases(self, day):
    return self.first_cases * (self.r**(day+1) - 1)/(self.r-1)


def SimulateData(entries):
  out = []
  for entry in entries:
    entry[CASES_ORIGINAL] = entry[CASES]
  first_index, last_index = FindFirstLast(entries)
  if first_index is None:
    logging.info(f"Skipping {entry['adm1_name']}")
    return entries

  first = entries[first_index]
  first_date = datetime.date.fromisoformat(first['date'])
  first_cases = float(first[CASES])

  last = entries[last_index]
  last_date = datetime.date.fromisoformat(last['date'])
  last_cases = float(last[CASES])

  total_days = (last_date - first_date).days
  interpolator = GeometricInterpolator(first_cases, last_cases, total_days)
#  interpolator = ExponentialInterpolator(first_cases, last_cases, total_days)
  out.extend(entries[0:first_index])
  for entry in entries[first_index:last_index+1]:
    date = datetime.date.fromisoformat(entry['date'])
    index_day = (date-first_date).days
    cases = interpolator.CumCases(index_day)
    entry[CASES] = str(int(math.floor(cases+.5)))
    logging.info(f"diff {entry[CASES]} {entry[CASES_ORIGINAL]}")
    out.append(entry)

  out.extend(entries[last_index + 1:])

  return out


def Process(entries):
  adm1s = defaultdict(lambda: [])
  names = []
  for entry in entries:
    name = entry['adm1_name']
    adm1s[name].append(entry)
    if name not in names:
      names.append(name)
  simulated = []
  for name in names:
    logging.info(f"doing {name}")
    simulated.extend(SimulateData(adm1s[name]))

  return simulated


def main(argv):
  if len(argv) > 2:
    raise ValueError('Too many command-line arguments.')

  in_fn = argv[1]
  with open(in_fn) as csvfile:
    entries = csv.DictReader(csvfile)
    simulated = Process(entries)
    fieldnames = list(entries.fieldnames)
    fieldnames.insert(fieldnames.index(CASES) + 1, CASES_ORIGINAL)
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames,
                            lineterminator="\n")
    writer.writeheader()
    writer.writerows(simulated)

if __name__ == '__main__':
  main(sys.argv)
