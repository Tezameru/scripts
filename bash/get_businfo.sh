#!/bin/bash
URL="http://www.saarfahrplan.de/cgi-bin/query.exe/dn?seqnr=1&ident=i4.0391210.1483569808&OK#focus"
##URL="http://www.saarfahrplan.de/cgi-bin/query.exe/dn?wai=yes&"
CURLARG=" -d "
DATUM=date +%R
ZEIT=date +%d.%m.%y



#!/bin/bash

curl -d "REQ0JourneyStopsSID=A=1@O=Universität Mensa, Saarbrücken@X=7043767@Y=49256392@U=80@L=000010905@B=1@V=11.9,@p=1494866999@&boardType=dep&maxJourneys=10&start=suchen" "http://www.saarfahrplan.de/cgi-bin/stboard.exe/dox?M=p2&dpm=0&dw=240&dh=320&" --output /tmp/newpost.html

html2text /tmp/newpost.html

credits to s.deu






curl $CURLARG "REQ0JourneyStopsS0G=Universität Mensa, Saarbrücken&REQ0JourneyStopsZ0G=Saarbrücken HBF&REQ0JourneyDate=$DATUM&REQ0JourneyTime=$ZEIT&submit=Verbindungen suchen" $URL --location --output /tmp/post.html

curl -d "REQ0JourneyStopsS0G=test&REQ0JourneyStopsZ0G=test&REQ0JourneyDate=$04.01.17&REQ0JourneyTime=20:50&submit=Verbindungen suchen" "http://www.saarfahrplan.de/cgi-bin/query.exe/dn?seqnr=1&ident=i4.0391210.1483569808&OK#focus"  --location --output /tmp/post.html

A=1@O=Universität Mensa, Saarbrücken@X=7043740@Y=49256410@U=80@L=000010905@B=1@V=11.9,@p=1482568137@"

curl -d "REQ0JourneyStopsS0G=Universität Mensa, Saarbrücken&REQ0JourneyStopsZ0G=Saarbrücken HBF&REQ0JourneyDate=$DATUM&REQ0JourneyTime=$ZEIT&submit=Verbindungen suchen" "http://www.saarfahrplan.de/cgi-bin/query.exe/dn?wai=yes&" --location --output /tmp/post.html

curl -d "REQ0JourneyStopsSID=A=1@O=Universität Mensa, Saarbrücken@X=7043767@Y=49256392@U=80@L=000010905@B=1@V=11.9,@p=1494866999@&boardType=dep&maxJourneys=10&start=suchen" "http://www.saarfahrplan.de/cgi-bin/stboard.exe/dox?M=p2&dpm=0&dw=240&dh=320&" |html2text

curl -d "Universit%E4t+Mensa%2C+Saarbr%FCcken&REQ0JourneyStopsSID=A%3D1%40O%3DUniversit%E4t+Mensa%2C+Saarbr%FCcken%40X%3D7043740%40Y%3D49256410%40U%3D80%40L%3D000010905%40B%3D1%40V%3D11.9%2C%40p%3D1482568137%40&disableEquivs=1&date=05.01.17&time=00%3A20&boardType=dep&maxJourneys=10&productsFilter=1111111111000000&start=Suchen" "http://www.saarfahrplan.de/cgi-bin/stboard.exe/dox?M=p2&dpm=0&dw=240&dh=320&" --location --output /tmp/newpost.html

curl -d "REQ0JourneyStopsSID=A=1@O=Universität Mensa, Saarbrücken@X=7043767@Y=49256392@U=80@L=000010905@B=1@V=11.9,@p=1494866999@" "http://www.saarfahrplan.de/cgi-bin/stboard.exe/dox?M=p2&dpm=0&dw=240&dh=320&" |html2text

Universit%E4t+Mensa%2C+Saarbr%FCcken&REQ0JourneyStopsSID=A%3D1%40O%3DUniversit%E4t+Mensa%2C+Saarbr%FCcken%40X%3D7043740%40Y%3D49256410%40U%3D80%40L%3D000010905%40B%3D1%40V%3D11.9%2C%40p%3D1482568137%40&disableEquivs=1&date=05.01.17&time=00%3A20&boardType=dep&maxJourneys=10&productsFilter=1111111111000000&start=Suchen

curl -d "REQ0JourneyStopsS0G=Universität Mensa, Saarbrücken&REQ0JourneyStopsZ0G=Saarbrücken HBF&REQ0JourneyDate=$DATUM&REQ0JourneyTime=$ZEIT&submit=Verbindungen suchen" $URL --location --output /tmp/post.html

html2text 
curl -d "REQ0JourneyStopsS0G=Universität Mensa, Saarbrücken&REQ0JourneyStopsZ0G=Saarbrücken HBF&REQ0JourneyDate=$DATUM&REQ0JourneyTime=$ZEIT&submit=Verbindungen suchen" "http://www.saarfahrplan.de/cgi-bin/stboard.exe/dox?M=p2&dpm=0&dw=240&dh=320&" --location --output /tmp/post.html
curl -d "Universit%E4t+Mensa%2C+Saarbr%FCcken&REQ0JourneyStopsSID=A%3D1%40O%3DUniversit%26%23228%3Bt+Mensa%2C+Saarbr%26%23252%3Bcken%40X%3D7043767%40Y%3D49256392%40U%3D80%40L%3D10905%40&disableEquivs=1&date=16.05.17&time=23%3A26&boardType=dep&maxJourneys=10&productsFilter=1111111111000000&start=Suchen" "http://www.saarfahrplan.de/cgi-bin/stboard.exe/dox?M=p2&dpm=0&dw=240&dh=320&" --location --output /tmp/newpost.html