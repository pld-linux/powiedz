Summary:	Text to speech system
Summary(pl):	Syntezator mowy
Name:		powiedz
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://www.linux.bielsko.pl/%{name}_%{version}.tgz
Patch0:		%{name}-rcfile.patch
Patch1: 	%{name}-dsp-handle-fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish text to speech system based on rsynth.

%description -l pl
Polski syntezator mowy stworzony na podstawie rsynth.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} CFLAGS="%{rpmcflags} -DUSE_RC_FILE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}

tail +3 <pars.def >sayrc.example
mv -f klatt_par.doc klatt_par
gzip -9nf PRZECZYTAJ.TO README README.linux sayrc.example klatt_par

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/powiedz
