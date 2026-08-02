---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241209.html
---

# Amazon Linux 2023 version 2023.6.20241209 release notes
<a name="relnotes-2023.6.20241209"></a>

**Warning**
 This release was recalled due to a bug introduced in the `python3.9` package which prevented the use of `venv` as described in [this GitHub issue](https://github.com/amazonlinux/amazon-linux-2023/issues/861).
 The [AL2023.6.20241212](relnotes-2023.6.20241212.md) release was subsequently released with a fix for this issue. The [AL2023.6.20241212](relnotes-2023.6.20241212.md) release includes all other changes that were present in the 2023.6.20241209 release.
 Customers are advised to update to the [AL2023.6.20241212](relnotes-2023.6.20241212.md) release to resolve this issue.

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20241209.

**Topics**
+ [Major updates](#major-updates-2023.6.20241209)
+ [Repository](#amis-2023.6.20241209.repository)
+ [Docker container image](#amis-2023.6.20241209.container-image)
+ [Default AMI](#amis-2023.6.20241209.default-ami)
+ [Minimal AMI](#amis-2023.6.20241209.minimal-ami)
+ [Minimal container image](#amis-2023.6.20241209.minimal-container-ami)
+ [Contact us](#amis-2023.6.20241209.contact-us)

## Major updates
<a name="major-updates-2023.6.20241209"></a>

**Known issues**
+ This release was recalled due to a bug introduced in the `python3.9` package which prevented the use of `venv` as described in [this GitHub issue](https://github.com/amazonlinux/amazon-linux-2023/issues/861). Customers are advised to update to the [AL2023.6.20241212](relnotes-2023.6.20241212.md) release to resolve this issue.
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20241209.repository"></a>

### New packages in AL2023.6.20241209 since AL2023.6.20241121
<a name="new-AL2023.6.20241121-AL2023.6.20241209"></a>

 Comparing AL2023.6.20241121 version 2023.6.20241121 to AL2023.6.20241209 version [2023.6.20241209](#relnotes-2023.6.20241209).

| Package Type | Number of new packages in AL2023.6.20241209 compared to AL2023.6.20241121 |
| --- | --- |
| Source RPMs | 7 |
| Total Binary RPMs | 39 |
|  noarch binary RPMs | 7 |
|  x86\_64 binary RPMs | 16 |
|  aarch64 binary RPMs | 16 |

New packages in AL2023.6.20241209:

- ** `cairomm1.16` **
  - **RPM:**  cairomm1.16  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairomm1.16-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairomm1.16-doc  / **Architectures:** noarch
  - **Version:** 1.18.0-36.amzn2023

- ** `flatpak-builder` **
  - **RPM:**  flatpak-builder-tests
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.4.4-1.amzn2023.0.1

- ** `glib2` **
  - **RPM:**  glib2-doc
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.82.2-764.amzn2023

- ** `glibmm2.4` **
  - **RPM:**  glibmm2.4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibmm2.4-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibmm2.4-doc  / **Architectures:** noarch
  - **Version:** 2.66.7-2.amzn2023

- ** `glibmm2.68` **
  - **RPM:**  glibmm2.68  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibmm2.68-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibmm2.68-doc  / **Architectures:** noarch
  - **Version:** 2.82.0-19.amzn2023

- ** `libsigc++30` **
  - **RPM:**  libsigc\+\+30  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsigc\+\+30-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsigc\+\+30-doc  / **Architectures:** noarch
  - **Version:** 3.6.0-3.amzn2023

- ** `pango` **
  - **RPM:**  pango-doc
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.54.0-2.amzn2023.0.4

- ** `pangomm2.48` **
  - **RPM:**  pangomm2.48  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pangomm2.48-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pangomm2.48-doc  / **Architectures:** noarch
  - **Version:** 2.54.0-15.amzn2023

- ** `python-dbusmock` **
  - **RPM:**  python3-dbusmock
  - **Architectures:** noarch
  - **Version:** 0.32.2-1.amzn2023

- ** `upower` **
  - **RPM:**  upower  / **Architectures:** aarch64, x86\_64
  - **RPM:**  upower-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  upower-devel-docs  / **Architectures:** noarch
  - **RPM:**  upower-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.90.6-139.amzn2023

### AL2023.6.20241209 upgrades from AL2023.6.20241121
<a name="vercmp-AL2023.6.20241121-AL2023.6.20241209"></a>

 Comparing [2023.6.20241121](relnotes-2023.6.20241121.md) to [2023.6.20241209](#relnotes-2023.6.20241209).

| Package Type | Count |
| --- | --- |
| Source | 53 |
| Total Binary | 528 |
|  noarch binary RPMs | 164 |
|  x86\_64 binary RPMs | 182 |
|  aarch64 binary RPMs | 182 |

The full comparison of RPM package versions is below.

- ** `appstream` **
  - **RPM:**  appstream  / **Architectures:** aarch64, x86\_64
  - **RPM:**  appstream-compose  / **Architectures:** aarch64, x86\_64
  - **RPM:**  appstream-compose-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  appstream-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 0.16.1-1.amzn2023.0.1
  - **AL2023.6.20241209 version:** 1.0.2-4.amzn2023.0.1

- ** `apr` **
  - **RPM:**  apr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.7.2-2.amzn2023.0.2
  - **AL2023.6.20241209 version:** 1.7.5-1.amzn2023.0.2

- ** `avahi` **
  - **RPM:**  avahi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-autoipd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-compat-howl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-compat-howl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-compat-libdns\_sd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-compat-libdns\_sd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-dnsconfd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-gobject  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-gobject-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-ui-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-ui-gtk3  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 0.8-14.amzn2023.0.12
  - **AL2023.6.20241209 version:** 0.8-14.amzn2023.0.14

- ** `awscli-2` **
  - **RPM:**  awscli-2
  - **Architectures:** noarch
  - **AL2023.6.20241121 version:** 2.15.30-1.amzn2023.0.1
  - **AL2023.6.20241209 version:** 2.17.18-1.amzn2023.0.1

- ** `aws-nitro-enclaves-acm` **
  - **RPM:**  aws-nitro-enclaves-acm
  - **Architectures:** aarch64
  - **AL2023.6.20241121 version:** 1.4.0-1.amzn2023
  - **AL2023.6.20241209 version:** 1.4.0-2.amzn2023

- ** `cairo` **
  - **RPM:**  cairo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-gobject  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-gobject-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.17.6-2.amzn2023.0.1
  - **AL2023.6.20241209 version:** 1.18.0-4.amzn2023.0.1

- ** `cairomm` **
  - **RPM:**  cairomm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairomm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairomm-doc  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 1.14.4-126.amzn2023.0.1
  - **AL2023.6.20241209 version:** 1.14.5-140.amzn2023

- ** `cloud-init` **
  - **RPM:**  cloud-init  / **Architectures:** noarch
  - **RPM:**  cloud-init-cfg-ec2  / **Architectures:** noarch
  - **RPM:**  cloud-init-cfg-onprem  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 22.2.2-1.amzn2023.1.12
  - **AL2023.6.20241209 version:** 22.2.2-1.amzn2023.1.13

- ** `desktop-file-utils` **
  - **RPM:**  desktop-file-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 0.26-3.amzn2023.0.2
  - **AL2023.6.20241209 version:** 0.27-2.amzn2023.0.1

- ** `dnf-plugins-core` **
  - **RPM:**  dnf-plugins-core  / **Architectures:** noarch
  - **RPM:**  dnf-utils  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-leaves  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-local  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-modulesync  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-post-transaction-actions  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugins-core  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-show-leaves  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-versionlock  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 4.3.0-13.amzn2023.0.4
  - **AL2023.6.20241209 version:** 4.3.0-13.amzn2023.0.5

- ** `dotnet6.0` **
  - **RPM:**  aspnetcore-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-6.0  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 6.0.32-1.amzn2023.0.1
  - **AL2023.6.20241209 version:** 6.0.36-1.amzn2023.0.1

- ** `dotnet8.0` **
  - **RPM:**  aspnetcore-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 8.0.7-1.amzn2023
  - **AL2023.6.20241209 version:** 8.0.11-1.amzn2023

- ** `dovecot` **
  - **RPM:**  dovecot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-pigeonhole  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 2.3.20-1.amzn2023.0.1
  - **AL2023.6.20241209 version:** 2.3.20-1.amzn2023.0.2

- ** `doxygen` **
  - **RPM:**  doxygen  / **Architectures:** aarch64, x86\_64
  - **RPM:**  doxygen-latex  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.9.4-1.amzn2023.0.3
  - **AL2023.6.20241209 version:** 1.12.0-2.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.87.1-1.amzn2023
  - **AL2023.6.20241209 version:** 1.89.1-1.amzn2023

- ** `flatpak` **
  - **RPM:**  flatpak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-selinux  / **Architectures:** noarch
  - **RPM:**  flatpak-session-helper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.15.10-1.amzn2023.0.1
  - **AL2023.6.20241209 version:** 1.15.10-1.amzn2023.0.2

- ** `flatpak-builder` **
  - **RPM:**  flatpak-builder
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.3.3-2.amzn2023.0.1
  - **AL2023.6.20241209 version:** 1.4.4-1.amzn2023.0.1

- ** `ghostscript` **
  - **RPM:**  ghostscript  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-doc  / **Architectures:** noarch
  - **RPM:**  ghostscript-gtk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-tools-dvipdf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-tools-fonts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-tools-printing  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-x11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 9.56.1-7.amzn2023.0.10
  - **AL2023.6.20241209 version:** 9.56.1-7.amzn2023.0.11

- ** `glib2` **
  - **RPM:**  glib2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 2.74.7-689.amzn2023.0.2
  - **AL2023.6.20241209 version:** 2.82.2-764.amzn2023

- ** `glib-networking` **
  - **RPM:**  glib-networking  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib-networking-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 2.68.2-1.amzn2023.0.3
  - **AL2023.6.20241209 version:** 2.80.0-186.amzn2023.0.1

- ** `gobject-introspection` **
  - **RPM:**  gobject-introspection  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gobject-introspection-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.73.0-2.amzn2023.0.3
  - **AL2023.6.20241209 version:** 1.82.0-1.amzn2023

- ** `grpc` **
  - **RPM:**  grpc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-data  / **Architectures:** noarch
  - **RPM:**  grpc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-doc  / **Architectures:** noarch
  - **RPM:**  grpc-plugins  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.60.0-10.amzn2023
  - **AL2023.6.20241209 version:** 1.60.2-10.amzn2023

- ** `gsettings-desktop-schemas` **
  - **RPM:**  gsettings-desktop-schemas  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gsettings-desktop-schemas-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 40.0-1.amzn2023.0.3
  - **AL2023.6.20241209 version:** 47.1-205.amzn2023

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
  - **AL2023.6.20241121 version:** 6.1.115-126.197.amzn2023
  - **AL2023.6.20241209 version:** 6.1.119-129.201.amzn2023

- ** `libappstream-glib` **
  - **RPM:**  libappstream-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libappstream-glib-builder  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libappstream-glib-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 0.7.18-2.amzn2023.0.2
  - **AL2023.6.20241209 version:** 0.8.3-139.amzn2023

- ** `libgudev` **
  - **RPM:**  libgudev  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgudev-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 237-1.amzn2023.0.2
  - **AL2023.6.20241209 version:** 238-5.amzn2023.0.1

- ** `libsoup` **
  - **RPM:**  libsoup  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsoup-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsoup-doc  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 2.72.0-6.amzn2023.0.2
  - **AL2023.6.20241209 version:** 2.72.0-6.amzn2023.0.3

- ** `libxml2` **
  - **RPM:**  libxml2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libxml2  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 2.10.4-1.amzn2023.0.6
  - **AL2023.6.20241209 version:** 2.10.4-1.amzn2023.0.7

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2023.6.20241121 version:** 2.1-53.amzn2023.0.9
  - **AL2023.6.20241209 version:** 2.1-53.amzn2023.0.10

- ** `mm-common` **
  - **RPM:**  mm-common  / **Architectures:** noarch
  - **RPM:**  mm-common-docs  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 1.0.3-1.amzn2023.0.3
  - **AL2023.6.20241209 version:** 1.0.6-3.amzn2023.0.3

- ** `nvme-cli` **
  - **RPM:**  nvme-cli
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.11.1-3.amzn2023.0.4
  - **AL2023.6.20241209 version:** 1.11.1-3.amzn2023.0.5

- ** `opensc` **
  - **RPM:**  opensc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 0.24.0-1.amzn2023.0.3
  - **AL2023.6.20241209 version:** 0.24.0-1.amzn2023.0.4

- ** `ostree` **
  - **RPM:**  ostree  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ostree-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ostree-grub2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ostree-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 2023.5-3.amzn2023.0.2
  - **AL2023.6.20241209 version:** 2024.8-306.amzn2023

- ** `pango` **
  - **RPM:**  pango  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pango-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.48.10-1.amzn2023.0.3
  - **AL2023.6.20241209 version:** 1.54.0-2.amzn2023.0.4

- ** `pangomm` **
  - **RPM:**  pangomm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pangomm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pangomm-doc  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 2.46.1-1.amzn2023.0.3
  - **AL2023.6.20241209 version:** 2.46.4-100.amzn2023

- ** `polkit` **
  - **RPM:**  polkit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  polkit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  polkit-docs  / **Architectures:** noarch
  - **RPM:**  polkit-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 0.117-11.amzn2023.0.1
  - **AL2023.6.20241209 version:** 125-1.amzn2023.0.1

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
  - **AL2023.6.20241121 version:** 15.8-1.amzn2023.0.1
  - **AL2023.6.20241209 version:** 15.9-1.amzn2023.0.1

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
  - **AL2023.6.20241121 version:** 16.4-1.amzn2023.0.1
  - **AL2023.6.20241209 version:** 16.5-1.amzn2023.0.1

- ** `pycairo` **
  - **RPM:**  python3-cairo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-cairo-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.20.1-1.amzn2023.0.2
  - **AL2023.6.20241209 version:** 1.25.1-5.amzn2023.0.1

- ** `pygobject3` **
  - **RPM:**  python3-gobject  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-gobject-base  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-gobject-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 3.42.2-2.amzn2023.0.3
  - **AL2023.6.20241209 version:** 3.48.2-3.amzn2023.0.2

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 3.11.6-1.amzn2023.0.4
  - **AL2023.6.20241209 version:** 3.11.6-1.amzn2023.0.5

- ** `python3.11-pip` **
  - **RPM:**  python3.11-pip  / **Architectures:** noarch
  - **RPM:**  python3.11-pip-wheel  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 22.3.1-2.amzn2023.0.4
  - **AL2023.6.20241209 version:** 22.3.1-2.amzn2023.0.5

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-unversioned-command  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 3.9.16-1.amzn2023.0.9
  - **AL2023.6.20241209 version:** 3.9.20-1.amzn2023.0.1

- ** `python-pip` **
  - **RPM:**  python3-pip  / **Architectures:** noarch
  - **RPM:**  python3-pip-wheel  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 21.3.1-2.amzn2023.0.9
  - **AL2023.6.20241209 version:** 21.3.1-2.amzn2023.0.10

- ** `python-requests` **
  - **RPM:**  python3-requests  / **Architectures:** noarch
  - **RPM:**  python3-requests\+security  / **Architectures:** noarch
  - **RPM:**  python3-requests\+socks  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 2.25.1-1.amzn2023.0.3
  - **AL2023.6.20241209 version:** 2.25.1-1.amzn2023.0.4

- ** `python-waitress` **
  - **RPM:**  python3-waitress
  - **Architectures:** noarch
  - **AL2023.6.20241121 version:** 2.1.2-1.amzn2023.0.2
  - **AL2023.6.20241209 version:** 2.1.2-1.amzn2023.0.3

- ** `runfinch-finch` **
  - **RPM:**  runfinch-finch
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 1.4.1-1.amzn2023.0.1
  - **AL2023.6.20241209 version:** 1.4.1-1.amzn2023.0.2

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20241121 version:** 2023.6.20241121-0.amzn2023
  - **AL2023.6.20241209 version:** 2023.6.20241209-0.amzn2023

- ** `umockdev` **
  - **RPM:**  umockdev  / **Architectures:** aarch64, x86\_64
  - **RPM:**  umockdev-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 0.16.3-1.amzn2023.0.2
  - **AL2023.6.20241209 version:** 0.18.4-1.amzn2023.0.1

- ** `update-motd` **
  - **RPM:**  update-motd
  - **Architectures:** noarch
  - **AL2023.6.20241121 version:** 2.2-1.amzn2023
  - **AL2023.6.20241209 version:** 2.3-1.amzn2023

- ** `xdg-dbus-proxy` **
  - **RPM:**  xdg-dbus-proxy
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 0.1.2-4.amzn2023.0.2
  - **AL2023.6.20241209 version:** 0.1.5-2.amzn2023.0.1

- ** `xdg-user-dirs` **
  - **RPM:**  xdg-user-dirs
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241121 version:** 0.17-8.amzn2023.0.2
  - **AL2023.6.20241209 version:** 0.18-4.amzn2023.0.1

- ** `xdg-utils` **
  - **RPM:**  xdg-utils
  - **Architectures:** noarch
  - **AL2023.6.20241121 version:** 1.1.3-12.amzn2023.0.1
  - **AL2023.6.20241209 version:** 1.2.1-1.amzn2023.0.1

## Docker container image
<a name="amis-2023.6.20241209.container-image"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20241209-0.amzn2023 |
| glib2-2.82.2-764.amzn2023  |
| libxml2-2.10.4-1.amzn2023.0.7  |
| python3-libs-3.9.20-1.amzn2023.0.1  |
| python3-pip-wheel-21.3.1-2.amzn2023.0.10  |
| python3-3.9.20-1.amzn2023.0.1  |
| system-release-2023.6.20241209-0.amzn2023 |

## Default AMI
<a name="amis-2023.6.20241209.default-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20241209-0.amzn2023 |
| awscli-2-2.17.18-1.amzn2023.0.1 |
| cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.13 |
| cloud-init-22.2.2-1.amzn2023.1.13 |
| dnf-plugins-core-4.3.0-13.amzn2023.0.5 |
| dnf-utils-4.3.0-13.amzn2023.0.5 |
| glib2-2.82.2-764.amzn2023 |
| kernel-libbpf-6.1.119-129.201.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20241209-0.amzn2023 |
| kernel-tools-6.1.119-129.201.amzn2023 |
| kernel-6.1.119-129.201.amzn2023 |
| libxml2-2.10.4-1.amzn2023.0.7 |
| microcode\_ctl-2:2.1-53.amzn2023.0.10 |
| python3-dnf-plugins-core-4.3.0-13.amzn2023.0.5 |
| python3-libs-3.9.20-1.amzn2023.0.1  |
| python3-pip-wheel-21.3.1-2.amzn2023.0.10  |
| python3-requests-2.25.1-1.amzn2023.0.4  |
| python3-3.9.20-1.amzn2023.0.1 |
| system-release-2023.6.20241209-0.amzn2023 |
| update-motd-2.3-1.amzn2023 |

## Minimal AMI
<a name="amis-2023.6.20241209.minimal-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20241209-0.amzn2023 |
| awscli-2-2.17.18-1.amzn2023.0.1 |
| cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.13 |
| cloud-init-22.2.2-1.amzn2023.1.13 |
| dnf-plugins-core-4.3.0-13.amzn2023.0.5 |
| glib2-2.82.2-764.amzn2023 |
| kernel-libbpf-6.1.119-129.201.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20241209-0.amzn2023 |
| kernel-6.1.119-129.201.amzn2023 |
| libxml2-2.10.4-1.amzn2023.0.7 |
| python3-dnf-plugins-core-4.3.0-13.amzn2023.0.5 |
| python3-libs-3.9.20-1.amzn2023.0.1  |
| python3-pip-wheel-21.3.1-2.amzn2023.0.10  |
| python3-requests-2.25.1-1.amzn2023.0.4  |
| python3-3.9.20-1.amzn2023.0.1 |
| system-release-2023.6.20241209-0.amzn2023 |
| update-motd-2.3-1.amzn2023 |

## Minimal container image
<a name="amis-2023.6.20241209.minimal-container-ami"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20241209-0.amzn2023 |
| glib2-2.82.2-764.amzn2023 |
| gobject-introspection-1.82.0-1.amzn2023 |
| libxml2-2.10.4-1.amzn2023.0.7 |
| system-release-2023.6.20241209-0.amzn2023 |

## Contact us
<a name="amis-2023.6.20241209.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
