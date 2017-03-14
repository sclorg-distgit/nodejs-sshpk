%{?scl:%scl_package nodejs-sshpk}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name sshpk

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    1.9.2
Release:    4%{?dist}
Summary:    A library for finding and using SSH public keys
License:    MIT
URL:        https://github.com/arekinath/node-sshpk#readme
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Patch0:     fix-opt-deps.patch

%description
A library for finding and using SSH public keys

%prep
%setup -q -n package

%patch0

%nodejs_fixdep tweetnacl

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr bin lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Fri Jan 27 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.9.2-4
- Patch package.json to include optional deps in dependencies

* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.9.2-1
- Updated with script

* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.7.4-3
- Add fixdep macro

* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.7.4-2
- Initial build

