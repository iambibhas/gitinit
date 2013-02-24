gitinit
=======
[![Build Status](https://travis-ci.org/iambibhas/gitinit.png?branch=master)](https://travis-ci.org/iambibhas/gitinit)

Initiates an empty git repository with a `.gitignore` file for the provided language.

Installation
------------

    $ [sudo] pip install gitinit

    # Or if you want the development version
    $ [sudo] pip install -e git+git@github.com:iambibhas/gitinit.git

Usage
-----

    # if you already have it installed, upgrade
    $ sudo pip install --upgrade gitinit
    
    # initiates with a generic .gitignore file  
    $ gitinit

    # initiates a Haskell .gitignore file  
    $ gitinit -l haskell

    # See a list of languages supported
    $ gitinit -L

Help
----

    $ gitinit -h

[Here is the full list](https://github.com/iambibhas/gitinit/tree/master/gitinit/gitignores) of supported languages. 
