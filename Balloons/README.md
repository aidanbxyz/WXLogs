# Balloons
> Payload is launch dependent

[More Information](https://sswa.tv/projects/balloon/)
## Format
**ALL DATES AND TIMES ARE IN UTC**

Balloon logs are named in the format `Atmos_YYYY-MM-DD_HHMM.log` where the date is the launch time of the balloon, rounded to the nearest 30 minutes.

Meteorological data is in tabular format, as used by the NWS:
```
%TITLE%
 SSWA YYMMDD/HHMM lat,lon

%RAW%
 LEVEL (mb), HEIGHT (m), TEMP (C), DEWPOINT (C), WINDDIR (deg), WINDSPEED (kt)
 ...snip...
%END%
```