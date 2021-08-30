#! /usr/bin/python3
"""Extracts the reghdfe sections from the output logs as markdown."""

import re
import sys


def ExtractReghdfes(lines):
  section = []
  in_section = False
  for line in lines:
    # Stata logs every command as ". some_command" so lines that start with
    # ". " indicate a new section. Close off the old section.
    if in_section and re.search("^\. ", line):
      yield section
      section = []
      in_section = False

    # We only want the reghdfe outputs.
    if re.search("^\. reghdfe", line):
      in_section = True

    if in_section:
      section.append(line)


def main(argv):
  for fn in argv[1:]:
    print(f"# {fn}\n")

    for section in ExtractReghdfes(open(fn)):
      print("```")
      for line in section:
        sys.stdout.write(line)
      print("```")


if __name__ == '__main__':
  main(sys.argv)
