Name: kde4-splash-mdv
Summary: KDE Splash supporting SVG files
Version: 2009.0
Release: %mkrel 1
License: GPL
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/splash-mdv
Group: Graphical desktop/KDE
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel

Requires: kde4-config-file

%description
Splash Screen Engine for KDE4 supporting SVG files on the theme

%prep 
%setup -q -n kde4-splash-mdv

%build 
%cmake_kde4 
%make

%install
rm -rf $RPM_BUILD_ROOT
pushd build
%makeinstall_std
popd

%clean 
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/kde4-splash-mdv
