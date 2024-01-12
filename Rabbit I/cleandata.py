logname = input('Log file: ')
logfile = open(logname, 'r')
lines = logfile.readlines()
logfile.close()
oldline = ''
liveline = ''
firstline = True
logfile = open(logname + '.clean.log', 'a')
for line in lines:
    if line[0] == "#": # check for comment
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
logfile.close()
print('Saved as ' + logname + '.clean.log')