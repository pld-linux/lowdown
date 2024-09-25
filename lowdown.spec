Summary:	Simple markdown translator library and tools
Summary(pl.UTF-8):	Prosta biblioteka i narzędzia do tłumaczenia formatu markdown
Name:		lowdown
Version:	1.1.1
Release:	1
License:	ISC
Group:		Applications/Text
Source0:	https://kristaps.bsd.lv/lowdown/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	a5af87053f2148efcbfcf58c388b4ef3
URL:		https://kristaps.bsd.lv/lowdown/
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
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for lowdown library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki lowdown.

%package static
Summary:	Static lowdown library
Summary(pl.UTF-8):	Statyczna biblioteka lowdown
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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
	MANDIR="%{_mandir}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install_libs \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PROGRAM="install -m755" \
	INSTALL_LIB="install -m755" \
	INSTALL_MAN="install -m644" \
	INSTALL_DATA="install -m644"

ln -sf liblowdown.so.1 $RPM_BUILD_ROOT%{_libdir}/liblowdown.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%attr(755,root,root) %{_bindir}/lowdown
%attr(755,root,root) %{_bindir}/lowdown-diff
%attr(755,root,root) %{_libdir}/liblowdown.so.1
%{_datadir}/lowdown
%{_mandir}/man1/lowdown.1*
%{_mandir}/man1/lowdown-diff.1*
%{_mandir}/man5/lowdown.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblowdown.so
%{_includedir}/lowdown.h
%{_pkgconfigdir}/lowdown.pc
%{_mandir}/man3/lowdown*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/liblowdown.a
