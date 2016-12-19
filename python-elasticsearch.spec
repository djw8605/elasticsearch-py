# Created by pyp2rpm-3.2.1
%global pypi_name elasticsearch

Name:           python-%{pypi_name}
Version:        5.0.1
Release:        1%{?dist}
Summary:        Python client for Elasticsearch

License:        Apache License, Version 2.0
URL:            https://github.com/elastic/elasticsearch-py
#Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-requests >= 1.0.0
BuildRequires:  python-requests < 3.0.0
BuildRequires:  python-nose
BuildRequires:  python-coverage
BuildRequires:  python-mock
BuildRequires:  python-pyaml
BuildRequires:  python-setuptools
#BuildRequires:  python-sphinx

%description
Python Elasticsearch Client Official lowlevel client for Elasticsearch. Its
goal is to provide common ground for all Elasticsearchrelated code in Python;
because of this it tries to be opinionfree and very extendable.For a more high
level client library with more limited scope, have a look at elasticsearchdsl_
a more pythonic library sitting on top of elasticsearchpy.It provides a more
...

%package -n     python2-%{pypi_name}
Summary:        Python client for Elasticsearch
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-urllib3 >= 1.8
Requires:       python-urllib3 < 2.0
Requires:       python-unittest2
%description -n python2-%{pypi_name}
Python Elasticsearch Client Official lowlevel client for Elasticsearch. Its
goal is to provide common ground for all Elasticsearchrelated code in Python;
because of this it tries to be opinionfree and very extendable.For a more high
level client library with more limited scope, have a look at elasticsearchdsl_
a more pythonic library sitting on top of elasticsearchpy.It provides a more
...

#%package -n python-%{pypi_name}-doc
#Summary:        elasticsearch documentation
#%description -n python-%{pypi_name}-doc
#Documentation for elasticsearch

%prep
%autosetup -n %{pypi_name}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
# generate html docs 
#sphinx-build docs html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
%py2_install


%check
%{__python2} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
#%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

#%files -n python-%{pypi_name}-doc
#%doc html 

%changelog
* Mon Dec 19 2016 Derek Weitzel <dweitzel@cse.unl.edu> - 5.0.1-1
- Initial package.
- Removing documentation building
