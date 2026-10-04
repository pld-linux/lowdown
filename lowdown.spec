Summary:	Simple markdown translator library and tools
Summary(pl.UTF-8):	Prosta biblioteka i narzędzia do tłumaczenia formatu markdown
Name:		lowdown
Version:	3.2.1
Release:	1
License:	ISC
Group:		Applications/Text
Source0:	https://kristaps.bsd.lv/lowdown/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	b41be8a843aeec4c88450de3030ff635
URL:		https://kristaps.bsd.lv/lowdown/
BuildRequires:	bmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lowdown is a Markdown translator producing HTML5, roff documents in
the ms and man formats, LaTeX, gemini, OpenDocument, and terminal
output.

%description -l pl.UTF-8
lowdown to translator formatu Markdown, generujący HTML5, dokumenty
roff w formatach ms i man, LaTeXa, gemini, OpenDocument oraz tekst.

%package devel
Summary:	Header file for lowdown library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki lowdown
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header file for lowdown library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki lowdown.

%package static
Summary:	Static lowdown library
Summary(pl.UTF-8):	Statyczna biblioteka lowdown
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static lowdown library.

%description static -l pl.UTF-8
Statyczna biblioteka lowdown.

%prep
%setup -q

%build
# not autoconf configure
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./configure \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}" \
	MANDIR="%{_mandir}" \
	LINK_METHOD=shared

bmake

%install
rm -rf $RPM_BUILD_ROOT

bmake install install_libs \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PROGRAM="install -m755" \
	INSTALL_LIB="install -m755" \
	INSTALL_MAN="install -m644" \
	INSTALL_DATA="install -m644"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%attr(755,root,root) %{_bindir}/lowdown
%attr(755,root,root) %{_bindir}/lowdown-diff
%{_libdir}/liblowdown.so.5
%{_datadir}/lowdown
%{_mandir}/man1/lowdown.1*
%{_mandir}/man1/lowdown-diff.1*
%{_mandir}/man5/lowdown.5*

%files devel
%defattr(644,root,root,755)
%{_libdir}/liblowdown.so
%{_includedir}/lowdown.h
%{_pkgconfigdir}/lowdown.pc
%{_mandir}/man3/lowdown*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/liblowdown.a
