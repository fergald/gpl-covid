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
  daily_diff = (math.log(last_cases) - math.log(first_cases)) / total_days
  out.extend(entries[0:first_index])
  for entry in entries[first_index:last_index+1]:
    date = datetime.date.fromisoformat(entry['date'])
    index_day = (last_date - date).days
    cases = math.exp(
      math.log(last_cases) -
      daily_diff * index_day)
    entry[CASES] = str(int(cases))
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
