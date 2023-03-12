import sys

from src.formatting import formatting, DEFAULT_FORMAT_RULES
from src.report import make_report
from src.parsing import DefaultParser
from src.validation import DefaultValidator
from src.ping import DefaultPinger

def main():
    path = sys.argv[1]
    with open(path) as file:
        report = make_report(
                    file,
                    DefaultParser(DefaultValidator()),
                    DefaultPinger()
                )
        for line in formatting(report, DEFAULT_FORMAT_RULES):
            print(line)

