#!/bin/bash

youtube-dl --yes-playlist -o '%(upload_date)s-%(title)s.%(ext)s' --playlist-start $2 --playlist-end $3 $1

for filename in *; do
	if ["$filename" != "get_subs.sh"]; then
		ffmpeg -i "$filename" -filter:v crop=220:240:1607:745 -c:a copy Crops/"$filename"
	fi
done
