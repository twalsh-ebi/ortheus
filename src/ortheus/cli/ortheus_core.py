#!/usr/bin/env python3

#Copyright (C) 2008-2011 by Benedict Paten (benedictpaten@gmail.com)
#
#Released under the MIT license, see LICENSE.txt

from importlib.resources import files
import subprocess
import sys


def main():
    args = sys.argv[1:]
    ortheusCore = files("ortheus.bin").joinpath("ortheus_core")
    cmdArgs = [str(ortheusCore)] + args
    process = subprocess.run(cmdArgs)
    return process.returncode


if __name__ == "__main__":
    sys.exit(main())
