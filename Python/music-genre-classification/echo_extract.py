import sys, os
import pandas as pd
import re
import csv

# Regular expression patterns for EF
########## patterns #############
pattern = "(((LV)?EF)|(([Ll]eft(\s+)[Vv]entricular\s+)?([Ee]jection\s+[Ff]raction)))\s*:*\s*\w*\s*(\d{1,2}/\d{1,2}/\d{2,4})?\W*(\w*\s*){0,4}\W?\s?(between|than)?((\d\d%?(-|(\s?and\s?)|(\s?to\s?))\d\d\s*(\W?\w*\s*\w*\s*\W?\s*)?%)|(\d\d(.\d)?\s*(\W?\w*\s*\w*\s*\W?)?(%|percent)))"
pattern0 = "(((\d\d-\d\d%)|(\d\d\s*%))\s?(((LV)?EF)|(([Ll]eft(\s+)[Vv]entricular\s+)?([Ee]jection\s+[Ff]raction))))"
pattern1 = "(((((mildly|moderately|severely)\s)?reduced|retained|preserved|dropped|decreased|[Ll]ow)|(([L|l]ow)\s)?([n|N]ormal)))\s((((LV)?EF))|(([Ll]eft(\s+)[Vv]entricular\s+)?([Ee]jection\s+[Ff]raction)))"
pattern2 = "(?<![Ii]f)\s*\w*\s*(((LV)?EF)|(([Ll]eft(\s+)[Vv]entricular\s+)?([Ee]jection\s+[Ff]raction)))\s(\w+\s){0,3}(mildly|(moderately)|(severely)|(low))?(reduced|retained|preserved|dropped|decreased|normal)"

pattern_g = '(gallbladder)\s(ejection)\s(fraction)'
pattern_r = 'FEF'
pattern_sf = '((((L|l)eft)\s(ventricular))|(LV))\s*(systolic)\s*(function)\s*\w*\s*(low\s)?(normal)'
pattern_sf1= '(The)\s(left)\s(ventricle)\s(is)\s(normal)\s(in)\s(structure,)\s(function)\s(and)\s(size)'
pattern_sf2 = '((L|l)ow\s)?((n|N)ormal)\s(left)\s(ventricular)\s(systolic)\s(function)'
 
regex_g = 
re.compile(pattern_g, re.IGNORECASE)
regexp = re.compile(pattern)
regexp0 = re.compile(pattern0)
regexp1 = re.compile(pattern1)
regexp2 = re.compile(pattern2)
regexp_r = re.compile(pattern_r)
regexp_sf = re.compile(pattern_sf)
regexp_sf1 = re.compile(pattern_sf1)
regexp_sf2 = re.compile(pattern_sf2)
regexp_value = re.compile("((\d\d%?(-|(\s?and\s?)|(\s?to\s?))\d\d\s*(\W?\w*\s*\w*\s*\W?)?%)|(\d\d(.\d)?\s*(\W?\w*\s*\w*\s*\W?)?(%|percent)))")
regexp_qtt = re.compile("(((((mildly)|(moderately)|(severely)\s)?reduced|retained|preserved|[Ll]ow)|(([L|l]ow)\s)?([n|N]ormal)))|(mildly|(low))?(reduced|retained|preserved|dropped|decreased|normal)")

# Initialize values
count = count_n = count_v = count_ v0 = count_q = count_sf = 0
echo=[]
pt=[]
sv=[]
od=[]
dt=[]

# Supporting functions
def append_echo(cond, regexp):
    group = cond.group()
    value = regexp.search(group)
    echo.append(value.group())

def append_info(row):
    pt.append(row['PATIENT_ID'])
    sv.append(row['SERVICE_ID'])
    od.append(row['ORDER_RESULT_ID'])
    dt.append(row['RESULT_DATETIME'])

# Main function
if __name__ == "__main__":

	# Get to file directory
	file_dir = sys.argv[1]
	os.chdir(file_dir)
	# Check current working directory
	retval = os.getcwd()
	print("Current working directory is %s" % retval)
