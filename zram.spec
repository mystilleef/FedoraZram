Summary: Enable compressed swap in memory
Name: zram
Version: 1.0.0
Release: 1%{?dist}
License: GPLv2 
Group: System Environment/Daemons
Source0: %{name}-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: bc > 1.0

%description
zram compresses swap partitions into RAM for performance.

You need Linux kernel version 2.6.37.1 or better to use zram.


%prep
%setup -q  


%build


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
%makeinstall DESTDIR=$RPM_BUILD_ROOT


%post
%systemd_post zram.service

%preun
%systemd_preun zram.service

%postun
%systemd_postun_with_restart zram.service

%files
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/zram.service
%{_sbindir}/zramstart
%{_sbindir}/zramstop
%{_sbindir}/zramstat


%changelog
* Tue Nov 25 2014 Juan Orti <jorti@fedoraproject.org> - 1.0.0-1
- Spec file cleanup

* Tue Mar 19 2013 Doncho Gunchev <dgunchev@gmail.com> - 1.0.0-0
- Initial package
