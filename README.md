# SMHI-VirtualPlanetBuilder

this repo contains the shell script and spec file needed to build en rpm for linux Redhat 7.
1) First get the code from https://github.com/openscenegraph/VirtualPlanetBuilder
2) Apply vpb.diff to source code.
3) Make it with CMAKE_INSTALL_PREFIX=<build_root>/local
4) Clone this repo to <build_root>/local.
5) Build the rpm with build_rpm_VirtualPlanetBuilder.sh.
