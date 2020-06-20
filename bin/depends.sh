#!/usr/bin/bash
# jsfsdb (c) Ian Dennis Miller

source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -a . -r requirements-dev.txt jsfsdb
source ~/.virtualenvs/jsfsdb/bin/activate
