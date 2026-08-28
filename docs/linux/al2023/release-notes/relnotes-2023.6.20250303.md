---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20250303.html
---

# Amazon Linux 2023 version 2023.6.20250303 release notes
<a name="relnotes-2023.6.20250303"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20250303.

**Topics**
+ [Major updates](#major-updates-2023.6.20250303)
+ [Repository](#amis-2023.6.20250303.repository)
+ [Default AMI](#amis-2023.6.20250303.default-ami)
+ [Docker container image](#amis-2023.6.20250303.docker-container-image)
+ [Minimal AMI](#amis-2023.6.20250303.minimal-ami)
+ [Minimal container image](#amis-2023.6.20250303.minimal-container-image)
+ [Contact us](#amis-2023.6.20250303.contact-us)

## Major updates
<a name="major-updates-2023.6.20250303"></a>

This release represents an update to the 6th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  clamav to clamav1.4 update: The latest version of clamav has been added to the AL2023 core repository in this release. To aid customers in migrating to the latest version, the latest clamav is provided in the clamav1.4 package. In 6 months from this release, installing clamav will install clamav1.4, and it will become the default (target date for transition is around Sept/Oct 2025). The clamav1.4 package will provide new versions of shared libraries, any applications that link to any of the clamav shared libraries will need to be re-linked or rebuilt. The older clamav (v 0.103.12) packages will still be available in the repo after the clamav1.4 packages are made the default, but will not receive further updates or security fixes. To ensure continued security and support, customers should migrate to clamav1.4 immediately.

**Known issues**
+  AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20250303.repository"></a>

### New packages in AL2023.6.20250303 since AL2023.6.20250218
<a name="new-AL2023.6.20250218-AL2023.6.20250303"></a>

 Comparing AL2023.6.20250218 version 2023.6.20250218 to AL2023.6.20250303 version [2023.6.20250303](#relnotes-2023.6.20250303).

| Package Type | Number of new packages in AL2023.6.20250303 compared to AL2023.6.20250218 |
| --- | --- |
| Source RPMs | 44 |
| Total Binary RPMs | 263 |
|  noarch binary RPMs | 19 |
|  x86\_64 binary RPMs | 122 |
|  aarch64 binary RPMs | 122 |

New packages in AL2023.6.20250303:

- ** `clamav1.4` **
  - **RPM:**  clamav1.4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav1.4-data  / **Architectures:** noarch
  - **RPM:**  clamav1.4-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav1.4-doc  / **Architectures:** noarch
  - **RPM:**  clamav1.4-filesystem  / **Architectures:** noarch
  - **RPM:**  clamav1.4-freshclam  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav1.4-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav1.4-milter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamd1.4  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.4.2-1.amzn2023.0.1

- ** `cups-pk-helper` **
  - **RPM:**  cups-pk-helper
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.2.7-8.amzn2023

- ** `exempi` **
  - **RPM:**  exempi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  exempi-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.6.4-6.amzn2023

- ** `exiv2` **
  - **RPM:**  exiv2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  exiv2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  exiv2-doc  / **Architectures:** noarch
  - **RPM:**  exiv2-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.28.3-1.amzn2023.0.1

- ** `freetds` **
  - **RPM:**  freetds  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freetds-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freetds-doc  / **Architectures:** noarch
  - **RPM:**  freetds-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.20-4.amzn2023

- ** `gcr3` **
  - **RPM:**  gcr3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcr3-base  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcr3-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.41.1-9.amzn2023.0.2

- ** `geoclue2` **
  - **RPM:**  geoclue2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  geoclue2-demos  / **Architectures:** aarch64, x86\_64
  - **RPM:**  geoclue2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  geoclue2-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.7.0-6.amzn2023.0.2

- ** `geocode-glib` **
  - **RPM:**  geocode-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  geocode-glib-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.26.4-1.amzn2023.0.1

- ** `gflags` **
  - **RPM:**  gflags  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gflags-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.2.2-15.amzn2023

- ** `graphene` **
  - **RPM:**  graphene  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphene-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphene-tests  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.10.6-9.amzn2023

- ** `gstreamer1` **
  - **RPM:**  gstreamer1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.24.10-1.amzn2023.0.1

- ** `gstreamer1-plugins-base` **
  - **RPM:**  gstreamer1-plugins-base  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-plugins-base-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-plugins-base-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.24.10-1.amzn2023.0.1

- ** `gstreamer1-plugins-good` **
  - **RPM:**  gstreamer1-plugins-good  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-plugins-good-gtk  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.24.10-1.amzn2023.0.1

- ** `highway` **
  - **RPM:**  highway  / **Architectures:** aarch64, x86\_64
  - **RPM:**  highway-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  highway-doc  / **Architectures:** noarch
  - **Version:** 1.2.0-30.amzn2023.0.1

- ** `inih` **
  - **RPM:**  inih-cpp
  - **Architectures:** aarch64, x86\_64
  - **Version:** 58-2.amzn2023.0.1

- ** `jpegxl` **
  - **RPM:**  jpegxl-doc  / **Architectures:** noarch
  - **RPM:**  jxl-pixbuf-loader  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjxl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjxl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjxl-devtools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjxl-utils  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.10.3-54.amzn2023

- ** `langtable` **
  - **RPM:**  langtable  / **Architectures:** noarch
  - **RPM:**  python3-langtable  / **Architectures:** noarch
  - **Version:** 0.0.68-2.amzn2023

- ** `libblockdev` **
  - **RPM:**  libblockdev-nvme  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-nvme-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-smart  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-smart-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-smartmontools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-smartmontools-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.2.1-1.amzn2023.0.2

- ** `libcanberra` **
  - **RPM:**  libcanberra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcanberra-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcanberra-gtk3  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.30-35.amzn2023

- ** `libgexiv2` **
  - **RPM:**  libgexiv2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgexiv2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-gexiv2  / **Architectures:** noarch
  - **Version:** 0.14.3-2.amzn2023

- ** `libgtop2` **
  - **RPM:**  libgtop2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgtop2-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.41.3-2.amzn2023.0.1

- ** `libgweather` **
  - **RPM:**  libgweather  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgweather-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgweather-doc  / **Architectures:** aarch64, x86\_64
  - **Version:** 4.4.4-1.amzn2023.0.1

- ** `libhandy` **
  - **RPM:**  libhandy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libhandy-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.8.3-3.amzn2023.0.1

- ** `libmpdclient` **
  - **RPM:**  libmpdclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmpdclient-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.22-2.amzn2023

- ** `libnvme` **
  - **RPM:**  libnvme  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnvme-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnvme-doc  / **Architectures:** noarch
  - **RPM:**  python3-libnvme  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.10-1.amzn2023.0.1

- ** `libosinfo` **
  - **RPM:**  libosinfo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libosinfo-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.12.0-1.amzn2023.0.1

- ** `libsecret` **
  - **RPM:**  libsecret-mock-service
  - **Architectures:** noarch
  - **Version:** 0.21.4-3.amzn2023.0.1

- ** `libsoup3` **
  - **RPM:**  libsoup3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsoup3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsoup3-doc  / **Architectures:** noarch
  - **Version:** 3.6.0-46.amzn2023

- ** `mpc` **
  - **RPM:**  mpc
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.35-4.amzn2023

- ** `opendbx` **
  - **RPM:**  opendbx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opendbx-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opendbx-mssql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opendbx-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opendbx-postgresql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opendbx-sqlite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opendbx-sybase  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opendbx-utils  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.4.6-39.amzn2023.0.1

- ** `opendkim` **
  - **RPM:**  libopendkim  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libopendkim-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opendkim  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opendkim-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.11.0-0.41.amzn2023

- ** `osinfo-db` **
  - **RPM:**  osinfo-db
  - **Architectures:** noarch
  - **Version:** 20240701-1.amzn2023.0.1

- ** `osinfo-db-tools` **
  - **RPM:**  osinfo-db-tools
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.12.0-1.amzn2023.0.1

- ** `perl-Crypt-OpenSSL-Guess` **
  - **RPM:**  perl-Crypt-OpenSSL-Guess  / **Architectures:** noarch
  - **RPM:**  perl-Crypt-OpenSSL-Guess-tests  / **Architectures:** noarch
  - **Version:** 0.15-9.amzn2023

- ** `pipewire` **
  - **RPM:**  pipewire  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-alsa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-config-rates  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-config-upmix  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-gstreamer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-jack-audio-connection-kit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-jack-audio-connection-kit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-jack-audio-connection-kit-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-module-x11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-plugin-vulkan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-pulseaudio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-v4l2  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.2.7-1.amzn2023.0.1

- ** `python-gstreamer1` **
  - **RPM:**  python3-gstreamer1
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.24.10-1.amzn2023

- ** `python-pam` **
  - **RPM:**  python3-pam
  - **Architectures:** noarch
  - **Version:** 2.0.2-10.amzn2023.0.1

- ** `shaderc` **
  - **RPM:**  glslc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libshaderc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libshaderc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libshaderc-static  / **Architectures:** aarch64, x86\_64
  - **Version:** 2024.3-45.amzn2023

- ** `sound-theme-freedesktop` **
  - **RPM:**  sound-theme-freedesktop
  - **Architectures:** noarch
  - **Version:** 0.8-22.amzn2023

- ** `tracker-miners` **
  - **RPM:**  tracker-miners
  - **Architectures:** aarch64, x86\_64
  - **Version:** 3.7.4-2.amzn2023.0.1

- ** `v4l-utils` **
  - **RPM:**  dvb-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdvbv5  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdvbv5-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libv4l  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libv4l-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v4l-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v4l-utils-devel-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.26.1-6.amzn2023.0.2

- ** `vulkan-tools` **
  - **RPM:**  vulkan-tools
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.296.0-2.amzn2023

- ** `vulkan-utility-libraries` **
  - **RPM:**  vulkan-utility-libraries-devel
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.296.0-1.amzn2023

- ** `vulkan-validation-layers` **
  - **RPM:**  vulkan-validation-layers
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.296.0-83.amzn2023

- ** `vulkan-volk` **
  - **RPM:**  vulkan-volk-devel
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.296.0-2.amzn2023

- ** `wireplumber` **
  - **RPM:**  wireplumber  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireplumber-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireplumber-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireplumber-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.5.7-1.amzn2023.0.1

- ** `wsdd` **
  - **RPM:**  wsdd
  - **Architectures:** noarch
  - **Version:** 0.8-2.amzn2023

### AL2023.6.20250303 upgrades from AL2023.6.20250218
<a name="vercmp-AL2023.6.20250218-AL2023.6.20250303"></a>

 Comparing [2023.6.20250218](relnotes-2023.6.20250218.md) to [2023.6.20250303](#relnotes-2023.6.20250303).

| Package Type | Count |
| --- | --- |
| Source | 49 |
| Total Binary | 626 |
|  noarch binary RPMs | 120 |
|  x86\_64 binary RPMs | 253 |
|  aarch64 binary RPMs | 253 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 1.300044.0-1.amzn2023
  - **AL2023.6.20250303 version:** 1.300052.1-1.amzn2023

- ** `at-spi2-core` (`at-spi2-atk` in AL2023.6.20250218) **
  - **RPM:**  at-spi2-atk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  at-spi2-atk-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.38.0-2.amzn2023.0.2
  - **AL2023.6.20250303 version:** 2.54.0-1.amzn2023.0.1

- ** `at-spi2-core` **
  - **RPM:**  at-spi2-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  at-spi2-core-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.40.3-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 2.54.0-1.amzn2023.0.1

- ** `at-spi2-core` (`atk` in AL2023.6.20250218) **
  - **RPM:**  atk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  atk-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.36.0-3.amzn2023.0.2
  - **AL2023.6.20250303 version:** 2.54.0-1.amzn2023.0.1

- ** [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-gprofng  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.39-6.amzn2023.0.10
  - **AL2023.6.20250303 version:** 2.39-6.amzn2023.0.11

- ** `cups` **
  - **RPM:**  cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filesystem  / **Architectures:** noarch
  - **RPM:**  cups-ipptool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-lpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-printerapp  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.3.3op2-18.amzn2023.0.8
  - **AL2023.6.20250303 version:** 2.4.11-8.amzn2023.0.1

- ** `dnf-plugin-support-info` **
  - **RPM:**  dnf-plugin-support-info
  - **Architectures:** noarch
  - **AL2023.6.20250218 version:** 1.2-1.amzn2023
  - **AL2023.6.20250303 version:** 1.3-1.amzn2023

- ** `emacs` **
  - **RPM:**  emacs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-filesystem  / **Architectures:** noarch
  - **RPM:**  emacs-lucid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-nox  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-terminal  / **Architectures:** noarch
  - **AL2023.6.20250218 version:** 28.2-3.amzn2023.0.9
  - **AL2023.6.20250303 version:** 28.2-3.amzn2023.0.10

- ** `enchant2` **
  - **RPM:**  enchant2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  enchant2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  enchant2-voikko  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.2.15-5.amzn2023.0.2
  - **AL2023.6.20250303 version:** 2.8.1-2.amzn2023.0.1

- ** `gdk-pixbuf2` **
  - **RPM:**  gdk-pixbuf2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-modules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.42.10-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 2.42.12-180.amzn2023

- ** `glslang` **
  - **RPM:**  glslang  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glslang-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 11.6.0-1.20210825.git2fb89a0.amzn2023.0.2
  - **AL2023.6.20250303 version:** 15.0.0-87.amzn2023

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.6.20250218 version:** 1.22.7-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 1.24.0-1.amzn2023.0.1

- ** `gssproxy` **
  - **RPM:**  gssproxy
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 0.8.4-2.amzn2023.0.3
  - **AL2023.6.20250303 version:** 0.9.2-6.amzn2023.0.1

- ** `gtk-doc` **
  - **RPM:**  gtk-doc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 1.33.2-3.amzn2023.0.4
  - **AL2023.6.20250303 version:** 1.34.0-2.amzn2023.0.1

- ** `inih` **
  - **RPM:**  inih  / **Architectures:** aarch64, x86\_64
  - **RPM:**  inih-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 49-3.amzn2023.0.2
  - **AL2023.6.20250303 version:** 58-2.amzn2023.0.1

- ** `json-glib` **
  - **RPM:**  json-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  json-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  json-glib-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 1.6.6-1.amzn2023.0.2
  - **AL2023.6.20250303 version:** 1.10.0-1.amzn2023.0.1

- ** `jsoup` **
  - **RPM:**  jsoup  / **Architectures:** noarch
  - **RPM:**  jsoup-javadoc  / **Architectures:** noarch
  - **AL2023.6.20250218 version:** 1.13.1-9.amzn2023.0.5
  - **AL2023.6.20250303 version:** 1.16.1-4.amzn2023.0.2

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 6.1.128-136.201.amzn2023
  - **AL2023.6.20250303 version:** 6.1.129-138.220.amzn2023

- ** `keyutils` **
  - **RPM:**  keyutils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  keyutils-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  keyutils-libs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 1.6.3-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 1.6.3-1.amzn2023.0.2

- ** `lcms2` **
  - **RPM:**  lcms2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lcms2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lcms2-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.12-1.amzn2023.0.3
  - **AL2023.6.20250303 version:** 2.16-73.amzn2023

- ** `libblockdev` **
  - **RPM:**  libblockdev  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-crypto  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-crypto-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-dm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-dm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-fs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-fs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-loop  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-loop-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-lvm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-lvm-dbus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-lvm-dbus-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-lvm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-mdraid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-mdraid-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-mpath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-mpath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-nvdimm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-nvdimm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-part  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-part-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-plugins-all  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-swap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-swap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-utils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-blockdev  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.28-2.amzn2023.0.1
  - **AL2023.6.20250303 version:** 3.2.1-1.amzn2023.0.2

- ** `libical` **
  - **RPM:**  libical  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libical-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libical-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libical-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libical-glib-doc  / **Architectures:** noarch
  - **AL2023.6.20250218 version:** 3.0.14-1.amzn2023.0.2
  - **AL2023.6.20250303 version:** 3.0.18-2.amzn2023.0.1

- ** `libnotify` **
  - **RPM:**  libnotify  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnotify-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 0.7.9-4.amzn2023.0.2
  - **AL2023.6.20250303 version:** 0.8.3-4.amzn2023.0.1

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 16.4-1.amzn2023.0.2
  - **AL2023.6.20250303 version:** 16.8-1.amzn2023.0.1

- ** `libsecret` **
  - **RPM:**  libsecret  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsecret-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 0.20.4-2.amzn2023.0.2
  - **AL2023.6.20250303 version:** 0.21.4-3.amzn2023.0.1

- ** `liburing` **
  - **RPM:**  liburing  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liburing-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.0-2.amzn2023.0.2
  - **AL2023.6.20250303 version:** 2.6-2.amzn2023.0.1

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 18.20.6-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 18.20.6-1.amzn2023.0.2

- ** `openjpeg2` **
  - **RPM:**  openjpeg2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openjpeg2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openjpeg2-devel-docs  / **Architectures:** noarch
  - **RPM:**  openjpeg2-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.4.0-11.amzn2023.0.5
  - **AL2023.6.20250303 version:** 2.4.0-11.amzn2023.0.6

- ** `openssh` **
  - **RPM:**  openssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-keycat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_ssh\_agent\_auth  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 8.7p1-8.amzn2023.0.13
  - **AL2023.6.20250303 version:** 8.7p1-8.amzn2023.0.14

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-snapsafe-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 3.0.8-1.amzn2023.0.18
  - **AL2023.6.20250303 version:** 3.0.8-1.amzn2023.0.19

- ** `PackageKit` **
  - **RPM:**  PackageKit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-command-not-found  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-cron  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-gtk3-module  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 1.2.4-2.amzn2023.0.5
  - **AL2023.6.20250303 version:** 1.2.8-2.amzn2023.0.1

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-sodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-zip  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 8.2.23-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 8.2.27-1.amzn2023.0.1

- ** [`php8.3`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.3`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-modphp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-sodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-zip  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 8.3.10-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 8.3.16-1.amzn2023.0.1

- ** `postgresql15` **
  - **RPM:**  postgresql15  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-contrib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-llvmjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plperl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plpython3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-pltcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-private-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-private-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-test-rpm-macros  / **Architectures:** noarch
  - **RPM:**  postgresql15-upgrade  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-upgrade-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 15.9-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 15.12-1.amzn2023.0.1

- ** `postgresql16` **
  - **RPM:**  postgresql16  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-contrib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-llvmjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-plperl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-plpython3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-pltcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-private-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-private-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-test-rpm-macros  / **Architectures:** noarch
  - **RPM:**  postgresql16-upgrade  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-upgrade-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 16.5-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 16.8-1.amzn2023.0.1

- ** `protobuf-c` **
  - **RPM:**  protobuf-c  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-c-compiler  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-c-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 1.4.1-2.amzn2023.0.3
  - **AL2023.6.20250303 version:** 1.5.0-4.amzn2023.0.1

- ** [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 3.11.6-1.amzn2023.0.6
  - **AL2023.6.20250303 version:** 3.11.11-5.amzn2023.0.1

- ** `rest` **
  - **RPM:**  rest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rest-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 0.8.1-9.amzn2023.0.2
  - **AL2023.6.20250303 version:** 0.9.1-11.amzn2023.0.1

- ** `rpcsvc-proto` **
  - **RPM:**  rpcgen  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpcsvc-proto-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 1.4-7.amzn2023.0.2
  - **AL2023.6.20250303 version:** 1.4-15.amzn2023.0.1

- ** `spirv-headers` **
  - **RPM:**  spirv-headers-devel
  - **Architectures:** noarch
  - **AL2023.6.20250218 version:** 1.5.5-42.amzn2023.0.1
  - **AL2023.6.20250303 version:** 1.5.5-60.amzn2023

- ** `spirv-tools` **
  - **RPM:**  spirv-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  spirv-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  spirv-tools-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2022.2-2.amzn2023.0.2
  - **AL2023.6.20250303 version:** 2024.3-90.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20250218 version:** 2023.6.20250218-0.amzn2023
  - **AL2023.6.20250303 version:** 2023.6.20250303-0.amzn2023

- ** `tracker` **
  - **RPM:**  libtracker-sparql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tracker  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tracker-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tracker-doc  / **Architectures:** noarch
  - **AL2023.6.20250218 version:** 3.1.2-1.amzn2023.0.2
  - **AL2023.6.20250303 version:** 3.7.3-3.amzn2023.0.1

- ** `tzdata` **
  - **RPM:**  tzdata  / **Architectures:** noarch
  - **RPM:**  tzdata-java  / **Architectures:** noarch
  - **AL2023.6.20250218 version:** 2024a-1.amzn2023.0.1
  - **AL2023.6.20250303 version:** 2025a-1.amzn2023.0.1

- ** `udisks2` **
  - **RPM:**  libudisks2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libudisks2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  udisks2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  udisks2-lsm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  udisks2-lvm2  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 2.9.4-1.amzn2023.0.4
  - **AL2023.6.20250303 version:** 2.10.1-6.amzn2023.0.1

- ** `vulkan-headers` **
  - **RPM:**  vulkan-headers
  - **Architectures:** noarch
  - **AL2023.6.20250218 version:** 1.3.290.0-57.amzn2023.0.1
  - **AL2023.6.20250303 version:** 1.3.296.0-59.amzn2023.0.1

- ** `vulkan-loader` **
  - **RPM:**  vulkan-loader  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vulkan-loader-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 1.3.290.0-71.amzn2023.0.1
  - **AL2023.6.20250303 version:** 1.3.296.0-72.amzn2023.0.1

- ** `wayland` **
  - **RPM:**  libwayland-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-cursor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-egl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wayland-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wayland-doc  / **Architectures:** noarch
  - **AL2023.6.20250218 version:** 1.22.0-1.amzn2023.0.2
  - **AL2023.6.20250303 version:** 1.23.0-2.amzn2023.0.1

- ** `xorg-x11-server` **
  - **RPM:**  xorg-x11-server-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-source  / **Architectures:** noarch
  - **RPM:**  xorg-x11-server-Xephyr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xnest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xorg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xvfb  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250218 version:** 21.1.13-5.amzn2023.0.2
  - **AL2023.6.20250303 version:** 21.1.13-5.amzn2023.0.3

- ** `yelp-tools` **
  - **RPM:**  yelp-tools
  - **Architectures:** noarch
  - **AL2023.6.20250218 version:** 40.0-1.amzn2023.0.3
  - **AL2023.6.20250303 version:** 42.1-6.amzn2023.0.1

- ** `yelp-xsl` **
  - **RPM:**  yelp-xsl  / **Architectures:** noarch
  - **RPM:**  yelp-xsl-devel  / **Architectures:** noarch
  - **AL2023.6.20250218 version:** 40.2-1.amzn2023.0.2
  - **AL2023.6.20250303 version:** 42.1-5.amzn2023.0.1

## Default AMI
<a name="amis-2023.6.20250303.default-ami"></a>

This section provides details about default ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.6.20250303-0.amzn2023  |
|  binutils-2.39-6.amzn2023.0.11  |
|  dnf-plugin-support-info-1.3-1.amzn2023  |
|  gssproxy-0.9.2-6.amzn2023.0.1  |
|  inih-58-2.amzn2023.0.1  |
|  kernel-libbpf-6.1.129-138.220.amzn2023  |
|  kernel-livepatch-repo-s3-2023.6.20250303-0.amzn2023  |
|  kernel-tools-6.1.129-138.220.amzn2023  |
|  kernel-6.1.129-138.220.amzn2023  |
|  keyutils-libs-1.6.3-1.amzn2023.0.2  |
|  keyutils-1.6.3-1.amzn2023.0.2  |
|  openssh-clients-8.7p1-8.amzn2023.0.14  |
|  openssh-server-8.7p1-8.amzn2023.0.14  |
|  openssh-8.7p1-8.amzn2023.0.14  |
|  openssl-libs-1:3.0.8-1.amzn2023.0.19  |
|  openssl-1:3.0.8-1.amzn2023.0.19  |
|  protobuf-c-1.5.0-4.amzn2023.0.1  |
|  system-release-2023.6.20250303-0.amzn2023  |
|  tzdata-2025a-1.amzn2023.0.1  |

## Docker container image
<a name="amis-2023.6.20250303.docker-container-image"></a>

This section provides details about docker container image.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.6.20250303-0.amzn2023  |
|  keyutils-libs-1.6.3-1.amzn2023.0.2  |
|  openssl-libs-1:3.0.8-1.amzn2023.0.19  |
|  system-release-2023.6.20250303-0.amzn2023  |
|  tzdata-2025a-1.amzn2023.0.1  |

## Minimal AMI
<a name="amis-2023.6.20250303.minimal-ami"></a>

This section provides details about minimal ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.6.20250303-0.amzn2023  |
|  dnf-plugin-support-info-1.3-1.amzn2023  |
|  inih-58-2.amzn2023.0.1  |
|  kernel-libbpf-6.1.129-138.220.amzn2023  |
|  kernel-livepatch-repo-s3-2023.6.20250303-0.amzn2023  |
|  kernel-6.1.129-138.220.amzn2023  |
|  keyutils-libs-1.6.3-1.amzn2023.0.2  |
|  openssh-clients-8.7p1-8.amzn2023.0.14  |
|  openssh-server-8.7p1-8.amzn2023.0.14  |
|  openssh-8.7p1-8.amzn2023.0.14  |
|  openssl-libs-1:3.0.8-1.amzn2023.0.19  |
|  openssl-1:3.0.8-1.amzn2023.0.19  |
|  system-release-2023.6.20250303-0.amzn2023  |
|  tzdata-2025a-1.amzn2023.0.1  |

## Minimal container image
<a name="amis-2023.6.20250303.minimal-container-image"></a>

This section provides details about minimal container image.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.6.20250303-0.amzn2023  |
|  keyutils-libs-1.6.3-1.amzn2023.0.2  |
|  openssl-libs-1:3.0.8-1.amzn2023.0.19  |
|  system-release-2023.6.20250303-0.amzn2023  |

## Contact us
<a name="amis-2023.6.20250303.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
