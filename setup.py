import os, sys
from distutils.core import setup


setup(
    # metadata
    name='pycparser',
    description='C parser in Python',
    long_description="""
        pycparser is a complete parser of the C language, written in 
        pure Python using the PLY parsing library.
        It parses C code into an AST and can serve as a front-end for
        C compilers or analysis tools.
    """,
    license='LGPL',
    version='1.07',
    author='Eli Bendersky',
    maintainer='Eli Bendersky',
    author_email='eliben@gmail.com',
    url='http://code.google.com/p/pycparser/',
    platforms='Cross Platform',
    
    packages=['pycparser'],
)

    
