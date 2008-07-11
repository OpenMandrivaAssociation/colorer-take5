%define	major 0
%define libname %mklibname colorer %{major}
%define develname %mklibname colorer -d

Summary:	Syntax highlighting and text parsing library
Name:		colorer-take5
Version:	0
Release:	%mkrel 0.beta5.3
Group:		Text tools
License:	MPL
URL:		http://colorer.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/colorer/Colorer-take5-linux.be5.tar.bz2
Patch0:		colorer-optflags.diff
Patch1:		colorer-soname.diff
Patch2:		colorer-DESTDIR.diff
BuildRequires:	libstdc++-devel
Requires:	%{libname} = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Colorer take5 is a syntax highlighting and text parsing library, that provides
services of text parsing in host editor systems in real-time and transforming
results into colored text. Result information allows to search and build
outlined lists of functions, structures, and to search and indent programming
language constructions (brackets, paired tags). Colorer uses pure C++, XML, it
is fully portable and works on either win32/unix/mac platforms. Top level Java
language API is also available. 

%package -n	%{libname}
Summary:	Syntax highlighting and text parsing library
Group:          System/Libraries

%description -n	%{libname}
Colorer take5 is a syntax highlighting and text parsing library, that provides
services of text parsing in host editor systems in real-time and transforming
results into colored text. Result information allows to search and build
outlined lists of functions, structures, and to search and indent programming
language constructions (brackets, paired tags). Colorer uses pure C++, XML, it
is fully portable and works on either win32/unix/mac platforms. Top level Java
language API is also available. 

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C++
Requires:	%{libname} = %{version}
Requires:	%{name}-base = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	libcolorer-devel = %{version}-%{release}
Obsoletes:	%{mklibname colorer 0 -d}

%description -n	%{develname}
Colorer take5 is a syntax highlighting and text parsing library, that provides
services of text parsing in host editor systems in real-time and transforming
results into colored text. Result information allows to search and build
outlined lists of functions, structures, and to search and indent programming
language constructions (brackets, paired tags). Colorer uses pure C++, XML, it
is fully portable and works on either win32/unix/mac platforms. Top level Java
language API is also available. 

This package contains the development files for the %{name} library.

%package	docs
Summary:	Documentation for Colorer take5
Group:		Development/C++

%description	docs
Colorer take5 is a syntax highlighting and text parsing library, that provides
services of text parsing in host editor systems in real-time and transforming
results into colored text. Result information allows to search and build
outlined lists of functions, structures, and to search and indent programming
language constructions (brackets, paired tags). Colorer uses pure C++, XML, it
is fully portable and works on either win32/unix/mac platforms. Top level Java
language API is also available. 

This package contains the documentation for Colorer take5.

%package	base
Summary:	Common files for Colorer take5
Group:		Text tools

%description	base
Colorer take5 is a syntax highlighting and text parsing library, that provides
services of text parsing in host editor systems in real-time and transforming
results into colored text. Result information allows to search and build
outlined lists of functions, structures, and to search and indent programming
language constructions (brackets, paired tags). Colorer uses pure C++, XML, it
is fully portable and works on either win32/unix/mac platforms. Top level Java
language API is also available. 

This package contains common files for Colorer take5.

%prep

%setup -q -c -n %{name}
%patch0 -p0
%patch1 -p0
%patch2 -p0

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build

%configure

%make RPM_OPT_FLAGS="%{optflags} -fpermissive -Wall -fPIC"

%install
rm -rf %{buildroot}

%makeinstall_std

ln -snf libcolorer.so.%{major} %{buildroot}%{_libdir}/libcolorer.so

rm -f %{buildroot}%{_datadir}/colorer/{LICENSE,README}

rm -rf installed_docs
mv %{buildroot}%{_datadir}/doc/colorer-take5 installed_docs

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{_bindir}/colorer

%files -n %{libname}
%defattr(-,root,root,-)
%doc LICENSE README
%attr(0755,root,root) %{_libdir}/libcolorer.so.%{major}

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/colorer
%{_libdir}/libcolorer.so
%{_datadir}/colorer/bin

%files docs
%defattr(-,root,root,-)
%doc installed_docs/*

%files base
%defattr(-,root,root,-)
%{_datadir}/colorer/catalog.xml
%{_datadir}/colorer/hrc
%{_datadir}/colorer/hrd
