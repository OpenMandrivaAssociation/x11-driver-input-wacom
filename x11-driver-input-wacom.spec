Name: x11-driver-input-wacom
Version: 0.10.8
Release: %mkrel 3
Summary: X.org input driver for Wacom tablets
Group: System/X11
URL: http://www.x.org/
Source0: http://prdownloads.sourceforge.net/linuxwacom/xf86-input-wacom-%{version}.tar.bz2

License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libxi-devel

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

Obsoletes: linuxwacom <= 0.8.4
Provides: linuxwacom = %{version}-%{release}


%description
X.Org X11 wacom input driver for Wacom tablets.

%package devel
Summary: Development files for %{name}
Group: Development/X11
License: MIT

Obsoletes: %{_lib}wacom-devel <= 0.8.4
Provides: %{_lib}wacom-devel = %{version}-%{release}

%description devel
Development files for %{name}

%prep
%setup -q -n xf86-input-wacom-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/hal/fdi/policy/20thirdparty/
cp -a conf/wacom.fdi %{buildroot}%{_datadir}/hal/fdi/policy/20thirdparty/10-wacom.fdi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/xorg/modules/input/wacom_drv.la
%{_libdir}/xorg/modules/input/wacom_drv.so
%{_mandir}/man?/*
%{_datadir}/hal/fdi/policy/20thirdparty/10-wacom.fdi
%{_datadir}/X11/xorg.conf.d/50-wacom.conf

%files devel
%{_includedir}/xorg/*
%{_libdir}/pkgconfig/xorg-wacom.pc

