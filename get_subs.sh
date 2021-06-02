#!/bin/bash

youtube-dl -u dalbianco.pedro --playlist-reverse --skip-download --write-auto-sub --sub-lang es --yes-playlist -o 'Subs/%(upload_date)s-%(title)s.%(ext)s' $1
