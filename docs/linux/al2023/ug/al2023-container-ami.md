---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/al2023-container-ami.html
---

# Comparing packages installed on Amazon Linux 2023 Minimal AMI and Container Images
<a name="al2023-container-ami"></a>

A comparison of the RPMs present on the AL2023 Minimial AMI to the RPMs present on the AL2023 base and minimal container images.

| Package | Minimal AMI | Container | Minimal Container |
| --- | --- | --- | --- |
|  alternatives  | 1.15 | 1.15 | 1.15 |
|  amazon-chrony-config  | 4.3 |  |  |
|  [`amazon-ec2-net-utils`](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html)  | 2.5.1 |  |  |
|  amazon-linux-repo-cdn  |  | 2023.6.20241031 | 2023.6.20241031 |
|  amazon-linux-repo-s3  | 2023.6.20241031 |  |  |
|  [`amazon-linux-sb-keys`](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html)  | 2023.1 |  |  |
|  amd-ucode-firmware  | 20210208 (noarch) |  |  |
|  audit  | 3.0.6 |  |  |
|  audit-libs  | 3.0.6 | 3.0.6 | 3.0.6 |
|  awscli-2  | 2.15.30 |  |  |
|  basesystem  | 11 | 11 | 11 |
|  bash  | 5.2.15 | 5.2.15 | 5.2.15 |
|  bzip2-libs  | 1.0.8 | 1.0.8 | 1.0.8 |
|  ca-certificates  | 2023.2.68 | 2023.2.68 | 2023.2.68 |
|  checkpolicy  | 3.4 |  |  |
|  chrony  | 4.3 |  |  |
|  cloud-init  | 22.2.2 |  |  |
|  cloud-init-cfg-ec2  | 22.2.2 |  |  |
|  cloud-utils-growpart  | 0.31 |  |  |
|  coreutils  | 8.32 |  |  |
|  coreutils-common  | 8.32 |  |  |
|  coreutils-single  |  | 8.32 | 8.32 |
|  cpio  | 2.13 |  |  |
|  cracklib  | 2.9.6 |  |  |
|  cracklib-dicts  | 2.9.6 |  |  |
|  crypto-policies  | 20220428 | 20220428 | 20220428 |
|  cryptsetup-libs  | 2.6.1 |  |  |
|  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  | 8.5.0 | 8.5.0 | 8.5.0 |
|  cyrus-sasl-lib  | 2.1.27 |  |  |
|  dbus  | 1.12.28 |  |  |
|  dbus-broker  | 32 |  |  |
|  dbus-common  | 1.12.28 |  |  |
|  dbus-libs  | 1.12.28 |  |  |
|  device-mapper  | 1.02.185 |  |  |
|  device-mapper-libs  | 1.02.185 |  |  |
|  diffutils  | 3.8 |  |  |
|  dnf  | 4.14.0 | 4.14.0 |  |
|  dnf-data  | 4.14.0 | 4.14.0 | 4.14.0 |
|  dnf-plugin-release-notification  | 1.2 |  |  |
|  dnf-plugins-core  | 4.3.0 |  |  |
|  dnf-plugin-support-info  | 1.2 |  |  |
|  dracut  | 055 |  |  |
|  dracut-config-ec2  | 3.0 |  |  |
|  dracut-config-generic  | 055 |  |  |
|  e2fsprogs  | 1.46.5 |  |  |
|  e2fsprogs-libs  | 1.46.5 |  |  |
|  ec2-utils  | 2.2.0 |  |  |
|  efi-filesystem  | 5 |  |  |
|  efivar  | 38 |  |  |
|  efivar-libs  | 38 |  |  |
|  elfutils-default-yama-scope  | 0.188 | 0.188 |  |
|  elfutils-libelf  | 0.188 | 0.188 |  |
|  elfutils-libs  | 0.188 | 0.188 |  |
|  expat  | 2.5.0 | 2.5.0 |  |
|  file  | 5.39 |  |  |
|  file-libs  | 5.39 | 5.39 | 5.39 |
|  filesystem  | 3.14 | 3.14 | 3.14 |
|  findutils  | 4.8.0 |  |  |
|  fuse-libs  | 2.9.9 |  |  |
|  gawk  | 5.1.0 | 5.1.0 | 5.1.0 |
|  gdbm-libs  | 1.19 | 1.19 |  |
|  gdisk  | 1.0.8 |  |  |
|  gettext  | 0.21 |  |  |
|  gettext-libs  | 0.21 |  |  |
|  glib2  | 2.74.7 | 2.74.7 | 2.74.7 |
|  [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html)  | 2.34 | 2.34 | 2.34 |
|  glibc-all-langpacks  | 2.34 |  |  |
|  glibc-common  | 2.34 | 2.34 | 2.34 |
|  glibc-locale-source  | 2.34 |  |  |
|  glibc-minimal-langpack  |  | 2.34 | 2.34 |
|  gmp  | 6.2.1 | 6.2.1 | 6.2.1 |
|  [`gnupg2-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  | 2.3.7 | 2.3.7 | 2.3.7 |
|  gnutls  | 3.8.0 |  |  |
|  gobject-introspection  |  |  | 1.73.0 |
|  gpgme  | 1.15.1 | 1.15.1 | 1.15.1 |
|  grep  | 3.8 | 3.8 | 3.8 |
|  groff-base  | 1.22.4 |  |  |
|  grub2-common  | 2.06 |  |  |
|  grub2-efi-aa64-ec2  | 2.06 (aarch64) |  |  |
|  grub2-efi-x64-ec2  | 2.06 (x86\_64) |  |  |
|  grub2-pc-modules  | 2.06 |  |  |
|  grub2-tools  | 2.06 |  |  |
|  grub2-tools-minimal  | 2.06 |  |  |
|  grubby  | 8.40 |  |  |
|  gzip  | 1.12 |  |  |
|  hostname  | 3.23 |  |  |
|  hwdata  | 0.384 |  |  |
|  inih  | 49 |  |  |
|  initscripts  | 10.09 |  |  |
|  iproute  | 6.10.0 |  |  |
|  iputils  | 20210202 |  |  |
|  irqbalance  | 1.9.0 |  |  |
|  jansson  | 2.14 |  |  |
|  jitterentropy  | 3.4.1 |  |  |
|  jq  | 1.7.1 |  |  |
|  json-c  | 0.14 | 0.14 | 0.14 |
|  kbd  | 2.4.0 |  |  |
|  kbd-misc  | 2.4.0 |  |  |
|  kernel  | 6.1.112 |  |  |
|  kernel-libbpf  | 6.1.112 |  |  |
|  kernel-livepatch-repo-s3  | 2023.6.20241031 |  |  |
|  keyutils-libs  | 1.6.3 | 1.6.3 | 1.6.3 |
|  kmod  | 29 |  |  |
|  kmod-libs  | 29 |  |  |
|  krb5-libs  | 1.21.3 | 1.21.3 | 1.21.3 |
|  less  | 608 |  |  |
|  libacl  | 2.3.1 | 2.3.1 | 2.3.1 |
|  libarchive  | 3.7.4 | 3.7.4 | 3.7.4 |
|  libargon2  | 20171227 |  |  |
|  libassuan  | 2.5.5 | 2.5.5 | 2.5.5 |
|  libattr  | 2.5.1 | 2.5.1 | 2.5.1 |
|  libblkid  | 2.37.4 | 2.37.4 | 2.37.4 |
|  libcap  | 2.48 | 2.48 | 2.48 |
|  libcap-ng  | 0.8.2 | 0.8.2 | 0.8.2 |
|  libcbor  | 0.7.0 |  |  |
|  libcom\_err  | 1.46.5 | 1.46.5 | 1.46.5 |
|  libcomps  | 0.1.20 | 0.1.20 |  |
|  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  | 8.5.0 | 8.5.0 | 8.5.0 |
|  [`libdb`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-bdb)  | 5.3.28 |  |  |
|  libdnf  | 0.69.0 | 0.69.0 | 0.69.0 |
|  libeconf  | 0.4.0 |  |  |
|  libedit  | 3.1 |  |  |
|  libfdisk  | 2.37.4 |  |  |
|  libffi  | 3.4.4 | 3.4.4 | 3.4.4 |
|  libfido2  | 1.10.0 |  |  |
|  libgcc  | 11.4.1 | 11.4.1 | 11.4.1 |
|  libgcrypt  | 1.10.2 | 1.10.2 | 1.10.2 |
|  libgomp  | 11.4.1 | 11.4.1 |  |
|  libgpg-error  | 1.42 | 1.42 | 1.42 |
|  libidn2  | 2.3.2 | 2.3.2 | 2.3.2 |
|  libkcapi  | 1.4.0 |  |  |
|  libkcapi-hmaccalc  | 1.4.0 |  |  |
|  libmnl  | 1.0.4 |  |  |
|  libmodulemd  | 2.13.0 | 2.13.0 | 2.13.0 |
|  libmount  | 2.37.4 | 2.37.4 | 2.37.4 |
|  libnghttp2  | 1.59.0 | 1.59.0 | 1.59.0 |
|  libpeas  |  |  | 1.32.0 |
|  libpipeline  | 1.5.3 |  |  |
|  libpsl  | 0.21.1 | 0.21.1 | 0.21.1 |
|  libpwquality  | 1.4.4 |  |  |
|  librepo  | 1.14.5 | 1.14.5 | 1.14.5 |
|  libreport-filesystem  | 2.15.2 | 2.15.2 | 2.15.2 |
|  libseccomp  | 2.5.3 |  |  |
|  libselinux  | 3.4 | 3.4 | 3.4 |
|  libselinux-utils  | 3.4 |  |  |
|  libsemanage  | 3.4 |  |  |
|  libsepol  | 3.4 | 3.4 | 3.4 |
|  libsigsegv  | 2.13 | 2.13 | 2.13 |
|  libsmartcols  | 2.37.4 | 2.37.4 | 2.37.4 |
|  libsolv  | 0.7.22 | 0.7.22 | 0.7.22 |
|  libss  | 1.46.5 |  |  |
|  libstdc\+\+  | 11.4.1 | 11.4.1 | 11.4.1 |
|  libtasn1  | 4.19.0 | 4.19.0 | 4.19.0 |
|  libtextstyle  | 0.21 |  |  |
|  libunistring  | 0.9.10 | 0.9.10 | 0.9.10 |
|  libuser  | 0.63 |  |  |
|  libutempter  | 1.2.1 |  |  |
|  libuuid  | 2.37.4 | 2.37.4 | 2.37.4 |
|  libverto  | 0.3.2 | 0.3.2 | 0.3.2 |
|  libxcrypt  | 4.4.33 | 4.4.33 |  |
|  libxml2  | 2.10.4 | 2.10.4 | 2.10.4 |
|  libyaml  | 0.2.5 | 0.2.5 | 0.2.5 |
|  libzstd  | 1.5.5 | 1.5.5 | 1.5.5 |
|  linux-firmware-whence  | 20210208 (noarch) |  |  |
|  logrotate  | 3.20.1 |  |  |
|  lua-libs  | 5.4.4 | 5.4.4 | 5.4.4 |
|  lz4-libs  | 1.9.4 | 1.9.4 | 1.9.4 |
|  man-db  | 2.9.3 |  |  |
|  microcode\_ctl  | 2.1 (x86\_64) |  |  |
|  microdnf  |  |  | 3.10.0 |
|  microdnf-dnf  |  |  | 3.10.0 |
|  mpfr  | 4.1.0 | 4.1.0 | 4.1.0 |
|  ncurses  | 6.2 |  |  |
|  ncurses-base  | 6.2 | 6.2 | 6.2 |
|  ncurses-libs  | 6.2 | 6.2 | 6.2 |
|  nettle  | 3.8 |  |  |
|  net-tools  | 2.0 |  |  |
|  npth  | 1.6 | 1.6 | 1.6 |
|  numactl-libs  | 2.0.14 |  |  |
|  oniguruma  | 6.9.7.1 |  |  |
|  openldap  | 2.4.57 |  |  |
|  openssh  | 8.7p1 |  |  |
|  openssh-clients  | 8.7p1 |  |  |
|  openssh-server  | 8.7p1 |  |  |
|  openssl  | 3.0.8 |  |  |
|  openssl-libs  | 3.0.8 | 3.0.8 | 3.0.8 |
|  openssl-pkcs11  | 0.4.12 |  |  |
|  os-prober  | 1.77 |  |  |
|  p11-kit  | 0.24.1 | 0.24.1 | 0.24.1 |
|  p11-kit-trust  | 0.24.1 | 0.24.1 | 0.24.1 |
|  pam  | 1.5.1 |  |  |
|  passwd  | 0.80 |  |  |
|  pciutils  | 3.7.0 |  |  |
|  pciutils-libs  | 3.7.0 |  |  |
|  pcre2  | 10.40 | 10.40 | 10.40 |
|  pcre2-syntax  | 10.40 | 10.40 | 10.40 |
|  policycoreutils  | 3.4 |  |  |
|  popt  | 1.18 | 1.18 | 1.18 |
|  procps-ng  | 3.3.17 |  |  |
|  psmisc  | 23.4 |  |  |
|  publicsuffix-list-dafsa  | 20240212 | 20240212 | 20240212 |
|  python3  | 3.9.16 | 3.9.16 |  |
|  python3-attrs  | 20.3.0 |  |  |
|  python3-audit  | 3.0.6 |  |  |
|  python3-awscrt  | 0.19.19 |  |  |
|  python3-babel  | 2.9.1 |  |  |
|  python3-cffi  | 1.14.5 |  |  |
|  python3-chardet  | 4.0.0 |  |  |
|  python3-colorama  | 0.4.4 |  |  |
|  python3-configobj  | 5.0.6 |  |  |
|  python3-cryptography  | 36.0.1 |  |  |
|  python3-dateutil  | 2.8.1 |  |  |
|  python3-dbus  | 1.2.18 |  |  |
|  python3-distro  | 1.5.0 |  |  |
|  python3-dnf  | 4.14.0 | 4.14.0 |  |
|  python3-dnf-plugins-core  | 4.3.0 |  |  |
|  python3-docutils  | 0.16 |  |  |
|  python3-gpg  | 1.15.1 | 1.15.1 |  |
|  python3-hawkey  | 0.69.0 | 0.69.0 |  |
|  python3-idna  | 2.10 |  |  |
|  python3-jinja2  | 2.11.3 |  |  |
|  python3-jmespath  | 0.10.0 |  |  |
|  python3-jsonpatch  | 1.21 |  |  |
|  python3-jsonpointer  | 2.0 |  |  |
|  python3-jsonschema  | 3.2.0 |  |  |
|  python3-libcomps  | 0.1.20 | 0.1.20 |  |
|  python3-libdnf  | 0.69.0 | 0.69.0 |  |
|  python3-libs  | 3.9.16 | 3.9.16 |  |
|  python3-libselinux  | 3.4 |  |  |
|  python3-libsemanage  | 3.4 |  |  |
|  python3-markupsafe  | 1.1.1 |  |  |
|  python3-netifaces  | 0.10.6 |  |  |
|  python3-oauthlib  | 3.0.2 |  |  |
|  python3-pip-wheel  | 21.3.1 | 21.3.1 |  |
|  python3-ply  | 3.11 |  |  |
|  python3-policycoreutils  | 3.4 |  |  |
|  python3-prettytable  | 0.7.2 |  |  |
|  python3-prompt-toolkit  | 3.0.24 |  |  |
|  python3-pycparser  | 2.20 |  |  |
|  python3-pyrsistent  | 0.17.3 |  |  |
|  python3-pyserial  | 3.4 |  |  |
|  python3-pysocks  | 1.7.1 |  |  |
|  python3-pytz  | 2022.7.1 |  |  |
|  python3-pyyaml  | 5.4.1 |  |  |
|  python3-requests  | 2.25.1 |  |  |
|  python3-rpm  | 4.16.1.3 | 4.16.1.3 |  |
|  python3-ruamel-yaml  | 0.16.6 |  |  |
|  python3-ruamel-yaml-clib  | 0.1.2 |  |  |
|  python3-setools  | 4.4.1 |  |  |
|  python3-setuptools  | 59.6.0 |  |  |
|  python3-setuptools-wheel  | 59.6.0 | 59.6.0 |  |
|  python3-six  | 1.15.0 |  |  |
|  python3-systemd  | 235 |  |  |
|  python3-urllib3  | 1.25.10 |  |  |
|  python3-wcwidth  | 0.2.5 |  |  |
|  readline  | 8.1 | 8.1 | 8.1 |
|  rng-tools  | 6.14 |  |  |
|  rootfiles  | 8.1 |  |  |
|  rpm  | 4.16.1.3 | 4.16.1.3 | 4.16.1.3 |
|  rpm-build-libs  | 4.16.1.3 | 4.16.1.3 |  |
|  rpm-libs  | 4.16.1.3 | 4.16.1.3 | 4.16.1.3 |
|  rpm-plugin-selinux  | 4.16.1.3 |  |  |
|  rpm-plugin-systemd-inhibit  | 4.16.1.3 |  |  |
|  rpm-sign-libs  | 4.16.1.3 | 4.16.1.3 |  |
|  sbsigntools  | 0.9.4 |  |  |
|  sed  | 4.8 | 4.8 | 4.8 |
|  selinux-policy  | 38.1.45 |  |  |
|  selinux-policy-targeted  | 38.1.45 |  |  |
|  setup  | 2.13.7 | 2.13.7 | 2.13.7 |
|  shadow-utils  | 4.9 |  |  |
|  sqlite-libs  | 3.40.0 | 3.40.0 | 3.40.0 |
|  sudo  | 1.9.15 |  |  |
|  sysctl-defaults  | 1.0 |  |  |
|  systemd  | 252.23 |  |  |
|  systemd-libs  | 252.23 |  |  |
|  systemd-networkd  | 252.23 |  |  |
|  systemd-pam  | 252.23 |  |  |
|  systemd-resolved  | 252.23 |  |  |
|  systemd-udev  | 252.23 |  |  |
|  system-release  | 2023.6.20241031 | 2023.6.20241031 | 2023.6.20241031 |
|  tar  | 1.34 |  |  |
|  tzdata  | 2024a | 2024a |  |
|  update-motd  | 2.2 |  |  |
|  userspace-rcu  | 0.12.1 |  |  |
|  util-linux  | 2.37.4 |  |  |
|  util-linux-core  | 2.37.4 |  |  |
|  vim-data  | 9.0.2153 |  |  |
|  vim-minimal  | 9.0.2153 |  |  |
|  which  | 2.21 |  |  |
|  xfsprogs  | 5.18.0 |  |  |
|  xz  | 5.2.5 |  |  |
|  xz-libs  | 5.2.5 | 5.2.5 | 5.2.5 |
|  yum  | 4.14.0 | 4.14.0 |  |
|  zlib  | 1.2.11 | 1.2.11 | 1.2.11 |
|  zram-generator  | 1.1.2 |  |  |
|  zram-generator-defaults  | 1.1.2 |  |  |
|  zstd  | 1.5.5 |  |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
