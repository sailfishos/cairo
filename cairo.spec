# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       cairo
Summary:    A vector graphics library
Version:    1.10.2
Release:    1
Group:      System/Libraries
License:    LGPLv2 or MPLv1.1
URL:        http://www.cairographics.org
Source0:    http://cairographics.org/releases/%{name}-%{version}.tar.gz
Source100:  cairo.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(glib-2.0)
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
Summary:    cairo-trace utility
License:    GPLv3
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description trace
cairo trace utility

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
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --enable-warnings \
    --enable-xlib \
    --enable-freetype \
    --enable-ps \
    --enable-pdf \
    --enable-svg \
    --enable-tee \
    --enable-gobject \
    --disable-gtk-doc \
%ifarch %{arm}
    --disable-atomic
%endif

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
gzip ChangeLog
gzip NEWS
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig











%files
%defattr(-,root,root,-)
# >> files
%doc COPYING-LGPL-2.1 COPYING-MPL-1.1 COPYING AUTHORS
%{_libdir}/libcairo*.so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc ChangeLog.gz NEWS.gz PORTING_GUIDE BUGS
%{_includedir}/*
%{_libdir}/libcairo*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/cairo
# << files devel

%files trace
%defattr(-,root,root,-)
# >> files trace
%{_bindir}/cairo-trace
%exclude %{_libdir}/cairo/libcairo-trace.so
%{_libdir}/cairo/libcairo-trace.so.*
# << files trace

%files gobject-devel
%defattr(-,root,root,-)
# >> files gobject-devel
%{_includedir}/cairo/cairo-gobject.h
%{_libdir}/libcairo-gobject.so
%{_libdir}/pkgconfig/cairo-gobject.pc
# << files gobject-devel

