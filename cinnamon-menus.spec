Name:    cinnamon-menus
Version: 5.2.0
Release: 1
Summary: A menu system for the Cinnamon project
License: LGPLv2+
URL:     https://github.com/linuxmint/%{name} 
Source0: https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:   %{ix86}

BuildRequires: intltool
BuildRequires: meson
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: python3

%description
cinnamon-menus is an implementation of the draft "Desktop
Menu Specification" from freedesktop.org. This package
also contains the Cinnamon menu layout configuration files,
.directory files and assorted menu related utility programs,
Python bindings, and a simple menu editor.

%package devel
Summary: Libraries and include files for the Cinnamon menu system
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the necessary development libraries for
writing applications that use the Cinnamon menu system.

%prep
%autosetup -p1

%build
%meson \
 -Ddeprecated_warnings=false \
 -Denable_debug=false

%meson_build

%install
%meson_install
%ldconfig_scriptlets

%files
%doc AUTHORS NEWS
%license COPYING COPYING.LIB
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/CMenu-3.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/cinnamon-menus-3.0
%{_datadir}/gir-1.0/CMenu-3.0.gir

%changelog
* Fri May 6 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 5.2.0-1
- Inital Packaging
