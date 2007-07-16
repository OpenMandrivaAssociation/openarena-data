%define gamename openarena
%define name %{gamename}-data
%define version 0.7.0
%define release %mkrel 2
%define oversion %(echo %{version} | sed -e 's/\\.//g')

Summary: An open-source content package for Quake III Arena
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://openarena.ws/rel/%{oversion}/oa%{oversion}.zip
License: Creative Commons
Group: Games/Arcade
Url: http://openarena.ws/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Conflicts: openarena < 0.7.0-3mdv2008.0

%description
OpenArena is an open-source content package for Quake III Arena
licensed under the GPL, effectively creating a free stand-alone
game. You do not need Quake III Arena to play this game.

This package contains data files for OpenArena.

%prep
%setup -q -n %{gamename}-%{version}
chmod 644 CHANGES CREDITS README

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesdatadir}/%{gamename}/baseoa
install -m644 baseoa/* %{buildroot}%{_gamesdatadir}/%{gamename}/baseoa

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CREDITS README
%{_gamesdatadir}/%{gamename}/baseoa
