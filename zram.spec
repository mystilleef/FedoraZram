Summary: Enable compressed swap in memory
Name: zram
Version: 1.0.1
Release: 2%{?dist}
License: GPLv2
Group: System Environment/Daemons
Source0: %{name}-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: systemd-units
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires: filesystem >= 2.0.1, initscripts, bc > 1.0
# No debug info for bare scripts, right?
%define debug_package %{nil}
# http://fedoraproject.org/wiki/Changes/UnversionedDocdirs
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global _docdir_fmt %{name}

%description
zram compresses swap partitions into RAM for performance.

You need Linux kernel version 2.6.37.1 or better to use zram.


%prep
%setup -q


%build


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
ln -s $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/lib
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
%makeinstall DESTDIR=$RPM_BUILD_ROOT


%post
%systemd_post mkzram.service

%preun
%systemd_preun mkzram.service

%postun
%systemd_postun_with_restart mkzram.service

%files
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/mkzram.service
%{_sbindir}/zramstart
%{_sbindir}/zramstop
%{_sbindir}/zramstat
%exclude /lib


%changelog
* Tue Nov 25 2014 Juan Orti <jorti@fedoraproject.org> - 1.0.0-1
- Spec file cleanup

* Mon Nov 25 2013 Doncho Gunchev <dgunchev@gmail.com> - 0:1.0.0-2
- http://fedoraproject.org/wiki/Changes/UnversionedDocdirs
- Added kmod-staging dependency
- Test on Fedora 19

* Mon Sep 02 2013 Doncho Gunchev <dgunchev@gmail.com> - 0:1.0.0-1
- Add Darren Steven's build fix for fedora 18

* Tue Mar 19 2013 Doncho Gunchev <dgunchev@gmail.com> - 0:1.0.0-0
- Initial package
