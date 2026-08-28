---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/amzn2-al2023-minimal-ami.html
---

# Comparing packages installed on Amazon Linux 2 and Amazon Linux 2023 Minimal AMIs
<a name="amzn2-al2023-minimal-ami"></a>

A comparison of the RPMs present on the Amazon Linux 2 and AL2023 Minimal AMIs.

| Package | AL2 Minimal | AL2023 Minimal |
| --- | --- | --- |
|  acl  | 2.2.51 |  |
|  alternatives  |  | 1.15 |
|  amazon-chrony-config  |  | 4.3 |
|  [`amazon-ec2-net-utils`](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html)  |  | 2.5.1 |
|  amazon-linux-extras  | 2.0.3 |  |
|  amazon-linux-repo-s3  |  | 2023.6.20241031 |
|  [`amazon-linux-sb-keys`](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html)  |  | 2023.1 |
|  amd-ucode-firmware  | 20200421 (noarch) | 20210208 (noarch) |
|  audit  | 2.8.1 | 3.0.6 |
|  audit-libs  | 2.8.1 | 3.0.6 |
|  authconfig  | 6.2.8 |  |
|  awscli-2  |  | 2.15.30 |
|  basesystem  | 10.0 | 11 |
|  bash  | 4.2.46 | 5.2.15 |
|  bind-export-libs  | 9.11.4 |  |
|  bzip2-libs  | 1.0.6 | 1.0.8 |
|  ca-certificates  | 2023.2.68 | 2023.2.68 |
|  checkpolicy  |  | 3.4 |
|  chkconfig  | 1.7.4 |  |
|  chrony  | 4.2 | 4.3 |
|  cloud-init  | 19.3 | 22.2.2 |
|  cloud-init-cfg-ec2  |  | 22.2.2 |
|  cloud-utils-growpart  | 0.31 | 0.31 |
|  coreutils  | 8.22 | 8.32 |
|  coreutils-common  |  | 8.32 |
|  cpio  | 2.12 | 2.13 |
|  cracklib  | 2.9.0 | 2.9.6 |
|  cracklib-dicts  | 2.9.0 | 2.9.6 |
|  [`cronie`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-cron)  | 1.4.11 |  |
|  cronie-anacron  | 1.4.11 |  |
|  crontabs  | 1.11 |  |
|  crypto-policies  |  | 20220428 |
|  cryptsetup-libs  | 1.7.4 | 2.6.1 |
|  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  | 8.3.0 |  |
|  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  |  | 8.5.0 |
|  cyrus-sasl-lib  | 2.1.26 | 2.1.27 |
|  dbus  | 1.10.24 | 1.12.28 |
|  dbus-broker  |  | 32 |
|  dbus-common  |  | 1.12.28 |
|  dbus-libs  | 1.10.24 | 1.12.28 |
|  device-mapper  | 1.02.170 | 1.02.185 |
|  device-mapper-libs  | 1.02.170 | 1.02.185 |
|  dhclient  | 4.2.5 |  |
|  dhcp-common  | 4.2.5 |  |
|  dhcp-libs  | 4.2.5 |  |
|  diffutils  | 3.3 | 3.8 |
|  dnf  |  | 4.14.0 |
|  dnf-data  |  | 4.14.0 |
|  dnf-plugin-release-notification  |  | 1.2 |
|  dnf-plugins-core  |  | 4.3.0 |
|  dnf-plugin-support-info  |  | 1.2 |
|  dracut  | 033 | 055 |
|  dracut-config-ec2  | 2.0 | 3.0 |
|  dracut-config-generic  | 033 | 055 |
|  e2fsprogs  | 1.42.9 | 1.46.5 |
|  e2fsprogs-libs  | 1.42.9 | 1.46.5 |
|  ec2-utils  | 1.2 | 2.2.0 |
|  efibootmgr  | 15 (aarch64) |  |
|  efi-filesystem  |  | 5 |
|  efivar  |  | 38 |
|  efivar-libs  | 31 (aarch64) | 38 |
|  elfutils-default-yama-scope  | 0.176 | 0.188 |
|  elfutils-libelf  | 0.176 | 0.188 |
|  elfutils-libs  | 0.176 | 0.188 |
|  expat  | 2.1.0 | 2.5.0 |
|  file  | 5.11 | 5.39 |
|  file-libs  | 5.11 | 5.39 |
|  filesystem  | 3.2 | 3.14 |
|  findutils  | 4.5.11 | 4.8.0 |
|  fipscheck  | 1.4.1 |  |
|  fipscheck-lib  | 1.4.1 |  |
|  freetype  | 2.8 |  |
|  fuse-libs  | 2.9.2 | 2.9.9 |
|  gawk  | 4.0.2 | 5.1.0 |
|  gdbm  | 1.13 |  |
|  gdbm-libs  |  | 1.19 |
|  gdisk  | 0.8.10 | 1.0.8 |
|  gettext  | 0.19.8.1 | 0.21 |
|  gettext-libs  | 0.19.8.1 | 0.21 |
|  glib2  | 2.56.1 | 2.74.7 |
|  [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html)  | 2.26 | 2.34 |
|  glibc-all-langpacks  | 2.26 | 2.34 |
|  glibc-common  | 2.26 | 2.34 |
|  glibc-locale-source  | 2.26 | 2.34 |
|  glibc-minimal-langpack  | 2.26 |  |
|  gmp  | 6.0.0 | 6.2.1 |
|  [`gnupg2`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  | 2.0.22 |  |
|  [`gnupg2-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  |  | 2.3.7 |
|  gnutls  |  | 3.8.0 |
|  gpgme  | 1.3.2 | 1.15.1 |
|  grep  | 2.20 | 3.8 |
|  groff-base  | 1.22.2 | 1.22.4 |
|  grub2  | 2.06 |  |
|  grub2-common  | 2.06 | 2.06 |
|  grub2-efi-aa64  | 2.06 (aarch64) |  |
|  grub2-efi-aa64-ec2  | 2.06 (aarch64) | 2.06 (aarch64) |
|  grub2-efi-aa64-modules  | 2.06 (noarch) |  |
|  grub2-efi-x64-ec2  | 2.06 (x86\_64) | 2.06 (x86\_64) |
|  grub2-pc  | 2.06 (x86\_64) |  |
|  grub2-pc-modules  | 2.06 (noarch) | 2.06 |
|  grub2-tools  | 2.06 | 2.06 |
|  grub2-tools-minimal  | 2.06 | 2.06 |
|  grubby  | 8.28 | 8.40 |
|  gzip  | 1.5 | 1.12 |
|  hardlink  | 1.3 |  |
|  hostname  | 3.13 | 3.23 |
|  hwdata  |  | 0.384 |
|  info  | 5.1 |  |
|  inih  |  | 49 |
|  initscripts  | 9.49.47 | 10.09 |
|  iproute  | 5.10.0 | 6.10.0 |
|  iptables  | 1.8.4 |  |
|  iptables-libs  | 1.8.4 |  |
|  iputils  | 20180629 | 20210202 |
|  irqbalance  | 1.7.0 | 1.9.0 |
|  jansson  |  | 2.14 |
|  jitterentropy  |  | 3.4.1 |
|  jq  |  | 1.7.1 |
|  json-c  |  | 0.14 |
|  kbd  |  | 2.4.0 |
|  kbd-misc  |  | 2.4.0 |
|  kernel  | 4.14.355 | 6.1.112 |
|  kernel-libbpf  |  | 6.1.112 |
|  kernel-livepatch-repo-s3  |  | 2023.6.20241031 |
|  keyutils-libs  | 1.5.8 | 1.6.3 |
|  kmod  | 25 | 29 |
|  kmod-libs  | 25 | 29 |
|  kpartx  | 0.4.9 |  |
|  krb5-libs  | 1.15.1 | 1.21.3 |
|  less  | 458 | 608 |
|  libacl  | 2.2.51 | 2.3.1 |
|  libarchive  |  | 3.7.4 |
|  libargon2  |  | 20171227 |
|  libassuan  | 2.1.0 | 2.5.5 |
|  libattr  | 2.4.46 | 2.5.1 |
|  libblkid  | 2.30.2 | 2.37.4 |
|  libcap  | 2.54 | 2.48 |
|  libcap-ng  | 0.7.5 | 0.8.2 |
|  libcbor  |  | 0.7.0 |
|  libcom\_err  | 1.42.9 | 1.46.5 |
|  libcomps  |  | 0.1.20 |
|  libcroco  | 0.6.12 |  |
|  libcrypt  | 2.26 |  |
|  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  | 8.3.0 |  |
|  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  |  | 8.5.0 |
|  [`libdb`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-bdb)  | 5.3.21 | 5.3.28 |
|  libdb-utils  | 5.3.21 |  |
|  libdnf  |  | 0.69.0 |
|  libeconf  |  | 0.4.0 |
|  libedit  | 3.0 | 3.1 |
|  libestr  | 0.1.9 |  |
|  libfastjson  | 0.99.4 |  |
|  libfdisk  | 2.30.2 | 2.37.4 |
|  libffi  | 3.0.13 | 3.4.4 |
|  libfido2  |  | 1.10.0 |
|  libgcc  | 7.3.1 | 11.4.1 |
|  libgcrypt  | 1.5.3 | 1.10.2 |
|  libgomp  | 7.3.1 | 11.4.1 |
|  libgpg-error  | 1.12 | 1.42 |
|  libicu  | 50.2 |  |
|  libidn  | 1.28 |  |
|  libidn2  | 2.3.0 | 2.3.2 |
|  libkcapi  |  | 1.4.0 |
|  libkcapi-hmaccalc  |  | 1.4.0 |
|  libmetalink  | 0.1.3 |  |
|  libmnl  | 1.0.3 | 1.0.4 |
|  libmodulemd  |  | 2.13.0 |
|  libmount  | 2.30.2 | 2.37.4 |
|  libnetfilter\_conntrack  | 1.0.6 |  |
|  libnfnetlink  | 1.0.1 |  |
|  libnghttp2  | 1.41.0 | 1.59.0 |
|  libpcap  | 1.5.3 |  |
|  libpipeline  | 1.2.3 | 1.5.3 |
|  libpng  | 1.5.13 |  |
|  libpsl  | 0.21.5 | 0.21.1 |
|  libpwquality  | 1.2.3 | 1.4.4 |
|  librepo  |  | 1.14.5 |
|  libreport-filesystem  |  | 2.15.2 |
|  libseccomp  | 2.5.2 | 2.5.3 |
|  libselinux  | 2.5 | 3.4 |
|  libselinux-utils  | 2.5 | 3.4 |
|  libsemanage  | 2.5 | 3.4 |
|  libsepol  | 2.5 | 3.4 |
|  libsigsegv  |  | 2.13 |
|  libsmartcols  | 2.30.2 | 2.37.4 |
|  libsolv  |  | 0.7.22 |
|  libss  | 1.42.9 | 1.46.5 |
|  libssh2  | 1.4.3 |  |
|  libstdc\+\+  | 7.3.1 | 11.4.1 |
|  libsysfs  | 2.1.0 |  |
|  libtasn1  | 4.10 | 4.19.0 |
|  libtextstyle  |  | 0.21 |
|  libunistring  | 0.9.3 | 0.9.10 |
|  libuser  | 0.60 | 0.63 |
|  libutempter  | 1.1.6 | 1.2.1 |
|  libuuid  | 2.30.2 | 2.37.4 |
|  libverto  | 0.2.5 | 0.3.2 |
|  libxcrypt  |  | 4.4.33 |
|  libxml2  | 2.9.1 | 2.10.4 |
|  libyaml  | 0.1.4 | 0.2.5 |
|  libzstd  |  | 1.5.5 |
|  linux-firmware-whence  |  | 20210208 (noarch) |
|  logrotate  | 3.8.6 | 3.20.1 |
|  lua  | 5.1.4 |  |
|  lua-libs  |  | 5.4.4 |
|  lz4  | 1.7.5 |  |
|  lz4-libs  |  | 1.9.4 |
|  make  | 3.82 |  |
|  man-db  | 2.6.3 | 2.9.3 |
|  mariadb-libs  | 5.5.68 |  |
|  microcode\_ctl  | 2.1 (x86\_64) | 2.1 (x86\_64) |
|  mpfr  |  | 4.1.0 |
|  ncurses  | 6.0 | 6.2 |
|  ncurses-base  | 6.0 | 6.2 |
|  ncurses-libs  | 6.0 | 6.2 |
|  nettle  | 2.7.1 | 3.8 |
|  net-tools  | 2.0 | 2.0 |
|  newt  | 0.52.15 |  |
|  newt-python  | 0.52.15 |  |
|  npth  |  | 1.6 |
|  nspr  | 4.35.0 |  |
|  nss  | 3.90.0 |  |
|  nss-pem  | 1.0.3 |  |
|  nss-softokn  | 3.90.0 |  |
|  nss-softokn-freebl  | 3.90.0 |  |
|  nss-sysinit  | 3.90.0 |  |
|  nss-tools  | 3.90.0 |  |
|  nss-util  | 3.90.0 |  |
|  numactl-libs  | 2.0.9 | 2.0.14 |
|  oniguruma  |  | 6.9.7.1 |
|  openldap  | 2.4.44 | 2.4.57 |
|  openssh  | 7.4p1 | 8.7p1 |
|  openssh-clients  | 7.4p1 | 8.7p1 |
|  openssh-server  | 7.4p1 | 8.7p1 |
|  openssl  | 1.0.2k | 3.0.8 |
|  openssl-libs  | 1.0.2k | 3.0.8 |
|  openssl-pkcs11  |  | 0.4.12 |
|  os-prober  | 1.58 | 1.77 |
|  p11-kit  | 0.23.22 | 0.24.1 |
|  p11-kit-trust  | 0.23.22 | 0.24.1 |
|  pam  | 1.1.8 | 1.5.1 |
|  passwd  | 0.79 | 0.80 |
|  pciutils  |  | 3.7.0 |
|  pciutils-libs  |  | 3.7.0 |
|  [`pcre`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-pcre)  | 8.32 |  |
|  pcre2  | 10.23 | 10.40 |
|  pcre2-syntax  |  | 10.40 |
|  pinentry  | 0.8.1 |  |
|  pkgconfig  | 0.27.1 |  |
|  policycoreutils  | 2.5 | 3.4 |
|  popt  | 1.13 | 1.18 |
|  postfix  | 2.10.1 |  |
|  procps-ng  | 3.3.10 | 3.3.17 |
|  psmisc  | 22.20 | 23.4 |
|  pth  | 2.0.7 |  |
|  publicsuffix-list-dafsa  | 20240208 | 20240212 |
|  pygpgme  | 0.3 |  |
|  pyliblzma  | 0.5.3 |  |
|  [`python`](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  | 2.7.18 |  |
|  python2-cryptography  | 1.7.2 |  |
|  python2-jsonschema  | 2.5.1 |  |
|  python2-oauthlib  | 2.0.1 |  |
|  python2-pyasn1  | 0.1.9 |  |
|  python2-rpm  | 4.11.3 |  |
|  python2-setuptools  | 41.2.0 |  |
|  python2-six  | 1.11.0 |  |
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
|  python-babel  | 0.9.6 |  |
|  python-backports  | 1.0 |  |
|  python-backports-ssl\_match\_hostname  | 3.5.0.1 |  |
|  python-cffi  | 1.6.0 |  |
|  python-chardet  | 2.2.1 |  |
|  python-configobj  | 4.7.2 |  |
|  python-devel  | 2.7.18 |  |
|  python-enum34  | 1.0.4 |  |
|  python-idna  | 2.4 |  |
|  python-iniparse  | 0.4 |  |
|  python-ipaddress  | 1.0.16 |  |
|  python-jinja2  | 2.7.2 |  |
|  python-jsonpatch  | 1.2 |  |
|  python-jsonpointer  | 1.9 |  |
|  python-jwcrypto  | 0.4.2 |  |
|  python-libs  | 2.7.18 |  |
|  python-markupsafe  | 0.11 |  |
|  python-ply  | 3.4 |  |
|  python-pycparser  | 2.14 |  |
|  python-pycurl  | 7.19.0 |  |
|  python-repoze-lru  | 0.4 |  |
|  python-requests  | 2.6.0 |  |
|  python-urlgrabber  | 3.10 |  |
|  python-urllib3  | 1.25.9 |  |
|  pyxattr  | 0.5.1 |  |
|  PyYAML  | 3.10 |  |
|  qrencode-libs  | 3.4.1 |  |
|  readline  | 6.2 | 8.1 |
|  rng-tools  | 6.8 | 6.14 |
|  rootfiles  | 8.1 | 8.1 |
|  rpm  | 4.11.3 | 4.16.1.3 |
|  rpm-build-libs  | 4.11.3 | 4.16.1.3 |
|  rpm-libs  | 4.11.3 | 4.16.1.3 |
|  rpm-plugin-selinux  |  | 4.16.1.3 |
|  rpm-plugin-systemd-inhibit  | 4.11.3 | 4.16.1.3 |
|  rpm-sign-libs  |  | 4.16.1.3 |
|  rsyslog  | 8.24.0 |  |
|  sbsigntools  |  | 0.9.4 |
|  sed  | 4.2.2 | 4.8 |
|  selinux-policy  | 3.13.1 | 38.1.45 |
|  selinux-policy-targeted  | 3.13.1 | 38.1.45 |
|  setup  | 2.8.71 | 2.13.7 |
|  shadow-utils  | 4.1.5.1 | 4.9 |
|  shared-mime-info  | 1.8 |  |
|  slang  | 2.2.4 |  |
|  sqlite  | 3.7.17 |  |
|  sqlite-libs  |  | 3.40.0 |
|  sudo  | 1.8.23 | 1.9.15 |
|  sysctl-defaults  | 1.0 | 1.0 |
|  systemd  | 219 | 252.23 |
|  systemd-libs  | 219 | 252.23 |
|  systemd-networkd  |  | 252.23 |
|  systemd-pam  |  | 252.23 |
|  systemd-resolved  |  | 252.23 |
|  systemd-sysv  | 219 |  |
|  systemd-udev  |  | 252.23 |
|  system-release  | 2 | 2023.6.20241031 |
|  sysvinit-tools  | 2.88 |  |
|  tar  | 1.26 | 1.34 |
|  tcp\_wrappers-libs  | 7.6 |  |
|  tzdata  | 2024a | 2024a |
|  update-motd  | 1.1.2 | 2.2 |
|  userspace-rcu  |  | 0.12.1 |
|  ustr  | 1.0.4 |  |
|  util-linux  | 2.30.2 | 2.37.4 |
|  util-linux-core  |  | 2.37.4 |
|  vim-data  | 9.0.2153 | 9.0.2153 |
|  vim-minimal  | 9.0.2153 | 9.0.2153 |
|  which  | 2.20 | 2.21 |
|  xfsprogs  | 5.0.0 | 5.18.0 |
|  xz  | 5.2.2 | 5.2.5 |
|  xz-libs  | 5.2.2 | 5.2.5 |
|  yum  | 3.4.3 | 4.14.0 |
|  yum-metadata-parser  | 1.1.4 |  |
|  yum-plugin-priorities  | 1.1.31 |  |
|  zlib  | 1.2.7 | 1.2.11 |
|  zram-generator  |  | 1.1.2 |
|  zram-generator-defaults  |  | 1.1.2 |
|  zstd  |  | 1.5.5 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
