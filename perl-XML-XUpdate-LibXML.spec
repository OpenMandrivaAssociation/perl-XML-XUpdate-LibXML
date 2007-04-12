%define	module	XML-XUpdate-LibXML
%define	name	perl-%{module}
%define	version	0.6.0
%define	release	%mkrel 2

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

