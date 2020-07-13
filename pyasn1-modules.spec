#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyasn1-modules
Version  : 0.2.8
Release  : 51
URL      : https://files.pythonhosted.org/packages/88/87/72eb9ccf8a58021c542de2588a867dbefc7556e14b2866d1e40e9e2b587e/pyasn1-modules-0.2.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/87/72eb9ccf8a58021c542de2588a867dbefc7556e14b2866d1e40e9e2b587e/pyasn1-modules-0.2.8.tar.gz
Summary  : A collection of ASN.1-based protocols modules.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pyasn1-modules-license = %{version}-%{release}
Requires: pyasn1-modules-python = %{version}-%{release}
Requires: pyasn1-modules-python3 = %{version}-%{release}
Requires: pyasn1
BuildRequires : buildreq-distutils3
BuildRequires : pyasn1

%description
ASN.1 modules for Python
------------------------
[![PyPI](https://img.shields.io/pypi/v/pyasn1-modules.svg?maxAge=2592000)](https://pypi.org/project/pyasn1-modules)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyasn1-modules.svg)](https://pypi.org/project/pyasn1-modules/)
[![Build status](https://travis-ci.org/etingof/pyasn1-modules.svg?branch=master)](https://travis-ci.org/etingof/pyasn1-modules)
[![Coverage Status](https://img.shields.io/codecov/c/github/etingof/pyasn1-modules.svg)](https://codecov.io/github/etingof/pyasn1-modules/)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/pyasn1-modules/master/LICENSE.txt)

%package license
Summary: license components for the pyasn1-modules package.
Group: Default

%description license
license components for the pyasn1-modules package.


%package python
Summary: python components for the pyasn1-modules package.
Group: Default
Requires: pyasn1-modules-python3 = %{version}-%{release}

%description python
python components for the pyasn1-modules package.


%package python3
Summary: python3 components for the pyasn1-modules package.
Group: Default
Requires: python3-core
Provides: pypi(pyasn1_modules)
Requires: pypi(pyasn1)

%description python3
python3 components for the pyasn1-modules package.


%prep
%setup -q -n pyasn1-modules-0.2.8
cd %{_builddir}/pyasn1-modules-0.2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583536484
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyasn1-modules
cp %{_builddir}/pyasn1-modules-0.2.8/LICENSE.txt %{buildroot}/usr/share/package-licenses/pyasn1-modules/7f822087024e192164d73581d9fba060445de7e8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyasn1-modules/7f822087024e192164d73581d9fba060445de7e8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
