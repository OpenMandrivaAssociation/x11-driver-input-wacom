Name:		x11-driver-input-wacom
Version:	0.17.0
Release:	1
Summary:	X.org input driver for Wacom tablets
Group:		System/X11
License:	GPLv2+
URL:		http://www.x.org/
Source0:	http://freefr.dl.sourceforge.net/project/linuxwacom/xf86-input-wacom/xf86-input-wacom-%version.tar.bz2

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xorg-server) >= 1.12
BuildRequires:	pkgconfig(xrandr)

Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%rename		linuxwacom


%description
X.Org X11 wacom input driver for Wacom tablets.

%package	devel
Summary:	Development files for %{name}
Group:		Development/X11
License:	MIT

%description	devel
Development files for %{name}.

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
