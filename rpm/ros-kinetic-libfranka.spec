Name:           ros-kinetic-libfranka
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS libfranka package

Group:          Development/Libraries
License:        Apache 2.0
URL:            https://frankaemika.github.io
Source0:        %{name}-%{version}.tar.gz

Requires:       poco-devel
Requires:       ros-kinetic-catkin
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  poco-devel

%description
libfranka is a C++ library for Franka Emika research robots

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DBUILD_DOCUMENTATION=OFF \
        -DBUILD_EXAMPLES=OFF \
        -DBUILD_TESTS=ON \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Jan 30 2018 Franka Emika GmbH <support@franka.de> - 0.2.0-0
- Autogenerated by Bloom

* Wed Nov 08 2017 Franka Emika GmbH <support@franka.de> - 0.1.0-3
- Autogenerated by Bloom

* Mon Oct 02 2017 Franka Emika GmbH <info@franka.de> - 0.1.0-2
- Autogenerated by Bloom

* Fri Sep 29 2017 Franka Emika GmbH <info@franka.de> - 0.1.0-1
- Autogenerated by Bloom

* Wed Sep 27 2017 Franka Emika GmbH <info@franka.de> - 0.1.0-0
- Autogenerated by Bloom
