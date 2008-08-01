Name:         pwgen
URL:          http://sourceforge.net/projects/pwgen/
License:      GPL
Group:        Text tools
Version:      2.06
Release:      %mkrel 4
Summary:      Password generator
Source:       http://belnet.dl.sourceforge.net/sourceforge/pwgen/pwgen-%{version}.tar.gz
Source1:      ftp://ftp.linpeople.org/pub/People/lilo/source/makepasswd-1.10.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
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
cd ../makepasswd-1.10
chmod 644 *

%build
autoconf
%configure
%make

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p	${RPM_BUILD_ROOT}%_bindir
mkdir -p	${RPM_BUILD_ROOT}%{_mandir}/man1
%makeinstall_std	
cd ../makepasswd-1.10
install -m 755 makepasswd	$RPM_BUILD_ROOT%_bindir/makepasswd2
install -m 644 makepasswd.1	$RPM_BUILD_ROOT%{_mandir}/man1/makepasswd2.1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc ChangeLog
%{_mandir}/man1/*
%_bindir/makepasswd2
%_bindir/pwgen
