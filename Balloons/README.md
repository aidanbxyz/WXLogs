# Balloons
> Payload is launch dependent
## Format
**ALL DATES AND TIMES ARE IN UTC**

Balloon logs are named in the format `Atmos_YYYY-MM-DD_HHMM.log` where the date is the launch time of the balloon, rounded to the nearest 30 minutes.

Meteorological data is in tabular format, as used by the NWS:
```
%TITLE%
 SSWA YYMMDD/HHMM

%RAW%
 LEVEL, HEIGHT, TEMP, DEWPOINT, WINDDIR, WINDSPEED
 ...snip...
%END%
```