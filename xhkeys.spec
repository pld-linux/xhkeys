Summary:	xhkeys - a tool for assigning various actions to unused keys in X
Summary(pl.UTF-8):   xhkeys - narzędzie do przypisywania nieużywanym klawiszom różnych akcji
Name:		xhkeys
Version:	2.2.1
Release:	1
License:	GPL
Group:		X11/Applications 
Source0:	http://www.geocities.com/wmalms/%{name}-%{version}.tar.gz
# Source0-md5:	412f498f833d5e07673261afa3d903bf
Patch0:		%{name}-DESTDIR.patch
URL:		http://wmalms.tripod.com/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application is designed to suit any PC keyboard that has some
extra keys that otherwise make no use with X (e.g. multimedia keys on
some keyboard models).

With xhkeys you can assign a particular action to any key or key
combination (key and shift state) that can be of one of the following
types:

 - built-in operation (e.g. window circulation)
 - calling an external application
 - calling a custom module (plugin)
 - sending a key event to a specified application (simulating key
   press/release)
 - sending a mouse button event to a specified application (simulating
   button press/release)

Features:
 - on-screen display
 - continuous plugin call (e.g. for monitoring CD Audio position)

The package includes configuration utility.

%description -l pl.UTF-8
Ta aplikacja została zaprojektowana z myślą o każdej klawiaturze,
która ma dodatkowe klawisze normalnie nieprzydatne w systemie X Window
(np. klawisze multimedialne).

Za pomocą xhkeys można przypisać jedną z poniższych czynności do
dowolnego klawisza lub kombinacji klawiszy:
- operacja wbudowana (np. przechodzenie po oknach)
- wywołanie zewnętrznej aplikacji
- wywoływanie własnego modułu (wtyczki)
- wysłanie zdarzenia klawiszowego do określonej aplikacji (symulacja
  naciśnięcia/puszczenia klawisza)
- wysłanie zdarzenia myszy do określonej aplikacji (symulacja
  wciśnięcia/puszczenia przycisku)

Cechy:
- OSD
- ciągłe wywołanie wtyczki (np. do monitorowania pozycji na ścieżce
  audio CD)

Pakiet zawiera narzędzie do konfiguracji.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	LDCONFIG=true \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install_doc \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES XHkeys.sample manual.html
%attr(755,root,root) %{_bindir}/xhkeys
%attr(755,root,root) %{_bindir}/xhkconf
%dir %{_libdir}/xhkeys
%attr(755,root,root) %{_libdir}/xhkeys/xhkeys_cdaudio.so
%attr(755,root,root) %{_libdir}/xhkeys/xhkeys_mixer.so
