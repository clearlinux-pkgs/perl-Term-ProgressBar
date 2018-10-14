#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Term-ProgressBar
Version  : 2.22
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Term-ProgressBar-2.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Term-ProgressBar-2.22.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libterm-progressbar-perl/libterm-progressbar-perl_2.22-1.debian.tar.xz
Summary  : 'provide a progress meter on a standard terminal'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(Class::MethodMaker)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Term::ReadKey)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Test::Warnings)

%description
Module Term-ProgressBar (2.09):
Description:
A progress bar for things that take a while.  It looks like

%package dev
Summary: dev components for the perl-Term-ProgressBar package.
Group: Development
Provides: perl-Term-ProgressBar-devel = %{version}-%{release}

%description dev
dev components for the perl-Term-ProgressBar package.


%prep
%setup -q -n Term-ProgressBar-2.22
cd ..
%setup -q -T -D -n Term-ProgressBar-2.22 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Term-ProgressBar-2.22/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/Term/ProgressBar.pm
/usr/lib/perl5/vendor_perl/5.26.1/Term/ProgressBar/IO.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Term::ProgressBar.3
/usr/share/man/man3/Term::ProgressBar::IO.3
