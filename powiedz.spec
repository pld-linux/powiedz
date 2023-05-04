#
# Conditional build:
%bcond_with	arts	# aRts support
%bcond_with	esd	# EsounD support

Summary:	Text to speech system
Summary(pl.UTF-8):	Syntezator mowy
Name:		powiedz
Version:	1.0
Release:	6
License:	GPL
Group:		Applications/Sound
Source0:	http://www.rivendell.eu.org/%{name}-%{version}.tgz
# Source0-md5:	e41665cc88c096473d48ff2fd32c4646
Patch0:		%{name}-dsp-handle-fix.patch
Patch1:		%{name}-Makefile.patch
%{?with_arts:BuildRequires:	artsc-devel}
%{?with_esd:BuildRequires:	esound-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish text to speech system based on rsynth.

%description -l pl.UTF-8
Polski syntezator mowy stworzony na podstawie rsynth.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} -f Makefile_plain \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} %{?with_arts:`artsc-config --cflags`}" \
	OPTDEFS="%{?with_arts:-DUSE_ARTS=1} %{?with_esd:-DUSE_ESD=1}" \
	OPTLIBS="%{?with_arts:`artsc-config --libs`} %{?with_esd:-lesd}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
tail -n +3 <pars.def >$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/sayrc.example

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/powiedz
%{_examplesdir}/%{name}-%{version}
