# Generated by rust2rpm 21
%bcond_without check
%global debug_package %{nil}

%global crate bevy_macro_utils

Name:           rust-%{crate}
Version:        0.7.0
Release:        %autorelease
Summary:        Collection of utils for Bevy Engine

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/bevy_macro_utils
Source:         %{crates_source}
Source1: https://github.com/bevyengine/bevy/raw/v0.7.0/docs/LICENSE-APACHE
Source2: https://github.com/bevyengine/bevy/raw/v0.7.0/docs/LICENSE-MIT

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Collection of utils for Bevy Engine.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%{crate_instdir}/
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep
cp %{SOURCE1} %{SOURCE2} .

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
