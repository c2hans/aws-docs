---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/al2027-container-ami.html
---

# Comparing packages installed on Amazon Linux 2027 Minimal AMI and Container Images
<a name="al2027-container-ami"></a>

A comparison of the RPMs present on the AL2027 Minimal AMI to the RPMs present on the AL2027 base and minimal container images.

| Package | Minimal AMI | Container | Minimal Container |
| --- | --- | --- | --- |
|  alternatives  | 1.33 | 1.33 | 1.33 |
|  amazon-chrony-config  | 4.8 |  |  |
|  amazon-ec2-net-utils  | 2.7.6 |  |  |
|  amazon-linux-repo-cdn  |  | 2027.0.20260903 | 2027.0.20260903 |
|  amazon-linux-repo-s3  | 2027.0.20260903 |  |  |
|  amazon-linux-sb-keys  | 2027.1 |  |  |
|  audit  | 4.1.3 |  |  |
|  audit-libs  | 4.1.3 |  |  |
|  audit-rules  | 4.1.3 |  |  |
|  authselect  | 1.7.1 |  |  |
|  authselect-libs  | 1.7.1 |  |  |
|  aws-lc-libs  | 5.2.0 |  |  |
|  awscli-2  | 2.36.2 |  |  |
|  bash  | 5.3.0 | 5.3.0 | 5.3.0 |
|  bzip2-libs  | 1.0.8 | 1.0.8 | 1.0.8 |
|  ca-certificates  | 2025.2.80\_v9.0.305 | 2025.2.80\_v9.0.305 | 2025.2.80\_v9.0.305 |
|  checkpolicy  | 3.10 |  |  |
|  chrony  | 4.8 |  |  |
|  cloud-init  | 26.1 |  |  |
|  cloud-init-cfg-ec2  | 26.1 |  |  |
|  cloud-utils-growpart  | 0.33 |  |  |
|  coreutils  | 9.10 |  |  |
|  coreutils-common  | 9.10 |  |  |
|  coreutils-single  |  | 9.10 | 9.10 |
|  cpio  | 2.15 |  |  |
|  cracklib  | 2.10.3 |  |  |
|  crypto-policies  | 20260525 | 20260525 | 20260525 |
|  cryptsetup-libs  | 2.8.4 |  |  |
|  curl  | 8.18.0 | 8.18.0 | 8.18.0 |
|  cyrus-sasl-lib  | 2.1.28 |  |  |
|  dbus  | 1.16.0 |  |  |
|  dbus-broker  | 37 |  |  |
|  dbus-common  | 1.16.0 |  |  |
|  dbus-libs  | 1.16.0 |  |  |
|  device-mapper  | 1.02.212 |  |  |
|  device-mapper-libs  | 1.02.212 |  |  |
|  diffutils  | 3.12 |  |  |
|  dnf-plugin-release-notification  | 2.0.0 |  |  |
|  dnf-plugin-support-info  | 3.0.0 |  |  |
|  dnf5  | 5.4.2.1 | 5.4.2.1 | 5.4.2.1 |
|  dracut  | 108 |  |  |
|  dracut-config-ec2  | 3.1 |  |  |
|  dracut-config-generic  | 108 |  |  |
|  e2fsprogs  | 1.47.3 |  |  |
|  e2fsprogs-libs  | 1.47.3 |  |  |
|  ec2-instance-connect  | 1.1 |  |  |
|  ec2-instance-connect-selinux  | 1.1 |  |  |
|  ec2-utils  | 2.2.0 |  |  |
|  efi-filesystem  | 6 |  |  |
|  efivar  | 39 |  |  |
|  efivar-libs  | 39 |  |  |
|  elfutils-libelf  | 0.195 |  |  |
|  expat  | 2.8.1 |  |  |
|  file  | 5.46 |  |  |
|  file-libs  | 5.46 |  |  |
|  filesystem  | 3.18 | 3.18 | 3.18 |
|  findutils  | 4.10.0 | 4.10.0 | 4.10.0 |
|  fmt  | 11.2.0 | 11.2.0 | 11.2.0 |
|  fuse3-libs  | 3.18.2 |  |  |
|  gawk  | 5.3.2 | 5.3.2 |  |
|  gdbm  | 1.23 |  |  |
|  gdbm-libs  | 1.23 |  |  |
|  gdisk  | 1.0.10 |  |  |
|  gettext  | 1.0 |  |  |
|  gettext-envsubst  | 1.0 |  |  |
|  gettext-libs  | 1.0 |  |  |
|  gettext-runtime  | 1.0 |  |  |
|  glib2  | 2.88.1 | 2.88.1 | 2.88.1 |
|  glibc  | 2.44 | 2.44 | 2.44 |
|  glibc-common  | 2.44 | 2.44 | 2.44 |
|  glibc-minimal-langpack  | 2.44 | 2.44 | 2.44 |
|  gmp  | 6.3.0 | 6.3.0 |  |
|  gnulib-l10n  | 20241231 |  |  |
|  gnutls  | 3.8.10 |  |  |
|  grep  | 3.12 | 3.12 | 3.12 |
|  grub2-common  | 2.12 |  |  |
|  grub2-efi-aa64-ec2  | 2.12 |  |  |
|  grub2-tools  | 2.12 |  |  |
|  grub2-tools-minimal  | 2.12 |  |  |
|  grubby  | 8.40 |  |  |
|  gzip  | 1.14 |  |  |
|  hostname  | 3.25 |  |  |
|  hwdata  | 0.409 |  |  |
|  inih  | 62 |  |  |
|  iproute  | 6.17.0 |  |  |
|  iputils  | 20250605 |  |  |
|  irqbalance  | 1.9.5 |  |  |
|  jq  | 1.8.1 |  |  |
|  json-c  | 0.18 | 0.18 | 0.18 |
|  kbd  | 2.10.0 |  |  |
|  kbd-legacy  | 2.10.0 |  |  |
|  kbd-misc  | 2.10.0 |  |  |
|  kernel7.1  | 7.1.0 |  |  |
|  keyutils-libs  | 1.6.3 | 1.6.3 | 1.6.3 |
|  kmod  | 34.2 |  |  |
|  kmod-libs  | 34.2 |  |  |
|  krb5-libs  | 1.22.2 | 1.22.2 | 1.22.2 |
|  less  | 702 |  |  |
|  libacl  | 2.4.0 | 2.4.0 | 2.4.0 |
|  libarchive  | 3.8.8 | 3.8.8 | 3.8.8 |
|  libattr  | 2.5.2 | 2.5.2 | 2.5.2 |
|  libblkid  | 2.41.5 | 2.41.5 | 2.41.5 |
|  libbpf  | 1.6.3 |  |  |
|  libcap  | 2.78 | 2.78 | 2.78 |
|  libcap-ng  | 0.9.3 |  |  |
|  libcbor  | 0.13.0 |  |  |
|  libcom\_err  | 1.47.3 | 1.47.3 | 1.47.3 |
|  libcurl-minimal  | 8.18.0 | 8.18.0 | 8.18.0 |
|  libdnf5  | 5.4.2.1 | 5.4.2.1 | 5.4.2.1 |
|  libdnf5-cli  | 5.4.2.1 | 5.4.2.1 | 5.4.2.1 |
|  libeconf  | 0.7.9 |  |  |
|  libedit  | 3.1 |  |  |
|  libevent  | 2.1.12 |  |  |
|  libfdisk  | 2.41.5 |  |  |
|  libffi  | 3.5.2 | 3.5.2 | 3.5.2 |
|  libfido2  | 1.16.0 |  |  |
|  libgcc  | 16.1.1 | 16.1.1 | 16.1.1 |
|  libgomp  | 16.1.1 |  |  |
|  libibverbs  | 61.0 |  |  |
|  libidn2  | 2.3.8 | 2.3.8 | 2.3.8 |
|  libkcapi  | 1.5.0 |  |  |
|  libkcapi-hasher  | 1.5.0 |  |  |
|  libkcapi-hmaccalc  | 1.5.0 |  |  |
|  liblastlog2  | 2.41.5 |  |  |
|  libmnl  | 1.0.5 |  |  |
|  libmount  | 2.41.5 | 2.41.5 | 2.41.5 |
|  libnghttp2  | 1.68.0 | 1.68.0 | 1.68.0 |
|  libnl3  | 3.12.0 |  |  |
|  libpcap  | 1.10.6 |  |  |
|  libpkgconf  | 2.5.1 |  |  |
|  libpsl  | 0.21.5 | 0.21.5 | 0.21.5 |
|  libpwquality  | 1.4.5 |  |  |
|  librepo  | 1.20.0 | 1.20.0 | 1.20.0 |
|  libseccomp  | 2.6.1 |  |  |
|  libselinux  | 3.10 | 3.10 | 3.10 |
|  libselinux-utils  | 3.10 |  |  |
|  libsemanage  | 3.10 |  |  |
|  libsepol  | 3.10 | 3.10 | 3.10 |
|  libsmartcols  | 2.41.5 | 2.41.5 | 2.41.5 |
|  libsolv  | 0.7.39 | 0.7.39 | 0.7.39 |
|  libss  | 1.47.3 |  |  |
|  libstdc\+\+  | 16.1.1 | 16.1.1 | 16.1.1 |
|  libsupportinfo  | 2.0.0 |  |  |
|  libtasn1  | 4.20.0 | 4.20.0 | 4.20.0 |
|  libtextstyle  | 1.0 |  |  |
|  libtool-ltdl  | 2.5.4 |  |  |
|  libunistring  | 1.1 | 1.1 | 1.1 |
|  libuuid  | 2.41.5 | 2.41.5 | 2.41.5 |
|  libverto  | 0.3.2 | 0.3.2 | 0.3.2 |
|  libxcrypt  | 4.5.2 |  |  |
|  libxkbcommon  | 1.13.1 |  |  |
|  libxml2  | 2.12.10 | 2.12.10 | 2.12.10 |
|  libyaml  | 0.2.5 |  |  |
|  libzstd  | 1.5.7 | 1.5.7 | 1.5.7 |
|  logrotate  | 3.22.0 |  |  |
|  lua-libs  | 5.4.8 | 5.4.8 | 5.4.8 |
|  lz4-libs  | 1.10.0 | 1.10.0 | 1.10.0 |
|  mpdecimal  | 4.0.1 |  |  |
|  mpfr  | 4.2.2 | 4.2.2 |  |
|  ncurses  | 6.6 |  |  |
|  ncurses-base  | 6.6 | 6.6 | 6.6 |
|  ncurses-libs  | 6.6 | 6.6 | 6.6 |
|  nettle  | 3.10.1 |  |  |
|  nmap-ncat  | 7.93 |  |  |
|  numactl-libs  | 2.0.19 |  |  |
|  oniguruma  | 6.9.10 |  |  |
|  openldap  | 2.6.13 |  |  |
|  openssh  | 9.9p1 |  |  |
|  openssh-clients  | 9.9p1 |  |  |
|  openssh-server  | 9.9p1 |  |  |
|  openssl  | 3.5.7 |  |  |
|  openssl-fips-provider-latest  | 3.5.7 | 3.5.7 | 3.5.7 |
|  openssl-libs  | 3.5.7 | 3.5.7 | 3.5.7 |
|  os-prober  | 1.81 |  |  |
|  p11-kit  | 0.26.2 | 0.26.2 | 0.26.2 |
|  p11-kit-trust  | 0.26.2 | 0.26.2 | 0.26.2 |
|  pam  | 1.7.1 |  |  |
|  pam-libs  | 1.7.1 |  |  |
|  pciutils  | 3.15.0 |  |  |
|  pciutils-libs  | 3.15.0 |  |  |
|  pcre2  | 10.47 | 10.47 | 10.47 |
|  pcre2-syntax  | 10.47 | 10.47 | 10.47 |
|  pkgconf  | 2.5.1 |  |  |
|  pkgconf-m4  | 2.5.1 |  |  |
|  pkgconf-pkg-config  | 2.5.1 |  |  |
|  policycoreutils  | 3.10 |  |  |
|  policycoreutils-python-utils  | 3.10 |  |  |
|  popt  | 1.19 | 1.19 | 1.19 |
|  procps-ng  | 4.0.6 |  |  |
|  psmisc  | 23.7 |  |  |
|  publicsuffix-list-dafsa  | 20260116 | 20260116 | 20260116 |
|  python3  | 3.14.7 |  |  |
|  python3-attrs  | 25.4.0 |  |  |
|  python3-audit  | 4.1.3 |  |  |
|  python3-awscrt  | 0.36.0 |  |  |
|  python3-cffi  | 2.0.0 |  |  |
|  python3-charset-normalizer  | 3.4.4 |  |  |
|  python3-colorama  | 0.4.6 |  |  |
|  python3-configobj  | 5.0.9 |  |  |
|  python3-cryptography  | 49.0.0 |  |  |
|  python3-dateutil  | 2.9.0.post0 |  |  |
|  python3-distro  | 1.9.0 |  |  |
|  python3-docutils  | 0.21.2 |  |  |
|  python3-idna  | 3.11 |  |  |
|  python3-jinja2  | 3.1.6 |  |  |
|  python3-jmespath  | 1.0.1 |  |  |
|  python3-jsonpatch  | 1.33 |  |  |
|  python3-jsonpointer  | 2.4 |  |  |
|  python3-jsonschema  | 4.23.0 |  |  |
|  python3-jsonschema-specifications  | 2024.10.1 |  |  |
|  python3-libs  | 3.14.7 |  |  |
|  python3-libselinux  | 3.10 |  |  |
|  python3-libsemanage  | 3.10 |  |  |
|  python3-markupsafe  | 3.0.2 |  |  |
|  python3-oauthlib  | 3.3.1 |  |  |
|  python3-pip-wheel  | 26.2.1 |  |  |
|  python3-ply  | 3.11 |  |  |
|  python3-policycoreutils  | 3.10 |  |  |
|  python3-prompt-toolkit  | 3.0.41 |  |  |
|  python3-pycparser  | 2.22 |  |  |
|  python3-pyyaml  | 6.0.3 |  |  |
|  python3-referencing  | 0.36.2 |  |  |
|  python3-requests  | 2.33.1 |  |  |
|  python3-rpds-py  | 0.27.0 |  |  |
|  python3-ruamel-yaml  | 0.19.1 |  |  |
|  python3-ruamel-yaml\+oldlibyaml  | 0.19.1 |  |  |
|  python3-ruamel-yaml-clib  | 0.2.15 |  |  |
|  python3-setools  | 4.6.0 |  |  |
|  python3-six  | 1.17.0 |  |  |
|  python3-urllib3  | 2.6.3 |  |  |
|  python3-wcwidth  | 0.6.0 |  |  |
|  rdma-core-common  | 61.0 |  |  |
|  readline  | 8.3 | 8.3 |  |
|  rootfiles  | 9.0 |  |  |
|  rpm  | 6.0.0 | 6.0.0 | 6.0.0 |
|  rpm-libs  | 6.0.0 | 6.0.0 | 6.0.0 |
|  rpm-plugin-selinux  | 6.0.0 |  |  |
|  rpm-plugin-systemd-inhibit  | 6.0.0 |  |  |
|  rpm-sequoia  | 1.10.2.1 | 1.10.2.1 | 1.10.2.1 |
|  sbsigntools  | 0.9.5 |  |  |
|  sdbus-cpp  | 2.2.1 | 2.2.1 | 2.2.1 |
|  sed  | 4.9 | 4.9 | 4.9 |
|  selinux-policy  | 44.5 |  |  |
|  selinux-policy-targeted  | 44.5 |  |  |
|  setup  | 2.15.1 | 2.15.1 | 2.15.1 |
|  shadow-utils  | 4.19.0 |  |  |
|  sqlite-libs  | 3.51.2 | 3.51.2 | 3.51.2 |
|  sudo  | 1.9.17 |  |  |
|  sysctl-defaults  | 1.0 |  |  |
|  system-release  | 2027.0.20260903 | 2027.0.20260903 | 2027.0.20260903 |
|  systemd  | 260.1 |  |  |
|  systemd-libs  | 260.1 | 260.1 | 260.1 |
|  systemd-networkd  | 260.1 |  |  |
|  systemd-resolved  | 260.1 |  |  |
|  systemd-shared  | 260.1 |  |  |
|  systemd-standalone-sysusers  |  | 260.1 | 260.1 |
|  systemd-sysusers  | 260.1 |  |  |
|  systemd-udev  | 260.1 |  |  |
|  tar  | 1.35 | 1.35 |  |
|  tzdata  | 2026c |  |  |
|  update-motd  | 2.3 |  |  |
|  userspace-rcu  | 0.15.6 |  |  |
|  util-linux  | 2.41.5 |  |  |
|  util-linux-core  | 2.41.5 |  |  |
|  vim-data  | 9.2.920 |  |  |
|  vim-minimal  | 9.2.920 |  |  |
|  which  | 2.25 |  |  |
|  xfsprogs  | 7.1.1 |  |  |
|  xkeyboard-config  | 2.47 |  |  |
|  xz  | 5.8.1 |  |  |
|  xz-libs  | 5.8.1 | 5.8.1 | 5.8.1 |
|  zlib-ng-compat  | 2.3.3 | 2.3.3 | 2.3.3 |
|  zram-generator  | 1.2.1 |  |  |
|  zram-generator-defaults  | 1.2.1 |  |  |
|  zstd  | 1.5.7 |  |  |
