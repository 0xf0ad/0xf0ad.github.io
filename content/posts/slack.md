+++
title = "my thoughts on Slackware Linux"
description = "I think outloud"
date = 2026-02-28
draft = false

[taxonomies]
tags = ['Linux', 'IT']

+++

My main machine didnt often got easy and reliable access to internet,
 this whasnt gonnna be a problem if it wasn't running Arch Linux as everyone
 knows it's a rolling release, and it's advised to not let the system
 unupdated for long, and let just say my ego made me deaf.

For the most part I could update the system after mounths although
 often a challenge and time consuming process taking a day or so, giving
 if the machine have access to internet, it was slow so much so I often
 had to check periodicly if pacman failed downloding binaries, to rerun
 the command. That until I beleive feb 2026, when I tried to update the
 system, I've met up with a hundred lines of
 'ldconfig: File /usr/lib/something.so.number is empty, not checked'
 and every library is compressed to a 0 byte file, unnecessary to say
 I had to chroot but I had used to it by now.

After a week of unproductive poking and unsafe pacman commands, I figured
 out the easiest solution is to reinstall Arch all togother, if I would do
 that I might as well install a stable release distro so I wouldn't fall
 on the same trap. I hesitated between Slackware and openSUSE, I saw that
 the stable release version of openSUSE is heavly marketed for enterprise
 users, and I thought Slackware was around for a long time it probably had
 matured and converged into a stable version, other than being a stable
 release itself, so I went on with it.

Although it require knolegde of how Linux was used to get installed and how
 computers used to do stuff, the installation process was suprisinly easy
 and user frindly throu a TUI, the only road bump I incoutered was
 installing grub as Slackware oringinly uses LILO as its bootloader, but it
 didn't work well with my UEFI motherboard, but that wasn't much of a hurdle.

All was sunshine and rainbows, until I wanted to install some software,
 you see Slackware doen't just have a package manager, it has 'installpkg',
 'removepkg', 'upgradepkg' and an easy TUI 'pkgtool' to manage packages
 from local tar files, meaning downloading them should be manual, also
 meaning reading the README files are not optional, the user should infer
 from them package dependencies, to go with the same process for eack one
 of them recurssivly, we consider a recurssive algorithms slow and
 inefficient in programming, I don't know what would be an appropriet
 adjective for it if was ment to be ran by humains. Well newbie, I sound
 like you would prefer the 'slackpkg' utility which enables the user to
 install and upgrade packages from the internet but still leaves resolving
 dependencies to the user to do manually, until now it isn't that complicated
 'slackpkg' packages can still be managed by 'installpkg' and other tools,
 but the package repo is limited and a lot of software need to be installed
 by this other tool 'SlackBuild' an other diffrent package manager with a
 different installation / build process where you still need to manually
 download the build script for the package, read the READMEs (plural) (still
 mandatory), run the build script manually, then install using 'installpkg',
 at least it comes with a nice TUI tool 'sbopkg', witch allows the user to
 build a queue file, which compiles dependencies of a package into a queue
 to install automaticlly, but this step still is explicit from the user.
 An other option is the extension 'slackpkg+' which allowes the user to
 install packages from third party repositories and made updating and
 upgrading easier but still dont't offer automatic dependency resolution.
 As if these methods aren't enough already, there still other third party
 package managers designed to solve these problems by being similar to 
 'apt-get' or 'dnf' notably 'slapt-get' and 'swaret' which were not
 supported I didn't honestly tried it because although I wan't happy with
 the current state of package management, after put some effort I managed
 to install software that I needed and I thought set it and forget it thing...

After I installed the essentional software, I've wanted to treat myself
 with a bit of gaming, so I've tried to install wine and steam and there
 is another complication waiting for me, it turns out that Slackware
 packages are only 64 bit, with the 32 bit ones not only on a seperate
 repository only with the 'slackpkg+' extension, but with additional
 steps, namely the users should download every 32 bit packages then
 strip them of unnecessary/unwanted files before reconstructing the
 compatible 32 bit pakages, quoting from the multilib page of the Slackware
 wiki:"I decided that it would be a waste of download bandwidth if I created
 32bit compatibility versions of Slackware packages myself. After all,
 you have probably bought the Slackware 14.2 DVD so you already possess
 both 64bit and 32bit versions of Slackware… or else the 32bit Slackware
 tree is available for free download of course ;-)" exept I didn't and
 the only link I found fouildr the tree was 5 READMEs deep and was down,
 luckly Claude found some mirrors for me (god knows from where), not to
 mention I should also reinstall the Nvidia driver with a COMPAT32
 parameter, meaning manually, I would actually be fine if this was
 a one time problem, and enjoyed my 2 days of uninterupted UNLTRAKILL
 epic gamming after wards, but after that a kernel update got pushed
 and multilib is broken once more, meaning redownloading these packages
 again and rebuilding them on my limited bandwidth, I would rather
 pick and download any other distro which has more robust package
 management, I ended up on Void Linux, which is infinitly better in
 and and every way.

There is a popular slang in Morocco that goes "سلاك أ جمي" (Sslak a jmmi),
it means "I'll just need to get throu this", and it suprinsenly sums up my
experience with Sslak ware


