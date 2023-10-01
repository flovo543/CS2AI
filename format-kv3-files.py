import re
import sys

stdin = sys.stdin
stdout = sys.stdout



#Leading white spaces entfernen
#Leere Zeilen weg (vlt.)
#counter für { [ +1 Tabanzahl       (Nicht in Kommentarzeile)
#counter für } ] -1 Tabanzahl       (Nicht in Kommentarzeile)

counter = 0

for line in stdin: 

    if re.match(r'^\s*$', line):
        continue

    newLine = line.lstrip()

    if '}' in line and '{' not in line:
        counter -= 1 
    if ']' in line and '[' not in line:
        counter -= 1 

    tabstring = ""
    for x in range(counter):
        tabstring += "\t"

    if '{' in line and '}' not in line:
        counter += 1
    if '[' in line and ']' not in line:
        counter += 1 
    
    stdout.write(tabstring + newLine)

