# coding: utf-8

import os

from setuptools import setup
from setuptools.command.develop import develop

requirements = [
    'Flask==0.12.2',
    'Flask-Bootstrap==3.3.7.1',
    'Flask-WTF==0.14.2',
    'dynaconf==0.5.2',
    'gunicorn==19.7.1',
    'import-string==0.1.0',
    'pymongo==3.6.0',
    'PyYAML==3.12'
]

requirements_dev = [
    'pep8==1.7.0',
    'flake8==3.4.1',
    'Flask-Testing==0.6.2',
    'mongomock==3.8.0',
    'selenium==3.6.0',
    'ipython==6.2.1',
    'Flask-DebugToolbar==0.10.1'
]


class PostDevelopCommand(develop):
    def run(self):
        command = f'pip install {" ".join(requirements_dev)}'
        os.system(command)
        develop.run(self)


setup(
    name='buscabike',
    version='0.0.1',
    description="Centralize bike ads",
    author="Bruno Rocha",
    author_email='rochacbruno@gmail.com',
    url='https://github.com/rochacbruno/buscabike',
    packages=['buscabike'],
    package_dir={'buscabike': 'buscabike'},
    entry_points={
        'console_scripts': [
            'bike=buscabike.cli:main'
        ]
    },
    cmdclass={
        'develop': PostDevelopCommand
    },
    include_package_data=True,
    install_requires=requirements,
    test_suite='tests'
)
