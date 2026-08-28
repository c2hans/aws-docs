---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.10.20260330.html
---

# Amazon Linux 2023 version 2023.10.20260330 release notes
<a name="relnotes-2023.10.20260330"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.10.20260330.

**Contents**
+ [Release Summary](#release-summary-2023.10.20260330)
+ [Repository Updates](#repository-updates-2023.10.20260330)
  + [Core New Packages](#amis-2023.10.20260330.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.10.20260330.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.10.20260330.Kernel-livepatch-New-Packages)
  + [Nvidia New Packages](#amis-2023.10.20260330.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.10.20260330.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.10.20260330)
  + [Default Kernel 6.18 AMI](#amis-2023.10.20260330.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.10.20260330.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.10.20260330.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.10.20260330.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.10.20260330.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.10.20260330.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.10.20260330.Default-Container)
  + [Minimal Container](#amis-2023.10.20260330.Minimal-Container)
+ [Contact us](#amis-2023.10.20260330.contact-us)

## Release Summary
<a name="release-summary-2023.10.20260330"></a>

This release represents an update to the 10th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ OpenSSL has been rebased to v3.5 :
  + Adds support for post-quantum algorithms (ML-KEM, ML-DSA, and SLH-DSA)
  + Adds support for the QUIC transport protocol
  + New support for the sslkeylogfile format via the SSLKEYLOGFILE environment variable. NOTE\! this feature allows logging of secrets produced by TLS connections for testing and debugging purposes, and should not be used in production environments. For more information see: [https://datatracker.ietf.org/doc/html/draft-thomson-tls-keylogfile-01](https://datatracker.ietf.org/doc/html/draft-thomson-tls-keylogfile-01)
  + For a detailed list of changes and enhancements, please see the upstream [OpenSSL Changelog](https://github.com/openssl/openssl/blob/openssl-3.5.5/CHANGES.md).
+ `curl (8.17.0-1.amzn2023.0.2)` now supports HTTP/3 via the `ngtcp2` and `nghttp3` libraries. HTTP/3 uses `QUIC` as its transport protocol, offering improved connection establishment times and better performance on lossy networks. HTTP/3 support is enabled in the full curl build only, not in curl-minimal. To use HTTP/3, pass `--http3 or --http3-only` to curl; existing behavior is unchanged for users who do not opt in. This also extends to wcurl, which can be used with wcurl `--curl-options=--http3` $URL.
+ PostgreSQL 18 has been Added : Please see the [PostgreSQL release notes](https://www.postgresql.org/docs/18/release-18.html) for a list of changes and improvements in this version.
+ Dotnet10.0 Added : `dotnet-10.0.105` is the new major release of the .NET platform, and it contains many new features and optimizations.
+ The `scap-security-guide` package is now updated to the latest upstream version with initial SCAP content for AL2023 STIG.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.10.20260330"></a>

### Core New Packages
<a name="amis-2023.10.20260330.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  dotnet10.0-10.0.105-1.amzn2023.0.1  |
|  freeipmi-1.6.15-159.amzn2023  |
|  gnome-app-list-3.0-1.amzn2023  |
|  gnome-software-47.5-1.amzn2023  |
|  nghttp3-1.15.0-1.amzn2023.0.1  |
|  ngtcp2-1.21.0-1.amzn2023.0.1  |
|  postgresql18-18.3-1.amzn2023.0.1  |
|  rclone-1.73.0-73.amzn2023  |
|  watchdog-5.16-11.amzn2023  |

### Core Updated Packages
<a name="amis-2023.10.20260330.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.13.41-1.amzn2023.0.2  |
|  amazon-efs-utils-2.4.2-1.amzn2023  |
|  amazon-ssm-agent-3.3.4108.0-1.amzn2023  |
|  appstream-data-2023-103.amzn2023  |
|  bind-9.18.33-1.amzn2023.0.5  |
|  credentials-fetcher-2.0.1-1.amzn2023.0.1  |
|  curl-8.17.0-1.amzn2023.0.2  |
|  dotnet8.0-8.0.125-1.amzn2023.0.2  |
|  dotnet9.0-9.0.115-1.amzn2023.0.1  |
|  ecs-init-1.102.1-1.amzn2023  |
|  ecs-service-connect-agent-v1.34.13.0-1.amzn2023  |
|  exiv2-0.28.5-132.amzn2023  |
|  firefox-140.8.0-1.amzn2023.0.2  |
|  freerdp-3.6.3-1.amzn2023.0.8  |
|  freetype-2.13.2-5.amzn2023.0.2  |
|  giflib-5.2.1-9.amzn2023.0.3  |
|  gnutls-3.8.3-8.amzn2023.0.2  |
|  golang-1.25.8-1.amzn2023.0.2  |
|  golist-0.10.4-12.amzn2023.0.7  |
|  gstreamer1-plugins-bad-free-1.24.10-1.amzn2023.0.5  |
|  gstreamer1-plugins-base-1.24.10-1.amzn2023.0.3  |
|  gstreamer1-plugins-good-1.24.10-1.amzn2023.0.4  |
|  gvfs-1.56.1-1.amzn2023.0.2  |
|  kernel-6.1.166-197.305.amzn2023  |
|  kernel6.12-6.12.77-99.140.amzn2023  |
|  kernel6.18-6.18.16-18.222.amzn2023  |
|  kiwi-10.2.38-1.amzn2023  |
|  lcms2-2.16-74.amzn2023  |
|  libde265-1.0.16-1.amzn2023.0.2  |
|  libheif-1.19.8-1.amzn2023.0.4  |
|  libsodium-1.0.19-5.amzn2023  |
|  libssh-0.10.6-1.amzn2023.0.5  |
|  libtiff-4.4.0-4.amzn2023.0.25  |
|  mount-s3-1.22.2-1.amzn2023  |
|  ncurses-6.6-1.amzn2023.0.1  |
|  nodejs20-20.20.1-1.amzn2023.0.3  |
|  nodejs22-22.22.1-1.amzn2023.0.2  |
|  nodejs24-24.14.0-1.amzn2023.0.2  |
|  nvidia-release-2023-5.amzn2023  |
|  ocaml-4.13.1-4.amzn2023.0.3  |
|  openexr-3.1.5-1.amzn2023.0.7  |
|  openssl-3.5.5-1.amzn2023.0.3  |
|  perl-Archive-Tar-3.04-522.amzn2023.0.1  |
|  perl-B-COW-0.007-12.amzn2023.0.1  |
|  perl-CGI-4.71-1.amzn2023.0.1  |
|  perl-CPAN-Meta-2.150013-1.amzn2023.0.1  |
|  perl-CPAN-Meta-Check-0.018-7.amzn2023.0.1  |
|  perl-CPAN-Meta-Requirements-2.145-1.amzn2023.0.1  |
|  perl-CPAN-Meta-YAML-0.020-522.amzn2023.0.1  |
|  perl-Capture-Tiny-0.50-4.amzn2023.0.1  |
|  perl-Class-Data-Inheritable-0.10-4.amzn2023.0.1  |
|  perl-Clone-0.47-4.amzn2023.0.1  |
|  perl-Compress-Raw-Bzip2-2.217-1.amzn2023.0.1  |
|  perl-Compress-Raw-Lzma-2.221-1.amzn2023.0.1  |
|  perl-Compress-Raw-Zlib-2.221-1.amzn2023.0.1  |
|  perl-Config-General-2.64-1.amzn2023.0.1  |
|  perl-Config-Perl-V-0.39-1.amzn2023.0.1  |
|  perl-Convert-ASN1-0.34-7.amzn2023.0.1  |
|  perl-Crypt-CBC-3.07-2.amzn2023.0.1  |
|  perl-Crypt-OpenSSL-Random-0.17-6.amzn2023.0.1  |
|  perl-CryptX-0.087-5.amzn2023.0.1  |
|  perl-Data-Dump-1.25-14.amzn2023.0.1  |
|  perl-Data-Dumper-2.191-522.amzn2023.0.1  |
|  perl-Data-UUID-1.227-7.amzn2023.0.1  |
|  perl-Devel-Caller-2.07-11.amzn2023.0.1  |
|  perl-Devel-FindPerl-0.016-11.amzn2023.0.1  |
|  perl-Devel-Hide-0.0016-2.amzn2023.0.1  |
|  perl-Devel-PPPort-3.73-522.amzn2023.0.1  |
|  perl-Devel-Size-0.86-1.amzn2023.0.1  |
|  perl-Devel-StackTrace-2.05-7.amzn2023.0.1  |
|  perl-Digest-CRC-0.24-13.amzn2023.0.1  |
|  perl-Digest-HMAC-1.05-4.amzn2023.0.1  |
|  perl-Digest-MD5-2.59-521.amzn2023.0.1  |
|  perl-Digest-Perl-MD5-1.91-1.amzn2023.0.1  |
|  perl-Digest-SHA-6.04-522.amzn2023.0.1  |
|  perl-Digest-SHA3-1.05-12.amzn2023.0.1  |
|  perl-DynaLoader-Functions-0.004-8.amzn2023.0.1  |
|  perl-Email-Date-Format-1.008-8.amzn2023.0.1  |
|  perl-Encode-3.21-520.amzn2023.0.1  |
|  perl-Encode-JIS2K-0.05-9.amzn2023.0.1  |
|  perl-Error-0.17030-2.amzn2023.0.1  |
|  perl-Exporter-5.79-520.amzn2023.0.1  |
|  perl-Exporter-Tiny-1.006003-2.amzn2023.0.1  |
|  perl-ExtUtils-Config-0.010-4.amzn2023.0.1  |
|  perl-ExtUtils-Depends-0.8002-3.amzn2023.0.1  |
|  perl-ExtUtils-HasCompiler-0.025-5.amzn2023.0.1  |
|  perl-ExtUtils-Helpers-0.028-4.amzn2023.0.1  |
|  perl-File-Find-Rule-0.35-3.amzn2023.0.1  |
|  perl-File-ReadBackwards-1.06-14.amzn2023.0.1  |
|  perl-File-Remove-1.61-11.amzn2023.0.1  |
|  perl-File-ShareDir-Install-0.14-10.amzn2023.0.1  |
|  perl-File-Temp-0.231.200-2.amzn2023.0.1  |
|  perl-File-Which-1.27-15.amzn2023.0.1  |
|  perl-FileHandle-Fmode-0.15-6.amzn2023.0.1  |
|  perl-Filter-1.65-2.amzn2023.0.1  |
|  perl-Getopt-Long-2.58-521.amzn2023.0.1  |
|  perl-HTML-Tagset-3.24-5.amzn2023.0.1  |
|  perl-IO-Pipely-0.006-11.amzn2023.0.1  |
|  perl-IO-Tty-1.20-9.amzn2023.0.1  |
|  perl-IPC-Run3-0.049-5.amzn2023.0.1  |
|  perl-Image-Xbm-1.11-4.amzn2023.0.1  |
|  perl-JSON-4.10-9.amzn2023.0.1  |
|  perl-JSON-XS-4.04-2.amzn2023.0.1  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.2  |
|  perl-Test-Deep-1.205-3.amzn2023.0.1  |
|  perl-Test-File-1.99.5-3.amzn2023.0.1  |
|  perl-Test-Fixme-0.17-3.amzn2023.0.1  |
|  perl-Test-Inter-1.12-4.amzn2023.0.1  |
|  perl-Test-Manifest-2.026-3.amzn2023.0.1  |
|  perl-Test-MemoryGrowth-0.05-4.amzn2023.0.1  |
|  perl-Test-NoWarnings-1.06-12.amzn2023.0.1  |
|  perl-Test-Simple-1.302219-2.amzn2023.0.1  |
|  perl-YAML-Syck-1.37-1.amzn2023.0.1  |
|  perl-autodie-2.37-522.amzn2023.0.1  |
|  perl-bignum-0.67-522.amzn2023.0.1  |
|  perl-experimental-0.036-3.amzn2023.0.1  |
|  python-flask-1.1.4-5.amzn2023.0.1  |
|  python-jwt-2.4.0-1.amzn2023.0.3  |
|  python-tornado-6.1.0-2.amzn2023.0.7  |
|  python3.11-3.11.14-1.amzn2023.0.5  |
|  python3.11-pip-22.3.1-2.amzn2023.0.11  |
|  python3.12-pip-23.2.1-4.amzn2023.0.8  |
|  python3.13-pip-24.2-259.amzn2023.0.4  |
|  python3.13-tornado-6.4.2-1.amzn2023.0.2  |
|  runfinch-finch-1.15.1-1.amzn2023.0.1  |
|  rust-below-0.11.0-1.amzn2023.0.2  |
|  rust-cargo-c-0.10.19-1.amzn2023.0.1  |
|  scap-security-guide-0.1.80-1.amzn2023.0.1  |
|  selinux-policy-38.1.73-1.amzn2023.0.2  |
|  sscg-3.0.3-77.amzn2023  |
|  swig-4.1.1-4.amzn2023.0.5  |
|  system-release-2023.10.20260330-0.amzn2023  |
|  systemtap-5.4-1.amzn2023.0.2  |
|  texlive-base-20210325-52.amzn2023.0.3  |
|  tomcat10-10.1.52-1.amzn2023.0.1  |
|  tomcat9-9.0.115-1.amzn2023.0.1  |
|  tzdata-2026a-1.amzn2023.0.1  |

### Kernel-livepatch New Packages
<a name="amis-2023.10.20260330.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.12.58-82.121-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.63-84.121-1.0-3.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.10.20260330.Nvidia-New-Packages"></a>

This section provides details about nvidia new packages.

|  |
| --- |
|  cublas-13.2.2-1  |
|  cublas-cuda-12-12.9.2.7-1  |
|  cublas-cuda-13-13.2.2.2-1  |
|  cublas13-13.2.2-1  |
|  cuda-13-2-13.2.0-1  |
|  cuda-cccl-13-2-13.2.27-1  |
|  cuda-command-line-tools-13-2-13.2.0-1  |
|  cuda-compiler-13-2-13.2.0-1  |
|  cuda-crt-13-2-13.2.51-1  |
|  cuda-ctadvisor-13-2-13.2.51-1  |
|  cuda-cudart-13-2-13.2.51-1  |
|  cuda-cudart-devel-13-2-13.2.51-1  |
|  cuda-culibos-devel-13-2-13.2.51-1  |
|  cuda-cuobjdump-13-2-13.2.51-1  |
|  cuda-cupti-13-2-13.2.23-1  |
|  cuda-cuxxfilt-13-2-13.2.51-1  |
|  cuda-documentation-13-2-13.2.51-1  |
|  cuda-driver-devel-13-2-13.2.51-1  |
|  cuda-gdb-13-2-13.2.20-1  |
|  cuda-gdb-src-13-2-13.2.20-1  |
|  cuda-libraries-13-2-13.2.0-1  |
|  cuda-libraries-devel-13-2-13.2.0-1  |
|  cuda-minimal-build-13-2-13.2.0-1  |
|  cuda-nsight-13-2-13.2.20-1  |
|  cuda-nsight-compute-13-2-13.2.0-1  |
|  cuda-nsight-systems-13-2-13.2.0-1  |
|  cuda-nvcc-13-2-13.2.51-1  |
|  cuda-nvdisasm-13-2-13.2.51-1  |
|  cuda-nvml-devel-13-2-13.2.51-1  |
|  cuda-nvprune-13-2-13.2.51-1  |
|  cuda-nvrtc-13-2-13.2.51-1  |
|  cuda-nvrtc-devel-13-2-13.2.51-1  |
|  cuda-nvtx-13-2-13.2.20-1  |
|  cuda-opencl-13-2-13.2.51-1  |
|  cuda-opencl-devel-13-2-13.2.51-1  |
|  cuda-profiler-api-13-2-13.2.20-1  |
|  cuda-runtime-13-2-13.2.0-1  |
|  cuda-sandbox-devel-13-2-13.2.51-1  |
|  cuda-sanitizer-13-2-13.2.23-1  |
|  cuda-tileiras-13-2-13.2.51-1  |
|  cuda-toolkit-13-2-13.2.0-1  |
|  cuda-toolkit-13-2-config-common-13.2.51-1  |
|  cuda-tools-13-2-13.2.0-1  |
|  cuda-visual-tools-13-2-13.2.0-1  |
|  gds-tools-13-2-1.17.0.44-1  |
|  libcublas-13-2-13.3.0.5-1  |
|  libcublas-devel-13-2-13.3.0.5-1  |
|  libcublas12-cuda-12-12.9.2.7-1  |
|  libcublas12-devel-cuda-12-12.9.2.7-1  |
|  libcublas13-cuda-13-13.2.2.2-1  |
|  libcublas13-devel-cuda-13-13.2.2.2-1  |
|  libcufft-13-2-12.2.0.37-1  |
|  libcufft-devel-13-2-12.2.0.37-1  |
|  libcufile-13-2-1.17.0.44-1  |
|  libcufile-devel-13-2-1.17.0.44-1  |
|  libcuobjclient-13-2-1.1.0.44-1  |
|  libcuobjclient-devel-13-2-1.1.0.44-1  |
|  libcurand-13-2-10.4.2.51-1  |
|  libcurand-devel-13-2-10.4.2.51-1  |
|  libcusolver-13-2-12.1.0.51-1  |
|  libcusolver-devel-13-2-12.1.0.51-1  |
|  libcusparse-13-2-12.7.9.17-1  |
|  libcusparse-devel-13-2-12.7.9.17-1  |
|  libnpp-13-2-13.1.0.44-1  |
|  libnpp-devel-13-2-13.1.0.44-1  |
|  libnvfatbin-13-2-13.2.51-1  |
|  libnvfatbin-devel-13-2-13.2.51-1  |
|  libnvjitlink-13-2-13.2.51-1  |
|  libnvjitlink-devel-13-2-13.2.51-1  |
|  libnvjpeg-13-2-13.0.4.44-1  |
|  libnvjpeg-devel-13-2-13.0.4.44-1  |
|  libnvptxcompiler-13-2-13.2.51-1  |
|  libnvvm-13-2-13.2.51-1  |
|  nsight-compute-2026.1.0-2026.1.0.9-1  |
|  nsight-systems-2025.6.3-2025.6.3.343\_256337165561v0-0  |
|  nvidia-gds-13-2-13.2.0-1  |

### Nvidia Updated Packages
<a name="amis-2023.10.20260330.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  corelib-1.0.0.1772474517-1  |
|  cuda-13.2.0-1  |
|  cuda-compat-13-0-580.126.20-1.amzn2023  |
|  cuda-drivers-580.126.20-1.amzn2023  |
|  cuda-toolkit-13.2.0-1  |
|  cuda-toolkit-13-13.2.0-1  |
|  cuda-toolkit-13-config-common-13.2.51-1  |
|  cuda-toolkit-config-common-13.2.51-1  |
|  cutensor-2.6.0-1  |
|  cutensor-cuda-12-2.6.0.4-1  |
|  cutensor-cuda-13-2.6.0.4-1  |
|  cutensor2-2.6.0-1  |
|  egl-wayland2-1.0.1\~20260109git1893c37-9.amzn2023  |
|  kmod-nvidia-latest-dkms-580.126.20-1.amzn2023  |
|  kmod-nvidia-open-dkms-580.126.20-1.amzn2023  |
|  libcorelib1-1.0.0.1772474517-1  |
|  libcorelib1-devel-1.0.0.1772474517-1  |
|  libcutensor2-cuda-12-2.6.0.4-1  |
|  libcutensor2-cuda-13-2.6.0.4-1  |
|  libcutensor2-devel-cuda-12-2.6.0.4-1  |
|  libcutensor2-devel-cuda-13-2.6.0.4-1  |
|  libnvat-1.2.0.1772475102-1  |
|  libnvat-devel-1.2.0.1772475102-1  |
|  libnvidia-cfg-580.126.20-1.amzn2023  |
|  libnvidia-container-devel-1.19.0-1  |
|  libnvidia-container-static-1.19.0-1  |
|  libnvidia-container-tools-1.19.0-1  |
|  libnvidia-container1-1.19.0-1  |
|  libnvidia-fbc-580.126.20-1.amzn2023  |
|  libnvidia-gpucomp-580.126.20-1.amzn2023  |
|  libnvidia-ml-580.126.20-1.amzn2023  |
|  libnvidia-nscq-580.126.20-1  |
|  libnvsdm-580.126.20-1  |
|  libnvsdm-devel-580.126.20-1  |
|  nvattest-1.2.0.1772475102-1  |
|  nvidia-container-toolkit-1.19.0-1  |
|  nvidia-container-toolkit-base-1.19.0-1  |
|  nvidia-driver-580.126.20-1.amzn2023  |
|  nvidia-driver-assistant-0.46.126.20-1  |
|  nvidia-driver-cuda-580.126.20-1.amzn2023  |
|  nvidia-driver-cuda-libs-580.126.20-1.amzn2023  |
|  nvidia-driver-libs-580.126.20-1.amzn2023  |
|  nvidia-fabric-manager-devel-580.126.20-1  |
|  nvidia-fabricmanager-580.126.20-1  |
|  nvidia-fs-2.28.2-1  |
|  nvidia-fs-dkms-2.28.2-1  |
|  nvidia-gds-13.2.0-1  |
|  nvidia-imex-580.126.20-1  |
|  nvidia-kmod-common-580.126.20-1.amzn2023  |
|  nvidia-libXNVCtrl-580.126.20-1.amzn2023  |
|  nvidia-libXNVCtrl-devel-580.126.20-1.amzn2023  |
|  nvidia-modprobe-580.126.20-1.amzn2023  |
|  nvidia-open-580.126.20-1.amzn2023  |
|  nvidia-persistenced-580.126.20-1.amzn2023  |
|  nvidia-settings-580.126.20-1.amzn2023  |
|  nvidia-xconfig-580.126.20-1.amzn2023  |
|  nvlink5-580.126.20-1  |
|  nvlink5-580-580.126.20-1  |
|  xorg-x11-nvidia-580.126.20-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.10.20260330"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.10.20260330.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260330-0.amzn2023  |
|  amazon-ssm-agent-3.3.4108.0-1.amzn2023  |
|  bind-libs-32:9.18.33-1.amzn2023.0.5  |
|  bind-license-32:9.18.33-1.amzn2023.0.5  |
|  bind-utils-32:9.18.33-1.amzn2023.0.5  |
|  curl-minimal-8.17.0-1.amzn2023.0.2  |
|  gnutls-3.8.3-8.amzn2023.0.2  |
|  kernel-livepatch-repo-s3-2023.10.20260330-0.amzn2023  |
|  kernel6.18-libbpf-1:6.18.16-18.222.amzn2023  |
|  kernel6.18-tools-1:6.18.16-18.222.amzn2023  |
|  kernel6.18-1:6.18.16-18.222.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.3  |
|  openssl-1:3.5.5-1.amzn2023.0.3  |
|  perl-Exporter-5.79-520.amzn2023.0.1  |
|  perl-File-Temp-1:0.231.200-2.amzn2023.0.1  |
|  perl-Getopt-Long-1:2.58-521.amzn2023.0.1  |
|  perl-base-2.27-477.amzn2023.0.7  |
|  system-release-2023.10.20260330-0.amzn2023  |
|  tzdata-2026a-1.amzn2023.0.1  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.10.20260330.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260330-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.2  |
|  gnutls-3.8.3-8.amzn2023.0.2  |
|  kernel-livepatch-repo-s3-2023.10.20260330-0.amzn2023  |
|  kernel6.18-libbpf-1:6.18.16-18.222.amzn2023  |
|  kernel6.18-1:6.18.16-18.222.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.3  |
|  openssl-1:3.5.5-1.amzn2023.0.3  |
|  system-release-2023.10.20260330-0.amzn2023  |
|  tzdata-2026a-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.10.20260330.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260330-0.amzn2023  |
|  amazon-ssm-agent-3.3.4108.0-1.amzn2023  |
|  bind-libs-32:9.18.33-1.amzn2023.0.5  |
|  bind-license-32:9.18.33-1.amzn2023.0.5  |
|  bind-utils-32:9.18.33-1.amzn2023.0.5  |
|  curl-minimal-8.17.0-1.amzn2023.0.2  |
|  gnutls-3.8.3-8.amzn2023.0.2  |
|  kernel-livepatch-repo-s3-2023.10.20260330-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.77-99.140.amzn2023  |
|  kernel6.12-tools-1:6.12.77-99.140.amzn2023  |
|  kernel6.12-1:6.12.77-99.140.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.3  |
|  openssl-1:3.5.5-1.amzn2023.0.3  |
|  perl-Exporter-5.79-520.amzn2023.0.1  |
|  perl-File-Temp-1:0.231.200-2.amzn2023.0.1  |
|  perl-Getopt-Long-1:2.58-521.amzn2023.0.1  |
|  perl-base-2.27-477.amzn2023.0.7  |
|  system-release-2023.10.20260330-0.amzn2023  |
|  tzdata-2026a-1.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.10.20260330.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260330-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.2  |
|  gnutls-3.8.3-8.amzn2023.0.2  |
|  kernel-livepatch-repo-s3-2023.10.20260330-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.77-99.140.amzn2023  |
|  kernel6.12-1:6.12.77-99.140.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.3  |
|  openssl-1:3.5.5-1.amzn2023.0.3  |
|  system-release-2023.10.20260330-0.amzn2023  |
|  tzdata-2026a-1.amzn2023.0.1  |

### Default Kernel 6.1 AMI
<a name="amis-2023.10.20260330.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260330-0.amzn2023  |
|  amazon-ssm-agent-3.3.4108.0-1.amzn2023  |
|  bind-libs-32:9.18.33-1.amzn2023.0.5  |
|  bind-license-32:9.18.33-1.amzn2023.0.5  |
|  bind-utils-32:9.18.33-1.amzn2023.0.5  |
|  curl-minimal-8.17.0-1.amzn2023.0.2  |
|  gnutls-3.8.3-8.amzn2023.0.2  |
|  kernel-libbpf-1:6.1.166-197.305.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260330-0.amzn2023  |
|  kernel-tools-1:6.1.166-197.305.amzn2023  |
|  kernel-1:6.1.166-197.305.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.3  |
|  openssl-1:3.5.5-1.amzn2023.0.3  |
|  perl-Exporter-5.79-520.amzn2023.0.1  |
|  perl-File-Temp-1:0.231.200-2.amzn2023.0.1  |
|  perl-Getopt-Long-1:2.58-521.amzn2023.0.1  |
|  perl-base-2.27-477.amzn2023.0.7  |
|  system-release-2023.10.20260330-0.amzn2023  |
|  tzdata-2026a-1.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.10.20260330.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260330-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.2  |
|  gnutls-3.8.3-8.amzn2023.0.2  |
|  kernel-libbpf-1:6.1.166-197.305.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260330-0.amzn2023  |
|  kernel-1:6.1.166-197.305.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.3  |
|  openssl-1:3.5.5-1.amzn2023.0.3  |
|  system-release-2023.10.20260330-0.amzn2023  |
|  tzdata-2026a-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.10.20260330.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260330-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.2  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.3  |
|  system-release-2023.10.20260330-0.amzn2023  |
|  tzdata-2026a-1.amzn2023.0.1  |

### Minimal Container
<a name="amis-2023.10.20260330.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260330-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.2  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.3  |
|  system-release-2023.10.20260330-0.amzn2023  |
|  tzdata-2026a-1.amzn2023.0.1  |

## Contact us
<a name="amis-2023.10.20260330.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
