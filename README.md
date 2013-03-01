# zram for Fedora

__zram__ compresses swap partitions into RAM for performance.

You need Linux kernel version 2.6.37.1 or better to use 
__zram__.

### Automated Install

    sudo make install
    sudo systemctl daemon-reload
    systemctl enable zram.service
    systemctl start zram.service

### Manual Install

There are 3 files you need to enable __zram__ for __Fedora__. They
are:

* __zramstart__
* __zramstop__
* __zram.service__

All these files can be found in the project folder.

Place __"zramstart"__ and __"zramstop"__ in the following folder.

    __/usr/local/sbin__

Place __"zram.service"__ in the following folder.

    __/etc/systemd/system__

Place __"zram"__ in the following folder.

    __/etc/default__

As root, run the following command to enable __zram__ for __Fedora__.

    systemctl daemon-reload
    systemctl enable zram.service
    systemctl start zram.service

Run the following command to make sure the service started properly.

    systemctl status zram.service

The output should look like this.

    zram.service - Enable compressed swap in memory using zram
        Loaded: loaded (/etc/systemd/system/zram.service; enabled)
        Active: active (exited) since Sun, 02 Oct 2011 22:46:31 -0400; 44min ago
        Process: 942 ExecStart=/usr/local/sbin/zramstart (code=exited, status=0/SUCCESS)
        CGroup: name=systemd:/system/zram.service

That's it!

### Credits:

The __zramstart__ and __zramstop__ scripts were written by __Sergey
Davidoff__ of Elementary OS.

### References:

* http://www.webupd8.org/2011/10/increased-performance-in-linux-with.html
* http://code.google.com/p/compcache
* http://weirdfellow.wordpress.com/2011/05/04/compressed-ram-with-zram/
