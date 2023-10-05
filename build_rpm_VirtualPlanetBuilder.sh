
export BASE=$PWD
rm -f SMHI-VirtualPlanetBuilder.tar.gz
rm -rf /local_disk/build1/SOURCES/SMHI-VirtualPlanetBuilder
mkdir -p /local_disk/build1/SOURCES/SMHI-VirtualPlanetBuilder

tar cvzf SMHI-VirtualPlanetBuilder.tar.gz bin include lib64
cp SMHI-VirtualPlanetBuilder.tar.gz  /local_disk/build1/SOURCES/SMHI-VirtualPlanetBuilder

rpmbuild -bb SMHI-VirtualPlanetBuilder.spec
