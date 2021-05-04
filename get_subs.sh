#!/bin/bash

youtube-dl --skip-download --write-auto-sub --sub-lang es --yes-playlist -o 'Subs/%(upload_date)s-%(title)s.%(ext)s' $1

