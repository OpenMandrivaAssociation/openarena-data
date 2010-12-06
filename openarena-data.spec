%define gamename openarena
%define name %{gamename}-data
%define rversion 0.8
%define baseversion %{rversion}.1
%define patchlevel 5
%define release %mkrel 2

%define bversion %(echo %{baseversion} | sed -e 's/\\.//g')
%if %{patchlevel}
%define patchversion %{rversion}.%{patchlevel}
%define pversion %(echo %{patchversion} | sed -e 's/\\.//g')
%endif
%define version %{?patchversion}%{!?patchversion:%{baseversion}}

Summary: An open-source content package for Quake III Arena
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://openarena.ws/rel/%{bversion}/oa%{bversion}.zip
%if %{patchlevel}
Source1: oa%{pversion}-patch.zip
%endif
License: Creative Commons
Group: Games/Arcade
Url: http://openarena.ws/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Conflicts: openarena <= 0.7.0-2%{distsuffix}%{mandriva_release}

%description
OpenArena is an open-source content package for Quake III Arena
licensed under the GPL, effectively creating a free stand-alone
game. You do not need Quake III Arena to play this game.

This package contains data files for OpenArena.

%prep
%setup -q -n %{gamename}-%{baseversion}
chmod 644 CHANGES CREDITS README
%if %{patchlevel}
yes | unzip -qq -d .. %{SOURCE1}
%endif

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
