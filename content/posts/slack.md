+++
title = "my thoughts on Slackware Linux"
description = "I think outloud"
date = 2026-05-28
draft = false

[taxonomies]
tags = ['Linux', 'IT']

+++

My main machine did not often get easy and reliable access to the internet.
 This would not have been a problem if it were not running Arch Linux.
 As everyone knows, it is a rolling release, and it is advised not to leave
 the system unupdated for long. Let us just say my ego made me deaf.

For the most part, I could update the system after months just fine,
although it was often a challenge and a time-consuming process that took
a day or so. Given that access to the internet the machine had was slow,
so much so I often had to check periodically whether pacman had
failed while downloading binaries, and if so rerun the command. That
lasted until February 2026, when I tried to update the system and was
greeted by a hundred lines of 'ldconfig: File /usr/lib/something.so.number
is empty, not checked' lines, and every library had been compressed to a
0-byte file. Needless to say, I had to chroot, but by then I was used to it.

After a week of unproductive poking and unsafe pacman commands, I figured
out that the easiest solution was to reinstall Arch altogether. If I was
going to do that, I might as well install a stable-release distribution
so I would not fall into the same trap. I hesitated at first between
Slackware and openSUSE. I saw that the stable-release version of openSUSE
is heavily marketed for enterprise users, and I thought Slackware had been
around for a long time, so it had probably matured into a stable system.
so I went with it.

Although it required knowledge of how Linux used to be installed and how
computers used to do things, the installation process was surprisingly
easy and user-friendly through a TUI. The only road bump I encountered
was installing a bootloader, since Slackware originally uses LILO. But
that was not much of a hurdle tp replace it with GRUB.


All was sunshine and rainbows until I wanted to install some software.
You see, Slackware does not just have a package manager. It has installpkg,
removepkg, upgradepkg, and an easy TUI called pkgtool to manage packages
from local tar files. That means downloading them has to be manual, and
reading the README files is not optional. The user is expected to infer
package dependencies from them, and then repeat the same process
recursively for each dependency. We already consider recursive algorithms
slow and inefficient, I do not know what adjective would be appropriate
if it were meant to be done by humans.

Ok newbie, I suppose you would prefer the 'slackpkg' utility, which lets
users install and upgrade official packages from Slackware’s servers, but
still leaves dependency resolution to the user. Even then, it is not that
complicated: packages managed with slackpkg can still be handled by
'installpkg' and the other tools. The catch is that the official repository
is limited, so a lot of software has to be installed through SlackBuilds,
which are build scripts rather than a package manager, where you still need
to download the build scripts and resolve dependencies manually and reading
READMEs (plural) is still mandatory. 'sbopkg' can help build queue files,
but the process still stays explicit and manual. the 'slackpkg+' extension
adds the option to install from third-party repositories and made updating
and upgrading easier but still dont't offer automatic dependency resolution.
Third-party tools simular to 'apt-get' and 'dnf' exists too such as
'slapt-get' and 'swaret', though they are not official Slackware tooling,
and I didnt bother since I wanted to put in the effort.

After I installed essential software, I wanted to treat myself to a bit
of gaming, so I tried to install Wine and Steam. That is where another
complication waited for me. It turns out that Slackware64 is out of the box
a pure 64-bit environment, and 32-bit compatibility is added through multilib,
throu a seperate 'sbopkg+' repo with additional steps, namely the users
should download every 32 bit packages then strip them of unnecessary/unwanted
files before reconstructing the compatible 32 bit pakages, quoting from the
multilib page of the Slackware wiki: "I decided that it would be a waste of
download bandwidth if I created 32bit compatibility versions of Slackware
packages myself. After all, you have probably bought the Slackware 14.2 DVD
so you already possess both 64bit and 32bit versions of Slackware… or else
the 32bit Slackware tree is available for free download of course ;-)", exept
I didn't and the only link I found for the tree was 5 READMEs deep and the
remote was down, luckly Claude found some mirrors for me (god knows from
where). I would have been fine if this were a one-time problem. I enjoyed
two days of uninterrupted ULTRAKILL after that, but then a kernel update
landed and multilib broke again, which meant redownloading and rebuilding
packages on my limited bandwidth. At that point I would rather pick a distro
with more robust package management, which is how I ended up on Void Linux
who is infinitly more usable.


There is a popular slang phrase in Morocco that goes "سلاك أ جمي" (Sslak a jmmi),
it means "I'll just need to get throu this", and it suprinsenly sums up my
experience with Sslak-ware, I understand that the choice of not including
a package manager is intentional to retain simplicity, but I dont get it,
a package amanger could be writen in a 100 lines of C, and it makes it
implicitly more bloated, as there is no official way to install packages
once the OS is installed the user might as well (and is recommended) to
install every package on the ISO, but it still don't cut it, an other
common argument is it's great for learning and getting your hands dirty
which I guess could be true if the comparisson is done against windows or
a user friendly distro, which the hole point for their existing is to
eliminate that problem, but if you compare with other just works distros
you will eventually be forced to get your hands dirty and learn sometimes,
not everytime wich makes them better for learning and worst for repeatetive
manual labour.

There is a popular slang phrase in Morocco that goes “سلاك أجمي” (Sslak a
jmmi), which means “I will just need to get through this,” and it
surprisingly sums up my experience with Slackware. I understand that not
including a package manager is intentional, to retain simplicity, but I do
not get it. A package manager could be written in 100 lines of C, and it
would make the system only marginally more bloated. Since there is no
official way to install packages once the OS is installed, the user might
as well (and is recommended to) install every package on the ISO, and that
still would not be enough. Another common argument is that it is great for
learning and getting your hands dirty, which could be true if the
comparison is against Windows or a user-friendly distro. But those distros
exist precisely to remove that problem. When compared with other “just
works” distros, you still end up learning and getting your hands dirty
sometimes, just not every time, which makes them better for learning and
less awful for repetitive manual labor.

