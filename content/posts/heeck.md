+++
title = "is this considered cybersec research ?"
description = "idk, just journalling things"
date = 2026-08-02

[taxonomies]
tags = ['cybersecurity']

+++

I live in a household yet uninfected by Internet access.
I am in no position to change that, yet the Internet recognizes
no frontiers; even walls prove incapable of restraining its reach.
What it annihilates is boredom. And boredom's deepest instinct is
self-annihilation, forever impelled toward its own extinction.
these are two matter and anti-matter particles drawn toward one
another by the very conditions of their existence knowing
well that the instant of collision is indistinguishable from the
instant of erasure.
( or something, idk how open this topic up ).

Anyway, I sensed that the Internet speed was slow but I am an
engineer, I have to talk with number not words, I also wanted to
confirm that Internet was faster at dawn rather more the rest of
the day, and how fast comparatevly. well I can just run a speed
test on my local machine, but I am connected through wifi so it
would just proof my antenna's gain rather than the actual speed,
I was connecting from a wifi repeater, so my first thought was to
download its firmware and patch it to log traffic, but soon I
found a better way, this [exploit](https://github.com/acecilia/OpenWRTInvasion/)
can give me access to telnet of the router, which means I can
test internet from the source (or so I thought).


fortuantly telnet give me an embedded linux shell, so I made a 
script that downloads a 100MB file and mesure how much time it
took to download, and to isolate this mesurment from rest of the
network, the script blocks internet from connected users until
the file is fully downloaded, and reanble it afterward. 

```bash
trap iptables -D FORWARD -i br-lan -o eth0.2 -j DROP EXIT
while true ; do
    iptables -I FORWARD -i br-lan -o eth0.2 -j DROP
    echo $(date +%s), $( (time curl -s http://ash-speed.hetzner.com/100MB.bin -o /dev/null) 2>&1|grep re)>>/tmp/mes
    iptables -D FORWARD -i br-lan -o eth0.2 -j DROP
    sleep 10m
    done &
echo $! > /tmp/pid
```

also
from my computer download the mesurments result using FTP.

```bash
while true; do
    curl "ftp://root:root@192.168.31.1/tmp/mes" -o mes
    sleep 30m
done
```

and rewrite to be in a single command because the filesystem
is locked so cant write a script other than to /tmp, and
break it down so it would fit the command lenght limit on the
embedded shell.

```bash
QTEAA="iptables -I FORWARD -i br-lan -o eth0.2 -j DROP"
TLEQ="iptables -D FORWARD -i br-lan -o eth0.2 -j DROP"
CURL="curl -s http://ash-speed.hetzner.com/100MB.bin -o /dev/null"
trap "$TLEQ" EXIT;while true;do $QTEAA;echo $(date +%s), $( (time $CURL) 2>&1|grep re)>>/tmp/mes;$TLEQ;sleep 10m;done&echo $! > /tmp/pid
```

and a script used to visualize data

```python
import matplotlib.pyplot as plt

def extract(filename, timestamp, s):
    with open(filename, "r") as file:
        for ent in file:
            huh = ent.split(", real")
            timestamp += [ int(huh[0]) ]
            t = huh[1].split('m')
            s += [800 / ((float(t[0]) * 60) + float(t[1][:-2]))]
        file.close()


timestamp = []
s = []
# loglog was old mesurments before a router reboot so it doesnt get overwritten
extract("loglog", timestamp, s)
extract("mes", timestamp, s)

lyoma = 0
nharlflanflani = []
ss = [] # no affeliation with certain national socialists
for i  in range(len(timestamp)):
    if lyoma != timestamp[i] // 86400:
        lyoma = timestamp[i] // 86400
        nharlflanflani += [[]]
        ss += [[]]
    else:
        if timestamp[i] > timestamp[i-1] + 3600:
            nharlflanflani[-1] += [ timestamp[i] + 1 ]
            ss[-1] += [ float("NaN") ]
    nharlflanflani[-1] += [ timestamp[i] ]
    ss[-1] += [ s[i] ]

for i in range(len(nharlflanflani)):
    for j in range(len(nharlflanflani[i])):
        plt.plot([(k % 86400)/3600 for k in nharlflanflani[i]], ss[i])

plt.xlabel("Time of the day")
plt.ylabel("Internet Speed (Mbps)")
plt.show()
```

And there are the results:

![Image](/cebersec/Figure_2.png)

Well now I got it in 4k, soon while tinkering in the telnet
searching for which ISP, I found out that it wasnt a full
router, but a meer AP, which is odd, I tought the slow speed
was due to using LTE modem instead of fixed installation since
it was displaying that kind of behavior like speed penalties for
extensive bandwidth cosumption. so I tracked the routing down
to a HG8145X6-10 Optical Router Terminal, I found out the
credentials for the Web UI hardly from an Algerian reddit post
which weird, they where in my case "telecomadmin:admintelecom",
and then I discovered that 10 (or more) people are sharing this
single fiber optic subscription.

![Image](/cebersec/fo9ara2.png)

Well that explains the slow speed, and I descovered which ISP
was it, Maroc Telecom, but I was still curius whats the real
bandwidth ?, I found that this ONT have a telnet enabled, it
took me a long time to find the default crendtials from a
Bahreinien comment of a writeup blog of the same exploite,
while prevlege escalation and accessing a shell is possible,
the busybox shell was only two useless commands, meaning I
can't rerun the previous script.

The best I can do was to mesure the real trafic whithout
stress testing it, using this set of odd comands, but I found
the one to display statistics, averaging for 2 hours the speed
was 50 Mbps which is more intact whith the actuall speed for
optical fiber.

```bash
while true; do
        echo $(date +%s) >> tende
        (sleep 8; echo "display pon statistics"; sleep 5; echo "quit") | sshpass -p "adminHW" ssh root@192.168.100.1 2>&1| grep "Rx octets" >> tende
        sleep 10m
done
```
The same script as above with little modifications.

```python
import matplotlib.pyplot as plt

def extract(filename, timestamp, s):
    with open(filename, "r") as file:
        for ent in file:
            huh = ent.split(", Rx octets :")
            timestamp += [ int(huh[0]) ]
            s += [8 * int(huh[1]) ]
        file.close()

def d(L):
    dL = []
    for i in range(1, len(L)):
        dL += [ L[i] - L[i-1] ]
    return dL


timestamp = []
s = []

extract("tende", timestamp, s)

ds = d(s)
dt = d(timestamp)
s = [ds[i]/dt[i] for i in range(len(ds))]
timestamp = timestamp[1:]

lyoma = 0
nharlflanflani = []
ss = [] # no affeliation with certain national socialists
for i  in range(len(timestamp)):
    if lyoma != timestamp[i] // 86400:
        lyoma = timestamp[i] // 86400
        nharlflanflani += [[]]
        ss += [[]]
    else:
        if timestamp[i] > timestamp[i-1] + 3600:
            nharlflanflani[-1] += [ timestamp[i] + 1 ]
            ss[-1] += [ float("NaN") ]
    nharlflanflani[-1] += [ timestamp[i] ]
    ss[-1] += [ s[i] ]

for i in range(len(nharlflanflani)):
    for j in range(len(nharlflanflani[i])):
        plt.plot([(k % 86400)/3600 for k in nharlflanflani[i]], ss[i])

plt.xlabel("Time of the day")
plt.ylabel("Internet Speed (Mbps)")
plt.show()
```
![Image](/cebersec/Figure_3.png)
