#!/usr/bin/python3
# -*- encoding: utf-8 -*-

#
# Created by:
#           ali_elainous
#

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
    try:
        res = get(url, timeoout=7)
        res.close()
        print('[ Done ]') if  res.ok else exit('[ Fail ]\nUrlNotExist:')
    except TimeoutError:
        quit('[ Fail ]\nTimeoutError')
    except Exception as err:
        exit('[ Fail ]\nError: Something is wrong, please check your url.')
        
def has_login(code):
    return any(findall(r'type="password"|type="submit"|type="email"', code))

def main():
    # url, users : http://localhost  user_list.txt
    url, users = argv[1:] if  len(argv) == 3 else input('url, usrs : ').split()
    url, users = url.strip(), open(users.strip())
    # check if  url exist.
    url += '' if  url.endswith('/') else '/'
    check(url)
    for user in users:
        if  not user.strip():
            continue
        sleep(.5)
        url_path = url + user.strip()
        print('[ ... ] Getting {}'.format(url_path), end='\r', flush=1)
        try:
            res = get(url_path, timeout=7)
            res.close()
        except Exception as err:
            print('err: ', err) ; continue
        if  has_login(res.text):
            print('[ Done ]')
            quit('====> login_screen_path : {} '.format(url_path))
        else:
            print('[ Fail ]')

if  __name__ == '__main__':
    main()
