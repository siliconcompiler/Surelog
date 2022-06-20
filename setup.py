from skbuild import setup

with open("README.md", "r", encoding="utf-8") as readme:
  long_desc = readme.read()

setup(
    name='Surelog',

    version='0.0',

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
    # download_url='https://cmake.org/download',
    # project_urls={
    #     "Documentation": "https://cmake-python-distributions.readthedocs.io/",
    #     "Source Code": "https://github.com/scikit-build/cmake-python-distributions",
    #     "Mailing list": "https://groups.google.com/forum/#!forum/scikit-build",
    #     "Bug Tracker": "https://github.com/scikit-build/cmake-python-distributions/issues",
    # },

    description='SystemVerilog 2017 Pre-processor, Parser, Elaborator, UHDM Compiler. ' \
                'Provides IEEE Design/TB C/C++ VPI and Python AST API.',

    long_description=long_desc,
    long_description_content_type="text/markdown",

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: C',
        'Programming Language :: C++',
        'Programming Language :: Fortran',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools'
        ],

    license='Apache 2.0',

    keywords='CMake build c++ fortran cross-platform cross-compilation',

    # extras_require={"test": test_requirements},
)