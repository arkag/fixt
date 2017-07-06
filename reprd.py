#!/usr/bin/env python3
import time
import random

tasks = [ 'Rejiggering the whosamawhatsit', 'Performing a physical reset', 'Hunting for semicolons', 'Checking for variable case', 'Pestering coworker', 'Verifying the cache', 'Removing malware', 'Highlighting syntax', 'Opening source', 'Spinning container', 'Containing spinner', 'Developing operations', 'Obfuscating shell', 'Removing eastereggs', 'Sourcing configurations', 'Prodding the daemons' ]

print('Fixing your issue...')

for i in range(4):
    print(random.choice(tasks) + '...')
    while(random.randint(0,10) != 2 ):
        time.sleep(.25)
        print('.', end='', flush=True)

    print('\nDone.\n')
    time.sleep(.5)

print('Your problem should now be fixed.')
