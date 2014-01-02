%bcond_with X11

Name:       cairo

Summary:    A vector graphics library
Version:    1.12.16
Release:    1
Group:      System/Libraries
License:    LGPLv2 or MPLv1.1
URL:        http://www.cairographics.org
Source0:    http://cairographics.org/releases/%{name}-%{version}.tar.xz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%if %{with X11}
BuildRequires:  pkgconfig(xrender) >= 0.6
BuildRequires:  pkgconfig(xcb-render) >= 0.16
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(freetype2) >= 9.7.3
BuildRequires:  pkgconfig(fontconfig) >= 2.2.95
BuildRequires:  pkgconfig(pixman-1) > 0.22.0
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
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pixman-devel

%description devel
Development package for the cairo library

%package trace
Summary:    Trace utility for cairo
License:    GPLv3
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description trace
%{summary}.


%package gobject-devel
Summary:    Development files for cairo-gobject
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description gobject-devel
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo Gobject library.



%prep
%setup -q -n %{name}-%{version}/%{name}

%build

%autogen --disable-static \
%if %{with X11}
    --enable-xlib \
%else
    --disable-xlib \
%endif
    --enable-ps \
    --enable-pdf \
    --enable-svg \
    --enable-tee \
    --enable-xml \
    --enable-gobject \
    --enable-glesv2 \
    --disable-gtk-doc \
%ifarch %{arm}
    --disable-atomic
%endif

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

gzip ChangeLog
gzip NEWS

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING-LGPL-2.1 COPYING-MPL-1.1 COPYING AUTHORS
%{_libdir}/libcairo*.so.*
%{_libdir}/cairo/cairo*.so*

%files devel
%defattr(-,root,root,-)
%doc ChangeLog.gz NEWS.gz PORTING_GUIDE BUGS
%{_includedir}/*
%{_libdir}/libcairo*.so
%{_libdir}/cairo/cairo*.so
%{_libdir}/pkgconfig/*
#%{_datadir}/gtk-doc/html/cairo

%files trace
%defattr(-,root,root,-)
%{_bindir}/cairo-trace
%{_bindir}/cairo-sphinx
%exclude %{_libdir}/cairo/libcairo-trace.so
%{_libdir}/cairo/libcairo-trace.so.*

%files gobject-devel
%defattr(-,root,root,-)
%{_includedir}/cairo/cairo-gobject.h
%{_libdir}/libcairo-gobject.so
%{_libdir}/pkgconfig/cairo-gobject.pc
