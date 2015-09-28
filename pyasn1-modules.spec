#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyasn1-modules
Version  : 0.0.8
Release  : 3
URL      : https://pypi.python.org/packages/source/p/pyasn1-modules/pyasn1-modules-0.0.8.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyasn1-modules/pyasn1-modules-0.0.8.tar.gz
Summary  : A collection of ASN.1-based protocols modules.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pyasn1-modules-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
ASN.1 modules for Python
------------------------
This is a small but growing collection of ASN.1 data structures
[1] expressed in Python terms using pyasn1 [2] data model.

%package python
Summary: python components for the pyasn1-modules package.
Group: Default

%description python
python components for the pyasn1-modules package.


%prep
%setup -q -n pyasn1-modules-0.0.8

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
