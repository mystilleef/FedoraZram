#!/bin/sh

ls /sys/block/zram* > /dev/null 2>&1 || exit 0

for i in /sys/block/zram*; do
	compr=$(< $i/compr_data_size)
	orig=$(< $i/orig_data_size)
	ratio=0
	if [ $compr -gt 0 ]; then
		ratio=$(echo "scale=2; $orig*100/$compr" | bc -q)
	fi
	echo -e "/dev/${i/*\/}:\t$ratio% ($orig -> $compr)"
done
