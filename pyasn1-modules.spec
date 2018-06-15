#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyasn1-modules
Version  : 0.2.1
Release  : 30
URL      : https://pypi.debian.net/pyasn1-modules/pyasn1-modules-0.2.1.tar.gz
Source0  : https://pypi.debian.net/pyasn1-modules/pyasn1-modules-0.2.1.tar.gz
Summary  : A collection of ASN.1-based protocols modules.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pyasn1-modules-python3
Requires: pyasn1-modules-python
Requires: pyasn1
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
ASN.1 modules for Python
------------------------
[![PyPI](https://img.shields.io/pypi/v/pyasn1-modules.svg?maxAge=2592000)](https://pypi.python.org/pypi/pyasn1-modules)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyasn1-modules.svg)](https://pypi.python.org/pypi/pyasn1-modules/)
[![Build status](https://travis-ci.org/etingof/pyasn1-modules.svg?branch=master)](https://secure.travis-ci.org/etingof/pyasn1-modules)
[![Coverage Status](https://img.shields.io/codecov/c/github/etingof/pyasn1-modules.svg)](https://codecov.io/github/etingof/pyasn1-modules/)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/pyasn1-modules/master/LICENSE.txt)

%package python
Summary: python components for the pyasn1-modules package.
Group: Default
Requires: pyasn1-modules-python3

%description python
python components for the pyasn1-modules package.


%package python3
Summary: python3 components for the pyasn1-modules package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyasn1-modules package.


%prep
%setup -q -n pyasn1-modules-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523298424
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
