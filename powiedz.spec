Summary:	Text to speech system
Summary(pl):	Syntezator mowy
Name:		powiedz
Version:	0.2
Release:	3
License:	GPL
Group:		Applications/Sound
Source0:	http://www.linux.bielsko.pl/%{name}_%{version}.tgz
# Source0-md5:	98e71acc4d24c4c9f83db7b52b306b6c
Patch0:		%{name}-rcfile.patch
Patch1:		%{name}-dsp-handle-fix.patch
Patch2:		%{name}-esd.patch
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish text to speech system based on rsynth.

%description -l pl
Polski syntezator mowy stworzony na podstawie rsynth.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} CFLAGS="%{rpmcflags} -DUSE_RC_FILE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

tail +3 <pars.def >$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/sayrc.example
mv -f klatt_par.doc klatt_par

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PRZECZYTAJ.TO README README.linux klatt_par
%attr(755,root,root) %{_bindir}/powiedz
%{_examplesdir}/%{name}-%{version}
