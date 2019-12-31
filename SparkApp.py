#!/usr/bin/python
  
###############################################################################
# Name       : SparkApp.py
# Usage      : ./SparkApp.py --infile /SomePath/SomeFile
# Author     : Stuart Pineo <svpineo@gmail.com>
# Description: Filter/aggregate lines using PySpark
#
##############################################################################

import sys
import time

import os.path
from os import path

import argparse

from string import ascii_lowercase


# Add the long and short argument
#
parser = argparse.ArgumentParser()
parser.add_argument("--infile", "-i", help="Set the input file (i.e., log file)")

args = parser.parse_args()

inFile = args.infile

if not (inFile and os.path.isfile(inFile)):
    print("The input file parameter --infile or -i must be defined and file must exist.")
    sys.exit(1)

from pyspark.sql import SparkSession

spark  = SparkSession.builder.appName("SimpleApp").getOrCreate()
inData = spark.read.text(inFile).cache()

for char in ascii_lowercase:
    count = inData.filter(inData.value.contains(char)).count()
    print("Number of lines with the character '%s': %i" % (char, count))

time.sleep(5)

spark.stop()
