# CentOS-3 singularity container bootstrap from a CentOS-7 host
- I am too lazy to fix the CentOS-5 compat-db-4.2.52-5.1.src.rpm to build on CentOS-7, so I just extract the db41_load and dependancy from the x86_64.rpm and manually put it in place.
- replacing the original yum.conf with one pointing to the archived vault.centos.org

# CentOS-3 has been End of Life (no support/no bug fix/...) since October 30th 2010.
(https://lists.centos.org/pipermail/centos-announce/2010-November/017141.html)

# howto:
1) Install db41_load from compat-db-4.2.52-5.1.x86_64.rpm
```
rpm2cpio  compat-db-4.2.52-5.1.x86_64.rpm| (cd /dev/shm && cpio -iudv ./usr/bin/db41_load ./lib64/libdb-4.1.so)
sudo cp /dev/shm/./usr/bin/db41_load /usr/bin/db41_lod
sudo cp  /dev/shm/./lib64/libdb-4.1.so /lib64/libdb-4.1.so
```
alternatively one could build a rpm file with only these 2 files inside
```
rpmbuild -ba compat-db41.spec && sudo yum install ~/rpmbuild/RPMS/x86_64/compat-db41-4.2.52-5.1.1.el7.centos.x86_64.rpm
```
2) singularity
```
singularity create c3-on-c7.img
sudo singularity bootstrap c3-on-c7.img singularity-centos3-on-centos7.def
```
