%global _missing_build_ids_terminate_build 0
%define debug_package %{nil}


Name:       gost

Summary:    A simple security tunnel written in Golang
Version:    2.7.2
Release:    1
Group:      Applications/Internet
License:    MIT
Source0:    %{name}-%{version}.tar.bz2

BuildRequires: tar systemd

%description
A simple security tunnel written in Golang


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

# >> build post
# << build post

%post
systemctl-user daemon-reload

%preun
systemctl-user daemon-reload

%postun
systemctl-user stop gost.service


%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/bin
osarch=$(uname -p)
if [[ "$osarch" = *"arm"* ]]; then
  tar -xvf %{name}_2.7.2_linux_arm.tar.gz
  install -m 755  %{name}_2.7.2_linux_arm/gost %{buildroot}/usr/bin/gost
else
  tar -xvf %{name}_2.7.2_linux_386.tar.gz
  install -m 755  %{name}_2.7.2_linux_386/gost %{buildroot}/usr/bin/gost
fi

mkdir -p %{buildroot}%{_libdir}/systemd/user
cp gost.service %{buildroot}%{_libdir}/systemd/user/.
mkdir -p %{buildroot}/home/nemo/.config/gost
cp gost.json %{buildroot}/home/nemo/.config/gost/gost.json
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%attr(0755, root, root) %{_bindir}/
%{_libdir}/systemd/user/
%dir %attr(0755, nemo, nemo) /home/nemo/.config/gost
%attr(0644, nemo, nemo) /home/nemo/.config/gost/gost.json
# >> files
# << files
