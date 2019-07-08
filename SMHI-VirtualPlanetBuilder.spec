%define appname SMHI-VirtualPlanetBuilder
%define name SMHI-VirtualPlanetBuilder
%define version 1.1.0
%define release 1.4
%define vendor	smhi.se

Summary: Systemd unit file for %{appname}
Name: %{appname}
Version: %{version}
Release: %{release}
License: SMHI
Group: Utilities
URL: http://www.smhi.se/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
osgQt lib and executables %{appname}

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
cd $RPM_BUILD_ROOT/usr
tar xvzf $RPM_SOURCE_DIR/SMHI-VirtualPlanetBuilder.tar.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post

%preun

%files
%defattr(-,root,root,-)
/usr/bin/osgdem
/usr/bin/vpbcache
/usr/bin/vpbmaster
/usr/bin/vpbsizes
/usr/include/vpb/BlockOperation
/usr/include/vpb/BuildLog
/usr/include/vpb/BuildOperation
/usr/include/vpb/BuildOptions
/usr/include/vpb/Commandline
/usr/include/vpb/DataSet
/usr/include/vpb/DatabaseBuilder
/usr/include/vpb/Date
/usr/include/vpb/Destination
/usr/include/vpb/Export
/usr/include/vpb/ExtrudeVisitor
/usr/include/vpb/FileCache
/usr/include/vpb/FileDetails
/usr/include/vpb/FilePathManager
/usr/include/vpb/FileUtils
/usr/include/vpb/GeospatialDataset
/usr/include/vpb/HeightFieldMapper
/usr/include/vpb/MachinePool
/usr/include/vpb/ObjectPlacer
/usr/include/vpb/PropertyFile
/usr/include/vpb/ShapeFilePlacer
/usr/include/vpb/Source
/usr/include/vpb/SourceData
/usr/include/vpb/SpatialProperties
/usr/include/vpb/System
/usr/include/vpb/Task
/usr/include/vpb/TaskManager
/usr/include/vpb/TextureUtils
/usr/include/vpb/ThreadPool
/usr/include/vpb/Version
/usr/lib64/libvpb.so
/usr/lib64/libvpb.so.1.1.0
/usr/lib64/libvpb.so.30


%changelog
* Mon Jul  8 2019 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- OpenSceneGraph 3.6.3
* Wed May  9 2018 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- Clean build
* Mon Apr 23 2018 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- OpenSceneGraph 3.6.0
* Thu Apr 6 2017 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- OpenSceneGraph updated.
* Wed Dec 28 2016 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- Initial build.


