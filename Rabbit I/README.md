# Rabbit 1
> GPS, Temperature, Humidity, Pressure

[More Information](https://sswa.tv/projects/ammets/)
## Format
**ALL DATES AND TIMES ARE IN UTC**

Rabbit 1 logs are named in the format `YYYY-MM-DD_HHMMSS-HHMMSS.log` where the date is the start date of the log and the time can go into the next day.

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
go = gps longitude (-DDMM.MMMM) <-- eg: log says 9845.9258 => is really -9845.9258
t = temperature    (deg C)
h = humidity       (percent)
p = pressure       (Pa)
```
and any lines starting with "#" are ignored.


## cleandata.py
A script for Python 3 to clean up Rabbit's data files.

Removes headers and fills in gaps in data.

Outputs file as `<logfile>.clean.log` to be pasted into plot.html.

Usage: `python3 cleandata.py logfile.log` or `python3 cleandata.py` then enter the file name when prompted.
