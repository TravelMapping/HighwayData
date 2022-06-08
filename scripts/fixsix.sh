#!/usr/bin/env bash
#
echo $1
java SixDigits < $1 > /tmp/x.wpt
mv /tmp/x.wpt $1

