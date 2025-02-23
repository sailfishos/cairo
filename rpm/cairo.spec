Name:       cairo

Summary:    A vector graphics library
Version:    1.18.2
Release:    1
License:    LGPLv2 or MPLv1.1
URL:        https://github.com/sailfishos/cairo
Source0:    %{name}-%{version}.tar.xz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(freetype2) >= 9.7.3
BuildRequires:  pkgconfig(fontconfig) >= 2.2.95
BuildRequires:  pkgconfig(pixman-1) >= 0.36.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  meson
BuildRequires:  ccache

%description
Cairo is a vector graphics library

%package devel
Summary:    Development components for the cairo library
Requires:   %{name} = %{version}-%{release}
Requires:   pixman-devel

%description devel
Development package for the cairo library

%package trace
Summary:    Trace utility for cairo
License:    GPLv3
Requires:   %{name} = %{version}-%{release}

%description trace
%{summary}.

%package gobject-devel
Summary:    Development files for cairo-gobject
Requires:   %{name} = %{version}-%{release}

%description gobject-devel
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo Gobject library.


%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build

%meson \
    -Dfontconfig=enabled \
    -Dfreetype=enabled \
    -Dglib=enabled \
    -Dgtk_doc=false \
    -Dpng=enabled \
    -Dspectre=disabled \
    -Dsymbol-lookup=disabled \
    -Dtee=disabled \
    -Dtests=disabled \
    -Dxcb=disabled \
    -Dxlib=disabled \
    -Dzlib=enabled

%meson_build

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING-LGPL-2.1 COPYING-MPL-1.1 COPYING
%{_libdir}/libcairo*.so.*

%files devel
%{_includedir}/*
%{_libdir}/libcairo*.so
%{_libdir}/pkgconfig/*

%files trace
%{_bindir}/cairo-trace
%exclude %{_libdir}/cairo/libcairo-trace.so
%{_libdir}/cairo/

%files gobject-devel
%{_includedir}/cairo/cairo-gobject.h
%{_libdir}/libcairo-gobject.so
%{_libdir}/pkgconfig/cairo-gobject.pc
