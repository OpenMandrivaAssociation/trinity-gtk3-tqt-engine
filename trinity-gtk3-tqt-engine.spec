%bcond clang 1

# TDE variables
%define tde_pkg gtk3-tqt-engine
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		14.1.6
Release:		1
Summary:		GTK3 theme engine for TDE
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/themes/%{tarball_name}-%{version}.tar.xz

BuildSystem:  	cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:  trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool


BuildRequires:  pkgconfig(gtk+-3.0)

%description
GTK3 style engine which uses the active TDE style to draw its widgets

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_prefix}/%{_lib}/libtqtcairo.so.0
%{tde_prefix}/%{_lib}/libtqtcairo.so.0.0.0
%{_libdir}/gtk-3.0/3.0.0/theming-engines/libtdegtk.la
%{_libdir}/gtk-3.0/3.0.0/theming-engines/libtdegtk.so
%{_libdir}/gtk-3.0/3.0.0/theming-engines/libtdegtk.so.0
%{_libdir}/gtk-3.0/3.0.0/theming-engines/libtdegtk.so.0.0.0
%dir %{_datadir}/themes/tdegtk
%dir %{_datadir}/themes/tdegtk/gtk-3.0
%{_datadir}/themes/tdegtk/gtk-3.0/gtk.css

##########

%package devel
Summary:		Files for the development of applications which will use %{name}
Group:			Development/Libraries
Requires:		%{name} = %{EVRD}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libtqtcairo.la
%{tde_prefix}/%{_lib}/libtqtcairo.so


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"

