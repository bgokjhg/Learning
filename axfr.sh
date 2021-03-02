#!/bin/bash

if [ $# -ne 1 ]
then
	echo 'Usage: axfr.sh <domain>'
elif ! echo "$1" |  egrep '[a-z0-9]+\.[a-z0-9]+' > /dev/null
then
	echo "Must specify a valid domain"
else
	if !  host -t ns $1 | grep 'not found' >/dev/null
	then
		for i in $(host -t ns $1 | cut -d' ' -f4)
		do
			if host -t axfr $1 $i | grep 'failed' > /dev/null
			then
				echo "============"
				echo "$i can't do zone-transfer"
				echo "============"
			else
				echo "============"
				echo $i
				echo "============"
				host -t axfr $1 $i | grep 'IN'
			fi
		done
	else
		echo "Domain does not have nameservers"
	fi
fi
