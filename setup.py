import re

from skbuild import setup

def parse_version():
    REGEX = r'kVersionNumber\("([0-9]+\.[0-9]+)"\)'
    with open('src/CommandLine/CommandLineParser.cpp', 'r') as f:
        match = re.search(REGEX, f.read())
        if match:
            return match.group(1)

    raise ValueError('Could not find version')

with open("README.md", "r", encoding="utf-8") as readme:
  long_desc = readme.read()

setup(
    name='Surelog',
    version='0.' + parse_version(),

    author='Alain Dargelas',
    author_email='',

    package_dir={'': 'pysrc'},
    packages=['surelog'],

    cmake_install_dir='pysrc/surelog/data',
    cmake_args=['-DSURELOG_WITH_PYTHON=1'],

    entry_points={
        'console_scripts': [
            'surelog=surelog:surelog',
        ]
    },

    url='https://github.com/chipsalliance/Surelog',
    project_urls={
        "Bug Tracker": "https://github.com/chipsalliance/Surelog/issues",
    },

    description='SystemVerilog 2017 Pre-processor, Parser, Elaborator, UHDM Compiler. ' \
                'Provides IEEE Design/TB C/C++ VPI and Python AST API.',

    long_description=long_desc,
    long_description_content_type="text/markdown",

    license='Apache 2.0',
)