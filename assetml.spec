%define name		assetml
%define version      	1.2.1
%define release: 	10

%define major 0
%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d



Summary: Library assetml to share and reuse content like image and audio file
Name: 		%name
Version: 	%version
Release: 	%release
License: 	GPLv2+
Group: 		System/Libraries
Source:		lib%name-%version.tar.bz2
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

%configure2_5x

%make

%install
%makeinstall

%find_lang lib%name


%files -f lib%name.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL README THANKS
%_bindir/*
%_datadir/gnome/help/*
%_infodir/*

%files -n %libname
%defattr(-,root,root)
%_libdir/libassetml.so.*

%files -n %libnamedev
%defattr(-, root, root)
%_libdir/lib*.so
%_includedir/libassetml*/*
%_libdir/pkgconfig/libassetml.pc




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-7mdv2011.0
+ Revision: 616614
- the mass rebuild of 2010.0 packages

* Mon Jun 22 2009 Jérôme Brenier <incubusss@mandriva.org> 1.2.1-6mdv2010.0
+ Revision: 388026
- fix build (use configure2_5x)
- fix license tag

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-5mdv2009.0
+ Revision: 226184
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2.1-4mdv2008.1
+ Revision: 140690
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Nov 15 2006 Lenny Cartier <lenny@mandriva.com> 1.2.1-4mdv2007.0
+ Revision: 84433
- Import assetml

