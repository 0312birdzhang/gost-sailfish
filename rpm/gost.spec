Name:       gost

# >> macros
#BuildArch: noarch
# << macros

Summary:    A simple security tunnel written in Golang
Version:    2.4
Release:    3
Group:      Applications/Internet
License:    MIT
Source0:    %{name}-%{version}.tar.bz2

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

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/bin
cp gost %{buildroot}/usr/bin/.
mkdir -p %{buildroot}/usr/lib/systemd/user
cp gost.service %{buildroot}/usr/lib/systemd/user/.
mkdir -p %{buildroot}/home/nemo/.config/gost
cp gost.json %{buildroot}/home/nemo/.config/gost/.
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%attr(0755, root, root) %{_bindir}/*
/usr/lib/systemd/user/
%dir %attr(0755, nemo, nemo) /home/nemo/.config/gost
%dir %attr(0644, nemo, nemo) /home/nemo/.config/gost/gost.json
# >> files
# << files
