Name:		asl
Version:	1.0.43
Release:	1%{?dist}
Summary:	Adobe Source Libraries

License:	MIT
URL:		http://stlab.adobe.com
Source0:	asl_1.0.43.tgz
Patch0:		asl-compile-without-boost.patch

BuildRequires:	boost-jam tbb-devel boost-build boost-devel

%description
Adobe Source Libraries

%prep
%setup -q -n source_release/
%patch0 -p1 -b boost.fix

%build
bjam link=shared %{name} release

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -D build/gcc-4.6.2/release/threading-multi/libasl.so $RPM_BUILD_ROOT%{_libdir}/libasl.so

%files
%{_libdir}/libasl.so

%changelog
* Mon Jan 30 2012 Aleksandra Bookwar <alpha@bookwar.info> - 1.0.43-1
- Initial build

