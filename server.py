# -*- coding: utf-8 -*-
# Author: Sébastien Combéfis
# Version: 5 Octobre 2015

from bottle import route, run, template, static_file, error, post, request
import json

# Load database from file
database = {'links': [
    {'name': 'AoT', 'url': 'http://0.media.dorkly.cvcdn.com/56/67/8187217c79de7ac6ac55e79f80c71232.gif', 'score': 10},
    {'name': 'SECRET DO NOT CLICK', 'url': 'http://goo.gl/jfc8di', 'score': 257}
]}

# Entry point of the application
@route('/gimmelink')
def app():
    links = '<ul>'
    for link in database['links']:
        links += '<li><a href="{}">{}</a> (popularité : {})</li>'.format(link['url'], link['name'], link['score'])
    links += '</ul>'
    return '<h1>Gimme link</h1>{}'.format(links)

# Get all the links
@route('/links')
def links():
    return json.dumps(database)

# Add a new link
@post('/addlink')
def addlink():
    newentry = json.loads(request.body.read().decode('utf-8'))
    database['links'].append(newentry)

# Launch the server
run(host='localhost', port=8080)