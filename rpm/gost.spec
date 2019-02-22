Name:       gost

Summary:    A simple security tunnel written in Golang
Version:    2.7.2
Release:    1
Group:      Applications/Internet
License:    MIT
Source0:    %{name}-%{version}.tar.bz2
Source1:    %{name}_%{version}_linux_386.tar.gz
Source2:    %{name}_%{version}_linux_arm.tar.gz

BuildRequire: tar systemd

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


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/bin
osarch=$(uname -p)
if [[ "$osarch" = *"arm"* ]]; then
  tar -xvf %{_sourcedir}/%{name}_%{version}_linux_arm.tar.gz
  cp %{name}_%{version}_linux_arm/gost %{buildroot}/usr/bin/.
else
  tar -xvf %{_sourcedir}/%{name}_%{version}_linux_arm.386.gz
  cp %{name}_%{version}_linux_386/gost %{buildroot}/usr/bin/.
fi

mkdir -p %{buildroot}%{_libdir}/systemd/user
cp gost.service %{buildroot}%{_libdir}/systemd/user/.
mkdir -p %{buildroot}/home/nemo/.config/gost
cp gost.json %{buildroot}/home/nemo/.config/gost/.
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%attr(0755, root, root) %{_bindir}/
%{_libdir}/systemd/user/
%dir /home/nemo/.config/gost
%attr(0644, nemo, nemo) /home/nemo/.config/gost/gost.json
# >> files
# << files
