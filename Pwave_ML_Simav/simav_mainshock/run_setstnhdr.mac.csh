#!/bin/csh -f

set txtfile=/home/komec/disk-1/SIMAV/station_shells/sta-deg.lst
set nbl=`wc -l $txtfile | awk '{print $1}'`
echo $nbl
@ i = 1
while ($i <= $nbl)
set line=`./ligne $txtfile $i`
#echo $line
echo $line > a

set stname=`awk '{print $1}' a `
set stla=`awk '{print $2}' a `
set stlo=`awk '{print $3}' a `
set stel=`awk '{print $4}' a `
echo $stname $stla $stlo $stel
set nof=`ls *$stname* | wc | awk '{print $1}'`
if ( $nof > 0 )  then
foreach file (*$stname*)
echo $file
sac  << !
macro setstnhdr.mac fil $file stlat $stla stlon $stlo stele $stel
q
!
end
endif

endif
@ i++
end

