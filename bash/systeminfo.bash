#!/bin/bash

#this creates an empty HTMl file with the basic tags already written down
#pipe it into a new file to produce a skeleton of an html-page

#####CONSTANTS

TITLE="System Information for $HOSTNAME"
RIGHT_NOW=$(date +"%x %r XZ")
TIME_STAMP="Updated on $RIGHT_NOW by $USER"

#####FUNCTIONS

function system_info
{
echo "<h2>System Release Info</h>"
echo "<p>Not Yet Implemented</p>"
}


function drive_space
{
    echo "<h2>Filesystem space</h2>"
    echo "<pre>"
    df
    echo "</pre>"
}


function show_uptime
{
echo "<h2>Home Directory Space by User</h2>"
echo "<pre>"
uptime
echo "</pre>"
}


function home_space
{
echo "<h2>Home Directory Space by User</h2>"
echo "<pre>"
echo "Bytes Directory"
du -s /Home/* | sort -nr
echo "</pre>"
}


#####MAIN

cat <<- _EOF_
<html>
        <head>
                <title>$TITLE</title>
        </head>

        <body>
                <h1>$title $HOSTNAME</h1>
                <p>$TIME_STAMP</p>
                $(system_info)
                $(show_uptime)
                $(drive_space)
                $(home_space)
        </body>
</html>
_EOF_