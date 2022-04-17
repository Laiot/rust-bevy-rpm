# Generated by rust2rpm 21
%bcond_without check
%global debug_package %{nil}

%global crate bevy_ecs

Name:           rust-%{crate}
Version:        0.7.0
Release:        %autorelease
Summary:        Bevy Engine's entity component system

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/bevy_ecs
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Bevy Engine's entity component system.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
# FIXME: no license files detected
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bevy_reflect-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bevy_reflect-devel %{_description}

This package contains library source intended for building other packages which
use the "bevy_reflect" feature of the "%{crate}" crate.

%files       -n %{name}+bevy_reflect-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+trace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trace-devel %{_description}

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

%files       -n %{name}+trace-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
