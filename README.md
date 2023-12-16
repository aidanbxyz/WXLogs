# WXLogs
Logs from weather research project deployments and processing software

All logs are collected as apart of the AMMETS project led by SSWA.TV. [Learn More](https://sswa.tv/projects/ammets/)

## Rabbit 1
> GPS, Temperature, Humidity, Pressure
### Format
**ALL DATES AND TIMES ARE IN UTC**

Rabbit 1 logs are named in the format `YYYY-MM-DD HHMMSS-HHMMSS` where the date is the start date of the log and the time can go into the next day.

Data is in the format
```
[f,da,db,dc,ga,go,t,h,p],
[f,da,db,dc,ga,go,t,h,p],
...snip...
[f,da,db,dc,ga,go,t,h,p],
[f,da,db,dc,ga,go,t,h,p]
```
where
```
f = frequency      (MHz)
da = hour          (HH or H)
db = minute        (MM or M)
bc = second        (SS or S)
ga = gps latitude  (DDMM.MMMM)
go = gps longitude (DDMM.MMMM)
t = temperature    (deg C)
h = humidity       (percent)
p = pressure       (Pa)
```

### cleandata.py
A script for Python 3 to clean up the data files. 

Removes headers and fills in gaps.

Outputs file as `<logfile>.clean.log` to be pasted into plot.

Usage: `python cleandata.py` then enter the file name.
