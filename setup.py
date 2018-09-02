import re
from os.path import join, dirname

from setuptools import setup, find_packages


with open(join(dirname(__file__), 'gecko', '__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read()).group(1)


dependencies = [
    'restfulpy >= 1.9.0',
]


setup(
    name='gecko',
    author='mehrdad',
    author_email='mehrdad1373pedramfar@gmail.com',
    version=package_version,
    install_requires=dependencies,
    packages=find_packages(),
    test_suite='gecko.tests',
    entry_points={
        'console_scripts': [
            'gecko = gecko:gecko.cli_main'
        ]
    }
)

