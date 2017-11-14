#!/usr/bin/env python3
import calendar
from os import system, path

km = [500, 1500, 400]


def dict_month():
    ''' '''
    dict_month = {calendar.month_name[i]: i for i in range(1, 13)}
    return dict_month


def add_km_dict(year, km):
    ''' '''
    for month in year:
        if year[month] <= 4:
            year[month] = km[0]
        elif year[month] <= 9:
            year[month] = km[1]
        elif year[month] <= 12:
            year[month] = km[2]
    return year


def sum_km(year):
    ''' '''
    return sum([year[month] for month in year])


def km_per_month(year):
    ''' '''
    return_str = '\n'
    for month in year:
        return_str += '{} {} km\n'.format(month, year[month])
    return return_str


if __name__ == '__main__':
    '''
    '''
    year = dict_month()
    print(year)
    year = add_km_dict(year, km)
    print(year)
    string = 'km total {} km'.format(sum_km(year))
    print(km_per_month(year))
    print(string)

    system('chmod +x {}'.format(path.basename(__file__)))
