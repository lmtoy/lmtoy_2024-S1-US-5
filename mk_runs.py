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

on["HI3"] = [ 112586, 112587, 112588, 112590, 112591, 112592,
        112595, 112596, 112597,]

# parameters for the first pass of the pipeline
pars1 = {}

pars1["C1"] = "badcb=3/0"
pars1["C2"] = "badcb=1/2"
pars1["HI3"] = ""

# parameters for the (optional) second pass of the pipeline
pars2 = {}

pars2["C1"] = ""
pars2["C2"] = ""
pars2["HI3"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
