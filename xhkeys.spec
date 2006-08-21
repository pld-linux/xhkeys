Summary:	xhkeys - a tool for assigning various actions to unused keys in X.
Summary(pl):	xhkeys - narzêdzie do przypisywania nieu¿ywanym w X'ach klawiszom ró¿nych akcji
Name:		xhkeys
Version:	2.2.1
Release:	1
License:	GPL

Vendor:		Michael Glickman <wmalms@yahoo.com>
Group:		X11/Applications 
######		Unknown group!
Source0:	http://www.geocities.com/wmalms/%{name}-%{version}.tar.gz
URL:		http://wmalms.tripod.com
BuildRequires:	sed
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
która ma dodatkowe klawisze normalnie nieprzydatne w X'ach (np.
klawisze multimedialne itd)

Za pomoc± xhkeys mo¿esz przypisaæ jedn± z poni¿szych czynno¶ci do
dowolnego klawisza lub kombinacji klawiszy:
- operacja wbudowana (e.g. przechodzenie po oknach)
- wywo³anie zewnêtrznej aplikacji
- wywo³ywanie pluginu
- wys³anie zdarzenia klawiszowego do okre¶lonej aplikacji (symulacja
  naci¶niêcia/puszczenia klawisza)
- wys³anie zdarzenia myszy do okre¶lonej aplikacji (symulacja
  wciêniêcia/puszczenia przycisku)

Cechy:
- OSD
- ci±g³e wywo³anie pluginu (np. do monitorowania pozycji na ¶cie¿ce
  audio CD)

Pakiet zawiera narzêdzie do konfiguracji.

%define prefix /usr

%prep
%setup -q

%build
export CFLAGS='-O4 -march=%_target_cpu -mcpu=%_target_cpu'
./configure --prefix=$RPM_BUILD_ROOT/%{_prefix}
mv Makefile Makefile.orig
sed -e "s/\$(LDCONFIG)/#\$(LDCONFIG)/g" Makefile.orig > Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install
%{__make} install_doc

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc XHkeys.sample
%doc manual.html
%doc xhkeys.lsm
%attr(755,root,root) %{_bindir}/xhkeys
%attr(755,root,root) %{_bindir}/xhkconf
%{_prefix}/lib/xhkeys/xhkeys_cdaudio.so
%{_prefix}/lib/xhkeys/xhkeys_mixer.so


%clean
rm -rf $RPM_BUILD_ROOT
