%define gamename openarena
%define bversion 081
%define baseversion 0.8.1

Name:		%{gamename}-data
Summary:	An open-source content package for Quake III Arena
Version:	0.8.8
Release:	%mkrel 1
Source0:	http://openarena.ws/rel/%{bversion}/oa%{bversion}.zip
Source1:	oa085-patch.zip
Source2:	oa088-patch.zip
License:	Creative Commons
Group:		Games/Arcade
Url:		http://openarena.ws/
BuildArch:	noarch
Conflicts:	openarena <= 0.7.0-2%{distsuffix}%{mandriva_release}

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
