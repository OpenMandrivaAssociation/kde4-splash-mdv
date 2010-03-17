Name: kde4-splash-mdv
Summary: KDE Splash supporting SVG files
Version: 2009.1.3
Release: %mkrel 4
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
%setup -q -n %{name}-%{version}

%build 
%cmake_kde4 
%make

%install
rm -rf $RPM_BUILD_ROOT
pushd build
%makeinstall_std
popd

mkdir -p %{buildroot}/%{_datadir}/kde4/servicetypes
mkdir -p %{buildroot}/%{_datadir}/kde4/services
cp -a  ksplashplugin.desktop %{buildroot}/%{_datadir}/kde4/servicetypes
cp -a  kde4-splash-mdv.desktop %{buildroot}/%{_datadir}/kde4/services
ln -s %{_bindir}/kde4-splash-mdv %{buildroot}/%{_bindir}/ksplash

pushd build
%find_lang %name
popd

%clean 
rm -rf $RPM_BUILD_ROOT 

%files -f build/%{name}.lang
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/kde4-splash-mdv
%attr(755,root,root) %{_bindir}/ksplash
%{_datadir}/kde4/servicetypes/ksplashplugin.desktop
%{_datadir}/kde4/services/kde4-splash-mdv.desktop
