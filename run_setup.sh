#!/bin/bash - 

virtualenv runme
source runme/bin/activate
pip3.7 install Django
pip3.7 install psycopg2
#Mac OSX
#env LDFLAGS='-L/usr/local/lib -L/usr/local/Cellar/openssl/1.0.2r/lib -L/usr/local/Cellar/readline/8.0.0/lib' pip3.7 install psycopg2
