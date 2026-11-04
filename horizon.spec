# Keep the existing permissive C++ flag until an actual Fedora build can
# establish that it is no longer needed.
%global optflags %{optflags} -fpermissive
%global shortname horizon
%global commit 2ca3a5cd414d4572a78a7780e824a4c2f2dc6a16

Name:           %{shortname}-eda
# This commit is newer than upstream v2.7.2, but is not tagged v2.7.3.
# Use RPM post-release snapshot ordering rather than inventing an upstream tag.
Version:        2.7.2^20261004git2ca3a5c
Release:        2%{?dist}
Summary:        Free electronic design automation package
License:        GPL-3.0-or-later
URL:            https://github.com/horizon-eda/horizon
Source0:        https://github.com/horizon-eda/horizon/archive/%{commit}.tar.gz

BuildRequires:  cairomm-devel
BuildRequires:  cmake
BuildRequires:  cppzmq-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libepoxy-devel
# Fedora 45 replaced unversioned libgit2-devel with ABI-versioned packages.
# Both development packages expose pkgconfig(libgit2) to Meson.
%if 0%{?fedora} >= 45
BuildRequires:  libgit2_1.9-devel
%else
BuildRequires:  libgit2-devel
%endif
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libspnav-devel
BuildRequires:  libuuid-devel
BuildRequires:  meson
BuildRequires:  opencascade-devel
BuildRequires:  pkgconf-pkg-config
# Fedora's primary PoDoFo package is 1.x; the podofo0.10 package is legacy.
BuildRequires:  podofo-devel >= 1.0
BuildRequires:  python3
BuildRequires:  sqlite-devel
BuildRequires:  zeromq-devel

%description
Horizon EDA is a free software suite for designing printed circuit boards,
from component and schematic design to PCB layout and manufacturing outputs.

%prep
%autosetup -n %{shortname}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/horizon-eda
%{_bindir}/horizon-imp
%{_datadir}/applications/org.horizon_eda.HorizonEDA.desktop
%{_datadir}/metainfo/org.horizon_eda.HorizonEDA.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/org.horizon_eda.HorizonEDA.*
%{_mandir}/man1/horizon-eda.1*
%{_mandir}/man1/horizon-imp.1*

%changelog
* Wed Nov 04 2026 Horizon EDA RPM packaging - 2.7.2^20261004git2ca3a5c-2
- Select the ABI-versioned libgit2_1.9-devel package for Fedora 45 and later.
- Preserve libgit2-devel on earlier Fedora releases.

* Tue Nov 03 2026 Horizon EDA RPM packaging - 2.7.2^20261004git2ca3a5c-1
- Package git revision 2ca3a5c with OpenCASCADE 8.0 compatibility changes.
- Switch to modern PoDoFo development files and declare missing build dependencies.
- Use an explicitly versioned upstream source snapshot and precise installed file paths.
