%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{!?upstream_name: %global upstream_name openstack-congress}

Name:                   puppet-congress
Version:                10.4.0
Release:                1%{?dist}
Summary:                Puppet module for OpenStack Congress
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-congress

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-stdlib
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet-keystone

Requires:               puppet >= 2.7.0

%description
Installs and configures OpenStack Congress.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/congress/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/congress/



%files
%{_datadir}/openstack-puppet/modules/congress/


%changelog
* Fri Jan 19 2018 RDO <dev@lists.rdoproject.org> 10.4.0-1
- Update to 10.4.0

* Mon May 01 2017 rdo-trunk <javier.pena@redhat.com> 10.3.1-1
- Update to 10.3.1

* Fri Feb 10 2017 Haikel Guemar <hguemar@fedoraproject.org> 10.3.0-1
- Update to 10.3.0

* Mon Jan 09 2017 Dan Radez <dradez@redhat.com> - XXX-XXX
- Initial Packaging
