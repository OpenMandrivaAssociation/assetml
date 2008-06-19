%define name		assetml
%define version      	1.2.1
%define release 	%mkrel 5

%define major 0
%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d



Summary: Library assetml to share and reuse content like image and audio file
Name: 		%name
Version: 	%version
Release: 	%release
License: 	GPL
Group: 		System/Libraries
Source:		lib%name-%version.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	glibc-devel
BuildRequires:	libxml2-devel
BuildRequires:	texi2html
BuildRequires:	texinfo
URL: 		http://ofset.sf.net/assetml

%description
This is a library based on an XML file format that is used to share and reuse 
content like image and audio file.
Application using this library can query files on their system that provides an
assetml xml file description.

%package -n %libname
Summary:        Library assetml to share image and audio file between project
Group:          System/Libraries

%description -n %libname
AssetML Library

%package  -n %libnamedev
Summary:        Devel Library assetml to share image and audio file between project
Group: 		System/Libraries
Requires:       %libname = %version
Provides:	libassetml-devel

%description -n %libnamedev
AssetML Devel Library

%prep

%setup -q -n lib%{name}-%version

%build

%configure

%make

%install
rm -Rf $RPM_BUILD_ROOT

%makeinstall

%find_lang lib%name

%post

%_install_info %{name}.info

%preun

%_remove_install_info %{name}.info

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f lib%name.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL README THANKS
%_bindir/*
%_datadir/gnome/help/*
%_infodir/*
%_bindir/*

%files -n %libname
%defattr(-,root,root)
%_libdir/libassetml.so.*

%files -n %libnamedev
%defattr(-, root, root)
%_libdir/lib*.so
%_libdir/*a
%_includedir/libassetml*/*
%_libdir/pkgconfig/libassetml.pc


