Summary:	DevHelp book: libgnomeui
Summary(pl):	Ksi±¿ka do DevHelpa o libgnomeui
Name:		devhelp-book-libgnomeui
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libgnomeui.tar.gz
# Source0-md5:	a8f1c95acb9da91009aac7592b8b9f88
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about libgnomeui.

%description -l pl
Ksi±¿ka do DevHelpa o libgnomeui.

%prep
%setup -q -c -n libgnomeui

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/libgnomeui-1.0,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/libgnomeui.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/libgnomeui-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
