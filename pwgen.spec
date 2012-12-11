Name:         pwgen
URL:          http://sourceforge.net/projects/pwgen/
License:      GPL
Group:        Text tools
Version:      2.06
Release:      %mkrel 6
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


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.06-6mdv2010.0
+ Revision: 433733
- rebuild
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.06-4mdv2009.0
+ Revision: 259371
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.06-3mdv2009.0
+ Revision: 247246
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.06-1mdv2008.1
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Olivier Thauvin <nanardon@mandriva.org> 2.06-1mdv2008.0
+ Revision: 52625
- 2.06


* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/08/06 00:02:25 (54297)
- rebuild

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/08/06 00:00:47 (54294)
Import pwgen

* Sun Feb 12 2006 Olivier Thauvin <nanardon@mandriva.org> 2.05-1mdk
- 2.05

* Wed Sep 07 2005 Olivier Thauvin <nanardon@mandriva.org> 2.04-1mdk
- 2.04

* Sat Aug 28 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.03-2mdk
- fix conflict with makepasswd

* Tue Aug 17 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.03-1mdk
- First mdk contrib from Suse spec

