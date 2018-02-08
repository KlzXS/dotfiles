import os
import subprocess

def get_passwd(acct):
    acct = os.path.basename(acct)
    path = "/home/ajaw/.passwd/%s.pass.gpg" % acct
    args = ["gpg", "--use-agent", "--quiet", "--batch", "-d", path]
    try:
        return subprocess.check_output(args).strip()
    except subprocess.CalledProcessError:
        return ""

def get_user(acct):
    acct = os.path.basename(acct)
    path = "/home/ajaw/.passwd/%s.use.gpg" % acct
    args = ["gpg", "--use-agent", "--quiet", "--batch", "-d", path]
    try:
        return subprocess.check_output(args).strip()
    except subprocess.CalledProcessError:
        return ""

def prime_gpg_agent():
    ret = False
    i = 1
    while not ret:
        ret = (get_passwd("prime") == "prime")
        if i > 2:
            from offlineimap.ui import getglobalui
            sys.stderr.write("Error reading in passwords. Terminating.\n")
            getglobalui.terminate()
        i += 1
    return ret

prime_gpg_agent()
