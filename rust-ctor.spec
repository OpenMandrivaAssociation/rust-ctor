%bcond_without check
%global debug_package %{nil}

%global crate ctor

Name:           rust-%{crate}
Version:        0.1.20
Release:        1%{?dist}
Summary:        __attribute__((constructor)) for Rust

# Upstream license specification: Apache-2.0 OR MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ctor
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(quote/default) >= 1.0.9 with crate(quote/default) < 2.0.0)
BuildRequires:  (crate(syn/full) >= 1.0.64 with crate(syn/full) < 2.0.0)
BuildRequires:  (crate(syn/parsing) >= 1.0.64 with crate(syn/parsing) < 2.0.0)
BuildRequires:  (crate(syn/printing) >= 1.0.64 with crate(syn/printing) < 2.0.0)
BuildRequires:  (crate(syn/proc-macro) >= 1.0.64 with crate(syn/proc-macro) < 2.0.0)
%if %{with check}
BuildRequires:  (crate(libc-print/default) >= 0.1.15 with crate(libc-print/default) < 0.2.0)
%endif
%endif

%global _description %{expand:
__attribute__((constructor)) for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ctor) = 0.1.20
Requires:       cargo
Requires:       (crate(quote/default) >= 1.0.9 with crate(quote/default) < 2.0.0)
Requires:       (crate(syn/full) >= 1.0.64 with crate(syn/full) < 2.0.0)
Requires:	(crate(syn/parsing) >= 1.0.64 with crate(syn/parsing) < 2.0.0)
Requires:	(crate(syn/printing) >= 1.0.64 with crate(syn/printing) < 2.0.0)
Requires:	(crate(syn/proc-macro) >= 1.0.64 with crate(syn/proc-macro) < 2.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc ../README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ctor/default) = 0.1.20
Requires:       cargo
Requires:       crate(ctor) = 0.1.20

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
