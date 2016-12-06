PREFIX ?= /usr
SYSTEMD_UNITDIR ?= $(PREFIX)/lib/systemd/system
SYSCONFDIR ?= /etc/sysconfig
VERSION=1.0.2
SRC_FILES=Makefile README.md zram mkzram.service zram.spec zramstart zramstat zramstop

install:
	install -d $(DESTDIR)$(PREFIX)/sbin
	install -m 0755 zramstart $(DESTDIR)$(PREFIX)/sbin
	install -m 0755 zramstop $(DESTDIR)$(PREFIX)/sbin
	install -m 0755 zramstat $(DESTDIR)$(PREFIX)/sbin

	install -d $(DESTDIR)$(SYSTEMD_UNITDIR)
	install -m 0644 mkzram.service $(DESTDIR)$(SYSTEMD_UNITDIR)

	install -d $(DESTDIR)$(SYSCONFDIR)
	install -m 0644 zram $(DESTDIR)$(SYSCONFDIR)

.PHONY: clean
clean:
	rm -rf zram-$(VERSION) zram-$(VERSION).tar.bz2

.PHONY: tarball
tarball: clean
	mkdir zram-$(VERSION)
	cp -a $(SRC_FILES) zram-$(VERSION)/
	tar -cjvf zram-$(VERSION).tar.bz2 zram-$(VERSION)/
	rm -rf zram-$(VERSION)

.PHONY: rpm
rpm: tarball
	rpmbuild -tb zram-$(VERSION).tar.bz2

.PHONY: srpm
srpm: tarball
	rpmbuild -ts zram-$(VERSION).tar.bz2
