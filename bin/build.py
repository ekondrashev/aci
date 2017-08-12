#!/usr/bin/env python3

import argparse
import json

import io
import logging

import ci

arguments = argparse.ArgumentParser()
arguments.add_argument("-b", "--build-log", default='/tmp/aci/build')

arguments.add_argument("-v", "--verbose", help="increase output verbosity",
                       action="store_true", default=True)


def main(args):
    config = json.loads(io.open(args.config, 'r').read())
    platforms = ci.Platforms.from_json(config['platforms'])


if __name__ == '__main__':
    args = arguments.parse_args()
    if args.verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(
#         filename=args.log,
        format="%(asctime)s %(levelname)s:%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=level
    )
    main(args)

