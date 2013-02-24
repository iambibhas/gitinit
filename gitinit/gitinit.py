#! /usr/bin/env python
# -*- coding: utf-8 -*-

__appname__ = 'gitinit'
__author__ = "Bibhas C Debnath <me@bibhas.in>"
__licence__ = "LGPL"

import os
from subprocess import call
try:
    import argparse
except ImportError:
    raise ImportError('argparse not found.')

__appdir__ = os.path.dirname(os.path.realpath(__file__))


class LanguageNotValidError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class GitignoreManager:
    def __init__(self, directory='gitignores'):
        self.directory = directory
        self.gitignores = []

    def filename(self, language):
        return '%s.gitignore' % language

    def read(self, filename):
        try:
            content = open(filename, 'r')
        except IOError:
            raise LanguageNotValidError('Cannot open the gitignore file: %s' % filename)
        return content.read()

    def all_gitignores(self):
        if self.gitignores:
            return self.gitignores

        gitignores = []

        def is_gitignore(filename):
            if filename:
                if filename.endswith('gitignore'):
                    return True
            return False

        def adddir(directory, files):
            def f(x): return os.path.join(directory, x)
            return map(f, files)

        for (path, dirs, files) in os.walk(os.path.join(__appdir__, self.directory)):
            gitignores += filter(is_gitignore, adddir(path, files))

        self.gitignores = gitignores
        return self.gitignores

    def exists(self, language):
        if language:
            filename = self.filename(language)
            for idx, gi in enumerate(self.all_gitignores()):
                if gi.lower().find(filename.lower()) >= 0:
                    return gi
        raise LanguageNotValidError('No gitignore file for the specified language "%s"' % language)

    def get_gitignore(self, language):
        filename = self.exists(language)
        content = self.read(filename)
        if content:
            print 'Creating .gitignore for "%s"' % language
            gifile = open(os.path.join(os.getcwd(), '.gitignore'), 'w')
            gifile.write(content)
            gifile.close()


manager = GitignoreManager()
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--language', help="create .gitignore file for this language")
parser.add_argument('-L', '--list', help="shows the list of available languages", action="store_true")


def main():
    args = parser.parse_args()

    if args.list:
        print "List of languages supported right now:"
        l = []
        gi_list = manager.all_gitignores()
        for gi in gi_list:
            if gi:
                l.append(gi.split('/')[-1].split('.')[0])
        print ', '.join(l)
        return

    language = args.language or 'generic'
    manager.get_gitignore(language)
    try:
        call(['git', 'init'])
    except Exception as e:
        print 'Error in initiaing git repository: %s' % str(e)
