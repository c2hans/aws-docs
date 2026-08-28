---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230823.html
---

# Amazon Linux 2023 version 2023.1.20230823 release notes
<a name="relnotes-2023.1.20230823"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.1.20230823 release

## Major updates
<a name="major-updates-2023.1.20230823"></a>

**Note**
The AMIs for this release were withdrawn shortly after release due to a bug that was found when launching an instance without `user-data`. This issue doesn't affect containers. A new release without this issue will be available soon.

This release represents an update to AL2023.1. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

For information about UEFI Secure Boot on AL2023, see [Amazon Linux announces support for secure boot with AL2023](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/).

AL2023 includes the following major updates.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ The AMIs for this release were withdrawn shortly after release due to a bug that was found when launching an instance without `user-data`. This issue doesn't affect containers. A new release without this issue will be available soon.
+ Kernel Live Patches will fail to apply on a system where UEFI Secure Boot is enabled. This will be fixed on an upcoming release.
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information about the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.1.20230823)
+ [Repository](#amis-2023.1.20230823.repository)
+ [Docker container image](#amis-2023.1.20230823.container-image)
+ [Default AMI](#amis-2023.1.20230823.default-ami)
+ [Minimal AMI](#amis-2023.1.20230823.minimal-ami)

## Repository
<a name="amis-2023.1.20230823.repository"></a>

### AL2023.1.20230823 upgrades from AL2023.1.20230809
<a name="vercmp-AL2023.1.20230809-AL2023.1.20230823"></a>

 Comparing [2023.1.20230809](relnotes-2023.1.20230809.md) to [2023.1.20230823](#relnotes-2023.1.20230823).

| Package Type | Count |
| --- | --- |
| Source | 30 |
| Total Binary | 404 |
|  noarch binary RPMs | 128 |
|  x86\_64 binary RPMs | 138 |
|  aarch64 binary RPMs | 138 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 1.300025.0-1.amzn2023
  - **AL2023.1.20230823 version:** 1.300026.2-1.amzn2023

- ** [`amazon-linux-onprem`](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html) **
  - **RPM:**  [`amazon-linux-onprem`](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html)  / **Architectures:** noarch
  - **RPM:**  [`amazon-onprem-network`](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html)  / **Architectures:** noarch
  - **AL2023.1.20230809 version:** 1.0-0.amzn2023
  - **AL2023.1.20230823 version:** 1.1-0.amzn2023

- ** `ca-certificates` **
  - **RPM:**  ca-certificates
  - **Architectures:** noarch
  - **AL2023.1.20230809 version:** 2023.2.60-1.0.amzn2023.0.2
  - **AL2023.1.20230823 version:** 2023.2.60-1.0.amzn2023.0.3

- ** `cairo` **
  - **RPM:**  cairo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-gobject  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-gobject-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 1.17.4-3.amzn2023.0.2
  - **AL2023.1.20230823 version:** 1.17.6-2.amzn2023.0.1

- ** `cairomm` **
  - **RPM:**  cairomm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairomm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairomm-doc  / **Architectures:** noarch
  - **AL2023.1.20230809 version:** 1.14.2-116.amzn2023.0.2
  - **AL2023.1.20230823 version:** 1.14.4-126.amzn2023.0.1

- ** `cloud-init` **
  - **RPM:**  cloud-init
  - **Architectures:** noarch
  - **AL2023.1.20230809 version:** 22.2.2-1.amzn2023.1.8
  - **AL2023.1.20230823 version:** 22.2.2-1.amzn2023.1.10

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 1.7.2-1.amzn2023.0.1
  - **AL2023.1.20230823 version:** 1.7.2-1.amzn2023.0.3

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
  - **AL2023.1.20230809 version:** 6.0.18-1.amzn2023.0.1
  - **AL2023.1.20230823 version:** 6.0.20-1.amzn2023.0.1

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 1.74.1-1.amzn2023
  - **AL2023.1.20230823 version:** 1.75.0-1.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** v1.25.4.0-1.amzn2023
  - **AL2023.1.20230823 version:** v1.26.4.0-1.amzn2023

- ** `gawk` **
  - **RPM:**  gawk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gawk-all-langpacks  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gawk-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gawk-doc  / **Architectures:** noarch
  - **AL2023.1.20230809 version:** 5.1.0-3.amzn2023.0.2
  - **AL2023.1.20230823 version:** 5.1.0-3.amzn2023.0.3

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
  - **AL2023.1.20230809 version:** 9.56.1-7.amzn2023.0.2
  - **AL2023.1.20230823 version:** 9.56.1-7.amzn2023.0.3

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.1.20230809 version:** 1.20.6-1.amzn2023.0.1
  - **AL2023.1.20230823 version:** 1.20.7-1.amzn2023.0.1

- ** `guava` **
  - **RPM:**  guava  / **Architectures:** noarch
  - **RPM:**  guava-javadoc  / **Architectures:** noarch
  - **RPM:**  guava-testlib  / **Architectures:** noarch
  - **AL2023.1.20230809 version:** 31.0.1-3.amzn2023.0.4
  - **AL2023.1.20230823 version:** 31.0.1-3.amzn2023.0.5

- ** `haproxy` **
  - **RPM:**  haproxy
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 2.8.0-1.amzn2023.0.1
  - **AL2023.1.20230823 version:** 2.8.0-1.amzn2023.0.2

- ** `ImageMagick` **
  - **RPM:**  ImageMagick  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 6.9.12.82-1.amzn2023.0.3
  - **AL2023.1.20230823 version:** 6.9.12.82-1.amzn2023.0.4

- ** `jsoup` **
  - **RPM:**  jsoup  / **Architectures:** noarch
  - **RPM:**  jsoup-javadoc  / **Architectures:** noarch
  - **AL2023.1.20230809 version:** 1.13.1-9.amzn2023.0.4
  - **AL2023.1.20230823 version:** 1.13.1-9.amzn2023.0.5

- ** `libqb` **
  - **RPM:**  doxygen2man  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libqb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libqb-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 2.0.6-1.amzn2023
  - **AL2023.1.20230823 version:** 2.0.6-1.amzn2023.0.1

- ** `librsvg2` **
  - **RPM:**  librsvg2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 2.50.7-1.amzn2023.0.2
  - **AL2023.1.20230823 version:** 2.50.7-1.amzn2023.0.3

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 4.4.0-4.amzn2023.0.10
  - **AL2023.1.20230823 version:** 4.4.0-4.amzn2023.0.12

- ** `lynis` **
  - **RPM:**  lynis
  - **Architectures:** noarch
  - **AL2023.1.20230809 version:** 3.0.8-3.amzn2023
  - **AL2023.1.20230823 version:** 3.0.8-3.amzn2023.0.1

- ** `nerdctl` **
  - **RPM:**  nerdctl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 1.1.0-1.amzn2023.0.1
  - **AL2023.1.20230823 version:** 1.1.0-1.amzn2023.0.3

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 18.12.1-1.amzn2023.0.9
  - **AL2023.1.20230823 version:** 18.12.1-1.amzn2023.0.10

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
  - **AL2023.1.20230809 version:** 4.35.0-4.amzn2023.0.2
  - **AL2023.1.20230823 version:** 4.35.0-5.amzn2023.0.2

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 3.0.8-1.amzn2023.0.3
  - **AL2023.1.20230823 version:** 3.0.8-1.amzn2023.0.4

- ** [`php8.1`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.1`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-xml  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 8.1.21-1.amzn2023.0.1
  - **AL2023.1.20230823 version:** 8.1.22-1.amzn2023.0.1

- ** `runc` **
  - **RPM:**  runc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 1.1.7-1.amzn2023.0.1
  - **AL2023.1.20230823 version:** 1.1.7-1.amzn2023.0.2

- ** `samba` **
  - **RPM:**  libnetapi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnetapi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmbclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmbclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwbclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwbclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-samba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-samba-dc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-samba-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-samba-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-client-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-common  / **Architectures:** noarch
  - **RPM:**  samba-common-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-common-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-dcerpc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-dc-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-krb5-printing  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-ldb-ldap-modules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-pidl  / **Architectures:** noarch
  - **RPM:**  samba-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-test-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-usershares  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-vfs-iouring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-krb5-locator  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-modules  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230809 version:** 4.17.8-0.amzn2023.0.2
  - **AL2023.1.20230823 version:** 4.17.10-0.amzn2023.0.1

- ** `selinux-policy` **
  - **RPM:**  selinux-policy  / **Architectures:** noarch
  - **RPM:**  selinux-policy-devel  / **Architectures:** noarch
  - **RPM:**  selinux-policy-doc  / **Architectures:** noarch
  - **RPM:**  selinux-policy-minimum  / **Architectures:** noarch
  - **RPM:**  selinux-policy-mls  / **Architectures:** noarch
  - **RPM:**  selinux-policy-sandbox  / **Architectures:** noarch
  - **RPM:**  selinux-policy-targeted  / **Architectures:** noarch
  - **AL2023.1.20230809 version:** 36.16-1.amzn2023.0.3
  - **AL2023.1.20230823 version:** 36.18-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.1.20230809 version:** 2023.1.20230809-0.amzn2023
  - **AL2023.1.20230823 version:** 2023.1.20230823-0.amzn2023

## Docker container image
<a name="amis-2023.1.20230823.container-image"></a>
+ `amazon-linux-repo-cdn-2023.1.20230823-0.amzn2023`
+ `ca-certificates-2023.2.60-1.0.amzn2023.0.3`
+ `gawk-5.1.0-3.amzn2023.0.3`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.4`
+ `system-release-2023.1.20230823-0.amzn2023`

## Default AMI
<a name="amis-2023.1.20230823.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230823-0.amzn2023` |
| `ca-certificates-2023.2.60-1.0.amzn2023.0.3` |
| `cloud-init-22.2.2-1.amzn2023.1.10` |
| `gawk-5.1.0-3.amzn2023.0.3` |
| `kernel-livepatch-repo-s3-2023.1.20230823-0.amzn2023` |
| `nspr-4.35.0-5.amzn2023.0.2` |
| `nss-softokn-freebl-3.90.0-3.amzn2023.0.2` |
| `nss-softokn-3.90.0-3.amzn2023.0.2` |
| `nss-sysinit-3.90.0-3.amzn2023.0.2` |
| `nss-util-3.90.0-3.amzn2023.0.2` |
| `nss-3.90.0-3.amzn2023.0.2` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.4` |
| `openssl-1:3.0.8-1.amzn2023.0.4` |
| `selinux-policy-targeted-36.18-1.amzn2023.0.1` |
| `selinux-policy-36.18-1.amzn2023.0.1` |
| `system-release-2023.1.20230823-0.amzn2023` |

## Minimal AMI
<a name="amis-2023.1.20230823.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.1.20230823-0.amzn2023`
+ `ca-certificates-2023.2.60-1.0.amzn2023.0.3`
+ `cloud-init-22.2.2-1.amzn2023.1.10`
+ `gawk-5.1.0-3.amzn2023.0.3`
+ `kernel-livepatch-repo-s3-2023.1.20230823-0.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.4`
+ `openssl-1:3.0.8-1.amzn2023.0.4`
+ `selinux-policy-targeted-36.18-1.amzn2023.0.1`
+ `selinux-policy-36.18-1.amzn2023.0.1`
+ `system-release-2023.1.20230823-0.amzn2023`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
