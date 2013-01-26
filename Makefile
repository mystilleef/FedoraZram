PREFIX ?= /usr/local
SYSTEMD_UNITDIR ?= /etc/systemd/system
DEFAULTDIR ?= /etc/default

install:
	install -d $(DESTDIR)$(PREFIX)/sbin
	install -m 0755 zramstart $(DESTDIR)$(PREFIX)/sbin
	install -m 0755 zramstop $(DESTDIR)$(PREFIX)/sbin

	install -d $(DESTDIR)$(SYSTEMD_UNITDIR)
	install -m 0644 zram.service $(DESTDIR)$(SYSTEMD_UNITDIR)

	install -d $(DESTDIR)$(DEFAULTDIR)
	install -m 0644 zram $(DESTDIR)$(DEFAULTDIR)

