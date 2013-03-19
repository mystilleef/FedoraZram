PREFIX ?= /usr
SYSTEMD_UNITDIR ?= /etc/systemd/system
SYSCONFDIR ?= /etc/sysconfing

install:
	install -d $(DESTDIR)$(PREFIX)/sbin
	install -m 0755 zramstart $(DESTDIR)$(PREFIX)/sbin
	install -m 0755 zramstop $(DESTDIR)$(PREFIX)/sbin

	install -d $(DESTDIR)$(SYSTEMD_UNITDIR)
	install -m 0644 zram.service $(DESTDIR)$(SYSTEMD_UNITDIR)

	install -d $(DESTDIR)$(SYSCONFDIR)
	install -m 0644 zram $(DESTDIR)$(SYSCONFDIR)

