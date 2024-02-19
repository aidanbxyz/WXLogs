import sys
if len(sys.argv) > 1:
    logname = sys.argv[1] # check for filename passed as argument
else:                     # if not, ask for a file name
    print('(can also be used "python3 cleandata.py filename.log")')
    logname = input('Log file: ')
try:
    logfile = open(logname, 'r')
except:  # check for errors (such as nonexistent file)
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
    liveline = line.replace('[', '').replace(']', '').replace(',\n', '').split(',') # removes brackets and newlines, splits line into array
    if liveline == ['f', 'da', 'db', 'dc', 'ga', 'go', 't', 'h', 'p']: # checks for signal
        continue                                                       # continue if none
    for i in range(9): # fills in gaps in data
        try:
            liveline[i] = float(liveline[i])
        except: # if there are any errors converting to float, use previous previous data point
            liveline[i] = oldline[i]
        liveline[i] = str(liveline[i])
    if liveline[4] == "0.0": # checks for GPS lock
        continue             # continue if none
    if firstline:
        logfile.write('[' + ','.join(liveline) + ']') # no comma needed before the first line
        firstline = False
    else:
        logfile.write(',')   # by default, this program outputs data as one line for use with plot.html
        #logfile.write('\n') # <-- Uncomment this line to output each line seperately
        logfile.write('[' + ','.join(liveline) + ']')
logfile.close() # closes the file
print('Saved as ' + logname + '.clean.log')