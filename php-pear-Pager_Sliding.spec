# Note: To be removed in favor of php-pear-Pager >= 2.0
%include	/usr/lib/rpm/macros.php
%define		_class		Pager
%define		_subclass	Sliding
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Sliding Window Pager
Summary(pl):	%{_pearname} - Stronnicowanie okienek z przewijaniem
Name:		php-pear-%{_pearname}
Version:	1.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	61c6d8e63c098efce4b04b99cfc81a30
URL:		http://pear.php.net/package/Pager_Sliding/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It takes an array of data as input and page it according to various
parameters. It also builds links within a specified range, and allows
complete customization of the output (it even works with mod_rewrite).
It is compatible with PEAR::Pager's API.

[Deprecated] Use PEAR::Pager v2.x with $mode = 'Sliding' instead.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa ta przyjmuje na wej¶ciu tablicê danych i stronnicuje je zgodnie
z ró¿nymi parametrami. Buduje tak¿e odno¶niki w ramach podanego
zakresu oraz pozwala na pe³ne dostosowanie wyj¶cia (dzia³a nawet z
mod_rewrite). Klasa jest kompatybilna z API PEAR::Pager.

[Niezalecany] U¿yj klasy PEAR::Pager v2.x z parametrem $mode = 'Sliding'.

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
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
