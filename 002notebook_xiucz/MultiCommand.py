#!/bin/env python
import sys, os
from subprocess import call
from multiprocessing import Process, Pool

__author__  = "Deng Junhao (ruocheng_huang@shbiochip.com)"
__version__ = "v0.1.0, 2016/10/20"

USAGE = """
    PYTHON MultCommand.py
    author: %s
    version: %s
    description: run commands in multi-process

    usage: python MultiCommand.py <CMDfile> <Number_Process>

    argument descriptions:
    CMDfile: command line file
    CMDfile example:
    sh 1.sh
    sh 2.sh > a
    sh 3.sh > b
    python 1.py xx
    ....
    Number_Process: the number of multi-process
""" % ( __author__, __version__ )

def runfun(cmd):
    call(cmd, shell = True)

def Multifun(cmdfile, number_process = 8):
    pool = Pool(processes = number_process)
    f = open(cmdfile, 'r')
    for cmdline in f:
        cmd = cmdline.strip()
        result = pool.apply_async(runfun, (cmd, ))
    f.close()
    pool.close()
    pool.join()

if __name__ == "__main__":

    if len(sys.argv) != 3:
        exit(USAGE)

    cmdfile = sys.argv[1]
    number_process = int( sys.argv[2] )

    Multifun(cmdfile, number_process)


