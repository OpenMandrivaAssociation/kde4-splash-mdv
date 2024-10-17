Name: kde4-splash-mdv
Summary: KDE Splash supporting SVG files
Version: 2010.1.0
Release: %mkrel 4
License: GPL
URL: https://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/splash-mdv
Group: Graphical desktop/KDE
Source: %{name}-%{version}.tar.xz
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2010.1.0-3mdv2011.0
+ Revision: 666017
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.1.0-2mdv2011.0
+ Revision: 606259
- rebuild

* Mon May 10 2010 Funda Wang <fwang@mandriva.org> 2010.1.0-1mdv2010.1
+ Revision: 544313
- New version with newer translation updates

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2009.1.3-4mdv2010.1
+ Revision: 523155
- rebuilt for 2010.1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Use the lang macro to tag langs

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.1.3-2mdv2010.0
+ Revision: 425482
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 2009.1.3-1mdv2009.1
+ Revision: 367525
- translation updates

* Fri Apr 03 2009 Gustavo Pichorim Boiko <boiko@mandriva.com> 2009.1.2-1mdv2009.1
+ Revision: 363766
- New release fixing the problem of some stages not being properly displayed

* Thu Apr 02 2009 Gustavo Pichorim Boiko <boiko@mandriva.com> 2009.1.1-1mdv2009.1
+ Revision: 363588
- New release fixing the test mode (and thus the theme previewing)

* Sun Feb 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2009.1-3mdv2009.1
+ Revision: 343940
- Update translations

* Mon Jan 19 2009 Arthur Renato Mello <arthur@mandriva.com> 2009.1-2mdv2009.1
+ Revision: 331284
- Added nem messages for splash status
- Do not repeate animation if the same state is loaded twice

* Fri Dec 12 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2009.1-1mdv2009.1
+ Revision: 313600
- Add translations

* Tue Sep 30 2008 Arthur Renato Mello <arthur@mandriva.com> 2009.0-5mdv2009.0
+ Revision: 290191
- Adding cache support to SVG images
- Adding default status messages to all splash steps
- Adding translation strings support

* Thu Sep 25 2008 Arthur Renato Mello <arthur@mandriva.com> 2009.0-4mdv2009.0
+ Revision: 288230
- Adding support to --test and --theme

* Wed Sep 24 2008 Arthur Renato Mello <arthur@mandriva.com> 2009.0-3mdv2009.0
+ Revision: 287955
- Adding support to new ksplash themes with system settings information
- Adding KSplash/Plugin service type and service kde4-splash-mdv to make things work properly on system settings

* Tue Sep 23 2008 Arthur Renato Mello <arthur@mandriva.com> 2009.0-2mdv2009.0
+ Revision: 287606
- Make the main window override redirect. Removing some flicks between splash transitions
- Renaming package to a proper name
- Renaming package to a proper name
- Renaming package to a proper name
- Renaming package to a proper name
- Renaming the package to a proper name

* Mon Sep 22 2008 Arthur Renato Mello <arthur@mandriva.com> 2009.0-1mdv2009.0
+ Revision: 287084
- import splash-mdv

