#!/usr/bin/env python
# -*- coding: utf8 -*-

#import cjson
import os
import logging
import json
import click
import socket

socket.setdefaulttimeout(50)

from orgprofile.builder import SOURCES_MAP
from orgprofile.builder import build_profile

def list_profiles():
    profiles = list(SOURCES_MAP.keys())
    profiles.sort()
    print('Профили для сбора данных об организации')
    for p in profiles:
        print('- %s: %s' % (p, SOURCES_MAP[p]['help']))
    pass


@click.group()
def cli1():
    pass

@cli1.command()
@click.argument('orgcode', default=None)
@click.option('--profiles', default='all', help='Profiles of report to collect the data. Default: all')
def collect(orgcode, profiles):
    """Формирует профиль организации. Собирает данные по коду ИНН из разрозненных источников"""
    if not os.path.exists('apicrafter.key'):
        print('Пожалуйста, используйте команду "init" и передайте её ключ для APICrafter')
        return 
    f = open('apicrafter.key', 'r', encoding='utf8')
    apikey = f.read().strip()
    f.close() 
    print('Начинаю собирать данные')
    build_profile(orgcode, profiles, apikey=apikey, filepath='data')
    print('Данные сохранены в data/%s/' % (orgcode))

@click.group()
def cli2():
    pass


@cli2.command()
@click.argument('apikey', default=None)
def init(apikey):
    """Инициализация APICrafter"""
    f = open('apicrafter.key', 'w')
    f.write("%s" % (apikey))
    f.close()
    print('Ключ сохранён в apicrafter.key')

@click.group()
def cli3():
    pass

@cli3.command()
def profiles():
    """Список профилей"""
    list_profiles()


cli = click.CommandCollection(sources=[cli1, cli2, cli3])

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
    cli()
