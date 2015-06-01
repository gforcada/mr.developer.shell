# -*- coding: utf-8 -*-
from setuptools import setup


version = '0.0.1'

description = 'mr.developer extension to run shell commands on repositories.'

long_description = """
{0}

{1}
""".format(
    open('README.rst').read(),
    open('CHANGES.rst').read(),
)

setup(
    name='mr.developer.shell',
    version=version,
    description=description,
    long_description=long_description,
    # Get more strings at http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Buildout',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='mr.developer extension shell',
    author='Gil Forcada Codinachs',
    author_email='gilforcada@gmail.com',
    url='http://github.com/gforcada/mr.developer.shell',
    license='BSD',
    py_modules=['shell'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'mr.developer',
        'setuptools',
    ],
    entry_points="""
    [mr.developer.commands]
    shell = shell:CmdShell
    """
)
