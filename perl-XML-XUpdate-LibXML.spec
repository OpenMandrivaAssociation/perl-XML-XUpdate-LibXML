%define	module	XML-XUpdate-LibXML
%define	name	perl-%{module}
%define	version	0.6.0
%define release	8

Summary:	%{module} module for perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MPL
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRequires:	libxml2-devel >= 2.4.20
BuildRequires:	perl-devel
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::LibXML::XPathContext)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(pre):	libxml2
Requires(pre):  perl(XML::LibXML)
Requires(pre):	perl(XML::SAX)

%description
%{module} module for perl
Simple implementation of XUpdate format

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
%{makeinstall_std}

%preun -p /usr/bin/perl
use XML::SAX;
XML::SAX->remove_parser(q(XML::LibXML::SAX::Parser))->save_parsers();

%post -p /usr/bin/perl
use XML::SAX;
XML::SAX->add_parser(q(XML::LibXML::SAX::Parser))->save_parsers();

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{_bindir}/xupdate
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-7mdv2010.0
+ Revision: 430667
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-6mdv2009.0
+ Revision: 258883
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-5mdv2009.0
+ Revision: 246787
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.0-3mdv2008.1
+ Revision: 136369
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.6.0-3mdv2008.0
+ Revision: 23482
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.0-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Requires
	- Source URL

* Fri May 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.0-1mdk
- 0.6.0
- Make rpmbuildable
- Fix pre-requires

* Mon Aug 30 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.5.0-2mdk
- Fix pre-requires

* Thu Jun 03 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.5.0-1mdk
- 0.5.0
- cosmetics

* Tue Aug 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2-4mdk
- rebuild

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2-3mdk
- disable failling tests for now
- rebuild for new auto{prov,req}

