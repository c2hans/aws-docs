---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.11.20260526.html
---

# Amazon Linux 2023 version 2023.11.20260526 release notes
<a name="relnotes-2023.11.20260526"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.11.20260526.

**Contents**
+ [Release Summary](#release-summary-2023.11.20260526)
+ [Repository Updates](#repository-updates-2023.11.20260526)
  + [Core Updated Packages](#amis-2023.11.20260526.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.11.20260526.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.11.20260526.Kernel-livepatch-Updated-Packages)
  + [Nvidia Updated Packages](#amis-2023.11.20260526.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.11.20260526)
  + [Default Kernel 6.18 AMI](#amis-2023.11.20260526.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.11.20260526.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.11.20260526.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.11.20260526.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.11.20260526.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.11.20260526.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.11.20260526.Default-Container)
  + [Minimal Container](#amis-2023.11.20260526.Minimal-Container)
+ [Contact us](#amis-2023.11.20260526.contact-us)

## Release Summary
<a name="release-summary-2023.11.20260526"></a>

This release represents an update to the 11th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.11.20260526"></a>

### Core Updated Packages
<a name="amis-2023.11.20260526.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

|  |
| --- |
|  amazon-cloudwatch-agent-1.300066.2-2.amzn2023  |
|  amazon-ecr-credential-helper-0.12.0-3.amzn2023  |
|  bind-9.18.49-1.amzn2023.0.1  |
|  cni-plugins-1.7.1-1.amzn2023.0.6  |
|  containerd-2.2.3-1.amzn2023.0.2  |
|  credentials-fetcher-2.0.1-1.amzn2023.0.5  |
|  dkms-3.4.1-184.amzn2023  |
|  dnf-plugin-support-info-1.13-1.amzn2023  |
|  dnsmasq-2.90-1.amzn2023.0.3  |
|  docker-25.0.14-1.amzn2023.0.6  |
|  firefox-140.10.2-1.amzn2023.0.3  |
|  git-lfs-3.7.1-80.amzn2023  |
|  glycin-1.1.2-11.amzn2023  |
|  gnutls-3.8.3-8.amzn2023.0.3  |
|  golang-1.25.10-1.amzn2023.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2023.0.1  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2023.0.3  |
|  golang-github-cpuguy83-md2man-2.0.2-24.amzn2023.0.7  |
|  golist-0.10.4-12.amzn2023.0.9  |
|  httpd-2.4.67-1.amzn2023.0.1  |
|  kernel-6.1.172-216.329.amzn2023  |
|  kernel6.12-6.12.88-119.157.amzn2023  |
|  kernel6.18-6.18.30-61.116.amzn2023  |
|  lasso-2.9.0-1.amzn2023.0.1  |
|  ldns-1.8.3-2.amzn2023.0.3  |
|  libcap-2.73-1.amzn2023.0.7  |
|  libpq-18.4-1.amzn2023.0.1  |
|  librsvg2-2.59.2-319.amzn2023  |
|  libsolv-0.7.22-1.amzn2023.0.3  |
|  libsoup-2.72.0-6.amzn2023.0.12  |
|  mod\_http2-2.0.39-1.amzn2023.0.1  |
|  nerdctl-2.2.2-1.amzn2023.0.2  |
|  nginx-1.30.1-1.amzn2023.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.6  |
|  nkf-2.1.4-19.amzn2023.0.4  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.11  |
|  openexr-3.1.5-1.amzn2023.0.11  |
|  openssh-8.7p1-8.amzn2023.0.18  |
|  perl-B-COW-0.007-12.amzn2023.0.2  |
|  perl-B-Compiling-0.06-21.amzn2023.0.3  |
|  perl-B-Hooks-OP-Check-0.22-13.amzn2023.0.3  |
|  perl-B-Utils-0.27-19.amzn2023.0.3  |
|  perl-BSD-Resource-1.291.100-15.amzn2023.0.3  |
|  perl-Bit-Vector-7.4-22.amzn2023.0.4  |
|  perl-Class-Load-XS-0.10-14.amzn2023.0.3  |
|  perl-Class-XSAccessor-1.19-23.amzn2023.0.3  |
|  perl-Clone-0.47-4.amzn2023.0.2  |
|  perl-Compress-Bzip2-2.28-3.amzn2023.0.3  |
|  perl-Compress-Raw-Bzip2-2.217-1.amzn2023.0.2  |
|  perl-Compress-Raw-Lzma-2.221-1.amzn2023.0.2  |
|  perl-Compress-Raw-Zlib-2.221-1.amzn2023.0.2  |
|  perl-Cpanel-JSON-XS-4.25-2.amzn2023.0.8  |
|  perl-Crypt-Blowfish-2.14-33.amzn2023.0.3  |
|  perl-Crypt-DES-2.07-30.amzn2023.0.4  |
|  perl-Crypt-IDEA-1.10-26.amzn2023.0.2  |
|  perl-Crypt-OpenSSL-Bignum-0.09-23.amzn2023.0.1  |
|  perl-Crypt-OpenSSL-RSA-0.33-3.amzn2023.0.1  |
|  perl-Crypt-OpenSSL-Random-0.17-6.amzn2023.0.2  |
|  perl-Crypt-Rijndael-1.16-7.amzn2023.0.2  |
|  perl-Crypt-SSLeay-0.72-45.amzn2023.0.2  |
|  perl-CryptX-0.088-2.amzn2023.0.2  |
|  perl-Curses-1.45-2.amzn2023.0.2  |
|  perl-DBD-MariaDB-1.22-1.amzn2023.0.5  |
|  perl-DBD-MySQL-4.050-10.amzn2023.0.3  |
|  perl-DBD-Pg-3.18.0-6.amzn2023.0.2  |
|  perl-DBD-SQLite-1.66-3.amzn2023.0.4  |
|  perl-DBI-1.647-1.amzn2023.0.2  |
|  perl-DB\_File-1.860-1.amzn2023.0.2  |
|  perl-Data-Dump-Streamer-2.40-17.amzn2023.0.3  |
|  perl-Data-Dumper-2.191-522.amzn2023.0.3  |
|  perl-Data-UUID-1.227-7.amzn2023.0.2  |
|  perl-Date-Simple-3.03-38.amzn2023.0.3  |
|  perl-DateTime-1.54-2.amzn2023.0.3  |
|  perl-Devel-CallChecker-0.008-12.amzn2023.0.3  |
|  perl-Devel-CallParser-0.002-24.amzn2023.0.3  |
|  perl-Devel-Caller-2.07-11.amzn2023.0.2  |
|  perl-Devel-Cover-1.36-4.amzn2023.0.3  |
|  perl-Devel-Declare-0.006022-5.amzn2023.0.3  |
|  perl-Devel-Leak-0.03-45.amzn2023.0.3  |
|  perl-Devel-LexAlias-0.05-25.amzn2023.0.3  |
|  perl-Devel-PPPort-3.73-522.amzn2023.0.2  |
|  perl-Devel-Refcount-0.10-24.amzn2023.0.3  |
|  perl-Devel-Size-0.86-1.amzn2023.0.2  |
|  perl-Digest-CRC-0.24-13.amzn2023.0.2  |
|  perl-Digest-MD4-1.9-27.amzn2023.0.3  |
|  perl-Digest-MD5-2.59-521.amzn2023.0.2  |
|  perl-Digest-SHA-6.04-522.amzn2023.0.2  |
|  perl-Digest-SHA1-2.13-32.amzn2023.0.3  |
|  perl-Digest-SHA3-1.05-12.amzn2023.0.2  |
|  perl-Encode-3.21-520.amzn2023.0.2  |
|  perl-Encode-Detect-1.01-44.amzn2023.0.1  |
|  perl-Encode-EUCJPASCII-0.03-32.amzn2023.0.3  |
|  perl-Encode-HanExtra-0.23-32.amzn2023.0.3  |
|  perl-Encode-JIS2K-0.05-9.amzn2023.0.2  |
|  perl-FileHandle-Fmode-0.15-6.amzn2023.0.2  |
|  perl-Filter-1.65-2.amzn2023.0.2  |
|  perl-Function-Parameters-2.1.3-11.amzn2023.0.3  |
|  perl-GD-2.80-1.amzn2023.0.2  |
|  perl-GSSAPI-0.28-35.amzn2023.0.3  |
|  perl-Graphics-TIFF-18-4.amzn2023.0.1  |
|  perl-HTML-Parser-3.76-1.amzn2023.0.3  |
|  perl-Hash-FieldHash-0.15-16.amzn2023.0.3  |
|  perl-IO-Tty-1.20-9.amzn2023.0.2  |
|  perl-IPC-ShareLite-0.17-35.amzn2023.0.3  |
|  perl-IPC-SysV-2.09-2.amzn2023.0.3  |
|  perl-JSON-XS-4.04-2.amzn2023.0.2  |
|  perl-Lexical-SealRequireHints-0.011-15.amzn2023.0.3  |
|  perl-Lexical-Var-0.009-25.amzn2023.0.3  |
|  perl-Linux-Pid-0.04-44.amzn2023.0.3  |
|  perl-List-MoreUtils-XS-0.430-2.amzn2023.0.4  |
|  perl-MIME-Base64-3.16-2.amzn2023.0.3  |
|  perl-Math-BigInt-FastCalc-0.501.400-3.amzn2023.0.2  |
|  perl-Moose-2.2014-2.amzn2023.0.5  |
|  perl-MooseX-Role-WithOverloading-0.17-19.amzn2023.0.3  |
|  perl-Mouse-2.5.10-5.amzn2023.0.3  |
|  perl-Net-CIDR-Lite-0.22-8.amzn2023.0.2  |
|  perl-Net-IDN-Encode-2.500-9.amzn2023.0.3  |
|  perl-Net-LibIDN-0.12-39.amzn2023.0.4  |
|  perl-Net-LibIDN2-1.02-4.amzn2023.0.1  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.3  |
|  perl-NetAddr-IP-4.079-25.amzn2023.0.1  |
|  perl-Package-Anon-0.05-28.amzn2023.0.3  |
|  perl-Package-Stash-XS-0.29-9.amzn2023.0.3  |
|  perl-PadWalker-2.5-2.amzn2023.0.3  |
|  perl-Params-Classify-0.015-12.amzn2023.0.3  |
|  perl-Params-Util-1.102-3.amzn2023.0.3  |
|  perl-Params-Validate-1.30-2.amzn2023.0.3  |
|  perl-PathTools-3.78-459.amzn2023.0.3  |
|  perl-Perl-Destruct-Level-0.02-29.amzn2023.0.3  |
|  perl-PerlIO-utf8\_strict-0.008-2.amzn2023.0.3  |
|  perl-Proc-ProcessTable-0.636-5.amzn2023.0.2  |
|  perl-Readonly-XS-1.05-39.amzn2023.0.3  |
|  perl-Ref-Util-XS-0.117-11.amzn2023.0.3  |
|  perl-Scalar-List-Utils-1.56-459.amzn2023.0.3  |
|  perl-Scope-Upper-0.32-6.amzn2023.0.3  |
|  perl-Sereal-Decoder-4.018-2.amzn2023.0.3  |
|  perl-Sereal-Encoder-4.018-2.amzn2023.0.3  |
|  perl-Set-Object-1.40-4.amzn2023.0.3  |
|  perl-Socket-2.032-1.amzn2023.0.3  |
|  perl-Socket6-0.29-9.amzn2023.0.3  |
|  perl-Sort-Key-1.33-20.amzn2023.0.3  |
|  perl-Storable-3.37-522.amzn2023.0.2  |
|  perl-String-CRC32-2.100-1.amzn2023.0.1  |
|  perl-String-Similarity-1.04-31.amzn2023.0.3  |
|  perl-Sub-Identify-0.14-15.amzn2023.0.3  |
|  perl-Sub-Name-0.26-5.amzn2023.0.3  |
|  perl-Sys-Syslog-0.36-459.amzn2023.0.3  |
|  perl-Taint-Runtime-0.03-41.amzn2023.0.3  |
|  perl-Template-Toolkit-3.009-3.amzn2023.0.3  |
|  perl-TermReadKey-2.38-9.amzn2023.0.3  |
|  perl-Test-LeakTrace-0.17-2.amzn2023.0.3  |
|  perl-Test-Taint-1.08-6.amzn2023.0.3  |
|  perl-Text-BibTeX-0.88-7.amzn2023.0.4  |
|  perl-Text-CSV\_XS-1.62-1.amzn2023.0.2  |
|  perl-Text-CharWidth-0.04-42.amzn2023.0.3  |
|  perl-Text-Iconv-1.7-41.amzn2023.0.3  |
|  perl-Text-Soundex-3.05-18.amzn2023.0.3  |
|  perl-Time-HiRes-1.9764-460.amzn2023.0.3  |
|  perl-Tk-804.036-3.amzn2023.0.3  |
|  perl-Unicode-CheckUTF8-1.03-31.amzn2023.0.3  |
|  perl-Unicode-Collate-1.29-2.amzn2023.0.3  |
|  perl-Unicode-LineBreak-2019.001-9.amzn2023.0.3  |
|  perl-Unicode-Map-0.112-53.amzn2023.0.3  |
|  perl-Unicode-Map8-0.13-37.amzn2023.0.3  |
|  perl-Unicode-Normalize-1.27-459.amzn2023.0.3  |
|  perl-Unicode-String-2.10-16.amzn2023.0.3  |
|  perl-Unicode-UTF8-0.62-14.amzn2023.0.3  |
|  perl-Variable-Magic-0.62-12.amzn2023.0.3  |
|  perl-Want-0.29-17.amzn2023.0.3  |
|  perl-XML-LibXML-2.0210-7.amzn2023.0.2  |
|  perl-XML-LibXSLT-1.99-5.amzn2023.0.3  |
|  perl-XML-Parser-2.51-1.amzn2023.0.2  |
|  perl-XString-0.005-2.amzn2023.0.3  |
|  perl-YAML-LibYAML-0.82-4.amzn2023.0.4  |
|  perl-YAML-Syck-1.37-1.amzn2023.0.2  |
|  perl-autobox-3.0.1-12.amzn2023.0.3  |
|  perl-autovivification-0.18-12.amzn2023.0.3  |
|  perl-bareword-filehandles-0.007-7.amzn2023.0.3  |
|  perl-gettext-1.07-19.amzn2023.0.3  |
|  perl-indirect-0.39-8.amzn2023.0.3  |
|  perl-libintl-perl-1.32-2.amzn2023.0.3  |
|  perl-multidimensional-0.014-10.amzn2023.0.3  |
|  perl-threads-2.25-458.amzn2023.0.4  |
|  perl-threads-shared-1.61-458.amzn2023.0.3  |
|  perl-version-0.99.29-1.amzn2023.0.3  |
|  php8.2-8.2.31-1.amzn2023.0.1  |
|  php8.3-8.3.31-1.amzn2023.0.1  |
|  php8.4-8.4.21-1.amzn2023.0.1  |
|  php8.5-8.5.6-1.amzn2023.0.1  |
|  python-pillow-9.4.0-2.amzn2023.0.8  |
|  python-twisted-22.4.0-129.amzn2023.0.6  |
|  python3.13-pip-24.2-259.amzn2023.0.6  |
|  python3.14-pip-25.1.1-1.amzn2023.0.3  |
|  rclone-1.73.5-76.amzn2023  |
|  runc-1.3.4-5.amzn2023.0.2  |
|  runfinch-finch-1.17.0-1.amzn2023.0.2  |
|  selinux-policy-38.1.76-1.amzn2023.0.2  |
|  soci-snapshotter-0.13.0-1.amzn2023.0.3  |
|  system-release-2023.11.20260526-0.amzn2023  |
|  unbound-1.17.1-1.amzn2023.0.12  |
|  valkey-9.0.4-1.amzn2023.0.1  |
|  yq-4.47.1-13.amzn2023  |

### Kernel-livepatch New Packages
<a name="amis-2023.11.20260526.Kernel-livepatch-New-Packages"></a>

This section provides details about Kernel-livepatch New Packages.

|  |
| --- |
|  kernel-livepatch-6.1.170-210.320-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.170-213.321-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.83-113.160-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.83-115.161-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.25-55.108-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.25-57.109-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.11.20260526.Kernel-livepatch-Updated-Packages"></a>

This section provides details about Kernel-livepatch Updated Packages.

|  |
| --- |
|  kernel-livepatch-6.1.163-186.299-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.164-196.303-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.166-197.305-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.168-202.320-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.168-203.330-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.170-208.319-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.73-95.123-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.74-98.124-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.77-99.140-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.79-101.147-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.80-105.147-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.80-106.156-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.83-111.159-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.15-14.217-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.16-18.222-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.20-20.229-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.20-41.237-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.25-52.107-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.8-9.213-1.0-4.amzn2023  |

### Nvidia Updated Packages
<a name="amis-2023.11.20260526.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

|  |
| --- |
|  cuda-12-9-12.9.2-1  |
|  cuda-command-line-tools-12-9-12.9.2-1  |
|  cuda-compat-13-0-580.159.04-1.amzn2023  |
|  cuda-compiler-12-9-12.9.2-1  |
|  cuda-libraries-12-9-12.9.2-1  |
|  cuda-libraries-devel-12-9-12.9.2-1  |
|  cuda-minimal-build-12-9-12.9.2-1  |
|  cuda-nsight-compute-12-9-12.9.2-1  |
|  cuda-nsight-systems-12-9-12.9.2-1  |
|  cuda-runtime-12-9-12.9.2-1  |
|  cuda-toolkit-12-12.9.2-1  |
|  cuda-toolkit-12-9-12.9.2-1  |
|  cuda-tools-12-9-12.9.2-1  |
|  cuda-visual-tools-12-9-12.9.2-1  |
|  libcublas-12-9-12.9.2.10-1  |
|  libcublas-devel-12-9-12.9.2.10-1  |
|  nvidia-gds-12-9-12.9.2-1  |
|  nvlink5-580-580.159.04-1  |

## Image Updates
<a name="ami-updates-2023.11.20260526"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.11.20260526.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260526-0.amzn2023  |
|  bind-libs-32:9.18.49-1.amzn2023.0.1  |
|  bind-license-32:9.18.49-1.amzn2023.0.1  |
|  bind-utils-32:9.18.49-1.amzn2023.0.1  |
|  dnf-plugin-support-info-1.13-1.amzn2023  |
|  gnutls-3.8.3-8.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260526-0.amzn2023  |
|  kernel6.18-tools-1:6.18.30-61.116.amzn2023  |
|  kernel6.18-1:6.18.30-61.116.amzn2023  |
|  libcap-2.73-1.amzn2023.0.7  |
|  libsolv-0.7.22-1.amzn2023.0.3  |
|  openssh-clients-8.7p1-8.amzn2023.0.18  |
|  openssh-server-8.7p1-8.amzn2023.0.18  |
|  openssh-8.7p1-8.amzn2023.0.18  |
|  perl-Data-Dumper-2.191-522.amzn2023.0.3  |
|  perl-Digest-MD5-2.59-521.amzn2023.0.2  |
|  perl-Encode-4:3.21-520.amzn2023.0.2  |
|  perl-MIME-Base64-3.16-2.amzn2023.0.3  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.3  |
|  perl-PathTools-3.78-459.amzn2023.0.3  |
|  perl-Scalar-List-Utils-4:1.56-459.amzn2023.0.3  |
|  perl-Socket-4:2.032-1.amzn2023.0.3  |
|  perl-Storable-1:3.37-522.amzn2023.0.2  |
|  perl-Time-HiRes-4:1.9764-460.amzn2023.0.3  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.2  |
|  selinux-policy-38.1.76-1.amzn2023.0.2  |
|  system-release-2023.11.20260526-0.amzn2023  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.11.20260526.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260526-0.amzn2023  |
|  dnf-plugin-support-info-1.13-1.amzn2023  |
|  gnutls-3.8.3-8.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260526-0.amzn2023  |
|  kernel6.18-1:6.18.30-61.116.amzn2023  |
|  libcap-2.73-1.amzn2023.0.7  |
|  libsolv-0.7.22-1.amzn2023.0.3  |
|  openssh-clients-8.7p1-8.amzn2023.0.18  |
|  openssh-server-8.7p1-8.amzn2023.0.18  |
|  openssh-8.7p1-8.amzn2023.0.18  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.2  |
|  selinux-policy-38.1.76-1.amzn2023.0.2  |
|  system-release-2023.11.20260526-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.11.20260526.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260526-0.amzn2023  |
|  bind-libs-32:9.18.49-1.amzn2023.0.1  |
|  bind-license-32:9.18.49-1.amzn2023.0.1  |
|  bind-utils-32:9.18.49-1.amzn2023.0.1  |
|  dnf-plugin-support-info-1.13-1.amzn2023  |
|  gnutls-3.8.3-8.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260526-0.amzn2023  |
|  kernel6.12-tools-1:6.12.88-119.157.amzn2023  |
|  kernel6.12-1:6.12.88-119.157.amzn2023  |
|  libcap-2.73-1.amzn2023.0.7  |
|  libsolv-0.7.22-1.amzn2023.0.3  |
|  openssh-clients-8.7p1-8.amzn2023.0.18  |
|  openssh-server-8.7p1-8.amzn2023.0.18  |
|  openssh-8.7p1-8.amzn2023.0.18  |
|  perl-Data-Dumper-2.191-522.amzn2023.0.3  |
|  perl-Digest-MD5-2.59-521.amzn2023.0.2  |
|  perl-Encode-4:3.21-520.amzn2023.0.2  |
|  perl-MIME-Base64-3.16-2.amzn2023.0.3  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.3  |
|  perl-PathTools-3.78-459.amzn2023.0.3  |
|  perl-Scalar-List-Utils-4:1.56-459.amzn2023.0.3  |
|  perl-Socket-4:2.032-1.amzn2023.0.3  |
|  perl-Storable-1:3.37-522.amzn2023.0.2  |
|  perl-Time-HiRes-4:1.9764-460.amzn2023.0.3  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.2  |
|  selinux-policy-38.1.76-1.amzn2023.0.2  |
|  system-release-2023.11.20260526-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.11.20260526.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260526-0.amzn2023  |
|  dnf-plugin-support-info-1.13-1.amzn2023  |
|  gnutls-3.8.3-8.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260526-0.amzn2023  |
|  kernel6.12-1:6.12.88-119.157.amzn2023  |
|  libcap-2.73-1.amzn2023.0.7  |
|  libsolv-0.7.22-1.amzn2023.0.3  |
|  openssh-clients-8.7p1-8.amzn2023.0.18  |
|  openssh-server-8.7p1-8.amzn2023.0.18  |
|  openssh-8.7p1-8.amzn2023.0.18  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.2  |
|  selinux-policy-38.1.76-1.amzn2023.0.2  |
|  system-release-2023.11.20260526-0.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.11.20260526.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260526-0.amzn2023  |
|  bind-libs-32:9.18.49-1.amzn2023.0.1  |
|  bind-license-32:9.18.49-1.amzn2023.0.1  |
|  bind-utils-32:9.18.49-1.amzn2023.0.1  |
|  dnf-plugin-support-info-1.13-1.amzn2023  |
|  gnutls-3.8.3-8.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260526-0.amzn2023  |
|  kernel-tools-1:6.1.172-216.329.amzn2023  |
|  kernel-1:6.1.172-216.329.amzn2023  |
|  libcap-2.73-1.amzn2023.0.7  |
|  libsolv-0.7.22-1.amzn2023.0.3  |
|  openssh-clients-8.7p1-8.amzn2023.0.18  |
|  openssh-server-8.7p1-8.amzn2023.0.18  |
|  openssh-8.7p1-8.amzn2023.0.18  |
|  perl-Data-Dumper-2.191-522.amzn2023.0.3  |
|  perl-Digest-MD5-2.59-521.amzn2023.0.2  |
|  perl-Encode-4:3.21-520.amzn2023.0.2  |
|  perl-MIME-Base64-3.16-2.amzn2023.0.3  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.3  |
|  perl-PathTools-3.78-459.amzn2023.0.3  |
|  perl-Scalar-List-Utils-4:1.56-459.amzn2023.0.3  |
|  perl-Socket-4:2.032-1.amzn2023.0.3  |
|  perl-Storable-1:3.37-522.amzn2023.0.2  |
|  perl-Time-HiRes-4:1.9764-460.amzn2023.0.3  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.2  |
|  selinux-policy-38.1.76-1.amzn2023.0.2  |
|  system-release-2023.11.20260526-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.11.20260526.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260526-0.amzn2023  |
|  dnf-plugin-support-info-1.13-1.amzn2023  |
|  gnutls-3.8.3-8.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260526-0.amzn2023  |
|  kernel-1:6.1.172-216.329.amzn2023  |
|  libcap-2.73-1.amzn2023.0.7  |
|  libsolv-0.7.22-1.amzn2023.0.3  |
|  openssh-clients-8.7p1-8.amzn2023.0.18  |
|  openssh-server-8.7p1-8.amzn2023.0.18  |
|  openssh-8.7p1-8.amzn2023.0.18  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.2  |
|  selinux-policy-38.1.76-1.amzn2023.0.2  |
|  system-release-2023.11.20260526-0.amzn2023  |

### Default Container
<a name="amis-2023.11.20260526.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260526-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.7  |
|  libsolv-0.7.22-1.amzn2023.0.3  |
|  system-release-2023.11.20260526-0.amzn2023  |

### Minimal Container
<a name="amis-2023.11.20260526.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260526-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.7  |
|  libsolv-0.7.22-1.amzn2023.0.3  |
|  system-release-2023.11.20260526-0.amzn2023  |

## Contact us
<a name="amis-2023.11.20260526.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
