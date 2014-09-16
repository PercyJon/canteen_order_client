import datetime
import os
from random import randint

now = datetime.datetime.now()
start = now.replace(year=2014)


def change_day():
    return datetime.timedelta(days=2, seconds=randint(0, 60), minutes=randint(0, 60), hours=randint(0, 24))


def change_time():
    return datetime.timedelta(seconds=randint(0, 60), minutes=randint(0, 60))


commit_date = (start + change_day())
times = randint(0, 5)

while commit_date < now:

    commit_date = commit_date + change_day()
    for i in range(times):
        f = open('data.txt', 'a+')
        commit_date = commit_date + change_time()
        f.writelines(commit_date.isoformat() + '\n')
        f.close()
        os.system('git add .')
        os.system('git commit --date={time} -m "Update {time}"'.format(time=commit_date.isoformat()))
