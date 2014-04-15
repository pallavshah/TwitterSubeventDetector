#! /bin/bash
if [ $# -ne 2 ]; then
	echo "format: bash build.sh <input file> <output file>"
	exit 0
fi
# Remove diacritical marks, extract tweet
iconv -c -f utf8 -t ascii//TRANSLIT//IGNORE "$1" | awk '{for (i = 9; i <= NF - 9; i++) print $i; print ""}' |  awk 'BEGIN {line = ""}{ if($0 == "" && line!=null) {print line; line = ""} else if (line != ""){line = line " " $0} else {line = $0}}' > tempFile

#eliminate duplicates
awk '!a[$0]++' tempFile > "$2"
rm tempFile