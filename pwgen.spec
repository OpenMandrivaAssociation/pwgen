Name:         pwgen
URL:          http://sourceforge.net/projects/pwgen/
License:      GPL
Group:        Text tools
Version:      2.08
Release:      1
Summary:      Password generator
Source:       http://prdownloads.sourceforge.net/pwgen/pwgen-%{version}.tar.gz
Source1:      https://salsa.debian.org/debian/makepasswd/-/archive/master/makepasswd-master.tar.bz2
BuildRequires: perl
BuildRequires: zlib-devel

%description
pwgen generates random, meaningless but pronounceable and thus easy to
remember passwords. The also contained makepasswd gives even more
options which are more aimed at security.

Authors:
--------
    Theodore Ts'o <tytso@alum.mit.edu> (this version)
    Brandon S. Allbery <allbery@ncoast.UUCP> (previous version)
    Rob Levin <levin@openproject.net> (previous version)

%prep
%setup -q -b 1
%autopatch -p1
cd ../makepasswd-master
chmod 644 *

%build
autoconf
%configure
%make_build

%install
mkdir -p	%{buildroot}%{_bindir}
mkdir -p	%{buildroot}%{_mandir}/man1
%make_install
cd ../makepasswd-master
install -m 755 makepasswd	%{buildroot}%{_bindir}/makepasswd2
install -m 644 makepasswd.1	%{buildroot}%{_mandir}/man1/makepasswd2.1

%files
%{_mandir}/man1/*
%{_bindir}/makepasswd2
%{_bindir}/pwgen
