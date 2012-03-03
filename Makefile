PREFIX ?= /usr
SYSTEMD_UNITDIR ?= /lib/systemd/system/

install:
	install -d $(DESTDIR)$(PREFIX)/sbin
	install -m 0755 zramstart $(DESTDIR)$(PREFIX)/sbin
	install -m 0755 zramstop $(DESTDIR)$(PREFIX)/sbin

	install -d $(DESTDIR)$(SYSTEMD_UNITDIR)
	install -m 0644 zram.service $(DESTDIR)$(SYSTEMD_UNITDIR)

