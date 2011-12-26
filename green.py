import datetime
import os


# from heavy import special_commit


def modify():
    file = open('zero.md', 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    os.system('git commit -a -m test_github_streak > /dev/null 2>&1')


def set_sys_time(month, day, year):
    print('sudo date %02d%02d1200%04d' % (month, day, year))
    os.system('sudo date %02d%02d1200%04d' % (month, day, year))


def trick_commit(year, month, day):
    set_sys_time(month, day, year)
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        trick_commit(cur_date.month, cur_date.day, cur_date.year)


if __name__ == '__main__':
    daily_commit(datetime.date(2009, 1, 1), datetime.date(2019, 12, 30))
