Name:       cairo

Summary:    A vector graphics library
Version:    1.17.4
Release:    1
License:    LGPLv2 or MPLv1.1
URL:        http://www.cairographics.org
Source0:    %{name}-%{version}.tar.xz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(freetype2) >= 9.7.3
BuildRequires:  pkgconfig(fontconfig) >= 2.2.95
BuildRequires:  pkgconfig(pixman-1) >= 0.30.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  libGLESv2-devel
BuildRequires:  libEGL-devel
BuildRequires:  binutils-devel

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
%autosetup -n %{name}-%{version}/upstream

%build

%autogen --disable-static \
    --disable-xlib \
    --enable-ps \
    --enable-pdf \
    --enable-svg \
    --enable-tee \
    --enable-xml \
    --enable-gobject \
    --enable-glesv3 \
    --disable-gtk-doc

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING-LGPL-2.1 COPYING-MPL-1.1 COPYING
%{_libdir}/libcairo*.so.*
%{_libdir}/cairo/cairo*.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/libcairo*.so
%{_libdir}/cairo/cairo*.so
%{_libdir}/pkgconfig/*

%files trace
%defattr(-,root,root,-)
%{_bindir}/cairo-trace
%exclude %{_libdir}/cairo/libcairo-trace.so
%{_libdir}/cairo/

%files gobject-devel
%defattr(-,root,root,-)
%{_includedir}/cairo/cairo-gobject.h
%{_libdir}/libcairo-gobject.so
%{_libdir}/pkgconfig/cairo-gobject.pc
