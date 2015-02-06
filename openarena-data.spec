%define gamename openarena
%define bversion 081
%define baseversion 0.8.1

Name:		%{gamename}-data
Summary:	An open-source content package for Quake III Arena
Version:	0.8.8
Release:	3
Source0:	http://openarena.ws/rel/%{bversion}/oa%{bversion}.zip
Source1:	oa085-patch.zip
Source2:	oa088-patch.zip
License:	Creative Commons
Group:		Games/Arcade
Url:		http://openarena.ws/
BuildArch:	noarch

%description
OpenArena is an open-source content package for Quake III Arena
licensed under the GPL, effectively creating a free stand-alone
game. You do not need Quake III Arena to play this game.

This package contains data files for OpenArena.

%prep
%setup -q -n %{gamename}-%{baseversion}
chmod 644 CHANGES CREDITS README
yes | unzip -qq -d .. %{SOURCE1}
yes | unzip -qq -d .. %{SOURCE2}

%build

%install
%__rm -rf %{buildroot}
%__install -d %{buildroot}%{_gamesdatadir}/%{gamename}/baseoa
%__install -m644 baseoa/* %{buildroot}%{_gamesdatadir}/%{gamename}/baseoa

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CREDITS README
%{_gamesdatadir}/%{gamename}/baseoa


%changelog
* Tue Feb 21 2012 Andrey Bondrov <abondrov@mandriva.org> 0.8.8-1mdv2011.0
+ Revision: 778534
- New version 0.8.8, make spec less complicated

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.5-2mdv2011.0
+ Revision: 613176
- rebuild

* Mon Mar 08 2010 Thierry Vignaud <tv@mandriva.org> 0.8.5-1mdv2010.1
+ Revision: 515992
- new release

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.8.1-2mdv2010.0
+ Revision: 440382
- rebuild

* Sat Nov 08 2008 Adam Williamson <awilliamson@mandriva.org> 0.8.1-1mdv2009.1
+ Revision: 301159
- new release 0.8.1

* Sat Aug 30 2008 Funda Wang <fwang@mandriva.org> 0.8.0-2mdv2009.0
+ Revision: 277560
- bump release
- New version 0.8.0

* Mon Aug 04 2008 Funda Wang <fwang@mandriva.org> 0.7.7-2mdv2009.0
+ Revision: 263059
- rebuild
- Patch077

* Tue Apr 22 2008 Olivier Blin <blino@mandriva.org> 0.7.6-1mdv2009.0
+ Revision: 196678
- 0.7.6
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.1-3mdv2008.0
+ Revision: 90022
- rebuild

* Fri Aug 10 2007 Olivier Blin <blino@mandriva.org> 0.7.1-2mdv2008.0
+ Revision: 61654
- use mandriva_release macro in conflicts to ease backports

* Thu Aug 09 2007 Olivier Blin <blino@mandriva.org> 1mdv2008.0-current
+ Revision: 60899
- 0.7.1 (add additionnal patch pk3)

* Mon Jul 16 2007 Olivier Blin <blino@mandriva.org> 0.7.0-2mdv2008.0
+ Revision: 52409
- conflicts with openarena releases that did not convert the baseoa dir to a symlink

* Thu Jul 12 2007 Olivier Blin <blino@mandriva.org> 0.7.0-1mdv2008.0
+ Revision: 51576
- initial openarena-data package (split out of openarena)
- Create openarena-data

