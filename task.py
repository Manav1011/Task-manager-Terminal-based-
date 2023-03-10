import subprocess
import sys
# Execute the other Python script

args = sys.argv;
try:
    if len(args) > 1 and args[1] == 'list':
        arg2 = args[2] if len(args) > 2 else ''
        subprocess.run(['python', '/home/manav1011/Documents/Python-Tasks-Terminal/list.py', arg2])
    if len(args) > 1 and args[1] == 'add':
        arg2 = args[2] if len(args) > 2 else ''
        subprocess.run(['python', '/home/manav1011/Documents/Python-Tasks-Terminal/add.py', arg2])
    if len(args) > 1 and args[1] == 'done':
        arg2 = args[2] if len(args) > 2 else ''
        subprocess.run(['python', '/home/manav1011/Documents/Python-Tasks-Terminal/done.py', arg2])
    if len(args) > 1 and args[1] == 'open':
        arg2 = args[2] if len(args) > 2 else ''
        subprocess.run(['python', '/home/manav1011/Documents/Python-Tasks-Terminal/open.py', arg2])
    if len(args) > 1 and args[1] == 'show':
        arg2 = args[2] if len(args) > 2 else ''
        subprocess.run(['python', '/home/manav1011/Documents/Python-Tasks-Terminal/show.py', arg2])
    if len(args) > 1 and args[1] == 'update':
        arg2 = args[2] if len(args) > 2 else ''
        subprocess.run(['python', '/home/manav1011/Documents/Python-Tasks-Terminal/update.py', arg2])
    if len(args) > 1 and args[1] == 'help':        
        subprocess.run(['python', '/home/manav1011/Documents/Python-Tasks-Terminal/help.py'])
    if len(args) == 1:
        subprocess.run(['python', '/home/manav1011/Documents/Python-Tasks-Terminal/help.py'])

except:
    pass