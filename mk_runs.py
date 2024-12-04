#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-5"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["C1"] = [ 112346, 112347, 112348, 112350, 112351, 112352,
             121810, 121811, 121812, 121816, 121817, 121818,]

on["C2"] = [ 112356, 112357, 112358, 112360, 112361, 112362,
             112366, 112367, 112368,
             121821, 121822, 121823,]

on["C3"] = [ 114083, 114084, 114085, 114087, 114088, 114089, 114091,
             114092, 114093, 114097, 114098, 114099, 114101, 114102,]

on["C5"] = [ 114408, 114409, 114410, 114412, 114413, 114414, 114416,
             114417, 114418, 114423, 114424, 114425,]

on["C6"] = [ 116614, 116615, 116616, 116724, 116725, 116726, 116728,
             116729, 116730, 117820, 117821, 117822, 117826, 117827, 117828,]

on["C7"] = [ 116627, 116628, 116629, 116733, 116734, 116735, 116737,
             116738, 116739, 117815, 117816, 117817,
             122191, 122192, 122193,]

on["C11"] = [-122196,-122197,-122198,-122200,-122201,-122202,
             -122406,-122407,-122408, 
             -123956,-123957,-123958,-123960,-123961,-123962,-123964,-123965,-123966,
              124239, 124240, 124241, 124243, 124244, 124245, 124247, 124248, 124249,]

on["HI3"] = [ 112586, 112587, 112588, 112590, 112591, 112592, 112595,
              112596, 112597, 114080, 114180, 114181, 114182,]

on["HI4"] = [ 114185, 114186, 114188, 114189, 114268, 114269, 114270,
              114273, 114274, 114275, 114278, 114279, 114280, 114282,
              114283, 114284, 114286, 114287, 114288, 114292, 114293,
              114294, 114296, 114297, 114298, 114399, 114400, 114401,
              114403, 114404, 114405,]

on["HI7"] = [ 123971, 123972, 123973, 123975, 123976, 123977,]

on["HI8"] = [ 114507, 114508, 114509, 114511, 114512, 114513, 114515,
              114516, 114517, 114521, 114522, 114523, 114525,]

on["HI9"] = [ 122207, 122208, 122209,
             -123694,-123695, 123696, 123698, 123699, 123700, 123702, 123703, 123704, 123706, 123707, 123708,]   # Nov 28


pars1 = {}

pars1["C1"] = "badcb=3/0"
pars1["C2"] = "badcb=1/2"
pars1["C3"] = ""
pars1["C5"] = ""
pars1["C6"] = ""
pars1["C7"] = ""
pars1["C11"] = "badcb=1/1,3/5 shortlags=32,10"
pars1["HI3"] = ""
pars1["HI4"] = ""
pars1["HI7"] = ""
pars1["HI8"] = ""
pars1["HI9"] = ""

# parameters for the (optional) second pass of the pipeline (e.g. for bank=0)
pars2 = {}

pars2["C1"] = ""
pars2["C2"] = ""
pars2["C3"] = ""
pars2["C5"] = ""
pars2["C6"] = ""
pars2["C7"] = ""
pars2["C11"] = ""
pars2["HI3"] = ""
pars2["HI4"] = ""
pars2["HI7"] = ""
pars2["HI8"] = ""
pars2["HI9"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
