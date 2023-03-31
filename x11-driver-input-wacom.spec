Name:		x11-driver-input-wacom
Version:	1.0.0
Release:	3
Summary:	X.org input driver for Wacom tablets
Group:		System/X11
License:	GPLv2+
URL:		http://www.x.org/
Source0:	https://github.com/linuxwacom/xf86-input-wacom/archive/xf86-input-wacom-%{version}.tar.bz2
Patch0:		xf86-input-wacom-0.19.0-fix-linking.patch
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xorg-server) >= 1.18
BuildRequires:	pkgconfig(xrandr)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
Obsoletes:	linuxwacom <= 0.8.4
Provides:	linuxwacom = %{version}-%{release}

%description
X.Org X11 wacom input driver for Wacom tablets.

%package devel
Summary:	Development files for %{name}
Group:		Development/X11
License:	MIT

%description devel
Development files for %{name}.

%prep
%autosetup -n xf86-input-wacom-%{version} -p1

%build
mkdir -p m4
autoreconf -fiv

%configure \
	--with-systemd-unit-dir=%{_unitdir} \
	--with-udev-rules-dir=%{_udevrulesdir}

%make_build

%install
%make_install
mv %{buildroot}/%{_udevrulesdir}/wacom.rules %{buildroot}/%{_udevrulesdir}/70-wacom.rules

%files
%{_bindir}/xsetwacom
%{_bindir}/isdv4-serial-debugger
%{_libdir}/xorg/modules/input/wacom_drv.so
%{_mandir}/man4/wacom.4*
%{_mandir}/man1/xsetwacom.1*
%{_datadir}/X11/xorg.conf.d/70-wacom.conf
%{_bindir}/isdv4-serial-inputattach
%{_prefix}/lib/udev/rules.d/70-wacom.rules
%{_unitdir}/wacom-inputattach@.service

%files devel
%{_includedir}/xorg/*
%{_libdir}/pkgconfig/xorg-wacom.pc
