%define upstream_name	 Net-CIDR-Lite
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl extension for merging IPv4 or IPv6 CIDR addresses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

BuildArch:	noarch

%description
Faster alternative to Net::CIDR when merging a large number of CIDR address
ranges. Works for IPv4 and IPv6 addresses.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc Changes README
%{perl_vendorlib}/Net
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.210.0-4mdv2012.0
+ Revision: 765521
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.210.0-3
+ Revision: 764037
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.210.0-2
+ Revision: 667268
- mass rebuild

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 527743
- update to 0.21

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 404064
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.20-5mdv2009.1
+ Revision: 351848
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.20-4mdv2009.0
+ Revision: 223848
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.20-3mdv2008.1
+ Revision: 180493
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-2mdv2007.0
+ Revision: 134315
- rebuild
- Import perl-Net-CIDR-Lite

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdk
- New release 0.20

* Thu Feb 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdk
- New release 0.19
- %%mkrel

* Thu Jun 02 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdk
- New release 0.18
- spec cleanup
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.15-2mdk
- fix buildrequires in a backward compatible way

* Sun Nov 14 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.15-1mdk 
- first mdk release

