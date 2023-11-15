import os
import random
import subprocess
from datetime import datetime, timedelta

# Début du 1er novembre 2023
start_date = datetime(2023, 11, 15)
# Fin au 1er janvier 2024
end_date = datetime(2023, 12, 10)

current_date = start_date

while current_date < end_date:
    date_str = current_date.strftime('%Y-%m-%d')
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    commit_datetime = datetime(
        current_date.year,
        current_date.month,
        current_date.day,
        random_hour,
        random_minute,
        random_second
    )
    commit_date_str = commit_datetime.strftime('%Y-%m-%dT%H:%M:%S')

    # Ecrire dans le fichier
    with open('file.txt', 'a') as file:
        file.write(f'Commit on {date_str}\n')

    # Ajouter les changements
    subprocess.run(['git', 'add', '.'])

    # Faire le commit avec une date spécifique
    subprocess.run(['git', 'commit', '--date', commit_date_str, '-m', f'Commit on {date_str}'])

    # Passer au jour suivant
    current_date += timedelta(days=1)

# Pousser tous les commits vers la branche principale
subprocess.run(['git', 'push', '-u', 'origin', 'main'])
