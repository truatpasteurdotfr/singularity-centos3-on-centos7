Name:		compat-db41
Version:	4.2.52
Release:	5.1.1%{?dist}
Summary:	quick and dirty db41_load
Group:		System Environment/Libraries
License:	BSD
URL:		http://www.oracle.com/database/berkeley-db/
Source:	compat-db-4.2.52-5.1.x86_64.rpm
Provides:  libdb-4.1.so()(64bit)
BuildRequires:	/usr/bin/rpm2cpio

%description
minimal compat-db41 for fixing rpm db4 on CentOS-7 host for a CentOS-3 container.

rpm2cpio  compat-db-4.2.52-5.1.x86_64.rpm| (cd /dev/shm && cpio -iudv ./usr/bin/db41_load ./lib64/libdb-4.1.so)
sudo cp /dev/shm/./usr/bin/db41_load /usr/bin/db41_lod
sudo cp  /dev/shm/./lib64/libdb-4.1.so /lib64/libdb-4.1.so

%prep
%setup -T -q -n compat-db-4.2.52-5.1.x86_64 -c
rpm2cpio %{_sourcedir}/compat-db-4.2.52-5.1.x86_64.rpm|  cpio -iudv ./usr/bin/db41_load ./lib64/libdb-4.1.so

%install
mkdir -p %{buildroot}/{%{_bindir},%{_libdir}}
install -m 0755 ./usr/bin/db41_load %{buildroot}%{_bindir}
install -m 0644 ./lib64/libdb-4.1.so %{buildroot}%{_libdir}

%files
%defattr(-,root,root)
%{_bindir}/db41_load
 %{_libdir}/libdb-4.1.so

%changelog
* Sun Jun 25 2017 Tru Huynh <tru@pasteur.fr> -
- initial release 
