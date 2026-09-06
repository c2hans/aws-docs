---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/amzn1-al2023-container.html
---

# Comparing packages installed on Amazon Linux 1 (AL1) and Amazon Linux 2023 base container images
<a name="amzn1-al2023-container"></a>

A comparison of the RPMs present on the AL1 and AL2023 base container images.

| Package | AL1 Container | AL2023 Container |
| --- | --- | --- |
|  alternatives  |  | 1.15 |
|  amazon-linux-repo-cdn  |  | 2023.6.20241031 |
|  audit-libs  |  | 3.0.6 |
|  basesystem  | 10.0 | 11 |
|  bash  | 4.2.46 | 5.2.15 |
|  bzip2-libs  | 1.0.6 | 1.0.8 |
|  ca-certificates  | 2023.2.62 | 2023.2.68 |
|  chkconfig  | 1.3.49.3 |  |
|  coreutils  | 8.22 |  |
|  coreutils-single  |  | 8.32 |
|  crypto-policies  |  | 20220428 |
|  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  | 7.61.1 |  |
|  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  |  | 8.5.0 |
|  cyrus-sasl-lib  | 2.1.23 |  |
|  db4  | 4.7.25 |  |
|  db4-utils  | 4.7.25 |  |
|  dnf  |  | 4.14.0 |
|  dnf-data  |  | 4.14.0 |
|  elfutils-default-yama-scope  |  | 0.188 |
|  elfutils-libelf  | 0.168 | 0.188 |
|  elfutils-libs  |  | 0.188 |
|  expat  | 2.1.0 | 2.5.0 |
|  file-libs  | 5.37 | 5.39 |
|  filesystem  | 2.4.30 | 3.14 |
|  gawk  | 3.1.7 | 5.1.0 |
|  gdbm  | 1.8.0 |  |
|  gdbm-libs  |  | 1.19 |
|  glib2  | 2.36.3 | 2.74.7 |
|  [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html)  | 2.17 | 2.34 |
|  glibc-common  | 2.17 | 2.34 |
|  glibc-minimal-langpack  |  | 2.34 |
|  gmp  | 6.0.0 | 6.2.1 |
|  [`gnupg2`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  | 2.0.28 |  |
|  [`gnupg2-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  |  | 2.3.7 |
|  gpgme  | 1.4.3 | 1.15.1 |
|  grep  | 2.20 | 3.8 |
|  gzip  | 1.5 |  |
|  info  | 5.1 |  |
|  json-c  |  | 0.14 |
|  keyutils-libs  | 1.5.8 | 1.6.3 |
|  krb5-libs  | 1.15.1 | 1.21.3 |
|  libacl  | 2.2.49 | 2.3.1 |
|  libarchive  |  | 3.7.4 |
|  libassuan  | 2.0.3 | 2.5.5 |
|  libattr  | 2.4.46 | 2.5.1 |
|  libblkid  |  | 2.37.4 |
|  libcap  | 2.16 | 2.48 |
|  libcap-ng  |  | 0.8.2 |
|  libcom\_err  | 1.43.5 | 1.46.5 |
|  libcomps  |  | 0.1.20 |
|  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  | 7.61.1 |  |
|  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  |  | 8.5.0 |
|  libdnf  |  | 0.69.0 |
|  libffi  | 3.0.13 | 3.4.4 |
|  libgcc  |  | 11.4.1 |
|  libgcc72  | 7.2.1 |  |
|  libgcrypt  | 1.5.3 | 1.10.2 |
|  libgomp  |  | 11.4.1 |
|  libgpg-error  | 1.11 | 1.42 |
|  libicu  | 50.2 |  |
|  libidn2  | 2.3.0 | 2.3.2 |
|  libmodulemd  |  | 2.13.0 |
|  libmount  |  | 2.37.4 |
|  libnghttp2  | 1.33.0 | 1.59.0 |
|  libpsl  | 0.6.2 | 0.21.1 |
|  librepo  |  | 1.14.5 |
|  libreport-filesystem  |  | 2.15.2 |
|  libselinux  | 2.1.10 | 3.4 |
|  libsepol  | 2.1.7 | 3.4 |
|  libsigsegv  |  | 2.13 |
|  libsmartcols  |  | 2.37.4 |
|  libsolv  |  | 0.7.22 |
|  libssh2  | 1.4.2 |  |
|  libstdc\+\+  |  | 11.4.1 |
|  libstdc\+\+72  | 7.2.1 |  |
|  libtasn1  | 2.3 | 4.19.0 |
|  libunistring  | 0.9.3 | 0.9.10 |
|  libuuid  |  | 2.37.4 |
|  libverto  | 0.2.5 | 0.3.2 |
|  libxcrypt  |  | 4.4.33 |
|  libxml2  | 2.9.1 | 2.10.4 |
|  libxml2-python27  | 2.9.1 |  |
|  libyaml  |  | 0.2.5 |
|  libzstd  |  | 1.5.5 |
|  lua  | 5.1.4 |  |
|  lua-libs  |  | 5.4.4 |
|  lz4-libs  |  | 1.9.4 |
|  make  | 3.82 |  |
|  mpfr  |  | 4.1.0 |
|  ncurses  | 5.7 |  |
|  ncurses-base  | 5.7 | 6.2 |
|  ncurses-libs  | 5.7 | 6.2 |
|  npth  |  | 1.6 |
|  nspr  | 4.25.0 |  |
|  nss  | 3.53.1 |  |
|  nss-pem  | 1.0.3 |  |
|  nss-softokn  | 3.53.1 |  |
|  nss-softokn-freebl  | 3.53.1 |  |
|  nss-sysinit  | 3.53.1 |  |
|  nss-tools  | 3.53.1 |  |
|  nss-util  | 3.53.1 |  |
|  openldap  | 2.4.40 |  |
|  openssl  | 1.0.2k |  |
|  openssl-libs  |  | 3.0.8 |
|  p11-kit  | 0.18.5 | 0.24.1 |
|  p11-kit-trust  | 0.18.5 | 0.24.1 |
|  [`pcre`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-pcre)  | 8.21 |  |
|  pcre2  |  | 10.40 |
|  pcre2-syntax  |  | 10.40 |
|  pinentry  | 0.7.6 |  |
|  pkgconfig  | 0.27.1 |  |
|  popt  | 1.13 | 1.18 |
|  pth  | 2.0.7 |  |
|  publicsuffix-list-dafsa  |  | 20240212 |
|  python27  | 2.7.18 |  |
|  python27-chardet  | 2.0.1 |  |
|  python27-iniparse  | 0.3.1 |  |
|  python27-kitchen  | 1.1.1 |  |
|  python27-libs  | 2.7.18 |  |
|  python27-pycurl  | 7.19.0 |  |
|  python27-pygpgme  | 0.3 |  |
|  python27-pyliblzma  | 0.5.3 |  |
|  python27-pyxattr  | 0.5.0 |  |
|  python27-urlgrabber  | 3.10 |  |
|  python3  |  | 3.9.16 |
|  python3-dnf  |  | 4.14.0 |
|  python3-gpg  |  | 1.15.1 |
|  python3-hawkey  |  | 0.69.0 |
|  python3-libcomps  |  | 0.1.20 |
|  python3-libdnf  |  | 0.69.0 |
|  python3-libs  |  | 3.9.16 |
|  python3-pip-wheel  |  | 21.3.1 |
|  python3-rpm  |  | 4.16.1.3 |
|  python3-setuptools-wheel  |  | 59.6.0 |
|  readline  | 6.2 | 8.1 |
|  rpm  | 4.11.3 | 4.16.1.3 |
|  rpm-build-libs  | 4.11.3 | 4.16.1.3 |
|  rpm-libs  | 4.11.3 | 4.16.1.3 |
|  rpm-python27  | 4.11.3 |  |
|  rpm-sign-libs  |  | 4.16.1.3 |
|  sed  | 4.2.1 | 4.8 |
|  setup  | 2.8.14 | 2.13.7 |
|  shared-mime-info  | 1.1 |  |
|  sqlite  | 3.7.17 |  |
|  sqlite-libs  |  | 3.40.0 |
|  sysctl-defaults  | 1.0 |  |
|  system-release  | 2018.03 | 2023.6.20241031 |
|  tar  | 1.26 |  |
|  tzdata  | 2023c | 2024a |
|  xz-libs  | 5.2.2 | 5.2.5 |
|  yum  | 3.4.3 | 4.14.0 |
|  yum-metadata-parser  | 1.1.4 |  |
|  yum-plugin-ovl  | 1.1.31 |  |
|  yum-plugin-priorities  | 1.1.31 |  |
|  yum-utils  | 1.1.31 |  |
|  zlib  | 1.2.8 | 1.2.11 |
