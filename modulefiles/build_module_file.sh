#!/bin/bash

#This script can be used to create a modulefile to setup the PYTHONPATH enviornment variable to run the deck dode
#It should be used from the base DeckSelector directory
#In addition to calling this script the "modulefiles" directory in the git repo needs to be added to your
#environment's MODULEPATH variable
#
TEXT="#%Module1.0\n## anaconda switch\n##\nproc ModulesHelp { } {\nputs stderr \"	This module switches to CK2Building setup\"\n}\n\nmodule-whatis   \"Add DeckSelector to PYTHONPATH\"\n\nprepend-path PYTHONPATH "
echo -e $TEXT `pwd` > modulefiles/deck
echo prepend-path PYTHONPATH `pwd`/UnitTestHelper >> modulefiles/deck
echo modulefile deck created in `pwd`/modulefiles
echo To use this export MODULEPATH=${MODULEPATH}:`pwd`/modulefiles