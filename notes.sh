#!/bin/bash

NOTES_FOLDER="$HOME/notes"
NOTE="$NOTES_FOLDER/$1.md"
TIMESTAMP="$(date "+%Y-%m-%d")"
EDITOR="${VISUAL:-vim}"

if [ -z "$1" ]; then
	printf "Usage: notes [NAME]\n"
	printf "Script to create new note files. There is no --help file available.\n"
	printf "New files will be placed in $NOTES_FOLDER.\n"
elif [[ -f $NOTE ]]; then
	$EDITOR $NOTE
else
	printf "#TITLE\n> " >> $NOTE
	printf "\n> "$TIMESTAMP >> $NOTE
	printf "\n>" >> $NOTE
fi
