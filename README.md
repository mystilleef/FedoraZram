# zram for Fedora

__zram__ compresses swap partitions into RAM for performance.

You need Linux kernel version 2.6.37.1 or better to use 
__zram__.

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
* __zram.service__

All these files can be found in the project folder.

Place __"zramstart"__, __zramstat__ and __"zramstop"__ in the following folder.

    __/usr/sbin__

Place __"zram.service"__ in the following folder.

    __/lib/systemd/system__

Place __"zram"__ in the following folder.

    __/etc/sysconfig__

As root, run the following command to enable __zram__ for __Fedora__.

    systemctl daemon-reload

### Starting

    sudo systemctl enable zram.service
    sudo systemctl start zram.service

Run the following command to make sure the service started properly.

    sudo systemctl status zram.service

The output should look like this:

    zram.service - Enable compressed swap in memory using zram
        Loaded: loaded (/lib/systemd/system/zram.service; enabled)
        Active: active (exited) since Sun, 02 Oct 2011 22:46:31 -0400; 44min ago
        Process: 942 ExecStart=/usr/sbin/zramstart (code=exited, status=0/SUCCESS)
        CGroup: name=systemd:/system/zram.service

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
