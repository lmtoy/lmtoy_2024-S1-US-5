#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-5"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["C1"] = [ 112346, 112347, 112348, 112350, 112351, 112352,]

on["C2"] = [ 112356, 112357, 112358, 112360, 112361, 112362,
             112366, 112367, 112368,]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["C1"] = ""
pars1["C2"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["C1"] = ""
pars2["C2"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
