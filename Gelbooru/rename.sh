#!/bin/sh

for file in [0-10000000]*.jpg; do
	echo "file: $file"
	# echo "contents: $(cat $file)"
	num=$(echo "$file" | grep -o "[0-9]*")
	echo "number: $num"
	padded_num=$(printf "%07d" $num)
	echo "padded number: $padded_num"
	mv "$file" "${padded_num}.jpg"
done
