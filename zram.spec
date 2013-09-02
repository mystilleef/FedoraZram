Summary: Enable compressed swap in memory
Name: zram
Version: 1.0.0
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Daemons
Epoch: 0
URL: http://code.google.com/p/compcache/
Source: %{name}-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: systemd-units
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires: filesystem >= 2.0.1, initscripts, bc > 1.0
# No debug info for bare scripts, right?
%define debug_package %{nil}

%description
zram compresses swap partitions into RAM for performance.

You need Linux kernel version 2.6.37.1 or better to use zram.


%prep
%setup -q


%build
true


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
ln -s $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/lib
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
%makeinstall DESTDIR=$RPM_BUILD_ROOT


%post
if [ $1 -eq 1 ] ; then 
    # Initial installation
    /bin/systemctl enable zram.service >/dev/null 2>&1 || :
fi


%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable zram.service > /dev/null 2>&1 || :
    /bin/systemctl stop zram.service > /dev/null 2>&1 || :
fi


%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart zram.service >/dev/null 2>&1 || :
fi


%files
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/zram.service
%{_sbindir}/zramstart
%{_sbindir}/zramstop
%{_sbindir}/zramstat
%exclude /lib


%changelog
* Mon Sep 02 2013 Doncho Gunchev <dgunchev@gmail.com> - 0:1.0.0-1
- Add Darren Steven's build fix for fedora 18

* Tue Mar 19 2013 Doncho Gunchev <dgunchev@gmail.com> - 0:1.0.0-0
- Initial package
