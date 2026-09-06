---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/amzn1-al2023-ami.html
---

# Comparing packages installed on Amazon Linux 1 (AL1) and Amazon Linux 2023 AMIs
<a name="amzn1-al2023-ami"></a>

A comparison of the RPMs present on the AL1 and AL2023 standard AMIs.

| Package | AL1 AMI | AL2023 AMI |
| --- | --- | --- |
|  acl  | 2.2.49 | 2.3.1 |
|  acpid  | 2.0.19 | 2.0.32 |
|  alsa-lib  | 1.0.22 |  |
|  alternatives  |  | 1.15 |
|  amazon-chrony-config  |  | 4.3 |
|  [`amazon-ec2-net-utils`](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html)  |  | 2.5.1 |
|  amazon-linux-repo-s3  |  | 2023.6.20241031 |
|  [`amazon-linux-sb-keys`](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html)  |  | 2023.1 |
|  amazon-rpm-config  |  | 228 |
|  amazon-ssm-agent  | 3.2.2222.0 | 3.3.987.0 |
|  amd-ucode-firmware  |  | 20210208 |
|  at  | 3.1.10 | 3.1.23 |
|  attr  | 2.4.46 | 2.5.1 |
|  audit  | 2.6.5 | 3.0.6 |
|  audit-libs  | 2.6.5 | 3.0.6 |
|  authconfig  | 6.2.8 |  |
|  aws-amitools-ec2  | 1.5.13 |  |
|  aws-cfn-bootstrap  | 1.4 | 2.0 |
|  aws-cli  | 1.18.107 |  |
|  awscli-2  |  | 2.15.30 |
|  basesystem  | 10.0 | 11 |
|  bash  | 4.2.46 | 5.2.15 |
|  bash-completion  |  | 2.11 |
|  bc  | 1.06.95 | 1.07.1 |
|  bind-libs  | 9.8.2 | 9.18.28 |
|  bind-license  |  | 9.18.28 |
|  bind-utils  | 9.8.2 | 9.18.28 |
|  [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  | 2.27 | 2.39 |
|  boost-filesystem  |  | 1.75.0 |
|  boost-system  |  | 1.75.0 |
|  boost-thread  |  | 1.75.0 |
|  bzip2  | 1.0.6 | 1.0.8 |
|  bzip2-libs  | 1.0.6 | 1.0.8 |
|  ca-certificates  | 2023.2.62 | 2023.2.68 |
|  c-ares  |  | 1.19.1 |
|  checkpolicy  | 2.1.10 | 3.4 |
|  chkconfig  | 1.3.49.3 | 1.15 |
|  chrony  |  | 4.3 |
|  cloud-disk-utils  | 0.27 |  |
|  cloud-init  | 0.7.6 | 22.2.2 |
|  cloud-init-cfg-ec2  |  | 22.2.2 |
|  cloud-utils-growpart  |  | 0.31 |
|  copy-jdk-configs  | 3.3 |  |
|  coreutils  | 8.22 | 8.32 |
|  coreutils-common  |  | 8.32 |
|  cpio  | 2.10 | 2.13 |
|  cracklib  | 2.8.16 | 2.9.6 |
|  cracklib-dicts  | 2.8.16 | 2.9.6 |
|  [`cronie`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-cron)  | 1.4.4 |  |
|  cronie-anacron  | 1.4.4 |  |
|  crontabs  | 1.10 | 1.11 |
|  crypto-policies  |  | 20220428 |
|  crypto-policies-scripts  |  | 20220428 |
|  cryptsetup  | 1.6.7 | 2.6.1 |
|  cryptsetup-libs  | 1.6.7 | 2.6.1 |
|  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  | 7.61.1 |  |
|  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  |  | 8.5.0 |
|  cyrus-sasl  | 2.1.23 |  |
|  cyrus-sasl-lib  | 2.1.23 | 2.1.27 |
|  cyrus-sasl-plain  | 2.1.23 | 2.1.27 |
|  dash  | 0.5.5.1 |  |
|  db4  | 4.7.25 |  |
|  db4-utils  | 4.7.25 |  |
|  dbus  | 1.6.12 | 1.12.28 |
|  dbus-broker  |  | 32 |
|  dbus-common  |  | 1.12.28 |
|  dbus-libs  | 1.6.12 | 1.12.28 |
|  dejavu-fonts-common  | 2.33 |  |
|  dejavu-sans-fonts  | 2.33 |  |
|  dejavu-serif-fonts  | 2.33 |  |
|  device-mapper  | 1.02.135 | 1.02.185 |
|  device-mapper-event  | 1.02.135 |  |
|  device-mapper-event-libs  | 1.02.135 |  |
|  device-mapper-libs  | 1.02.135 | 1.02.185 |
|  device-mapper-persistent-data  | 0.6.3 |  |
|  dhclient  | 4.1.1 |  |
|  dhcp-common  | 4.1.1 |  |
|  diffutils  | 3.3 | 3.8 |
|  dmraid  | 1.0.0.rc16 |  |
|  dmraid-events  | 1.0.0.rc16 |  |
|  dnf  |  | 4.14.0 |
|  dnf-data  |  | 4.14.0 |
|  dnf-plugin-release-notification  |  | 1.2 |
|  dnf-plugins-core  |  | 4.3.0 |
|  dnf-plugin-support-info  |  | 1.2 |
|  dnf-utils  |  | 4.3.0 |
|  dosfstools  |  | 4.2 |
|  dracut  | 004 | 055 |
|  dracut-config-ec2  |  | 3.0 |
|  dracut-config-generic  |  | 055 |
|  dracut-modules-growroot  | 0.20 |  |
|  dump  | 0.4 |  |
|  dwz  |  | 0.14 |
|  dyninst  |  | 10.2.1 |
|  e2fsprogs  | 1.43.5 | 1.46.5 |
|  e2fsprogs-libs  | 1.43.5 | 1.46.5 |
|  ec2-hibinit-agent  | 1.0.0 | 1.0.8 |
|  [`ec2-instance-connect`](https://docs.aws.amazon.com/linux/al2023/ug/connecting-to-instances.html)  |  | 1.1 |
|  ec2-instance-connect-selinux  |  | 1.1 |
|  ec2-net-utils  | 0.7 |  |
|  ec2-utils  | 0.7 | 2.2.0 |
|  ed  | 1.1 | 1.14.2 |
|  efi-filesystem  |  | 5 |
|  efi-srpm-macros  |  | 5 |
|  efivar  |  | 38 |
|  efivar-libs  |  | 38 |
|  elfutils-debuginfod-client  |  | 0.188 |
|  elfutils-default-yama-scope  |  | 0.188 |
|  elfutils-libelf  | 0.168 | 0.188 |
|  elfutils-libs  |  | 0.188 |
|  epel-release  | 6 |  |
|  ethtool  | 3.15 | 5.15 |
|  expat  | 2.1.0 | 2.5.0 |
|  file  | 5.37 | 5.39 |
|  file-libs  | 5.37 | 5.39 |
|  filesystem  | 2.4.30 | 3.14 |
|  findutils  | 4.4.2 | 4.8.0 |
|  fipscheck  | 1.3.1 |  |
|  fipscheck-lib  | 1.3.1 |  |
|  fontconfig  | 2.8.0 |  |
|  fontpackages-filesystem  | 1.41 |  |
|  fonts-srpm-macros  |  | 2.0.5 |
|  freetype  | 2.3.11 |  |
|  fstrm  |  | 0.6.1 |
|  fuse-libs  | 2.9.4 | 2.9.9 |
|  gawk  | 3.1.7 | 5.1.0 |
|  gdbm  | 1.8.0 |  |
|  gdbm-libs  |  | 1.19 |
|  gdisk  | 0.8.10 | 1.0.8 |
|  generic-logos  | 17.0.0 |  |
|  get\_reference\_source  | 1.2 |  |
|  gettext  |  | 0.21 |
|  gettext-libs  |  | 0.21 |
|  ghc-srpm-macros  |  | 1.5.0 |
|  giflib  | 4.1.6 |  |
|  glib2  | 2.36.3 | 2.74.7 |
|  [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html)  | 2.17 | 2.34 |
|  glibc-all-langpacks  |  | 2.34 |
|  glibc-common  | 2.17 | 2.34 |
|  glibc-gconv-extra  |  | 2.34 |
|  glibc-locale-source  |  | 2.34 |
|  gmp  | 6.0.0 | 6.2.1 |
|  [`gnupg2`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  | 2.0.28 |  |
|  [`gnupg2-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  |  | 2.3.7 |
|  gnutls  |  | 3.8.0 |
|  go-srpm-macros  |  | 3.2.0 |
|  gpgme  | 1.4.3 | 1.15.1 |
|  gpm-libs  | 1.20.6 | 1.20.7 |
|  grep  | 2.20 | 3.8 |
|  groff  | 1.22.2 |  |
|  groff-base  | 1.22.2 | 1.22.4 |
|  grub  | 0.97 |  |
|  grub2-common  |  | 2.06 |
|  grub2-efi-x64-ec2  |  | 2.06 |
|  grub2-pc-modules  |  | 2.06 |
|  grub2-tools  |  | 2.06 |
|  grub2-tools-minimal  |  | 2.06 |
|  grubby  | 7.0.15 | 8.40 |
|  gssproxy  |  | 0.8.4 |
|  gzip  | 1.5 | 1.12 |
|  hesiod  | 3.1.0 |  |
|  hibagent  | 1.0.0 |  |
|  hmaccalc  | 0.9.12 |  |
|  hostname  |  | 3.23 |
|  hunspell  |  | 1.7.0 |
|  hunspell-en  |  | 0.20140811.1 |
|  hunspell-en-GB  |  | 0.20140811.1 |
|  hunspell-en-US  |  | 0.20140811.1 |
|  hunspell-filesystem  |  | 1.7.0 |
|  hwdata  | 0.233 | 0.384 |
|  info  | 5.1 | 6.7 |
|  inih  |  | 49 |
|  initscripts  | 9.03.58 | 10.09 |
|  iproute  | 4.4.0 | 6.10.0 |
|  iptables  | 1.4.21 |  |
|  iputils  | 20121221 | 20210202 |
|  irqbalance  | 1.5.0 | 1.9.0 |
|  jansson  |  | 2.14 |
|  [`java-1.7.0-openjdk`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2.html#deprecated-openjdk7)  | 1.7.0.321 |  |
|  javapackages-tools  | 0.9.1 |  |
|  jemalloc  |  | 5.2.1 |
|  jitterentropy  |  | 3.4.1 |
|  jpackage-utils  | 1.7.5 |  |
|  jq  |  | 1.7.1 |
|  json-c  |  | 0.14 |
|  kbd  | 1.15 | 2.4.0 |
|  kbd-misc  | 1.15 | 2.4.0 |
|  kernel  | 4.14.336 | 6.1.112 |
|  kernel-libbpf  |  | 6.1.112 |
|  kernel-livepatch-repo-s3  |  | 2023.6.20241031 |
|  kernel-srpm-macros  |  | 1.0 |
|  kernel-tools  | 4.14.336 | 6.1.112 |
|  keyutils  | 1.5.8 | 1.6.3 |
|  keyutils-libs  | 1.5.8 | 1.6.3 |
|  kmod  | 14 | 29 |
|  kmod-libs  | 14 | 29 |
|  kpartx  | 0.4.9 |  |
|  kpatch-runtime  |  | 0.9.7 |
|  krb5-libs  | 1.15.1 | 1.21.3 |
|  lcms2  | 2.6 |  |
|  less  | 436 | 608 |
|  libacl  | 2.2.49 | 2.3.1 |
|  libaio  | 0.3.109 | 0.3.111 |
|  libarchive  |  | 3.7.4 |
|  libargon2  |  | 20171227 |
|  libassuan  | 2.0.3 | 2.5.5 |
|  libattr  | 2.4.46 | 2.5.1 |
|  libbasicobjects  |  | 0.1.1 |
|  libblkid  | 2.23.2 | 2.37.4 |
|  libcap  | 2.16 | 2.48 |
|  libcap54  | 2.54 |  |
|  libcap-ng  | 0.7.5 | 0.8.2 |
|  libcbor  |  | 0.7.0 |
|  libcgroup  | 0.40.rc1 |  |
|  libcollection  |  | 0.7.0 |
|  libcom\_err  | 1.43.5 | 1.46.5 |
|  libcomps  |  | 0.1.20 |
|  libconfig  |  | 1.7.2 |
|  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  | 7.61.1 |  |
|  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  |  | 8.5.0 |
|  [`libdb`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-bdb)  |  | 5.3.28 |
|  libdhash  |  | 0.5.0 |
|  libdnf  |  | 0.69.0 |
|  libeconf  |  | 0.4.0 |
|  libedit  | 2.11 | 3.1 |
|  libev  |  | 4.33 |
|  libevent  | 2.0.21 | 2.1.12 |
|  libfdisk  |  | 2.37.4 |
|  libffi  | 3.0.13 | 3.4.4 |
|  libfido2  |  | 1.10.0 |
|  libfontenc  | 1.0.5 |  |
|  libgcc  |  | 11.4.1 |
|  libgcc72  | 7.2.1 |  |
|  libgcrypt  | 1.5.3 | 1.10.2 |
|  libgomp  |  | 11.4.1 |
|  libgpg-error  | 1.11 | 1.42 |
|  libgssglue  | 0.1 |  |
|  libibverbs  |  | 48.0 |
|  libICE  | 1.0.6 |  |
|  libicu  | 50.2 |  |
|  libidn  | 1.18 |  |
|  libidn2  | 2.3.0 | 2.3.2 |
|  libini\_config  |  | 1.3.1 |
|  libjpeg-turbo  | 1.2.90 |  |
|  libkcapi  |  | 1.4.0 |
|  libkcapi-hmaccalc  |  | 1.4.0 |
|  libldb  |  | 2.6.2 |
|  libmaxminddb  |  | 1.5.2 |
|  libmetalink  |  | 0.1.3 |
|  libmnl  | 1.0.3 | 1.0.4 |
|  libmodulemd  |  | 2.13.0 |
|  libmount  | 2.23.2 | 2.37.4 |
|  libnetfilter\_conntrack  | 1.0.4 |  |
|  libnfnetlink  | 1.0.1 |  |
|  libnfsidmap  | 0.25 | 2.5.4 |
|  libnghttp2  | 1.33.0 | 1.59.0 |
|  libnih  | 1.0.1 |  |
|  libnl  | 1.1.4 |  |
|  libnl3  |  | 3.5.0 |
|  libpath\_utils  |  | 0.2.1 |
|  libpcap  |  | 1.10.1 |
|  libpipeline  | 1.2.3 | 1.5.3 |
|  libpkgconf  |  | 1.8.0 |
|  libpng  | 1.2.49 |  |
|  libpsl  | 0.6.2 | 0.21.1 |
|  libpwquality  | 1.2.3 | 1.4.4 |
|  libref\_array  |  | 0.1.5 |
|  librepo  |  | 1.14.5 |
|  libreport-filesystem  |  | 2.15.2 |
|  libseccomp  |  | 2.5.3 |
|  libselinux  | 2.1.10 | 3.4 |
|  libselinux-utils  | 2.1.10 | 3.4 |
|  libsemanage  | 2.1.6 | 3.4 |
|  libsepol  | 2.1.7 | 3.4 |
|  libsigsegv  |  | 2.13 |
|  libSM  | 1.2.1 |  |
|  libsmartcols  | 2.23.2 | 2.37.4 |
|  libsolv  |  | 0.7.22 |
|  libss  | 1.43.5 | 1.46.5 |
|  libssh2  | 1.4.2 |  |
|  libsss\_certmap  |  | 2.9.4 |
|  libsss\_idmap  |  | 2.9.4 |
|  libsss\_nss\_idmap  |  | 2.9.4 |
|  libsss\_sudo  |  | 2.9.4 |
|  libstdc\+\+  |  | 11.4.1 |
|  libstdc\+\+72  | 7.2.1 |  |
|  libstoragemgmt  |  | 1.9.4 |
|  libsysfs  | 2.1.0 |  |
|  libtalloc  |  | 2.3.4 |
|  libtasn1  | 2.3 | 4.19.0 |
|  libtdb  |  | 1.4.7 |
|  libtevent  |  | 0.13.0 |
|  libtextstyle  |  | 0.21 |
|  libtirpc  | 0.2.4 | 1.3.3 |
|  libudev  | 173 |  |
|  libunistring  | 0.9.3 | 0.9.10 |
|  libuser  | 0.60 | 0.63 |
|  libutempter  | 1.1.5 | 1.2.1 |
|  libuuid  | 2.23.2 | 2.37.4 |
|  libuv  |  | 1.47.0 |
|  libverto  | 0.2.5 | 0.3.2 |
|  libverto-libev  |  | 0.3.2 |
|  libX11  | 1.6.0 |  |
|  libX11-common  | 1.6.0 |  |
|  libXau  | 1.0.6 |  |
|  libxcb  | 1.11 |  |
|  libXcomposite  | 0.4.3 |  |
|  libxcrypt  |  | 4.4.33 |
|  libXext  | 1.3.2 |  |
|  libXfont  | 1.4.5 |  |
|  libXi  | 1.7.2 |  |
|  libxml2  | 2.9.1 | 2.10.4 |
|  libxml2-python27  | 2.9.1 |  |
|  libXrender  | 0.9.8 |  |
|  libxslt  | 1.1.28 |  |
|  libXtst  | 1.2.2 |  |
|  libyaml  | 0.1.6 | 0.2.5 |
|  libzstd  |  | 1.5.5 |
|  linux-firmware-whence  |  | 20210208 |
|  lm\_sensors-libs  |  | 3.6.0 |
|  lmdb-libs  |  | 0.9.29 |
|  [`log4j-cve-2021-44228-hotpatch`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2.html#deprecated-log4j-hotpatch)  | 1.3 |  |
|  logrotate  | 3.7.8 | 3.20.1 |
|  lsof  | 4.82 | 4.94.0 |
|  lua  | 5.1.4 |  |
|  lua-libs  |  | 5.4.4 |
|  lua-srpm-macros  |  | 1 |
|  lvm2  | 2.02.166 |  |
|  lvm2-libs  | 2.02.166 |  |
|  lz4-libs  |  | 1.9.4 |
|  mailcap  | 2.1.31 |  |
|  make  | 3.82 |  |
|  man-db  | 2.6.3 | 2.9.3 |
|  man-pages  | 4.10 | 5.10 |
|  mdadm  | 3.2.6 |  |
|  microcode\_ctl  | 2.1 | 2.1 |
|  mingetty  | 1.08 |  |
|  mpfr  |  | 4.1.0 |
|  nano  | 2.5.3 | 5.8 |
|  nc  | 1.84 |  |
|  ncurses  | 5.7 | 6.2 |
|  ncurses-base  | 5.7 | 6.2 |
|  ncurses-libs  | 5.7 | 6.2 |
|  nettle  |  | 3.8 |
|  net-tools  | 1.60 | 2.0 |
|  newt  | 0.52.11 | 0.52.21 |
|  newt-python27  | 0.52.11 |  |
|  nfs-utils  | 1.3.0 | 2.5.4 |
|  npth  |  | 1.6 |
|  nspr  | 4.25.0 | 4.35.0 |
|  nss  | 3.53.1 | 3.90.0 |
|  nss-pem  | 1.0.3 |  |
|  nss-softokn  | 3.53.1 | 3.90.0 |
|  nss-softokn-freebl  | 3.53.1 | 3.90.0 |
|  nss-sysinit  | 3.53.1 | 3.90.0 |
|  nss-tools  | 3.53.1 |  |
|  nss-util  | 3.53.1 | 3.90.0 |
|  ntp  | 4.2.8p15 |  |
|  ntpdate  | 4.2.8p15 |  |
|  ntsysv  | 1.3.49.3 | 1.15 |
|  numactl  | 2.0.7 |  |
|  numactl-libs  |  | 2.0.14 |
|  ocaml-srpm-macros  |  | 6 |
|  oniguruma  |  | 6.9.7.1 |
|  openblas-srpm-macros  |  | 2 |
|  openldap  | 2.4.40 | 2.4.57 |
|  openssh  | 7.4p1 | 8.7p1 |
|  openssh-clients  | 7.4p1 | 8.7p1 |
|  openssh-server  | 7.4p1 | 8.7p1 |
|  openssl  | 1.0.2k | 3.0.8 |
|  openssl-libs  |  | 3.0.8 |
|  openssl-pkcs11  |  | 0.4.12 |
|  os-prober  |  | 1.77 |
|  p11-kit  | 0.18.5 | 0.24.1 |
|  p11-kit-trust  | 0.18.5 | 0.24.1 |
|  package-notes-srpm-macros  |  | 0.4 |
|  pam  | 1.1.8 | 1.5.1 |
|  pam\_ccreds  | 10 |  |
|  pam\_krb5  | 2.3.11 |  |
|  pam\_passwdqc  | 1.0.5 |  |
|  parted  | 2.1 | 3.4 |
|  passwd  | 0.79 | 0.80 |
|  pciutils  | 3.1.10 | 3.7.0 |
|  pciutils-libs  | 3.1.10 | 3.7.0 |
|  [`pcre`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-pcre)  | 8.21 |  |
|  pcre2  |  | 10.40 |
|  pcre2-syntax  |  | 10.40 |
|  [`perl`](https://docs.aws.amazon.com/linux/al2023/ug/perl.html)  | 5.16.3 |  |
|  perl-Carp  | 1.26 | 1.50 |
|  perl-Class-Struct  |  | 0.66 |
|  perl-constant  | 1.27 | 1.33 |
|  perl-Digest  | 1.17 |  |
|  perl-Digest-HMAC  | 1.03 |  |
|  perl-Digest-MD5  | 2.52 |  |
|  perl-Digest-SHA  | 5.85 |  |
|  perl-DynaLoader  |  | 1.47 |
|  perl-Encode  | 2.51 | 3.15 |
|  perl-Errno  |  | 1.30 |
|  perl-Exporter  | 5.68 | 5.74 |
|  perl-Fcntl  |  | 1.13 |
|  perl-File-Basename  |  | 2.85 |
|  perl-File-Path  | 2.09 | 2.18 |
|  perl-File-stat  |  | 1.09 |
|  perl-File-Temp  | 0.23.01 | 0.231.100 |
|  perl-Filter  | 1.49 |  |
|  perl-Getopt-Long  | 2.40 | 2.52 |
|  perl-Getopt-Std  |  | 1.12 |
|  perl-HTTP-Tiny  | 0.033 | 0.078 |
|  perl-if  |  | 0.60.800 |
|  perl-interpreter  |  | 5.32.1 |
|  perl-IO  |  | 1.43 |
|  perl-IPC-Open3  |  | 1.21 |
|  perl-libs  | 5.16.3 | 5.32.1 |
|  perl-macros  | 5.16.3 |  |
|  perl-MIME-Base64  |  | 3.16 |
|  perl-mro  |  | 1.23 |
|  perl-overload  |  | 1.31 |
|  perl-overloading  |  | 0.02 |
|  perl-parent  | 0.225 | 0.238 |
|  perl-PathTools  | 3.40 | 3.78 |
|  perl-Pod-Escapes  | 1.04 | 1.07 |
|  perl-podlators  | 2.5.1 | 4.14 |
|  perl-Pod-Perldoc  | 3.20 | 3.28.01 |
|  perl-Pod-Simple  | 3.28 | 3.42 |
|  perl-Pod-Usage  | 1.63 | 2.01 |
|  perl-POSIX  |  | 1.94 |
|  perl-Scalar-List-Utils  | 1.27 | 1.56 |
|  perl-SelectSaver  |  | 1.02 |
|  perl-Socket  | 2.010 | 2.032 |
|  perl-srpm-macros  |  | 1 |
|  perl-Storable  | 2.45 | 3.21 |
|  perl-subs  |  | 1.03 |
|  perl-Symbol  |  | 1.08 |
|  perl-Term-ANSIColor  |  | 5.01 |
|  perl-Term-Cap  |  | 1.17 |
|  perl-Text-ParseWords  | 3.29 | 3.30 |
|  perl-Text-Tabs\+Wrap  |  | 2021.0726 |
|  perl-threads  | 1.87 |  |
|  perl-threads-shared  | 1.43 |  |
|  perl-Time-HiRes  | 1.9725 |  |
|  perl-Time-Local  | 1.2300 | 1.300 |
|  perl-vars  |  | 1.05 |
|  pinentry  | 0.7.6 |  |
|  pkgconf  |  | 1.8.0 |
|  pkgconfig  | 0.27.1 |  |
|  pkgconf-m4  |  | 1.8.0 |
|  pkgconf-pkg-config  |  | 1.8.0 |
|  pm-utils  | 1.4.1 |  |
|  policycoreutils  | 2.1.12 | 3.4 |
|  policycoreutils-python-utils  |  | 3.4 |
|  popt  | 1.13 | 1.18 |
|  procmail  | 3.22 |  |
|  procps  | 3.2.8 |  |
|  procps-ng  |  | 3.3.17 |
|  protobuf-c  |  | 1.4.1 |
|  psacct  | 6.3.2 | 6.6.4 |
|  psmisc  | 22.20 | 23.4 |
|  pth  | 2.0.7 |  |
|  publicsuffix-list-dafsa  |  | 20240212 |
|  python27  | 2.7.18 |  |
|  python27-babel  | 0.9.4 |  |
|  python27-backports  | 1.0 |  |
|  python27-backports-ssl\_match\_hostname  | 3.4.0.2 |  |
|  python27-boto  | 2.48.0 |  |
|  python27-botocore  | 1.17.31 |  |
|  python27-chardet  | 2.0.1 |  |
|  python27-colorama  | 0.4.1 |  |
|  python27-configobj  | 4.7.2 |  |
|  python27-crypto  | 2.6.1 |  |
|  python27-daemon  | 1.5.2 |  |
|  python27-dateutil  | 2.1 |  |
|  python27-devel  | 2.7.18 |  |
|  python27-docutils  | 0.11 |  |
|  python27-ecdsa  | 0.11 |  |
|  python27-futures  | 3.0.3 |  |
|  python27-imaging  | 1.1.6 |  |
|  python27-iniparse  | 0.3.1 |  |
|  python27-jinja2  | 2.7.2 |  |
|  python27-jmespath  | 0.9.2 |  |
|  python27-jsonpatch  | 1.2 |  |
|  python27-jsonpointer  | 1.0 |  |
|  python27-kitchen  | 1.1.1 |  |
|  python27-libs  | 2.7.18 |  |
|  python27-lockfile  | 0.8 |  |
|  python27-markupsafe  | 0.11 |  |
|  python27-paramiko  | 1.15.1 |  |
|  python27-pip  | 9.0.3 |  |
|  python27-ply  | 3.4 |  |
|  python27-pyasn1  | 0.1.7 |  |
|  python27-pycurl  | 7.19.0 |  |
|  python27-pygpgme  | 0.3 |  |
|  python27-pyliblzma  | 0.5.3 |  |
|  python27-pystache  | 0.5.3 |  |
|  python27-pyxattr  | 0.5.0 |  |
|  python27-PyYAML  | 3.10 |  |
|  python27-requests  | 1.2.3 |  |
|  python27-rsa  | 3.4.1 |  |
|  python27-setuptools  | 36.2.7 |  |
|  python27-simplejson  | 3.6.5 |  |
|  python27-six  | 1.8.0 |  |
|  python27-urlgrabber  | 3.10 |  |
|  python27-urllib3  | 1.24.3 |  |
|  python27-virtualenv  | 15.1.0 |  |
|  python3  |  | 3.9.16 |
|  python3-attrs  |  | 20.3.0 |
|  python3-audit  |  | 3.0.6 |
|  python3-awscrt  |  | 0.19.19 |
|  python3-babel  |  | 2.9.1 |
|  python3-cffi  |  | 1.14.5 |
|  python3-chardet  |  | 4.0.0 |
|  python3-colorama  |  | 0.4.4 |
|  python3-configobj  |  | 5.0.6 |
|  python3-cryptography  |  | 36.0.1 |
|  python3-daemon  |  | 2.3.0 |
|  python3-dateutil  |  | 2.8.1 |
|  python3-dbus  |  | 1.2.18 |
|  python3-distro  |  | 1.5.0 |
|  python3-dnf  |  | 4.14.0 |
|  python3-dnf-plugins-core  |  | 4.3.0 |
|  python3-docutils  |  | 0.16 |
|  python3-gpg  |  | 1.15.1 |
|  python3-hawkey  |  | 0.69.0 |
|  python3-idna  |  | 2.10 |
|  python3-jinja2  |  | 2.11.3 |
|  python3-jmespath  |  | 0.10.0 |
|  python3-jsonpatch  |  | 1.21 |
|  python3-jsonpointer  |  | 2.0 |
|  python3-jsonschema  |  | 3.2.0 |
|  python3-libcomps  |  | 0.1.20 |
|  python3-libdnf  |  | 0.69.0 |
|  python3-libs  |  | 3.9.16 |
|  python3-libselinux  |  | 3.4 |
|  python3-libsemanage  |  | 3.4 |
|  python3-libstoragemgmt  |  | 1.9.4 |
|  python3-lockfile  |  | 0.12.2 |
|  python3-markupsafe  |  | 1.1.1 |
|  python3-netifaces  |  | 0.10.6 |
|  python3-oauthlib  |  | 3.0.2 |
|  python3-pip-wheel  |  | 21.3.1 |
|  python3-ply  |  | 3.11 |
|  python3-policycoreutils  |  | 3.4 |
|  python3-prettytable  |  | 0.7.2 |
|  python3-prompt-toolkit  |  | 3.0.24 |
|  python3-pycparser  |  | 2.20 |
|  python3-pyrsistent  |  | 0.17.3 |
|  python3-pyserial  |  | 3.4 |
|  python3-pysocks  |  | 1.7.1 |
|  python3-pytz  |  | 2022.7.1 |
|  python3-pyyaml  |  | 5.4.1 |
|  python3-requests  |  | 2.25.1 |
|  python3-rpm  |  | 4.16.1.3 |
|  python3-ruamel-yaml  |  | 0.16.6 |
|  python3-ruamel-yaml-clib  |  | 0.1.2 |
|  python3-setools  |  | 4.4.1 |
|  python3-setuptools  |  | 59.6.0 |
|  python3-setuptools-wheel  |  | 59.6.0 |
|  python3-six  |  | 1.15.0 |
|  python3-systemd  |  | 235 |
|  python3-urllib3  |  | 1.25.10 |
|  python3-wcwidth  |  | 0.2.5 |
|  python-chevron  |  | 0.13.1 |
|  python-srpm-macros  |  | 3.9 |
|  quota  | 4.00 | 4.06 |
|  quota-nls  | 4.00 | 4.06 |
|  readline  | 6.2 | 8.1 |
|  rmt  | 0.4 |  |
|  rng-tools  | 5 | 6.14 |
|  rootfiles  | 8.1 | 8.1 |
|  rpcbind  | 0.2.0 | 1.2.6 |
|  rpm  | 4.11.3 | 4.16.1.3 |
|  rpm-build-libs  | 4.11.3 | 4.16.1.3 |
|  rpm-libs  | 4.11.3 | 4.16.1.3 |
|  rpm-plugin-selinux  |  | 4.16.1.3 |
|  rpm-plugin-systemd-inhibit  |  | 4.16.1.3 |
|  rpm-python27  | 4.11.3 |  |
|  rpm-sign-libs  |  | 4.16.1.3 |
|  rsync  | 3.0.6 | 3.2.6 |
|  rsyslog  | 5.8.10 |  |
|  ruby  | 2.0 |  |
|  ruby20  | 2.0.0.648 |  |
|  ruby20-irb  | 2.0.0.648 |  |
|  ruby20-libs  | 2.0.0.648 |  |
|  rubygem20-bigdecimal  | 1.2.0 |  |
|  rubygem20-json  | 1.8.3 |  |
|  rubygem20-psych  | 2.0.0 |  |
|  rubygem20-rdoc  | 4.2.2 |  |
|  rubygems20  | 2.0.14.1 |  |
|  rust-srpm-macros  |  | 21 |
|  sbsigntools  |  | 0.9.4 |
|  screen  | 4.0.3 | 4.8.0 |
|  sed  | 4.2.1 | 4.8 |
|  selinux-policy  |  | 38.1.45 |
|  selinux-policy-targeted  |  | 38.1.45 |
|  sendmail  | 8.14.4 |  |
|  setserial  | 2.17 |  |
|  setup  | 2.8.14 | 2.13.7 |
|  sgpio  | 1.2.0.10 |  |
|  shadow-utils  | 4.1.4.2 | 4.9 |
|  shared-mime-info  | 1.1 |  |
|  slang  | 2.2.1 | 2.3.2 |
|  sqlite  | 3.7.17 |  |
|  sqlite-libs  |  | 3.40.0 |
|  sssd-client  |  | 2.9.4 |
|  sssd-common  |  | 2.9.4 |
|  sssd-kcm  |  | 2.9.4 |
|  sssd-nfs-idmap  |  | 2.9.4 |
|  strace  |  | 6.8 |
|  sudo  | 1.8.23 | 1.9.15 |
|  sysctl-defaults  | 1.0 | 1.0 |
|  sysfsutils  | 2.1.0 |  |
|  sysstat  |  | 12.5.6 |
|  systemd  |  | 252.23 |
|  systemd-libs  |  | 252.23 |
|  systemd-networkd  |  | 252.23 |
|  systemd-pam  |  | 252.23 |
|  systemd-resolved  |  | 252.23 |
|  systemd-udev  |  | 252.23 |
|  system-release  | 2018.03 | 2023.6.20241031 |
|  systemtap-runtime  |  | 4.8 |
|  sysvinit  | 2.87 |  |
|  tar  | 1.26 | 1.34 |
|  tbb  |  | 2020.3 |
|  tcp\_wrappers  | 7.6 |  |
|  tcp\_wrappers-libs  | 7.6 |  |
|  tcpdump  |  | 4.99.1 |
|  tcsh  |  | 6.24.07 |
|  time  | 1.7 | 1.9 |
|  tmpwatch  | 2.9.16 |  |
|  traceroute  | 2.0.14 | 2.1.3 |
|  ttmkfdir  | 3.0.9 |  |
|  tzdata  | 2023c | 2024a |
|  tzdata-java  | 2023c |  |
|  udev  | 173 |  |
|  unzip  | 6.0 | 6.0 |
|  update-motd  | 1.0.1 | 2.2 |
|  [`upstart`](https://docs.aws.amazon.com/linux/al1/ug/deprecated-al1.html#deprecated-upstart)  | 0.6.5 |  |
|  userspace-rcu  |  | 0.12.1 |
|  ustr  | 1.0.4 |  |
|  util-linux  | 2.23.2 | 2.37.4 |
|  util-linux-core  |  | 2.37.4 |
|  vim-common  | 9.0.2120 | 9.0.2153 |
|  vim-data  | 9.0.2120 | 9.0.2153 |
|  vim-enhanced  | 9.0.2120 | 9.0.2153 |
|  vim-filesystem  | 9.0.2120 | 9.0.2153 |
|  vim-minimal  | 9.0.2120 | 9.0.2153 |
|  wget  | 1.18 | 1.21.3 |
|  which  | 2.19 | 2.21 |
|  words  | 3.0 | 3.0 |
|  xfsdump  |  | 3.1.11 |
|  xfsprogs  |  | 5.18.0 |
|  xorg-x11-fonts-Type1  | 7.2 |  |
|  xorg-x11-font-utils  | 7.2 |  |
|  xxd  | 9.0.2120 | 9.0.2153 |
|  xxhash-libs  |  | 0.8.0 |
|  xz  | 5.2.2 | 5.2.5 |
|  xz-libs  | 5.2.2 | 5.2.5 |
|  yum  | 3.4.3 | 4.14.0 |
|  yum-metadata-parser  | 1.1.4 |  |
|  yum-plugin-priorities  | 1.1.31 |  |
|  yum-plugin-upgrade-helper  | 1.1.31 |  |
|  yum-utils  | 1.1.31 |  |
|  zip  | 3.0 | 3.0 |
|  zlib  | 1.2.8 | 1.2.11 |
|  zram-generator  |  | 1.1.2 |
|  zram-generator-defaults  |  | 1.1.2 |
|  zstd  |  | 1.5.5 |
