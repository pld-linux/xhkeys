Summary:	xhkeys - a tool for assigning various actions to unused keys in X
Summary(pl):	xhkeys - narzêdzie do przypisywania nieu¿ywanym klawiszom ró¿nych akcji
Name:		xhkeys
Version:	2.2.1
Release:	1
License:	GPL
Group:		X11/Applications 
Source0:	http://www.geocities.com/wmalms/%{name}-%{version}.tar.gz
# Source0-md5:	412f498f833d5e07673261afa3d903bf
Patch0:		%{name}-DESTDIR.patch
URL:		http://wmalms.tripod.com
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

%description -l pl
Ta aplikacja zosta³a zaprojektowana z my¶l± o ka¿dej klawiaturze,
która ma dodatkowe klawisze normalnie nieprzydatne w systemie X Window
(np. klawisze multimedialne).

Za pomoc± xhkeys mo¿na przypisaæ jedn± z poni¿szych czynno¶ci do
dowolnego klawisza lub kombinacji klawiszy:
- operacja wbudowana (np. przechodzenie po oknach)
- wywo³anie zewnêtrznej aplikacji
- wywo³ywanie w³asnego modu³u (wtyczki)
- wys³anie zdarzenia klawiszowego do okre¶lonej aplikacji (symulacja
  naci¶niêcia/puszczenia klawisza)
- wys³anie zdarzenia myszy do okre¶lonej aplikacji (symulacja
  wci¶niêcia/puszczenia przycisku)

Cechy:
- OSD
- ci±g³e wywo³anie wtyczki (np. do monitorowania pozycji na ¶cie¿ce
  audio CD)

Pakiet zawiera narzêdzie do konfiguracji.

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
%doc XHkeys.sample manual.html
%attr(755,root,root) %{_bindir}/xhkeys
%attr(755,root,root) %{_bindir}/xhkconf
%dir %{_libdir}/xhkeys
%attr(755,root,root) %{_libdir}/xhkeys/xhkeys_cdaudio.so
%attr(755,root,root) %{_libdir}/xhkeys/xhkeys_mixer.so
