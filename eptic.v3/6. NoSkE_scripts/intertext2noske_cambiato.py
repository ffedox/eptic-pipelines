#!/usr/bin/python
#
# Initial version March 8, 2021
#
# Latest version March 12, 2021
#
# This scripts converts an InterText alignment file into an alignment file usable by NoSketchEngine.
#
# The script reads an InterText alignment file (which tipically contains sentence IDs in the form of strings) and
# finds the corresponding numeric IDs assigned to the sentences by NoSke/Manatee.
#
# A typical line in an InterText alignment file looks like this:
#
# <link type='1-1' xtargets='agr000_it_1;agr000_de_1' status='man'/>
#
# The assumption is that each "sentence" is NoSke is contained in a structural attribute named "s" that
# has a string ID, the NoSke vertical file should look like this:
#
# <s id="agr000_it_1">
# Accordo NOUN    accordo-n
# sullo   ARTPRE  sul-x
# statuto NOUN    statuto-n
# giuridico       ADJ     giuridico-j
# in      PRE     in-i
# Svizzera        NPR     Svizzera-n
# della   ARTPRE  della-x
# Banca   NPR     Banca-n
# Europea NPR     Europea-n
# d'      PRE     da|di-i
# <g/>
# Investimento    NPR     Investimento-n
# </s>

import argparse, fileinput, manatee, os, re, sys
from os import path

sys.settrace

# define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("corpus_from", help="the NoSKE name of the corpus corresponding to the 'fromDoc' corpus in the Intertext alignment file")
parser.add_argument("corpus_to", help="the NoSKE name of the corpus corresponding to the 'toDoc' corpus in the Intertext alignment file")
parser.add_argument("alignment_file", help="the Intertext alignment file")
args = parser.parse_args()

# initialize a few things
criticalError = False
version = 1.0

# process arguments
corpusFromName = args.corpus_from
corpusToName = args.corpus_to
alignmentFilename = args.alignment_file

# access corpus on manatee, if corpora do not exist, complain and exit
try:
	corpusFrom = manatee.Corpus(corpusFromName)
except:
	sys.stderr.write("Critical error: corpus '" + corpusFromName + "' not found in manatee\n")
	exit()

try:
	corpusTo = manatee.Corpus(corpusToName)
except:
	sys.stderr.write("Critical error: corpus '" + corpusToName + "' not found in manatee\n")
	exit()

# check if alignment file exists
if path.exists(alignmentFilename) == False:
	sys.stderr.write("Critical error: alignment file '" + alignmentFilename + "' not found\n")
	exit()
    
    
corpusFromName = os.path.basename(args.corpus_from)
corpusToName = os.path.basename(args.corpus_to)

# check if output files already exist
outputFileName = corpusFromName + "-" + corpusToName + "-ids.txt"
revOutputFileName = corpusToName + "-" + corpusFromName + "-ids.txt"

if path.exists(outputFileName):
	sys.stderr.write("Output file '" + outputFileName + "' already exists\n")
	exit()

if path.exists(revOutputFileName):
	sys.stderr.write("Reverse output file '" + revOutputFileName + "' already exists\n")
	exit()

# create output files
try:
	outputFile = open(outputFileName, "w")
	revOutputFile = open(revOutputFileName, "w")

except IOError:
	sys.stderr.write("Unable to create output files\n")
	exit()

# count the number of "s" structures i.e. sentences both corpora
sFrom = corpusFrom.get_struct("s")
sentenceCount1 = sFrom.size()

sTo = corpusTo.get_struct("s")
sentenceCount2 = sTo.size()

# define PosAttr, it's an object containing all the id elements in the "s" structure
idFrom = sFrom.get_attr("id")
idTo = sTo.get_attr("id")

# cycle through all sentences in corpusFrom and create a dictionary containing pairs of string ID => numeric ID
corpusFromIndex = {}
numidFrom=0
while numidFrom < sentenceCount1:
	corpusFromIndex[idFrom.id2str(numidFrom)] = numidFrom
	numidFrom=numidFrom+1

# cycle through all sentences in corpusFrom and create a dictionary containing pairs of string ID => numeric ID
corpusToIndex = {}
numidTo=0
while numidTo < sentenceCount2:
	corpusToIndex[idTo.id2str(numidTo)] = numidTo
	numidTo=numidTo+1

# define regex only once for efficiency. Also, we're naming the capture group
# (i.e. the backreference) 'xtargets', so we can easily access it later
regex = re.compile("<link type='.*' xtargets='(?P<xtargets>.*)' status='.*'/>")

# count lines in alignment file
lineCount = 0

# parse alignment file
for line in fileinput.input(alignmentFilename):
	# increment lineCount
	lineCount = lineCount + 1

	# find the xtargets in the line
	result = re.match(regex, line)
	print(result)

	# if a match is found (i.e. this is not the beginning or the end of the XML file)
	if result != None:
		xtargets = result.group('xtargets')

		# separate IDs of corpusFrom from IDs of corpusTo
		elements = xtargets.split(";")

		# if both elements are empty skip the line and print warning to console
		if elements[0] == '' and elements[1] == '':
			sys.stderr.write("Warning: empty alignment in line " + str(lineCount) + ", skipping it\n")
			continue

		idsTo = elements[0].split(" ")
		idsFrom = elements[1].split(" ")

		outputTo = "";
		outputFrom = "";

		# look for the numeric IDs of the stringIDs we extracted in the corpus index
		# if the segment is empty, insert -1
		if idsTo[0] == '':
			outputTo = str(-1)

		# if first and last element of the list are different (i.e. there's more than one element),
		# then it's a range, so first and last elements separated by a comma
		elif idsTo[0] != idsTo[-1]:

			# check if ID is in index before trying to access it
			skip = False
			for checkId in idsTo:
				# if string id is not in the dictionary, something's wrong with the alignment file or the corpus;
				# this is a critical error, print an error message but keep going: if there are more errors, the
				# script will find and report them all
				if corpusToIndex.get(checkId) is None:
					sys.stderr.write("Critical error: ID '" + checkId + "' does not exist in corpus '" + corpusToName + "'\n")
					skip = True
					criticalError = True

			if skip:
				continue

			outputTo = str(corpusToIndex[idsTo[0]]) + "," + str(corpusToIndex[idsTo[-1]])

		#  if there's only one element, then just print it
		else:
			outputTo = str(corpusToIndex[idsTo[0]])

		#  repeat the process for the other corpus
		if idsFrom[0] == '':
			outputFrom = str(-1)

		elif idsFrom[0] != idsFrom[-1]:

			# check if ID is in index before trying to access it
			skip = False
			for checkId in idsFrom:
				# if string id is not in the dictionary, something's wrong with the alignment file or the corpus;
				# this is a critical error, print an error message but keep going: if there are more errors, the
				# script will find and report them all
				if corpusFromIndex.get(checkId) is None:
					sys.stderr.write("Critical error: ID '" + checkId + "' does not exist in corpus '" + corpusFromName + "'\n")
					skip = True
					criticalError = True

			if skip:
				continue

			outputFrom = str(corpusFromIndex[idsFrom[0]]) + "," + str(corpusFromIndex[idsFrom[-1]])

		else:
			outputFrom = str(corpusFromIndex[idsFrom[0]])

		# write to output files
		outputFile.write(outputFrom + "\t" + outputTo + "\n")
		revOutputFile.write(outputTo + "\t" + outputFrom + "\n")

outputFile.close()
revOutputFile.close()

if criticalError == False:
	# if the script completed without errors, print a reassuring message
	sys.stdout.write("Two output files have been created: \n")
	sys.stdout.write(outputFileName + "\n")
	sys.stdout.write(revOutputFileName + "\n")

else:
	# if a critical error occurred, delete output files and issue a warning
	os.remove(outputFileName)
	os.remove(revOutputFileName)
	sys.stderr.write("Critical errors where encountered, please fix input files and/or corpora\n")

