#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##----------------------------------------------------------------------------------------------------------------------
##
## Installer for tmuxomatic
##
## The distutils is the only standard packaging library included with Python 3.x
##
##----------------------------------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
	name="tmuxomatic",
	version='0.0',
	author="Oxidane",

	description="A completely different kind of tmux session manager.",
	license="BSD 3-Clause (tmuxomatic), Other (windowgram)",
	url="https://github.com/oxidane/tmuxomatic",
	download_url="https://pypi.python.org/pypi/tmuxomatic",

	author_email="invalid",

	packages=find_packages(),
    install_requires=[],
    scripts=['bin/tmuxomatic'],

)

