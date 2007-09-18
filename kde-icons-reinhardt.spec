%define base_name	kde-icons
%define theme_name	reinhardt
%define version		0.8
%define name		%{base_name}-%{theme_name}
%define release		%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Reinhardt icons for KDE Desktop
License:	LGPL
Group:		Graphical desktop/KDE
Source:		%{theme_name}icons-%{version}.tar.bz2
URL:		http://kde-look.org/content/show.php?content=6153
Requires:	kdebase-progs kdegraphics-ksvg
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is The Reinhardt Icon Set                       

- This icon set has been created for use with the Reinhardt Style
  available from the kde-look site at ( www.kde-look.org ), and is a
  proposal for the default Slicker icon set.
- If you wish to have the icons a different colour, this is possible by
  selecting the Icons section of the Control Panel, then selecting Advanced.
  Here you can set the effect used on all the icons, one of which is
  Colouration. (thanks to spooq for this tip)
- All the original SVGs are included (sorted in the proper way, under
  ./scalable, for when KDE gets proper svg support for icons).
- The icon set is based on an original concept by Alexander Smith.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{theme_name}icons-%{version}

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/icons/%{theme_name}-%{version}
cp -r 16x16/ 22x22/ 32x32/ 48x48/ 64x64/ 128x128/ scalable/ index.desktop index.desktop.svg $RPM_BUILD_ROOT/%{_datadir}/icons/%{theme_name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc icon-guidelines.txt README 
%{_iconsdir}/%{theme_name}-%{version}/*
