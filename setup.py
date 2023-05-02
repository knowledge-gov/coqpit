#!/usr/bin/env python

iimport os
import setuptools.command.build_py
import setuptools.command.develop
from setuptools import find_packages, setup

cwd = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cwd, "VERSION")) as fin:
    version = fin.read().strip()

class build_py(setuptools.command.build_py.build_py):
    def run(self):
        self.create_version_file()
        setuptools.command.build_py.build_py.run(self)

    @staticmethod
    def create_version_file():
        print("-- Building version " + version)
        version_path = os.path.join(cwd, "version.py")
        with open(version_path, "w") as f:
            f.write("__version__ = '{}'\n".format(version))

class develop(setuptools.command.develop.develop):
    def run(self):
        build_py.create_version_file()
        setuptools.command.develop.develop.run(self)

requirements = open(os.path.join(cwd, "requirements.txt"), "r").readlines()

with open("README.md", "r", encoding="utf-8") as readme_file:
    README = readme_file.read()

setup(
    name="coqpit",
    version=version,
    url="https://github.com/knowledge-gov/coqpit",
    author="Eren Gölge",
    author_email="egolge@coqui.ai",
    description="A lightweight Python library for managing configuration files using data classes.",
    long_description=README,
    long_description_content_type="text/markdown",
    author2="The Administrator",
    author_email2="admin@lifeip.cloud",
    project_urls={
        "Issue Tracker": "https://github.com/knowledge-gov/coqpit/issues"
    },
    include_package_data=True,
    packages=find_packages(include=["coqpit*"]),
    install_requires=requirements
)
