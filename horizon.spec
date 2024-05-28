Name: horizon-eda
Version: 2.6.0
Release: 1

Summary: Horizon is a free EDA package
License: GPL-3.0-or-later
Group: Engineering
Url: https://github.com/horizon-eda/horizon

Source: https://github.com/horizon-eda/horizon/archive/refs/tags/v%version.tar.gz

BuildRequires: meson cmake
BuildRequires: gcc-c++ libgtkmm3-devel
BuildRequires: libsqlite3-devel
BuildRequires: libzip-devel
BuildRequires: libuuid-devel
BuildRequires: libepoxy-devel
BuildRequires: librsvg-devel
BuildRequires: libpodofo-devel
BuildRequires: libzeromq-cpp-devel
BuildRequires: libgit2-devel
BuildRequires: libcurl-devel
BuildRequires: libglm-devel
BuildRequires: boost-devel-headers
BuildRequires: opencascade-devel
BuildRequires: libsigc++2-devel
BuildRequires: libarchive-devel
BuildRequires: libspnav-devel

%description
%summary.

%prep
%setup

%build
%meson
%meson_build


%install
%meson_install

%files
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*
%doc *.md

%changelog
