%include	/usr/lib/rpm/macros.php
%define		_class		Pager
%define		_subclass	Sliding
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Sliding Window Pager
Summary(pl):	%{_pearname} - Stronnicowanie okienek z przewijaniem
Name:		php-pear-%{_pearname}
Version:	1.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	700fb47233b2c371991e74bf26acc453
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It takes an array of data as input and page it according to various
parameters. It also builds links within a specified range, and allows
complete customization of the output (it even works with mod_rewrite).
It is compatible with PEAR::Pager's API.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa ta przyjmuje na wej�ciu tablic� danych i stronnicuje je zgodnie
z r�nymi parametrami. Buduje tak�e odno�niki w ramach podanego
zakresu oraz pozwala na pe�ne dostosowanie wyj�cia (dzia�a nawet z
mod_rewrite). Klasa jest kompatybilna z API PEAR::Pager.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples/*
%{php_pear_dir}/%{_class}/*.php
