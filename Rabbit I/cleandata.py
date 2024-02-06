import sys
if len(sys.argv) > 1:
    logname = sys.argv[1] # check for filename passed as argument
else:                     # if not, ask for a file name
    print('(can also be used "python3 cleandata.py filename.log")')
    logname = input('Log file: ')
try:
    logfile = open(logname, 'r')
except:
    print('Error opening input file..Exiting cleanly')
    sys.exit()
lines = logfile.readlines()
logfile.close()
oldline = ''
liveline = ''
firstline = True
logfile = open(logname + '.clean.log', 'a') # load the log file
for line in lines: # loop over each line in the file
    if line[0] == "#": # check if line is a comment
        continue
    oldline = liveline
    liveline = line.replace('[', '').replace(']', '').replace(',\n', '').split(',')
    if liveline == ['f', 'da', 'db', 'dc', 'ga', 'go', 't', 'h', 'p']: # checks for signal
        continue
    for i in range(9): # fills in gaps in data
        try:
            liveline[i] = float(liveline[i])
        except:
            liveline[i] = oldline[i]
        liveline[i] = str(liveline[i])
    if liveline[4] == "0.0": # Checks for GPS lock
        continue
    if firstline:
        logfile.write('[' + ','.join(liveline) + ']')
        firstline = False
    else:
        logfile.write(',[' + ','.join(liveline) + ']')
logfile.close() # closes the file
print('Saved as ' + logname + '.clean.log')