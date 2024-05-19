%global build_ldflags %{build_ldflags} -Wl,--undefined-version

%global major   2
%define libname %mklibname uring %major
%define devname %mklibname uring -d

Name: liburing
Version: 2.6
Release: 1
Summary: Linux-native io_uring I/O access library
Group: System/Libraries
License: (GPLv2 with exceptions and LGPLv2+) or MIT
Source0: https://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2
URL: https://git.kernel.dk/cgit/liburing

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package -n %{libname}
Summary: Linux-native io_uring I/O access library
Group: System/Libraries

%description -n %{libname}
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package -n %{devname}
Group: Development/C
Summary: Development files for Linux-native io_uring I/O access library
Requires: %{libname}%{_isa} = %{EVRD}
Provides: %{name}-devel = %{EVRD}

%description -n %{devname}
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%prep
%autosetup -p1

%build
%set_build_flags
# (tpg) don't use macro here
./configure --prefix=%{_prefix} --libdir=/%{_libdir} --libdevdir=/%{_libdir} --mandir=%{_mandir} --includedir=%{_includedir} --cc=%{__cc} --cxx=%{__cxx}

%make_build

%install
%make_install

%files -n %{libname}
%attr(0755,root,root) %{_libdir}/liburing.so.%{major}{,.*}
%{_libdir}/liburing-ffi.so.%{major}{,.*}
%license COPYING

%files -n %{devname}
%{_includedir}/liburing/
%{_includedir}/liburing.h
%{_libdir}/liburing.so
%{_libdir}/liburing.a
%{_libdir}/liburing-ffi.a
%{_libdir}/liburing-ffi.so
%{_libdir}/pkgconfig/*
%doc %{_mandir}/man*/*
