Summary:	Text to speech system
Summary(pl):	Syntezator mowy
Name:		powiedz
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.rivendell.eu.org/%{name}-%{version}.tgz
# Source0-md5:	e41665cc88c096473d48ff2fd32c4646
Patch0:		%{name}-dsp-handle-fix.patch
Patch1:		%{name}-Makefile.patch
Buildrequires:	arts-devel
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish text to speech system based on rsynth.

%description -l pl
Polski syntezator mowy stworzony na podstawie rsynth.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
cp Makefile_plain Makefile
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/artsc"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
tail +3 <pars.def >$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/sayrc.example

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_examplesdir}/%{name}-%{version}
