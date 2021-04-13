"""
Плакунов Иван - Python.Март2021.7урок.1задание

"""

import os

dir_name = ['settings', 'mainapp', 'authapp']
dir_name_subfolder = ['', 'templates', 'templates']
dir_name_subfolder_templates = ['', 'mainapp', 'authapp']
files = ['settings/__init__.py', 'settings/dev.py', 'settings/prod.py',
         'mainapp/__init__.py', 'mainapp/models.py', 'mainapp/views.py',
         'mainapp/templates/mainapp/base.html', 'mainapp/templates/mainapp/index.html',
         'authapp/__init__.py', 'authapp/models.py', 'authapp/views.py',
         'authapp/templates/authapp/base.html', 'authapp/templates/authapp/index.html'
         ]

el = 0
for i in dir_name:
    dir_path = os.path.join(i, dir_name_subfolder[el], dir_name_subfolder_templates[el])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    el += 1

for i in files:
    with open(i, 'w'):
        pass
