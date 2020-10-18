%global major   1
%define libname %mklibname uring %major
%define devname %mklibname uring -d

Name: liburing
Version: 0.7
Release: %mkrel 1
Summary: Linux-native io_uring I/O access library
Group: System/Libraries
License: (GPLv2 with exceptions and LGPLv2+) or MIT
Source0: https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz
Source1: https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz.asc
URL: https://git.kernel.dk/cgit/liburing/
BuildRequires: gcc

# Fails to build and therefore isn't supported upstream
ExcludeArch: armv7hl

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package -n %libname
Summary: Linux-native io_uring I/O access library
Group: System/Libraries
# Temp Cauldron fix:
Obsoletes: %{_lib}uring0 = 0.5-1.mga8
Conflicts: %{_lib}uring0 = 0.5-1.mga8

%description -n %libname
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package -n %devname
Group: Development/C
Summary: Development files for Linux-native io_uring I/O access library
Requires: %{libname}%{_isa} = %{version}-%{release}
Requires: pkgconfig
Provides: %{name}-devel = %{version}-%{release}

%description -n %devname
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%prep
%autosetup

%build
%set_build_flags
./configure --prefix=%{_prefix} --libdir=/%{_libdir} --libdevdir=/%{_libdir} --mandir=%{_mandir} --includedir=%{_includedir}

%make_build

%install
%make_install

%files -n %libname
%attr(0755,root,root) %{_libdir}/liburing.so.%{major}{,.*}
%license COPYING

%files -n %devname
%{_includedir}/liburing/
%{_includedir}/liburing.h
%{_libdir}/liburing.so
%exclude %{_libdir}/liburing.a
%{_libdir}/pkgconfig/*
%{_mandir}/man2/*