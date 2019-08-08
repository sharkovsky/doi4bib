# -*- coding: utf-8 -*-
"""
Contains the entry point to the utility
"""

import argparse
import sys
import logging
import biblib.bib
from . import bibparser

from doi4bib import __version__

__author__ = "sharkovsky"
__copyright__ = "sharkovsky"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """

    ARG_HELP_STRINGS = {
      "bib_file": "path to .bib file",
      "out_file": "path to output file (default: out.bib)",
      "desc"    : "Utility to copy a bib file and add doi references where missing.\
out_file is a copy of bib_file, with additional DOI references added whenever possible."
    }

    parser = argparse.ArgumentParser(
        description=ARG_HELP_STRINGS["desc"])
    parser.add_argument(
        "bib_file",
        help=ARG_HELP_STRINGS["bib_file"])
    parser.add_argument(
        "-o",
        "--out-file",
        help=ARG_HELP_STRINGS["out_file"],
        default="out.bib")
    parser.add_argument(
        "--version",
        action="version",
        version="doi4bib {ver}".format(ver=__version__))
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug('Starting now')
    with open(args.bib_file) as f:
        db = biblib.bib.Parser().parse(f).get_entries()

    db = bibparser.add_dois_to_bib(db, _logger)

    with open(args.out_file, 'w') as f:
        for entry in db.values():
            f.write(entry.to_bib() + '\n')

    _logger.info('Finished')

def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
