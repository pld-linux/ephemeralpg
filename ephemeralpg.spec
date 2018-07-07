Summary:	Run tests on an isolated, temporary PostgreSQL database
Name:		ephemeralpg
Version:	2.5
Release:	2
License:	ISC
Group:		Applications/Databases
URL:		http://ephemeralpg.org/
Source0:	http://ephemeralpg.org/code/%{name}-%{version}.tar.gz
# Source0-md5:	ba86b5f7a868f46fa314b0f6e563c750
Requires:	postgresql >= 9.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pg_tmp is a compact shell script designed to make unit testing,
integration testing with PostgreSQL easy in any language.

%prep
%setup -q -n eradman-%{name}-5041d6685332

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	MANPREFIX=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.md
%attr(755,root,root) %{_bindir}/getsocket
%attr(755,root,root) %{_bindir}/pg_tmp
%{_mandir}/man1/pg_tmp.1.*
%{_mandir}/man1/getsocket.1.*
