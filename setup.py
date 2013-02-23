import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "gitinit",
    version = "1.0.0",
    author = "Bibhas C Debnath",
    author_email = "me@bibhas.in",
    description = ("Initiates git with gitignore for provided language"),
    license = "LGPL",
    keywords = "example documentation tutorial",
    url = "https://github.com/iambibhas/gitinit",
    packages=find_packages(),
    long_description=read('README.md'),
    package_data={'gitinit': ['*.gitignore', 'gitinit/gitignores/*.gitignore', 'gitinit/gitignores/Global/*.gitignore']},
    include_package_data=True,
    entry_points={"console_scripts": ["gitinit=gitinit.gitinit:main"]},
)
