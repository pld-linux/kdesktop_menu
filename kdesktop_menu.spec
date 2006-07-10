Summary:	A replacement menu for use with kicker (KDE)
Summary(pl):	Zamiennik menu dla KDE
Name:		kdesktop_menu
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kde-look.org/content/files/22605-%{name}-%{version}.tar.bz2
# Source0-md5:	c9095d41467d9256c334d552bb936e1e
URL:		http://www.kde-look.org/content/download.php?content=22605&id=1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDesktop Menu is a replacement menu for use with kicker (KDE). It was inspired
from the Gnome menu applet.... heavily.

%description -l pl
KDesktop Menu to zamiennik menu dla KDE zainspirowany przez menu GNOME.
 
%prep
%setup -q

%build
#cp -f /usr/share/automake/config.sub admin
#{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir} \
	--libdir=%{_libdir}/kde3
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/config.kcfg/*
