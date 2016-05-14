# zram for Fedora

__zram__ compresses swap partitions into RAM for performance.

You need Linux kernel version 2.6.37.1 or better to use 
__zram__. For Fedora 16 you can just install kmod-staging from
[rpmfusion](http://rpmfusion.org/Configuration/) to get the module:

    sudo yum install kmod-staging

### Automated Install

First you have to setup your rpm build environment. For details see
[How to create an RPM package - Preparing your system](http://fedoraproject.org/wiki/How_to_create_an_RPM_package#Preparing_your_system).

    # Short version of the howto
    sudo yum install @development-tools fedora-packager
    rpmdev-setuptree

    # the real thing(tm)
    make rpm
    sudo rpm -Uhv ~/rpmbuild/RPMS/noarch/zram-*.noarch.rpm

### Manual Install

There are 4 files you need to enable __zram__ for __Fedora__. They
are:

* __zramstart__
* __zramstat__
* __zramstop__
* __mkzram.service__

All these files can be found in the project directory.

Place __"zramstart"__, __zramstat__ and __"zramstop"__ in the following directory.

    /usr/sbin/

Place __"mkzram.service"__ in the following directory.

    /lib/systemd/system

Place __"zram"__ in the following directory.

    /etc/sysconfig

As root, run the following command to enable __zram__ for __Fedora__.

    systemctl daemon-reload

### Starting

    sudo systemctl enable mkzram.service
    sudo systemctl start mkzram.service

Run the following command to make sure the service started properly.

    sudo systemctl status mkzram.service

The output should look like this:

    mkzram.service - Enable compressed swap in memory using zram
        Loaded: loaded (/usr/lib/systemd/system/mkzram.service; enabled)
        Active: active (exited) since Mon 2015-11-30 12:26:21 UTC; 2min 45s ago
        Process: 2437 ExecStart=/usr/sbin/zramstart (code=exited, status=0/SUCCESS)
        Main PID: 2437 (code=exited, status=0/SUCCESS)

To see how well your compressed swap performs run

    zramstat # no sudo needed

The output looks like this:

    /dev/zram0:     362.18% (180998144 -> 49973309)
    /dev/zram1:     356.50% (180924416 -> 50749160)

This means 180,998,144 bytes got compressed to 49,973,309 bytes. The "swapped"
memory is 362.18% of the RAM used. That's it!

### Credits:

The __zramstart__ and __zramstop__ scripts were written by __Sergey
Davidoff__ of Elementary OS.
The __zramstat__ script and RPM packaging bits by Doncho N. Gunchev.

### References:

* http://www.webupd8.org/2011/10/increased-performance-in-linux-with.html
* http://code.google.com/p/compcache
* http://weirdfellow.wordpress.com/2011/05/04/compressed-ram-with-zram/
