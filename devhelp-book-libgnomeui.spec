Summary:	DevHelp book: libgnomeui
Summary(pl):	Ksi±¿ka do DevHelp'a o libgnomeui
Name:		devhelp-book-libgnomeui
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libgnomeui.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about libgnomeui

%description -l pl
Ksi±¿ka do DevHelp o libgnomeui

%prep
%setup -q -c libgnomeui -n libgnomeui

%build
mv -f book libgnomeui
mv -f book.devhelp libgnomeui.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/libgnomeui-1.0
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install libgnomeui.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install libgnomeui/* $RPM_BUILD_ROOT%{_prefix}/books/libgnomeui-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
