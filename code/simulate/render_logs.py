#! /usr/bin/python3
"""Extracts the reghdfe sections from the output logs as markdown."""

import re
import sys


def main(argv):
  for fn in argv[1:]:
    print(f"# {fn}\n")

    in_section = False
    for line in open(fn):
      # Stata logs every command as ". some_command" so lines that start with
      # ". " indicate a new section. Close off the old section.
      if in_section and re.search("^\. ", line):
        print("```")
        in_section = False

      # We only want the reghdfe outputs.
      if re.search("^\. reghdfe", line):
        print("```")
        in_section = True

      if in_section:
        sys.stdout.write(line)


if __name__ == '__main__':
  main(sys.argv)
