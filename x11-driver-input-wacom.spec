Name: x11-driver-input-wacom
Version: 0.16.0
Release: 1
Summary: X.org input driver for Wacom tablets
Group: System/X11
License: GPLv2+
URL: http://www.x.org/
Source0: http://freefr.dl.sourceforge.net/project/linuxwacom/xf86-input-wacom/xf86-input-wacom-%version.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xorg-server) >= 1.12
BuildRequires: pkgconfig(xrandr)

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

Obsoletes: linuxwacom <= 0.8.4
Provides: linuxwacom = %{version}-%{release}


%description
X.Org X11 wacom input driver for Wacom tablets.

%package devel
Summary: Development files for %{name}
Group: Development/X11
License: MIT

%description devel
Development files for %{name}

%prep
%setup -q -n xf86-input-wacom-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xsetwacom
%{_bindir}/isdv4-serial-debugger
%{_libdir}/xorg/modules/input/wacom_drv.so
%{_mandir}/man4/wacom.4*
%{_mandir}/man1/xsetwacom.1*
%{_datadir}/X11/xorg.conf.d/50-wacom.conf

%files devel
%{_includedir}/xorg/*
%{_libdir}/pkgconfig/xorg-wacom.pc


%changelog
* Mon Jun 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.15.0-1
+ Revision: 806792
- version update 0.15.0

* Fri Apr 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.14.0-2
+ Revision: 794109
- rebuild
- do not obsolete new libwacom devel pkg
- cleaned up spec

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.14.0-1
+ Revision: 787192
- Update to 0.14.0
- Build for x11-server 1.12

* Mon Feb 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.13.0-1
+ Revision: 773785
- BuildReq: xinerama x11
- version update 0.13.0

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.11.0-3
+ Revision: 703625
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.11.0-2
+ Revision: 683572
- Rebuild for new x11-server

* Wed May 25 2011 Funda Wang <fwang@mandriva.org> 0.11.0-1
+ Revision: 679001
- br udev
- update to new version 0.11.0

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.10-2
+ Revision: 671135
- mass rebuild

* Sun Jan 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.10.10-1
+ Revision: 631153
- new version

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.10.8-3mdv2011.0
+ Revision: 595759
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.10.8-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9
- new release
- drop patch0 (merged upstream)
- adjust file list
- manuall install HAL file for now

* Thu May 06 2010 Frederic Crozat <fcrozat@mandriva.com> 0.10.6-1mdv2010.1
+ Revision: 542957
- Release 0.10.6

* Tue Apr 13 2010 Frederic Crozat <fcrozat@mandriva.com> 0.10.5-1mdv2010.1
+ Revision: 534186
- Release 0.10.5

* Mon Mar 15 2010 Frederic Crozat <fcrozat@mandriva.com> 0.10.4-4mdv2010.1
+ Revision: 519826
- Patch0 (Ubuntu forums): add support for N-Trig hardware

* Thu Feb 25 2010 Frederic Crozat <fcrozat@mandriva.com> 0.10.4-3mdv2010.1
+ Revision: 511132
- force rebuild
- force rebuild
- import x11-driver-input-wacom

