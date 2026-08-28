---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230906.html
---

# Amazon Linux 2023 version 2023.1.20230906 release notes
<a name="relnotes-2023.1.20230906"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.1.20230906 release.

## Major updates
<a name="major-updates-2023.1.20230906"></a>

This release represents an update to AL2023.1. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads and customers are encouraged to start migrations from previous versions of Amazon Linux today.

For information about UEFI Secure Boot on AL2023, see [Amazon Linux announces support for secure boot with AL2023](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/).

AL2023 includes the following major updates.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.1.20230906)
+ [Repository](#amis-2023.1.20230906.repository)
+ [Docker container image](#amis-2023.1.20230906.container-image)
+ [Default AMI](#amis-2023.1.20230906.default-ami)
+ [Minimal AMI](#amis-2023.1.20230906.minimal-ami)

## Repository
<a name="amis-2023.1.20230906.repository"></a>

### New packages in AL2023.1.20230906 since AL2023.1.20230825
<a name="new-AL2023.1.20230825-AL2023.1.20230906"></a>

 Comparing AL2023.1.20230825 version 2023.1.20230825 to AL2023.1.20230906 version [2023.1.20230906](#relnotes-2023.1.20230906).

| Package Type | Number of new packages in AL2023.1.20230906 compared to AL2023.1.20230825 |
| --- | --- |
| Source RPMs | 8 |
| Total Binary RPMs | 45 |
|  noarch binary RPMs | 1 |
|  x86\_64 binary RPMs | 22 |
|  aarch64 binary RPMs | 22 |

New packages in AL2023.1.20230906:

- ** `docbook2X` **
  - **RPM:**  docbook2X
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.8.8-43.amzn2023

- ** `flatpak` **
  - **RPM:**  flatpak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-selinux  / **Architectures:** noarch
  - **RPM:**  flatpak-session-helper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-tests  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.15.4-3.amzn2023.0.1

- ** `flatpak-builder` **
  - **RPM:**  flatpak-builder
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.3-2.amzn2023.0.1

- ** `libxmlb` **
  - **RPM:**  libxmlb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxmlb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxmlb-tests  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.3.11-42.amzn2023

- ** `lttng-tools` **
  - **RPM:**  lttng-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lttng-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-lttng  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.13.4-1.amzn2023

- ** `mutt` **
  - **RPM:**  mutt
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.2.9-1.amzn2023.0.1

- ** `nodejs` **
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 9.6.7-1.18.17.1.1.amzn2023.0.2

- ** `ostree` **
  - **RPM:**  ostree  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ostree-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ostree-grub2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ostree-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 2023.5-3.amzn2023.0.2

- ** `rsyslog` **
  - **RPM:**  rsyslog-mmtaghostname
  - **Architectures:** aarch64, x86\_64
  - **Version:** 8.2204.0-3.amzn2023.0.4

- ** `urlview` **
  - **RPM:**  urlview
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.9-32.20131022git08767a.amzn2023

### AL2023.1.20230906 upgrades from AL2023.1.20230825
<a name="vercmp-AL2023.1.20230825-AL2023.1.20230906"></a>

 Comparing [2023.1.20230825](relnotes-2023.1.20230825.md) to [2023.1.20230906](#relnotes-2023.1.20230906).

| Package Type | Count |
| --- | --- |
| Source | 46 |
| Total Binary | 636 |
|  noarch binary RPMs | 124 |
|  x86\_64 binary RPMs | 256 |
|  aarch64 binary RPMs | 256 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 1.300026.2-1.amzn2023
  - **AL2023.1.20230906 version:** 1.300026.3-2.amzn2023

- ** `amazon-ecr-credential-helper` **
  - **RPM:**  amazon-ecr-credential-helper
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 0.6.0-1.amzn2023
  - **AL2023.1.20230906 version:** 0.7.1-1.amzn2023

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 3.1.1927.0-1.amzn2023
  - **AL2023.1.20230906 version:** 3.2.1377.0-1.amzn2023

- ** `apache-ivy` **
  - **RPM:**  apache-ivy  / **Architectures:** noarch
  - **RPM:**  apache-ivy-javadoc  / **Architectures:** noarch
  - **AL2023.1.20230825 version:** 2.5.1-1.amzn2023.0.1
  - **AL2023.1.20230906 version:** 2.5.1-1.amzn2023.0.2

- ** `appstream` **
  - **RPM:**  appstream  / **Architectures:** aarch64, x86\_64
  - **RPM:**  appstream-compose  / **Architectures:** aarch64, x86\_64
  - **RPM:**  appstream-compose-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  appstream-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 0.14.5-1.amzn2023.0.3
  - **AL2023.1.20230906 version:** 0.16.1-1.amzn2023.0.1

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
  - **AL2023.1.20230825 version:** 0.8-14.amzn2023.0.8
  - **AL2023.1.20230906 version:** 0.8-14.amzn2023.0.10

- ** `bind` **
  - **RPM:**  bind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-chroot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-sqlite3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dnssec-doc  / **Architectures:** noarch
  - **RPM:**  bind-dnssec-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-doc  / **Architectures:** noarch
  - **RPM:**  bind-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-license  / **Architectures:** noarch
  - **RPM:**  bind-pkcs11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-bind  / **Architectures:** noarch
  - **AL2023.1.20230825 version:** 9.16.42-1.amzn2023.0.1
  - **AL2023.1.20230906 version:** 9.16.42-1.amzn2023.0.3

- ** [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-gprofng  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 2.39-6.amzn2023.0.7
  - **AL2023.1.20230906 version:** 2.39-6.amzn2023.0.9

- ** `bubblewrap` **
  - **RPM:**  bubblewrap
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 0.4.1-3.amzn2023.0.2
  - **AL2023.1.20230906 version:** 0.7.0-2.amzn2023.0.1

- ** `clamav` **
  - **RPM:**  clamav  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-data  / **Architectures:** noarch
  - **RPM:**  clamav-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-doc  / **Architectures:** noarch
  - **RPM:**  clamav-filesystem  / **Architectures:** noarch
  - **RPM:**  clamav-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-milter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-update  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamd  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 0.103.8-1.amzn2023.0.2
  - **AL2023.1.20230906 version:** 0.103.9-1.amzn2023.0.2

- ** `cni-plugins` **
  - **RPM:**  cni-plugins
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 1.2.0-1.amzn2023.0.1
  - **AL2023.1.20230906 version:** 1.2.0-1.amzn2023.0.2

- ** `cups` **
  - **RPM:**  cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filesystem  / **Architectures:** noarch
  - **RPM:**  cups-ipptool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-lpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-printerapp  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 2.3.3op2-18.amzn2023.0.5
  - **AL2023.1.20230906 version:** 2.3.3op2-18.amzn2023.0.6

- ** [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal) **
  - **RPM:**  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcurl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 8.0.1-1.amzn2023.0.1
  - **AL2023.1.20230906 version:** 8.2.1-1.amzn2023.0.2

- ** `dmidecode` **
  - **RPM:**  dmidecode
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 3.3-1.amzn2023.0.2
  - **AL2023.1.20230906 version:** 3.5-1.amzn2023.0.2

- ** `dnsmasq` **
  - **RPM:**  dnsmasq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dnsmasq-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 2.86-10.amzn2023.0.3
  - **AL2023.1.20230906 version:** 2.89-2.amzn2023.0.1

- ** `dotnet6.0` **
  - **RPM:**  aspnetcore-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 6.0.20-1.amzn2023.0.1
  - **AL2023.1.20230906 version:** 6.0.21-1.amzn2023.0.2

- ** `file` **
  - **RPM:**  file  / **Architectures:** aarch64, x86\_64
  - **RPM:**  file-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  file-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  file-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-file-magic  / **Architectures:** noarch
  - **AL2023.1.20230825 version:** 5.39-7.amzn2023.0.2
  - **AL2023.1.20230906 version:** 5.39-7.amzn2023.0.4

- ** `gdk-pixbuf2` **
  - **RPM:**  gdk-pixbuf2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-modules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 2.42.6-1.amzn2023.0.2
  - **AL2023.1.20230906 version:** 2.42.6-1.amzn2023.0.3

- ** `go-rpm-macros` **
  - **RPM:**  go-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  go-rpm-macros  / **Architectures:** aarch64, x86\_64
  - **RPM:**  go-rpm-templates  / **Architectures:** aarch64, x86\_64
  - **RPM:**  go-srpm-macros  / **Architectures:** noarch
  - **AL2023.1.20230825 version:** 3.1.0-32.amzn2023.0.2
  - **AL2023.1.20230906 version:** 3.2.0-37.amzn2023

- ** `hwloc` **
  - **RPM:**  hwloc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hwloc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hwloc-gui  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hwloc-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hwloc-plugins  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 2.4.1-3.amzn2023.0.3
  - **AL2023.1.20230906 version:** 2.4.1-3.amzn2023.0.6

- ** `ImageMagick` **
  - **RPM:**  ImageMagick  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 6.9.12.82-1.amzn2023.0.4
  - **AL2023.1.20230906 version:** 6.9.12.82-1.amzn2023.0.6

- ** `indent` **
  - **RPM:**  indent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 2.2.12-7.amzn2023.0.3
  - **AL2023.1.20230906 version:** 2.2.12-7.amzn2023.0.5

- ** [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 11.0.20\+8-1.amzn2023
  - **AL2023.1.20230906 version:** 11.0.20\+9-1.amzn2023

- ** [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 17.0.8\+7-1.amzn2023.1
  - **AL2023.1.20230906 version:** 17.0.8\+8-1.amzn2023.1

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 6.1.41-63.114.amzn2023
  - **AL2023.1.20230906 version:** 6.1.49-69.116.amzn2023

- ** `krb5` **
  - **RPM:**  krb5-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-pkinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-server-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-workstation  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libkadm5  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 1.20.1-8.amzn2023.0.2
  - **AL2023.1.20230906 version:** 1.21-3.amzn2023.0.3

- ** `libidn` **
  - **RPM:**  libidn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn-java  / **Architectures:** noarch
  - **RPM:**  libidn-javadoc  / **Architectures:** noarch
  - **AL2023.1.20230825 version:** 1.38-4.amzn2023.0.3
  - **AL2023.1.20230906 version:** 1.38-4.amzn2023.0.5

- ** `libidn2` **
  - **RPM:**  idn2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 2.3.2-1.amzn2023.0.2
  - **AL2023.1.20230906 version:** 2.3.2-1.amzn2023.0.4

- ** `libjpeg-turbo` **
  - **RPM:**  libjpeg-turbo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjpeg-turbo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjpeg-turbo-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  turbojpeg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  turbojpeg-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 2.1.4-2.amzn2023.0.2
  - **AL2023.1.20230906 version:** 2.1.4-2.amzn2023.0.4

- ** `libpng` **
  - **RPM:**  libpng  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpng-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpng-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpng-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 1.6.37-10.amzn2023.0.2
  - **AL2023.1.20230906 version:** 1.6.37-10.amzn2023.0.4

- ** `libtasn1` **
  - **RPM:**  libtasn1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtasn1-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtasn1-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 4.19.0-1.amzn2023.0.1
  - **AL2023.1.20230906 version:** 4.19.0-1.amzn2023.0.3

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 4.4.0-4.amzn2023.0.12
  - **AL2023.1.20230906 version:** 4.4.0-4.amzn2023.0.13

- ** `libxml2` **
  - **RPM:**  libxml2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libxml2  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 2.10.4-1.amzn2023.0.1
  - **AL2023.1.20230906 version:** 2.10.4-1.amzn2023.0.3

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 18.12.1-1.amzn2023.0.10
  - **AL2023.1.20230906 version:** 18.17.1-1.amzn2023.0.2

- ** `nss` **
  - **RPM:**  nspr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nspr-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-freebl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-freebl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-sysinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-util  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-util-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 4.35.0-5.amzn2023.0.2
  - **AL2023.1.20230906 version:** 4.35.0-5.amzn2023.0.3

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
  - **RPM:**  php8.2-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-xml  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 8.2.7-1.amzn2023.0.1
  - **AL2023.1.20230906 version:** 8.2.9-1.amzn2023.0.2

- ** `poppler` **
  - **RPM:**  poppler  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-cpp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib-doc  / **Architectures:** noarch
  - **RPM:**  poppler-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 22.08.0-3.amzn2023.0.1
  - **AL2023.1.20230906 version:** 22.08.0-3.amzn2023.0.3

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
  - **AL2023.1.20230825 version:** 15.0-1.amzn2023.0.3
  - **AL2023.1.20230906 version:** 15.0-1.amzn2023.0.4

- ** [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 3.11.2-2.amzn2023.0.7
  - **AL2023.1.20230906 version:** 3.11.2-2.amzn2023.0.10

- ** [`python3.9`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-unversioned-command  / **Architectures:** noarch
  - **AL2023.1.20230825 version:** 3.9.16-1.amzn2023.0.3
  - **AL2023.1.20230906 version:** 3.9.16-1.amzn2023.0.5

- ** `rsyslog` **
  - **RPM:**  rsyslog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-crypto  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-doc  / **Architectures:** noarch
  - **RPM:**  rsyslog-elasticsearch  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-logrotate  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-mmaudit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-mmfields  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-mmjsonparse  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-mmkubernetes  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-mmnormalize  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-openssl  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 8.2204.0-3.amzn2023.0.2
  - **AL2023.1.20230906 version:** 8.2204.0-3.amzn2023.0.4

- ** [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html) **
  - **RPM:**  cargo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clippy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-analysis  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-analyzer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-debugger-common  / **Architectures:** noarch
  - **RPM:**  rust-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rustfmt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-gdb  / **Architectures:** noarch
  - **RPM:**  rust-lldb  / **Architectures:** noarch
  - **RPM:**  rust-src  / **Architectures:** noarch
  - **RPM:**  rust-std-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-std-static-wasm32-unknown-unknown  / **Architectures:** noarch
  - **RPM:**  rust-std-static-wasm32-wasi  / **Architectures:** noarch
  - **AL2023.1.20230825 version:** 1.68.2-1.amzn2023.0.1
  - **AL2023.1.20230906 version:** 1.68.2-1.amzn2023.0.2

- ** `sudo` **
  - **RPM:**  sudo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-logsrvd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-python-plugin  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 1.9.13-1.p2.amzn2023.0.1
  - **AL2023.1.20230906 version:** 1.9.13-1.p2.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.1.20230825 version:** 2023.1.20230825-0.amzn2023
  - **AL2023.1.20230906 version:** 2023.1.20230906-0.amzn2023

- ** `update-motd` **
  - **RPM:**  update-motd
  - **Architectures:** noarch
  - **AL2023.1.20230825 version:** 2.1-1.amzn2023
  - **AL2023.1.20230906 version:** 2.1-1.amzn2023.0.1

- ** `userspace-rcu` **
  - **RPM:**  userspace-rcu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  userspace-rcu-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230825 version:** 0.12.1-3.amzn2023.0.2
  - **AL2023.1.20230906 version:** 0.12.1-3.amzn2023.0.4

## Docker container image
<a name="amis-2023.1.20230906.container-image"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.1.20230906-0.amzn2023` |
| `curl-minimal-8.2.1-1.amzn2023.0.2` |
| `file-libs-5.39-7.amzn2023.0.4` |
| `krb5-libs-1.21-3.amzn2023.0.3` |
| `libcurl-minimal-8.2.1-1.amzn2023.0.2` |
| `libidn2-2.3.2-1.amzn2023.0.4` |
| `libtasn1-4.19.0-1.amzn2023.0.3` |
| `libxml2-2.10.4-1.amzn2023.0.3` |
| `python3-libs-3.9.16-1.amzn2023.0.5` |
| `python3-3.9.16-1.amzn2023.0.5` |
| `system-release-2023.1.20230906-0.amzn2023` |

## Default AMI
<a name="amis-2023.1.20230906.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230906-0.amzn2023` |
| `amazon-ssm-agent-3.2.1377.0-1.amzn2023` |
| `bind-libs-32:9.16.42-1.amzn2023.0.3` |
| `bind-license-32:9.16.42-1.amzn2023.0.3` |
| `bind-utils-32:9.16.42-1.amzn2023.0.3` |
| `binutils-2.39-6.amzn2023.0.9` |
| `curl-minimal-8.2.1-1.amzn2023.0.2` |
| `file-libs-5.39-7.amzn2023.0.4` |
| `file-5.39-7.amzn2023.0.4` |
| `go-srpm-macros-3.2.0-37.amzn2023` |
| `kernel-livepatch-repo-s3-2023.1.20230906-0.amzn2023` |
| `kernel-tools-6.1.49-69.116.amzn2023` |
| `kernel-6.1.49-69.116.amzn2023` |
| `krb5-libs-1.21-3.amzn2023.0.3` |
| `libcurl-minimal-8.2.1-1.amzn2023.0.2` |
| `libidn2-2.3.2-1.amzn2023.0.4` |
| `libtasn1-4.19.0-1.amzn2023.0.3` |
| `libxml2-2.10.4-1.amzn2023.0.3` |
| `nspr-4.35.0-5.amzn2023.0.3` |
| `nss-softokn-freebl-3.90.0-3.amzn2023.0.3` |
| `nss-softokn-3.90.0-3.amzn2023.0.3` |
| `nss-sysinit-3.90.0-3.amzn2023.0.3` |
| `nss-util-3.90.0-3.amzn2023.0.3` |
| `nss-3.90.0-3.amzn2023.0.3` |
| `python3-libs-3.9.16-1.amzn2023.0.5` |
| `python3-3.9.16-1.amzn2023.0.5` |
| `sudo-1.9.13-1.p2.amzn2023.0.3` |
| `system-release-2023.1.20230906-0.amzn2023` |
| `update-motd-2.1-1.amzn2023.0.1` |
| `userspace-rcu-0.12.1-3.amzn2023.0.4` |

## Minimal AMI
<a name="amis-2023.1.20230906.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230906-0.amzn2023` |
| `curl-minimal-8.2.1-1.amzn2023.0.2file-libs-5.39-7.amzn2023.0.4` |
| `file-5.39-7.amzn2023.0.4` |
| `kernel-livepatch-repo-s3-2023.1.20230906-0.amzn2023` |
| `kernel-6.1.49-69.116.amzn2023` |
| `krb5-libs-1.21-3.amzn2023.0.3` |
| `libcurl-minimal-8.2.1-1.amzn2023.0.2` |
| `libidn2-2.3.2-1.amzn2023.0.4` |
| `libtasn1-4.19.0-1.amzn2023.0.3` |
| `libxml2-2.10.4-1.amzn2023.0.3` |
| `python3-libs-3.9.16-1.amzn2023.0.5` |
| `python3-3.9.16-1.amzn2023.0.5` |
| `sudo-1.9.13-1.p2.amzn2023.0.3` |
| `system-release-2023.1.20230906-0` |
| `update-motd-2.1-1.amzn2023.0.1` |
| `userspace-rcu-0.12.1-3.amzn2023.0.4` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
