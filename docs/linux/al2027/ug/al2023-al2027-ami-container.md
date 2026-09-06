---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/al2023-al2027-ami-container.html
---

# AMI package changes
<a name="al2023-al2027-ami-container"></a>

The set of packages installed by default differs between the AL2023 and AL2027 AMIs. The following tables list the RPMs present on the AL2023 and AL2027 standard and Minimal AMIs, along with their versions. A blank cell means the package is not installed by default on that AMI.

For the complete list of packages added, removed, and upgraded in the AL2027 repositories compared to AL2023, see [Package changes in Amazon Linux 2027](https://docs.aws.amazon.com/linux/al2027/release-notes/compare-packages.html).

AL2027 installs fewer packages by default than AL2023, which reduces the disk space used on the root volume, as shown in the following table.

## Comparing Amazon Linux 2023 and Amazon Linux 2027 AMI disk usage
<a name="al2023-al2027-ami-disk-usage"></a>

Root-filesystem disk usage of the AL2023 and AL2027 standard and Minimal AMIs, measured with `df -m` on the `aarch64` images. Lower usage leaves more free space on the root volume.

| AMI type | AL2023 | AL2027 | Reduction in AL2027 |
| --- | --- | --- | --- |
| Standard AMI | 1715 MiB | 1142 MiB | 33.4% |
| Minimal AMI | 1246 MiB | 893 MiB | 28.3% |

## Comparing packages installed on Amazon Linux 2023 and Amazon Linux 2027 AMIs
<a name="al2023-al2027-ami"></a>

A comparison of the RPMs present on the AL2023 and AL2027 standard AMIs.

| Package | AL2023 AMI | AL2027 AMI |
| --- | --- | --- |
|  acl  | 2.4.0 | 2.4.0 |
|  acpid  | 2.0.32 | 2.0.34 |
|  alternatives  | 1.15 | 1.33 |
|  amazon-chrony-config  | 4.3 | 4.8 |
|  amazon-ec2-net-utils  | 2.7.6 | 2.7.6 |
|  amazon-linux-repo-s3  | 2023.12.20260831 | 2027.0.20260903 |
|  amazon-linux-sb-keys  | 2023.1 | 2027.1 |
|  amazon-rpm-config  | 228 |  |
|  amazon-ssm-agent  | 3.3.4624.0 | 3.3.5226.0 |
|  at  | 3.1.23 |  |
|  attr  | 2.5.1 | 2.5.2 |
|  audit  | 3.1.5 | 4.1.3 |
|  audit-libs  | 3.1.5 | 4.1.3 |
|  audit-rules  |  | 4.1.3 |
|  authselect  |  | 1.7.1 |
|  authselect-libs  |  | 1.7.1 |
|  aws-cfn-bootstrap  | 2.0 | 2.0 |
|  aws-lc-libs  |  | 5.2.0 |
|  awscli-2  | 2.33.15 | 2.36.2 |
|  basesystem  | 11 |  |
|  bash  | 5.2.15 | 5.3.0 |
|  bash-completion  | 2.11 | 2.17 |
|  bc  | 1.07.1 |  |
|  bind-libs  | 9.18.50 |  |
|  bind-license  | 9.18.50 |  |
|  bind-utils  | 9.18.50 |  |
|  binutils  | 2.41 |  |
|  boost-filesystem  | 1.75.0 |  |
|  boost-system  | 1.75.0 |  |
|  boost-thread  | 1.75.0 |  |
|  bzip2  | 1.0.8 | 1.0.8 |
|  bzip2-libs  | 1.0.8 | 1.0.8 |
|  c-ares  | 1.19.1 | 1.34.6 |
|  ca-certificates  | 2025.2.76 | 2025.2.80\_v9.0.305 |
|  checkpolicy  | 3.4 | 3.10 |
|  chkconfig  | 1.15 |  |
|  chrony  | 4.3 | 4.8 |
|  cloud-init  | 22.2.2 | 26.1 |
|  cloud-init-cfg-ec2  | 22.2.2 | 26.1 |
|  cloud-utils-growpart  | 0.31 | 0.33 |
|  compact-dnf-utils  |  | 5.4.2.1 |
|  coreutils  | 8.32 | 9.10 |
|  coreutils-common  | 8.32 | 9.10 |
|  cpio  | 2.13 | 2.15 |
|  cracklib  | 2.9.6 | 2.10.3 |
|  cracklib-dicts  | 2.9.6 |  |
|  crontabs  | 1.11 |  |
|  crypto-policies  | 20260224 | 20260525 |
|  crypto-policies-scripts  | 20260224 |  |
|  cryptsetup  | 2.6.1 |  |
|  cryptsetup-libs  | 2.6.1 | 2.8.4 |
|  curl  |  | 8.18.0 |
|  curl-minimal  | 8.17.0 |  |
|  cyrus-sasl-gssapi  |  | 2.1.28 |
|  cyrus-sasl-lib  | 2.1.27 | 2.1.28 |
|  cyrus-sasl-plain  | 2.1.27 |  |
|  dbus  | 1.12.28 | 1.16.0 |
|  dbus-broker  | 32 | 37 |
|  dbus-common  | 1.12.28 | 1.16.0 |
|  dbus-libs  | 1.12.28 | 1.16.0 |
|  device-mapper  | 1.02.185 | 1.02.212 |
|  device-mapper-libs  | 1.02.185 | 1.02.212 |
|  diffutils  | 3.8 | 3.12 |
|  dnf  | 4.14.0 |  |
|  dnf-data  | 4.14.0 |  |
|  dnf-plugin-release-notification  | 1.4 | 2.0.0 |
|  dnf-plugin-support-info  | 2.0.0 | 3.0.0 |
|  dnf-plugins-core  | 4.3.0 |  |
|  dnf-utils  | 4.3.0 |  |
|  dnf5  |  | 5.4.2.1 |
|  dnf5-plugins  |  | 5.4.2.1 |
|  dosfstools  | 4.2 |  |
|  dracut  | 102 | 108 |
|  dracut-config-ec2  | 3.1 | 3.1 |
|  dracut-config-generic  | 102 | 108 |
|  dwz  | 0.16 |  |
|  dyninst  | 10.2.1 |  |
|  e2fsprogs  | 1.46.5 | 1.47.3 |
|  e2fsprogs-libs  | 1.46.5 | 1.47.3 |
|  ec2-hibinit-agent  | 1.0.12 |  |
|  ec2-instance-connect  | 1.1 | 1.1 |
|  ec2-instance-connect-selinux  | 1.1 | 1.1 |
|  ec2-utils  | 2.3.0 | 2.2.0 |
|  ed  | 1.14.2 |  |
|  efi-filesystem  | 5 | 6 |
|  efi-srpm-macros  | 5 |  |
|  efivar  | 38 | 39 |
|  efivar-libs  | 38 | 39 |
|  elfutils-debuginfod-client  | 0.188 |  |
|  elfutils-default-yama-scope  | 0.188 | 0.195 |
|  elfutils-libelf  | 0.188 | 0.195 |
|  elfutils-libs  | 0.188 | 0.195 |
|  ethtool  | 5.15 |  |
|  expat  | 2.6.3 | 2.8.1 |
|  file  | 5.39 | 5.46 |
|  file-libs  | 5.39 | 5.46 |
|  filesystem  | 3.14 | 3.18 |
|  findutils  | 4.8.0 | 4.10.0 |
|  fmt  |  | 11.2.0 |
|  fonts-srpm-macros  | 2.0.5 |  |
|  fstrm  | 0.6.1 |  |
|  fuse-libs  | 2.9.9 |  |
|  fuse3-libs  |  | 3.18.2 |
|  gawk  | 5.1.0 | 5.3.2 |
|  gdbm  |  | 1.23 |
|  gdbm-libs  | 1.19 | 1.23 |
|  gdisk  | 1.0.8 | 1.0.10 |
|  gettext  | 0.21 | 1.0 |
|  gettext-envsubst  |  | 1.0 |
|  gettext-libs  | 0.21 | 1.0 |
|  gettext-runtime  |  | 1.0 |
|  ghc-srpm-macros  | 1.5.0 |  |
|  glib2  | 2.82.2 | 2.88.1 |
|  glibc  | 2.34 | 2.44 |
|  glibc-all-langpacks  | 2.34 |  |
|  glibc-common  | 2.34 | 2.44 |
|  glibc-gconv-extra  | 2.34 |  |
|  glibc-locale-source  | 2.34 |  |
|  glibc-minimal-langpack  |  | 2.44 |
|  gmp  | 6.2.1 | 6.3.0 |
|  gnulib-l10n  |  | 20241231 |
|  gnupg2  |  | 2.4.9 |
|  gnupg2-dirmngr  |  | 2.4.9 |
|  gnupg2-gpg-agent  |  | 2.4.9 |
|  gnupg2-gpgconf  |  | 2.4.9 |
|  gnupg2-keyboxd  |  | 2.4.9 |
|  gnupg2-minimal  | 2.3.7 |  |
|  gnupg2-verify  |  | 2.4.9 |
|  gnutls  | 3.8.10 | 3.8.10 |
|  go-srpm-macros  | 3.8.0 |  |
|  gpgme  | 1.23.2 |  |
|  gpm-libs  | 1.20.7 |  |
|  grep  | 3.8 | 3.12 |
|  groff-base  | 1.22.4 | 1.23.0 |
|  grub2-common  | 2.06 | 2.12 |
|  grub2-efi-aa64-ec2  | 2.06 | 2.12 |
|  grub2-pc-modules  | 2.06 |  |
|  grub2-tools  | 2.06 | 2.12 |
|  grub2-tools-minimal  | 2.06 | 2.12 |
|  grubby  | 8.40 | 8.40 |
|  gssproxy  | 0.9.2 |  |
|  gzip  | 1.12 | 1.14 |
|  hostname  | 3.23 | 3.25 |
|  hunspell  | 1.7.0 |  |
|  hunspell-en  | 0.20201207 |  |
|  hunspell-en-GB  | 0.20201207 |  |
|  hunspell-en-US  | 0.20201207 |  |
|  hunspell-filesystem  | 1.7.0 |  |
|  hwdata  | 0.384 | 0.409 |
|  ima-evm-utils-libs  |  | 1.6.2 |
|  info  | 6.7 |  |
|  inih  | 58 | 62 |
|  initscripts  | 10.09 |  |
|  iproute  | 6.10.0 | 6.17.0 |
|  iputils  | 20210202 | 20250605 |
|  irqbalance  | 1.9.0 | 1.9.5 |
|  jansson  | 2.14 | 2.14 |
|  jemalloc  | 5.2.1 |  |
|  jitterentropy  | 3.4.1 |  |
|  jq  | 1.8.1 | 1.8.1 |
|  json-c  | 0.14 | 0.18 |
|  kbd  | 2.4.0 | 2.10.0 |
|  kbd-legacy  |  | 2.10.0 |
|  kbd-misc  | 2.4.0 | 2.10.0 |
|  kernel  | 6.1.182 |  |
|  kernel-livepatch-repo-s3  | 2023.12.20260831 |  |
|  kernel-srpm-macros  | 1.0 |  |
|  kernel-tools  | 6.1.182 |  |
|  kernel7.1  |  | 7.1.0 |
|  kernel7.1-tools  |  | 7.1.0 |
|  keyutils  | 1.6.3 |  |
|  keyutils-libs  | 1.6.3 | 1.6.3 |
|  kmod  | 29 | 34.2 |
|  kmod-libs  | 29 | 34.2 |
|  kpatch-runtime  | 0.9.10 |  |
|  krb5-libs  | 1.21.3 | 1.22.2 |
|  less  | 608 | 702 |
|  libacl  | 2.4.0 | 2.4.0 |
|  libaio  | 0.3.111 |  |
|  libarchive  | 3.7.4 | 3.8.8 |
|  libargon2  | 20171227 |  |
|  libassuan  | 2.5.5 | 2.5.7 |
|  libattr  | 2.5.1 | 2.5.2 |
|  libbasicobjects  | 0.1.1 | 0.1.1 |
|  libblkid  | 2.37.4 | 2.41.5 |
|  libbpf  | 1.6.1 | 1.6.3 |
|  libcap  | 2.73 | 2.78 |
|  libcap-ng  | 0.8.2 | 0.9.3 |
|  libcbor  | 0.7.0 | 0.13.0 |
|  libcollection  | 0.7.0 | 0.7.0 |
|  libcom\_err  | 1.46.5 | 1.47.3 |
|  libcomps  | 0.1.20 |  |
|  libconfig  | 1.7.2 |  |
|  libcurl-minimal  | 8.17.0 | 8.18.0 |
|  libdb  | 5.3.28 |  |
|  libdhash  | 0.5.0 | 0.5.0 |
|  libdnf  | 0.69.0 |  |
|  libdnf5  |  | 5.4.2.1 |
|  libdnf5-cli  |  | 5.4.2.1 |
|  libeconf  | 0.7.9 | 0.7.9 |
|  libedit  | 3.1 | 3.1 |
|  libev  | 4.33 |  |
|  libevent  | 2.1.12 | 2.1.12 |
|  libfdisk  | 2.37.4 | 2.41.5 |
|  libffi  | 3.4.4 | 3.5.2 |
|  libfido2  | 1.10.0 | 1.16.0 |
|  libgcc  | 14.2.1 | 16.1.1 |
|  libgcrypt  | 1.10.2 | 1.11.1 |
|  libgomp  | 14.2.1 | 16.1.1 |
|  libgpg-error  | 1.42 | 1.50 |
|  libibverbs  | 48.0 | 61.0 |
|  libicu  |  | 77.1 |
|  libidn2  | 2.3.2 | 2.3.8 |
|  libini\_config  | 1.3.1 | 1.3.1 |
|  libkcapi  | 1.4.0 | 1.5.0 |
|  libkcapi-hasher  |  | 1.5.0 |
|  libkcapi-hmaccalc  | 1.4.0 | 1.5.0 |
|  libksba  |  | 1.6.7 |
|  liblastlog2  |  | 2.41.5 |
|  libldb  | 2.6.2 | 4.24.6 |
|  libmaxminddb  | 1.5.2 |  |
|  libmetalink  | 0.1.3 |  |
|  libmnl  | 1.0.4 | 1.0.5 |
|  libmodulemd  | 2.13.0 |  |
|  libmount  | 2.37.4 | 2.41.5 |
|  libnfsidmap  | 2.5.4 |  |
|  libnghttp2  | 1.59.0 | 1.68.0 |
|  libnl3  | 3.5.0 | 3.12.0 |
|  libpath\_utils  | 0.2.1 | 0.2.1 |
|  libpcap  | 1.10.1 | 1.10.6 |
|  libpipeline  | 1.5.3 | 1.5.8 |
|  libpkgconf  | 1.8.0 | 2.5.1 |
|  libpsl  | 0.21.5 | 0.21.5 |
|  libpwquality  | 1.4.4 | 1.4.5 |
|  libref\_array  | 0.1.5 | 0.1.5 |
|  librepo  | 1.14.5 | 1.20.0 |
|  libreport-filesystem  | 2.15.2 |  |
|  libseccomp  | 2.5.3 | 2.6.1 |
|  libselinux  | 3.4 | 3.10 |
|  libselinux-utils  | 3.4 | 3.10 |
|  libsemanage  | 3.4 | 3.10 |
|  libsepol  | 3.4 | 3.10 |
|  libsigsegv  | 2.13 |  |
|  libsmartcols  | 2.37.4 | 2.41.5 |
|  libsolv  | 0.7.22 | 0.7.39 |
|  libss  | 1.46.5 | 1.47.3 |
|  libsss\_certmap  | 2.9.4 | 2.13.1 |
|  libsss\_idmap  | 2.9.4 | 2.13.1 |
|  libsss\_nss\_idmap  | 2.9.4 | 2.13.1 |
|  libsss\_sudo  | 2.9.4 | 2.13.1 |
|  libstdc\+\+  | 14.2.1 | 16.1.1 |
|  libstoragemgmt  | 1.9.4 |  |
|  libsupportinfo  |  | 2.0.0 |
|  libtalloc  | 2.3.4 | 2.4.4 |
|  libtasn1  | 4.19.0 | 4.20.0 |
|  libtdb  | 1.4.7 | 1.4.15 |
|  libtevent  | 0.13.0 | 0.17.1 |
|  libtextstyle  | 0.21 | 1.0 |
|  libtirpc  | 1.3.3 | 1.3.7 |
|  libtool-ltdl  |  | 2.5.4 |
|  libunistring  | 0.9.10 | 1.1 |
|  libusb1  |  | 1.0.30 |
|  libuser  | 0.63 |  |
|  libutempter  | 1.2.1 |  |
|  libuuid  | 2.37.4 | 2.41.5 |
|  libuv  | 1.51.0 |  |
|  libverto  | 0.3.2 | 0.3.2 |
|  libverto-libev  | 0.3.2 |  |
|  libxcrypt  | 4.4.33 | 4.5.2 |
|  libxkbcommon  |  | 1.13.1 |
|  libxml2  | 2.10.4 | 2.12.10 |
|  libxslt  | 1.1.43 |  |
|  libyaml  | 0.2.5 | 0.2.5 |
|  libzstd  | 1.5.5 | 1.5.7 |
|  lm\_sensors-libs  | 3.6.0 |  |
|  lmdb-libs  | 0.9.29 | 0.9.34 |
|  logrotate  | 3.20.1 | 3.22.0 |
|  lsof  | 4.94.0 | 4.98.0 |
|  lua-libs  | 5.4.4 | 5.4.8 |
|  lua-srpm-macros  | 1 |  |
|  lz4-libs  | 1.9.4 | 1.10.0 |
|  man-db  | 2.9.3 | 2.13.1 |
|  man-pages  | 6.04 | 6.13 |
|  mpdecimal  |  | 4.0.1 |
|  mpfr  | 4.1.0 | 4.2.2 |
|  nano  | 8.3 | 8.7.1 |
|  ncurses  | 6.6 |  |
|  ncurses-base  | 6.6 | 6.6 |
|  ncurses-libs  | 6.6 | 6.6 |
|  net-tools  | 2.0 |  |
|  nettle  | 3.10.1 | 3.10.1 |
|  newt  | 0.52.21 |  |
|  nfs-utils  | 2.5.4 |  |
|  nmap-ncat  |  | 7.93 |
|  npth  | 1.6 | 1.8 |
|  nspr  | 4.36.0 |  |
|  nss  | 3.112.0 |  |
|  nss-softokn  | 3.112.0 |  |
|  nss-softokn-freebl  | 3.112.0 |  |
|  nss-sysinit  | 3.112.0 |  |
|  nss-util  | 3.112.0 |  |
|  ntsysv  | 1.15 |  |
|  numactl-libs  | 2.0.14 | 2.0.19 |
|  ocaml-srpm-macros  | 6 |  |
|  oniguruma  | 6.9.7.1 | 6.9.10 |
|  openblas-srpm-macros  | 2 |  |
|  openldap  | 2.4.57 | 2.6.13 |
|  openssh  | 9.9p1 | 9.9p1 |
|  openssh-clients  | 9.9p1 | 9.9p1 |
|  openssh-server  | 9.9p1 | 9.9p1 |
|  openssl  | 3.5.7 | 3.5.7 |
|  openssl-fips-provider-latest  | 3.5.7 | 3.5.7 |
|  openssl-libs  | 3.5.7 | 3.5.7 |
|  openssl-pkcs11  | 0.4.12 |  |
|  os-prober  | 1.77 | 1.81 |
|  p11-kit  | 0.24.1 | 0.26.2 |
|  p11-kit-trust  | 0.24.1 | 0.26.2 |
|  package-notes-srpm-macros  | 0.4 |  |
|  pam  | 1.5.1 | 1.7.1 |
|  pam-libs  |  | 1.7.1 |
|  parted  | 3.4 |  |
|  passwd  | 0.80 |  |
|  pciutils  | 3.7.0 | 3.15.0 |
|  pciutils-libs  | 3.7.0 | 3.15.0 |
|  pcre2  | 10.40 | 10.47 |
|  pcre2-syntax  | 10.40 | 10.47 |
|  perl-AutoLoader  | 5.74 |  |
|  perl-B  | 1.80 |  |
|  perl-base  | 2.27 |  |
|  perl-Carp  | 1.50 |  |
|  perl-Class-Struct  | 0.66 |  |
|  perl-constant  | 1.33 |  |
|  perl-Data-Dumper  | 2.191 |  |
|  perl-Digest  | 1.20 |  |
|  perl-Digest-MD5  | 2.59 |  |
|  perl-DynaLoader  | 1.47 |  |
|  perl-Encode  | 3.21 |  |
|  perl-Errno  | 1.30 |  |
|  perl-Exporter  | 5.79 |  |
|  perl-Fcntl  | 1.13 |  |
|  perl-File-Basename  | 2.85 |  |
|  perl-File-Path  | 2.18 |  |
|  perl-File-stat  | 1.09 |  |
|  perl-File-Temp  | 0.231.200 |  |
|  perl-FileHandle  | 2.03 |  |
|  perl-Getopt-Long  | 2.58 |  |
|  perl-Getopt-Std  | 1.12 |  |
|  perl-HTTP-Tiny  | 0.092 |  |
|  perl-if  | 0.60.800 |  |
|  perl-interpreter  | 5.32.1 |  |
|  perl-IO  | 1.43 |  |
|  perl-IO-Socket-IP  | 0.43 |  |
|  perl-IO-Socket-SSL  | 2.075 |  |
|  perl-IPC-Open3  | 1.21 |  |
|  perl-libnet  | 3.13 |  |
|  perl-libs  | 5.32.1 |  |
|  perl-MIME-Base64  | 3.16 |  |
|  perl-mro  | 1.23 |  |
|  perl-Net-SSLeay  | 1.94 |  |
|  perl-overload  | 1.31 |  |
|  perl-overloading  | 0.02 |  |
|  perl-parent  | 0.238 |  |
|  perl-PathTools  | 3.78 |  |
|  perl-Pod-Escapes  | 1.07 |  |
|  perl-Pod-Perldoc  | 3.28.01 |  |
|  perl-Pod-Simple  | 3.42 |  |
|  perl-Pod-Usage  | 2.01 |  |
|  perl-podlators  | 4.14 |  |
|  perl-POSIX  | 1.94 |  |
|  perl-Scalar-List-Utils  | 1.56 |  |
|  perl-SelectSaver  | 1.02 |  |
|  perl-Socket  | 2.032 |  |
|  perl-srpm-macros  | 1 |  |
|  perl-Storable  | 3.37 |  |
|  perl-subs  | 1.03 |  |
|  perl-Symbol  | 1.08 |  |
|  perl-Term-ANSIColor  | 5.01 |  |
|  perl-Term-Cap  | 1.17 |  |
|  perl-Text-ParseWords  | 3.30 |  |
|  perl-Text-Tabs\+Wrap  | 2021.0726 |  |
|  perl-Time-HiRes  | 1.9764 |  |
|  perl-Time-Local  | 1.300 |  |
|  perl-URI  | 5.18 |  |
|  perl-vars  | 1.05 |  |
|  pkgconf  | 1.8.0 | 2.5.1 |
|  pkgconf-m4  | 1.8.0 | 2.5.1 |
|  pkgconf-pkg-config  | 1.8.0 | 2.5.1 |
|  policycoreutils  | 3.4 | 3.10 |
|  policycoreutils-python-utils  | 3.4 | 3.10 |
|  popt  | 1.18 | 1.19 |
|  procps-ng  | 3.3.17 | 4.0.6 |
|  protobuf-c  | 1.5.0 |  |
|  psacct  | 6.6.4 |  |
|  psmisc  | 23.4 | 23.7 |
|  publicsuffix-list-dafsa  | 20260116 | 20260116 |
|  python-chevron  | 0.13.1 | 0.14.0 |
|  python-srpm-macros  | 3.9 |  |
|  python3  | 3.9.25 | 3.14.7 |
|  python3-attrs  | 20.3.0 | 25.4.0 |
|  python3-audit  | 3.1.5 | 4.1.3 |
|  python3-awscrt  | 0.31.1 | 0.36.0 |
|  python3-babel  | 2.9.1 |  |
|  python3-cffi  | 1.14.5 |  |
|  python3-chardet  | 4.0.0 |  |
|  python3-charset-normalizer  |  | 3.4.4 |
|  python3-colorama  | 0.4.4 | 0.4.6 |
|  python3-configobj  | 5.0.6 | 5.0.9 |
|  python3-cryptography  | 36.0.1 |  |
|  python3-daemon  | 2.3.0 | 3.1.0 |
|  python3-dateutil  | 2.8.1 | 2.9.0.post0 |
|  python3-dbus  | 1.2.18 |  |
|  python3-distro  | 1.5.0 | 1.9.0 |
|  python3-dnf  | 4.14.0 |  |
|  python3-dnf-plugins-core  | 4.3.0 |  |
|  python3-docutils  | 0.16 | 0.21.2 |
|  python3-elementpath  | 2.3.2 |  |
|  python3-gpg  | 1.23.2 |  |
|  python3-hawkey  | 0.69.0 |  |
|  python3-idna  | 2.10 | 3.11 |
|  python3-jinja2  | 2.11.3 | 3.1.6 |
|  python3-jmespath  | 0.10.0 | 1.0.1 |
|  python3-jsonpatch  | 1.21 | 1.33 |
|  python3-jsonpointer  | 2.0 | 2.4 |
|  python3-jsonschema  | 3.2.0 | 4.23.0 |
|  python3-jsonschema-specifications  |  | 2024.10.1 |
|  python3-libcomps  | 0.1.20 |  |
|  python3-libdnf  | 0.69.0 |  |
|  python3-libs  | 3.9.25 | 3.14.7 |
|  python3-libselinux  | 3.4 | 3.10 |
|  python3-libsemanage  | 3.4 | 3.10 |
|  python3-libstoragemgmt  | 1.9.4 |  |
|  python3-lockfile  | 0.12.2 | 0.12.2 |
|  python3-lxml  | 4.7.1 |  |
|  python3-markupsafe  | 1.1.1 | 3.0.2 |
|  python3-netifaces  | 0.10.6 |  |
|  python3-oauthlib  | 3.0.2 | 3.3.1 |
|  python3-pip-wheel  | 21.3.1 | 26.2.1 |
|  python3-ply  | 3.11 |  |
|  python3-policycoreutils  | 3.4 | 3.10 |
|  python3-prettytable  | 0.7.2 |  |
|  python3-prompt-toolkit  | 3.0.24 | 3.0.41 |
|  python3-pycparser  | 2.20 |  |
|  python3-pyrsistent  | 0.17.3 |  |
|  python3-pyserial  | 3.4 |  |
|  python3-pysocks  | 1.7.1 |  |
|  python3-pytz  | 2022.7.1 |  |
|  python3-pyyaml  | 5.4.1 | 6.0.3 |
|  python3-referencing  |  | 0.36.2 |
|  python3-requests  | 2.25.1 | 2.33.1 |
|  python3-rpds-py  |  | 0.27.0 |
|  python3-rpm  | 4.16.1.3 |  |
|  python3-ruamel-yaml  | 0.16.6 | 0.19.1 |
|  python3-ruamel-yaml\+oldlibyaml  |  | 0.19.1 |
|  python3-ruamel-yaml-clib  | 0.1.2 | 0.2.15 |
|  python3-setools  | 4.4.1 | 4.6.0 |
|  python3-setuptools  | 59.6.0 |  |
|  python3-setuptools-wheel  | 59.6.0 |  |
|  python3-six  | 1.15.0 | 1.17.0 |
|  python3-supportinfo  | 1.0.0 |  |
|  python3-systemd  | 235 |  |
|  python3-urllib3  | 1.25.10 | 2.6.3 |
|  python3-wcwidth  | 0.2.5 | 0.6.0 |
|  python3-xmlschema  | 1.4.2 |  |
|  quota  | 4.06 |  |
|  quota-nls  | 4.06 |  |
|  rdma-core-common  |  | 61.0 |
|  readline  | 8.1 | 8.3 |
|  rng-tools  | 6.17 |  |
|  rootfiles  | 8.1 | 9.0 |
|  rpcbind  | 1.2.6 |  |
|  rpm  | 4.16.1.3 | 6.0.0 |
|  rpm-build-libs  | 4.16.1.3 | 6.0.0 |
|  rpm-libs  | 4.16.1.3 | 6.0.0 |
|  rpm-plugin-selinux  | 4.16.1.3 | 6.0.0 |
|  rpm-plugin-systemd-inhibit  | 4.16.1.3 | 6.0.0 |
|  rpm-sequoia  |  | 1.10.2.1 |
|  rpm-sign-libs  | 4.16.1.3 | 6.0.0 |
|  rsync  | 3.4.0 |  |
|  rust-toolset-srpm-macros  | 1.97.0 |  |
|  samba-common  |  | 4.24.6 |
|  samba-core-libs  |  | 4.24.6 |
|  samba-ndr-libs  |  | 4.24.6 |
|  sbsigntools  | 0.9.4 | 0.9.5 |
|  screen  | 4.8.0 |  |
|  sdbus-cpp  |  | 2.2.1 |
|  sed  | 4.8 | 4.9 |
|  selinux-policy  | 38.1.76 | 44.5 |
|  selinux-policy-targeted  | 38.1.76 | 44.5 |
|  setup  | 2.13.7 | 2.15.1 |
|  shadow-utils  | 4.9 | 4.19.0 |
|  slang  | 2.3.2 |  |
|  sqlite-libs  | 3.40.0 | 3.51.2 |
|  sssd-client  | 2.9.4 | 2.13.1 |
|  sssd-common  | 2.9.4 | 2.13.1 |
|  sssd-kcm  | 2.9.4 | 2.13.1 |
|  sssd-krb5-common  |  | 2.13.1 |
|  sssd-nfs-idmap  | 2.9.4 |  |
|  strace  | 6.12 |  |
|  sudo  | 1.9.15 | 1.9.17 |
|  sysctl-defaults  | 1.0 | 1.0 |
|  sysstat  | 12.5.6 |  |
|  system-release  | 2023.12.20260831 | 2027.0.20260903 |
|  systemd  | 252.23 | 260.1 |
|  systemd-libs  | 252.23 | 260.1 |
|  systemd-networkd  | 252.23 | 260.1 |
|  systemd-pam  | 252.23 | 260.1 |
|  systemd-resolved  | 252.23 | 260.1 |
|  systemd-shared  |  | 260.1 |
|  systemd-sysusers  |  | 260.1 |
|  systemd-udev  | 252.23 | 260.1 |
|  systemtap-runtime  | 5.4 |  |
|  tar  | 1.34 | 1.35 |
|  tbb  | 2020.3 |  |
|  tcpdump  | 4.99.1 |  |
|  tcsh  | 6.24.14 |  |
|  time  | 1.9 |  |
|  tpm2-tss  |  | 4.1.3 |
|  traceroute  | 2.1.3 |  |
|  tzdata  | 2026c | 2026c |
|  unzip  | 6.0 | 6.0 |
|  update-motd  | 2.3 | 2.3 |
|  userspace-rcu  | 0.12.1 | 0.15.6 |
|  util-linux  | 2.37.4 | 2.41.5 |
|  util-linux-core  | 2.37.4 | 2.41.5 |
|  vim-common  | 9.2.920 |  |
|  vim-data  | 9.2.920 | 9.2.920 |
|  vim-enhanced  | 9.2.920 |  |
|  vim-filesystem  | 9.2.920 |  |
|  vim-minimal  | 9.2.920 | 9.2.920 |
|  wget  | 1.21.3 |  |
|  which  | 2.21 | 2.25 |
|  words  | 3.0 |  |
|  xfsdump  | 3.1.11 |  |
|  xfsprogs  | 6.12.0 | 7.1.1 |
|  xkeyboard-config  |  | 2.47 |
|  xxd  | 9.2.920 |  |
|  xxhash-libs  | 0.8.0 |  |
|  xz  | 5.2.5 | 5.8.1 |
|  xz-libs  | 5.2.5 | 5.8.1 |
|  yum  | 4.14.0 |  |
|  zip  | 3.0 | 3.0 |
|  zlib  | 1.2.11 |  |
|  zlib-ng-compat  |  | 2.3.3 |
|  zram-generator  | 1.1.2 | 1.2.1 |
|  zram-generator-defaults  | 1.1.2 | 1.2.1 |
|  zstd  | 1.5.5 | 1.5.7 |

## Comparing packages installed on Amazon Linux 2023 and Amazon Linux 2027 Minimal AMIs
<a name="al2023-al2027-minimal-ami"></a>

A comparison of the RPMs present on the AL2023 and AL2027 Minimal AMIs.

| Package | AL2023 Minimal | AL2027 Minimal |
| --- | --- | --- |
|  alternatives  | 1.15 | 1.33 |
|  amazon-chrony-config  | 4.3 | 4.8 |
|  amazon-ec2-net-utils  | 2.7.6 | 2.7.6 |
|  amazon-linux-repo-s3  | 2023.12.20260831 | 2027.0.20260903 |
|  amazon-linux-sb-keys  | 2023.1 | 2027.1 |
|  audit  | 3.1.5 | 4.1.3 |
|  audit-libs  | 3.1.5 | 4.1.3 |
|  audit-rules  |  | 4.1.3 |
|  authselect  |  | 1.7.1 |
|  authselect-libs  |  | 1.7.1 |
|  aws-lc-libs  |  | 5.2.0 |
|  awscli-2  | 2.33.15 | 2.36.2 |
|  basesystem  | 11 |  |
|  bash  | 5.2.15 | 5.3.0 |
|  bzip2-libs  | 1.0.8 | 1.0.8 |
|  ca-certificates  | 2025.2.76 | 2025.2.80\_v9.0.305 |
|  checkpolicy  | 3.4 | 3.10 |
|  chrony  | 4.3 | 4.8 |
|  cloud-init  | 22.2.2 | 26.1 |
|  cloud-init-cfg-ec2  | 22.2.2 | 26.1 |
|  cloud-utils-growpart  | 0.31 | 0.33 |
|  coreutils  | 8.32 | 9.10 |
|  coreutils-common  | 8.32 | 9.10 |
|  cpio  | 2.13 | 2.15 |
|  cracklib  | 2.9.6 | 2.10.3 |
|  cracklib-dicts  | 2.9.6 |  |
|  crypto-policies  | 20260224 | 20260525 |
|  cryptsetup-libs  | 2.6.1 | 2.8.4 |
|  curl  |  | 8.18.0 |
|  curl-minimal  | 8.17.0 |  |
|  cyrus-sasl-lib  | 2.1.27 | 2.1.28 |
|  dbus  | 1.12.28 | 1.16.0 |
|  dbus-broker  | 32 | 37 |
|  dbus-common  | 1.12.28 | 1.16.0 |
|  dbus-libs  | 1.12.28 | 1.16.0 |
|  device-mapper  | 1.02.185 | 1.02.212 |
|  device-mapper-libs  | 1.02.185 | 1.02.212 |
|  diffutils  | 3.8 | 3.12 |
|  dnf  | 4.14.0 |  |
|  dnf-data  | 4.14.0 |  |
|  dnf-plugin-release-notification  | 1.4 | 2.0.0 |
|  dnf-plugin-support-info  | 2.0.0 | 3.0.0 |
|  dnf-plugins-core  | 4.3.0 |  |
|  dnf5  |  | 5.4.2.1 |
|  dracut  | 102 | 108 |
|  dracut-config-ec2  | 3.1 | 3.1 |
|  dracut-config-generic  | 102 | 108 |
|  e2fsprogs  | 1.46.5 | 1.47.3 |
|  e2fsprogs-libs  | 1.46.5 | 1.47.3 |
|  ec2-instance-connect  |  | 1.1 |
|  ec2-instance-connect-selinux  |  | 1.1 |
|  ec2-utils  | 2.3.0 | 2.2.0 |
|  efi-filesystem  | 5 | 6 |
|  efivar  | 38 | 39 |
|  efivar-libs  | 38 | 39 |
|  elfutils-default-yama-scope  | 0.188 |  |
|  elfutils-libelf  | 0.188 | 0.195 |
|  elfutils-libs  | 0.188 |  |
|  expat  | 2.6.3 | 2.8.1 |
|  file  | 5.39 | 5.46 |
|  file-libs  | 5.39 | 5.46 |
|  filesystem  | 3.14 | 3.18 |
|  findutils  | 4.8.0 | 4.10.0 |
|  fmt  |  | 11.2.0 |
|  fuse-libs  | 2.9.9 |  |
|  fuse3-libs  |  | 3.18.2 |
|  gawk  | 5.1.0 | 5.3.2 |
|  gdbm  |  | 1.23 |
|  gdbm-libs  | 1.19 | 1.23 |
|  gdisk  | 1.0.8 | 1.0.10 |
|  gettext  | 0.21 | 1.0 |
|  gettext-envsubst  |  | 1.0 |
|  gettext-libs  | 0.21 | 1.0 |
|  gettext-runtime  |  | 1.0 |
|  glib2  | 2.82.2 | 2.88.1 |
|  glibc  | 2.34 | 2.44 |
|  glibc-all-langpacks  | 2.34 |  |
|  glibc-common  | 2.34 | 2.44 |
|  glibc-locale-source  | 2.34 |  |
|  glibc-minimal-langpack  |  | 2.44 |
|  gmp  | 6.2.1 | 6.3.0 |
|  gnulib-l10n  |  | 20241231 |
|  gnupg2-minimal  | 2.3.7 |  |
|  gnutls  | 3.8.10 | 3.8.10 |
|  gpgme  | 1.23.2 |  |
|  grep  | 3.8 | 3.12 |
|  groff-base  | 1.22.4 |  |
|  grub2-common  | 2.06 | 2.12 |
|  grub2-efi-aa64-ec2  | 2.06 | 2.12 |
|  grub2-pc-modules  | 2.06 |  |
|  grub2-tools  | 2.06 | 2.12 |
|  grub2-tools-minimal  | 2.06 | 2.12 |
|  grubby  | 8.40 | 8.40 |
|  gzip  | 1.12 | 1.14 |
|  hostname  | 3.23 | 3.25 |
|  hwdata  | 0.384 | 0.409 |
|  inih  | 58 | 62 |
|  initscripts  | 10.09 |  |
|  iproute  | 6.10.0 | 6.17.0 |
|  iputils  | 20210202 | 20250605 |
|  irqbalance  | 1.9.0 | 1.9.5 |
|  jansson  | 2.14 |  |
|  jitterentropy  | 3.4.1 |  |
|  jq  | 1.8.1 | 1.8.1 |
|  json-c  | 0.14 | 0.18 |
|  kbd  | 2.4.0 | 2.10.0 |
|  kbd-legacy  |  | 2.10.0 |
|  kbd-misc  | 2.4.0 | 2.10.0 |
|  kernel  | 6.1.182 |  |
|  kernel-livepatch-repo-s3  | 2023.12.20260831 |  |
|  kernel7.1  |  | 7.1.0 |
|  keyutils-libs  | 1.6.3 | 1.6.3 |
|  kmod  | 29 | 34.2 |
|  kmod-libs  | 29 | 34.2 |
|  krb5-libs  | 1.21.3 | 1.22.2 |
|  less  | 608 | 702 |
|  libacl  | 2.4.0 | 2.4.0 |
|  libarchive  | 3.7.4 | 3.8.8 |
|  libargon2  | 20171227 |  |
|  libassuan  | 2.5.5 |  |
|  libattr  | 2.5.1 | 2.5.2 |
|  libblkid  | 2.37.4 | 2.41.5 |
|  libbpf  | 1.6.1 | 1.6.3 |
|  libcap  | 2.73 | 2.78 |
|  libcap-ng  | 0.8.2 | 0.9.3 |
|  libcbor  | 0.7.0 | 0.13.0 |
|  libcom\_err  | 1.46.5 | 1.47.3 |
|  libcomps  | 0.1.20 |  |
|  libcurl-minimal  | 8.17.0 | 8.18.0 |
|  libdb  | 5.3.28 |  |
|  libdnf  | 0.69.0 |  |
|  libdnf5  |  | 5.4.2.1 |
|  libdnf5-cli  |  | 5.4.2.1 |
|  libeconf  | 0.7.9 | 0.7.9 |
|  libedit  | 3.1 | 3.1 |
|  libevent  |  | 2.1.12 |
|  libfdisk  | 2.37.4 | 2.41.5 |
|  libffi  | 3.4.4 | 3.5.2 |
|  libfido2  | 1.10.0 | 1.16.0 |
|  libgcc  | 14.2.1 | 16.1.1 |
|  libgcrypt  | 1.10.2 |  |
|  libgomp  | 14.2.1 | 16.1.1 |
|  libgpg-error  | 1.42 |  |
|  libibverbs  |  | 61.0 |
|  libidn2  | 2.3.2 | 2.3.8 |
|  libkcapi  | 1.4.0 | 1.5.0 |
|  libkcapi-hasher  |  | 1.5.0 |
|  libkcapi-hmaccalc  | 1.4.0 | 1.5.0 |
|  liblastlog2  |  | 2.41.5 |
|  libmnl  | 1.0.4 | 1.0.5 |
|  libmodulemd  | 2.13.0 |  |
|  libmount  | 2.37.4 | 2.41.5 |
|  libnghttp2  | 1.59.0 | 1.68.0 |
|  libnl3  |  | 3.12.0 |
|  libpcap  |  | 1.10.6 |
|  libpipeline  | 1.5.3 |  |
|  libpkgconf  |  | 2.5.1 |
|  libpsl  | 0.21.5 | 0.21.5 |
|  libpwquality  | 1.4.4 | 1.4.5 |
|  librepo  | 1.14.5 | 1.20.0 |
|  libreport-filesystem  | 2.15.2 |  |
|  libseccomp  | 2.5.3 | 2.6.1 |
|  libselinux  | 3.4 | 3.10 |
|  libselinux-utils  | 3.4 | 3.10 |
|  libsemanage  | 3.4 | 3.10 |
|  libsepol  | 3.4 | 3.10 |
|  libsigsegv  | 2.13 |  |
|  libsmartcols  | 2.37.4 | 2.41.5 |
|  libsolv  | 0.7.22 | 0.7.39 |
|  libss  | 1.46.5 | 1.47.3 |
|  libstdc\+\+  | 14.2.1 | 16.1.1 |
|  libsupportinfo  |  | 2.0.0 |
|  libtasn1  | 4.19.0 | 4.20.0 |
|  libtextstyle  | 0.21 | 1.0 |
|  libtool-ltdl  |  | 2.5.4 |
|  libunistring  | 0.9.10 | 1.1 |
|  libuser  | 0.63 |  |
|  libutempter  | 1.2.1 |  |
|  libuuid  | 2.37.4 | 2.41.5 |
|  libverto  | 0.3.2 | 0.3.2 |
|  libxcrypt  | 4.4.33 | 4.5.2 |
|  libxkbcommon  |  | 1.13.1 |
|  libxml2  | 2.10.4 | 2.12.10 |
|  libxslt  | 1.1.43 |  |
|  libyaml  | 0.2.5 | 0.2.5 |
|  libzstd  | 1.5.5 | 1.5.7 |
|  logrotate  | 3.20.1 | 3.22.0 |
|  lua-libs  | 5.4.4 | 5.4.8 |
|  lz4-libs  | 1.9.4 | 1.10.0 |
|  man-db  | 2.9.3 |  |
|  mpdecimal  |  | 4.0.1 |
|  mpfr  | 4.1.0 | 4.2.2 |
|  ncurses  | 6.6 | 6.6 |
|  ncurses-base  | 6.6 | 6.6 |
|  ncurses-libs  | 6.6 | 6.6 |
|  net-tools  | 2.0 |  |
|  nettle  | 3.10.1 | 3.10.1 |
|  nmap-ncat  |  | 7.93 |
|  npth  | 1.6 |  |
|  numactl-libs  | 2.0.14 | 2.0.19 |
|  oniguruma  | 6.9.7.1 | 6.9.10 |
|  openldap  | 2.4.57 | 2.6.13 |
|  openssh  | 9.9p1 | 9.9p1 |
|  openssh-clients  | 9.9p1 | 9.9p1 |
|  openssh-server  | 9.9p1 | 9.9p1 |
|  openssl  | 3.5.7 | 3.5.7 |
|  openssl-fips-provider-latest  | 3.5.7 | 3.5.7 |
|  openssl-libs  | 3.5.7 | 3.5.7 |
|  openssl-pkcs11  | 0.4.12 |  |
|  os-prober  | 1.77 | 1.81 |
|  p11-kit  | 0.24.1 | 0.26.2 |
|  p11-kit-trust  | 0.24.1 | 0.26.2 |
|  pam  | 1.5.1 | 1.7.1 |
|  pam-libs  |  | 1.7.1 |
|  passwd  | 0.80 |  |
|  pciutils  | 3.7.0 | 3.15.0 |
|  pciutils-libs  | 3.7.0 | 3.15.0 |
|  pcre2  | 10.40 | 10.47 |
|  pcre2-syntax  | 10.40 | 10.47 |
|  pkgconf  |  | 2.5.1 |
|  pkgconf-m4  |  | 2.5.1 |
|  pkgconf-pkg-config  |  | 2.5.1 |
|  policycoreutils  | 3.4 | 3.10 |
|  policycoreutils-python-utils  |  | 3.10 |
|  popt  | 1.18 | 1.19 |
|  procps-ng  | 3.3.17 | 4.0.6 |
|  psmisc  | 23.4 | 23.7 |
|  publicsuffix-list-dafsa  | 20260116 | 20260116 |
|  python3  | 3.9.25 | 3.14.7 |
|  python3-attrs  | 20.3.0 | 25.4.0 |
|  python3-audit  | 3.1.5 | 4.1.3 |
|  python3-awscrt  | 0.31.1 | 0.36.0 |
|  python3-babel  | 2.9.1 |  |
|  python3-cffi  | 1.14.5 | 2.0.0 |
|  python3-chardet  | 4.0.0 |  |
|  python3-charset-normalizer  |  | 3.4.4 |
|  python3-colorama  | 0.4.4 | 0.4.6 |
|  python3-configobj  | 5.0.6 | 5.0.9 |
|  python3-cryptography  | 36.0.1 | 49.0.0 |
|  python3-dateutil  | 2.8.1 | 2.9.0.post0 |
|  python3-dbus  | 1.2.18 |  |
|  python3-distro  | 1.5.0 | 1.9.0 |
|  python3-dnf  | 4.14.0 |  |
|  python3-dnf-plugins-core  | 4.3.0 |  |
|  python3-docutils  | 0.16 | 0.21.2 |
|  python3-elementpath  | 2.3.2 |  |
|  python3-gpg  | 1.23.2 |  |
|  python3-hawkey  | 0.69.0 |  |
|  python3-idna  | 2.10 | 3.11 |
|  python3-jinja2  | 2.11.3 | 3.1.6 |
|  python3-jmespath  | 0.10.0 | 1.0.1 |
|  python3-jsonpatch  | 1.21 | 1.33 |
|  python3-jsonpointer  | 2.0 | 2.4 |
|  python3-jsonschema  | 3.2.0 | 4.23.0 |
|  python3-jsonschema-specifications  |  | 2024.10.1 |
|  python3-libcomps  | 0.1.20 |  |
|  python3-libdnf  | 0.69.0 |  |
|  python3-libs  | 3.9.25 | 3.14.7 |
|  python3-libselinux  | 3.4 | 3.10 |
|  python3-libsemanage  | 3.4 | 3.10 |
|  python3-lxml  | 4.7.1 |  |
|  python3-markupsafe  | 1.1.1 | 3.0.2 |
|  python3-netifaces  | 0.10.6 |  |
|  python3-oauthlib  | 3.0.2 | 3.3.1 |
|  python3-pip-wheel  | 21.3.1 | 26.2.1 |
|  python3-ply  | 3.11 | 3.11 |
|  python3-policycoreutils  | 3.4 | 3.10 |
|  python3-prettytable  | 0.7.2 |  |
|  python3-prompt-toolkit  | 3.0.24 | 3.0.41 |
|  python3-pycparser  | 2.20 | 2.22 |
|  python3-pyrsistent  | 0.17.3 |  |
|  python3-pyserial  | 3.4 |  |
|  python3-pysocks  | 1.7.1 |  |
|  python3-pytz  | 2022.7.1 |  |
|  python3-pyyaml  | 5.4.1 | 6.0.3 |
|  python3-referencing  |  | 0.36.2 |
|  python3-requests  | 2.25.1 | 2.33.1 |
|  python3-rpds-py  |  | 0.27.0 |
|  python3-rpm  | 4.16.1.3 |  |
|  python3-ruamel-yaml  | 0.16.6 | 0.19.1 |
|  python3-ruamel-yaml\+oldlibyaml  |  | 0.19.1 |
|  python3-ruamel-yaml-clib  | 0.1.2 | 0.2.15 |
|  python3-setools  | 4.4.1 | 4.6.0 |
|  python3-setuptools  | 59.6.0 |  |
|  python3-setuptools-wheel  | 59.6.0 |  |
|  python3-six  | 1.15.0 | 1.17.0 |
|  python3-supportinfo  | 1.0.0 |  |
|  python3-systemd  | 235 |  |
|  python3-urllib3  | 1.25.10 | 2.6.3 |
|  python3-wcwidth  | 0.2.5 | 0.6.0 |
|  python3-xmlschema  | 1.4.2 |  |
|  rdma-core-common  |  | 61.0 |
|  readline  | 8.1 | 8.3 |
|  rng-tools  | 6.17 |  |
|  rootfiles  | 8.1 | 9.0 |
|  rpm  | 4.16.1.3 | 6.0.0 |
|  rpm-build-libs  | 4.16.1.3 |  |
|  rpm-libs  | 4.16.1.3 | 6.0.0 |
|  rpm-plugin-selinux  | 4.16.1.3 | 6.0.0 |
|  rpm-plugin-systemd-inhibit  | 4.16.1.3 | 6.0.0 |
|  rpm-sequoia  |  | 1.10.2.1 |
|  rpm-sign-libs  | 4.16.1.3 |  |
|  sbsigntools  | 0.9.4 | 0.9.5 |
|  sdbus-cpp  |  | 2.2.1 |
|  sed  | 4.8 | 4.9 |
|  selinux-policy  | 38.1.76 | 44.5 |
|  selinux-policy-targeted  | 38.1.76 | 44.5 |
|  setup  | 2.13.7 | 2.15.1 |
|  shadow-utils  | 4.9 | 4.19.0 |
|  sqlite-libs  | 3.40.0 | 3.51.2 |
|  sudo  | 1.9.15 | 1.9.17 |
|  sysctl-defaults  | 1.0 | 1.0 |
|  system-release  | 2023.12.20260831 | 2027.0.20260903 |
|  systemd  | 252.23 | 260.1 |
|  systemd-libs  | 252.23 | 260.1 |
|  systemd-networkd  | 252.23 | 260.1 |
|  systemd-pam  | 252.23 |  |
|  systemd-resolved  | 252.23 | 260.1 |
|  systemd-shared  |  | 260.1 |
|  systemd-sysusers  |  | 260.1 |
|  systemd-udev  | 252.23 | 260.1 |
|  tar  | 1.34 | 1.35 |
|  tzdata  | 2026c | 2026c |
|  update-motd  | 2.3 | 2.3 |
|  userspace-rcu  | 0.12.1 | 0.15.6 |
|  util-linux  | 2.37.4 | 2.41.5 |
|  util-linux-core  | 2.37.4 | 2.41.5 |
|  vim-data  | 9.2.920 | 9.2.920 |
|  vim-minimal  | 9.2.920 | 9.2.920 |
|  which  | 2.21 | 2.25 |
|  xfsprogs  | 6.12.0 | 7.1.1 |
|  xkeyboard-config  |  | 2.47 |
|  xz  | 5.2.5 | 5.8.1 |
|  xz-libs  | 5.2.5 | 5.8.1 |
|  yum  | 4.14.0 |  |
|  zlib  | 1.2.11 |  |
|  zlib-ng-compat  |  | 2.3.3 |
|  zram-generator  | 1.1.2 | 1.2.1 |
|  zram-generator-defaults  | 1.1.2 | 1.2.1 |
|  zstd  | 1.5.5 | 1.5.7 |
