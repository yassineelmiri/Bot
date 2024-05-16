import os 
import random

for i in range(30):
    d =  str(i) + ' days ago '
    rand = random.randrange(11)
    with open('file.txt', 'a') as file:
        file.write(d + '\n')
        os.system('git add .')
        os.system('git commit --date=" 2023'+str(rand)+'-'+d+'" -m "test"')
os.system('git push -u origin main')