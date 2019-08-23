#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:07:49 2019

@author: oelmas
"""

from jira import JIRA, JIRAError
import re

options = {'server':'http://localhost:2990/jira'}
#options = {'server':'http://jira.icterra.com:8443'}

#jira = JIRA(options,basic_auth=('oner.elmas','!Oner0201976'))
jira = JIRA(options,basic_auth=('admin','admin'))
projetcs = jira.projects()

keys = sorted([project.key for project in projetcs])[:]
print(keys)

jra = jira.project('PROJ')

roles = jira.project_roles(jra)
print(roles)
users = jira.search_users('.')


print([user.name for user in users])


# Create multiple issues
issue_list = [
{
    'project': {'key': 'PROJ-1'},
    'summary': 'First issue of many',
    'description': 'Look into this one',
    'issuetype': {'name': ' Task'},
},
{
    'project': {'key': 'PROJ-1'},
    'summary': 'Second issue',
    'description': 'Another one',
    'issuetype': {'name': ' Task'},
},
{
    'project': {'key': 'PROJ-1'},
    'summary': 'Last issue',
    'description': 'Final issue of batch.',
    'issuetype': {'name': ' Task'},
}]
issues = jira.create_issues(field_list=issue_list)
issues_in_proj = jira.search_issues('project=PROJ')

oh_crap = jira.search_issues('assignee = {0} and due < endOfWeek() order by priority desc'.format('testuser1'), maxResults=5)
print([iss for iss in oh_crap])
