%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	MAC
%define		_status		alpha
%define		_pearname	Net_MAC
Summary:	%{_pearname} - validates and formats MAC addresses
Summary(pl.UTF-8):	%{_pearname} - kontrola poprawności i formatowanie adresów MAC
Name:		php-pear-%{_pearname}
Version:	0.1.5
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a518dbb6fb6517eb4fc47bb7dacfcfd4
URL:		http://pear.php.net/package/Net_MAC/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package validates and cleanly formats Media Access Control (MAC)
addresses. The Net_MAC class can also import a list of MAC address
vendors and store them in a database which the class can then use to
identify vendors of any MAC address.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten sprawdza poprawnoaść oraz formatuje adres Media Access
Control (MAC). Klasa Net_MAC pozwala także na import listy dostawców
MAC i zapisanie jej w bazie, z której klasa ta może skorzystać do
identyfikacji adresów.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/MAC.php
