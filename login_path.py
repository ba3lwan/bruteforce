#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# Script for get username of a website login_screen
# ex: http://localhost/iname
# input:
#    url : http://localhost , http://web.facebook.com ...
#    lst : users_list.txt
# output:
#    path : http://localhost/Admin_panel

from  requests  import  get
from  time      import  sleep
from  sys       import  argv
from  re        import  findall

def check(url):
    print('[ .... ] Checking url', end='\r', flush=1)
    res = get(url)
    res.close()
    print('[ Done ]') if  res.ok else exit('[ Fail ]\nUrlNotExist:')

def has_login(code):
    return 

def main():
    # url, users : http://localhost  user_list.txt
    url, users = argv[1:] if  len(argv) == 3 else input('url, usrs : ').split()
    url, users = url.strip(), open(users.strip())
    # check if  url exist.
    url += '' if  url.endswith('/') else '/'
    check(url)
    for user in users:
        sleep(.5)
        url_path = url + user.strip()
        print('[ ... ] Getting {}'.format(url_path), end='\r', flush=1)
        res = get(url_path)
        res.close()
        if  has_login(res.text):
            print('[ Done ]')
            quit('====> login_screen_path : {} '.format(url_path))
        else:
            print('[ Fail ]')

if  __name__ == '__main__':
    main()
