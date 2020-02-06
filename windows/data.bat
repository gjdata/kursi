bitsadmin /Transfer x  http://www.atd.lv/sites/default/files/GTFS/gtfs-latvia-lv.zip c:\temp\gotten.zip
powershell Expand-Archive -Force c:\temp\gotten.zip C:\temp\result
cd C:\temp\result
type stops.txt | find "Gauja"

