---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230607.html
---

# Amazon Linux 2023 version 2023.0.20230607 release notes
<a name="relnotes-2023.0.20230607"></a>

This topic includes release notes for the 2023.0.20230607 version of AL2023.

## Major updates
<a name="major-updates-20230607"></a>

This release represents an update to the General Availability (GA) release of Amazon Linux 2023 (AL2023). AL2023 is the next generation of Amazon Linux. It comes with 5 years of support and brings features like Deterministic Updates, better optimizations for Graviton processors and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

See the [Amazon Linux What's New Post](https://aws.amazon.com/about-aws/whats-new/2023/03/amazon-linux-2023/) for more information about AL2023.

AL2023 includes the following major updates.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**New packages**
+ `libecap`
+ `squid`

**Known Issues**
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, refer to [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-20230607)
+ [Repository](#amis-2023.0.20230607.repository)
+ [Docker container image](#amis-2023020230607.container-image)
+ [Default AMI](#amis-2023020230607.default-ami)
+ [Minimal AMI](#amis-2023020230607.minimal-ami)

## Repository
<a name="amis-2023.0.20230607.repository"></a>

### New packages in AL2023.0.20230607 since AL2023.0.20230517
<a name="new-AL2023.0.20230517-AL2023.0.20230607"></a>

 Comparing AL2023.0.20230517 version 2023.0.20230517 to AL2023.0.20230607 version [2023.0.20230607](#relnotes-2023.0.20230607).

| Package Type | Number of new packages in AL2023.0.20230607 compared to AL2023.0.20230517 |
| --- | --- |
| Source RPMs | 2 |
| Total Binary RPMs | 12 |
|  x86\_64 binary RPMs | 6 |
|  aarch64 binary RPMs | 6 |

New packages in AL2023.0.20230607:

- ** `libecap` **
  - **RPM:**  libecap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libecap-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.1-10.amzn2023

- ** `samba` **
  - **RPM:**  python3-samba-dc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 4.17.8-0.amzn2023.0.2

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **Version:** 5.8-1.amzn2023

- ** `vim` **
  - **RPM:**  xxd
  - **Architectures:** aarch64, x86\_64
  - **Version:** 9.0.1592-1.amzn2023.0.1

### AL2023.0.20230607 upgrades from AL2023.0.20230517
<a name="vercmp-AL2023.0.20230517-AL2023.0.20230607"></a>

 Comparing [2023.0.20230517](relnotes-2023.0.20230517.md) to [2023.0.20230607](#relnotes-2023.0.20230607).

| Package Type | Count |
| --- | --- |
| Source | 25 |
| Total Binary | 265 |
|  noarch binary RPMs | 84 |
|  x86\_64 binary RPMs | 91 |
|  aarch64 binary RPMs | 90 |

The full comparison of RPM package versions is below.

- ** `byacc` **
  - **RPM:**  byacc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 2.0.20210109-2.amzn2023.0.2
  - **AL2023.0.20230607 version:** 2.0.20210109-2.amzn2023.0.3

- ** `c-ares` **
  - **RPM:**  c-ares  / **Architectures:** aarch64, x86\_64
  - **RPM:**  c-ares-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 1.17.2-1.amzn2023.0.2
  - **AL2023.0.20230607 version:** 1.19.0-1.amzn2023

- ** `cloud-init` **
  - **RPM:**  cloud-init
  - **Architectures:** noarch
  - **AL2023.0.20230517 version:** 22.2.2-1.amzn2023.1.7
  - **AL2023.0.20230607 version:** 22.2.2-1.amzn2023.1.8

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 1.1.0-6.amzn2023.0.2
  - **AL2023.0.20230607 version:** 1.2.0-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcurl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 7.88.1-1.amzn2023.0.1
  - **AL2023.0.20230607 version:** 8.0.1-1.amzn2023

- ** `dnsmasq` **
  - **RPM:**  dnsmasq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dnsmasq-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 2.86-10.amzn2023.0.2
  - **AL2023.0.20230607 version:** 2.86-10.amzn2023.0.3

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 1.71.0-1.amzn2023
  - **AL2023.0.20230607 version:** 1.71.2-1.amzn2023

- ** `freetype` **
  - **RPM:**  freetype  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freetype-demos  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freetype-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 2.12.1-3.amzn2023.0.1
  - **AL2023.0.20230607 version:** 2.13.0-2.amzn2023.0.1

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
  - **AL2023.0.20230517 version:** 6.1.27-43.48.amzn2023
  - **AL2023.0.20230607 version:** 6.1.29-47.49.amzn2023

- ** `libcap` **
  - **RPM:**  libcap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 2.48-2.amzn2023.0.2
  - **AL2023.0.20230607 version:** 2.48-2.amzn2023.0.3

- ** `libfastjson` **
  - **RPM:**  libfastjson  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfastjson-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 0.99.9-1.amzn2023.0.2
  - **AL2023.0.20230607 version:** 0.99.9-1.amzn2023.0.3

- ** `libldb` **
  - **RPM:**  ldb-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libldb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libldb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-ldb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-ldb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-ldb-devel-common  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 2.6.1-1.amzn2023.0.2
  - **AL2023.0.20230607 version:** 2.6.2-1.amzn2023.0.2

- ** `libssh` **
  - **RPM:**  libssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libssh-config  / **Architectures:** noarch
  - **RPM:**  libssh-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 0.10.4-3.amzn2023.0.3
  - **AL2023.0.20230607 version:** 0.10.5-1.amzn2023.0.1

- ** `libwebp` **
  - **RPM:**  libwebp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwebp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwebp-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwebp-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 1.2.4-1.amzn2023.0.3
  - **AL2023.0.20230607 version:** 1.2.4-1.amzn2023.0.4

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2023.0.20230517 version:** 2.1-53.amzn2023
  - **AL2023.0.20230607 version:** 2.1-53.amzn2023.0.1

- ** `nginx` **
  - **RPM:**  nginx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-all-modules  / **Architectures:** noarch
  - **RPM:**  nginx-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-filesystem  / **Architectures:** noarch
  - **RPM:**  nginx-mod-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-image-filter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-xslt-filter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-mail  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-stream  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 1.22.1-1.amzn2023.0.3
  - **AL2023.0.20230607 version:** 1.24.0-1.amzn2023.0.1

- ** `perl-CPAN` **
  - **RPM:**  perl-CPAN  / **Architectures:** noarch
  - **RPM:**  perl-CPAN-tests  / **Architectures:** noarch
  - **AL2023.0.20230517 version:** 2.34-1.amzn2023.0.2
  - **AL2023.0.20230607 version:** 2.34-1.amzn2023.0.3

- ** `python-flask` **
  - **RPM:**  python3-flask  / **Architectures:** noarch
  - **RPM:**  python-flask-doc  / **Architectures:** noarch
  - **AL2023.0.20230517 version:** 1.1.2-5.amzn2023.0.2
  - **AL2023.0.20230607 version:** 1.1.2-5.amzn2023.0.3

- ** `samba` **
  - **RPM:**  libnetapi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnetapi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmbclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmbclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwbclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwbclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-samba  / **Architectures:** aarch64, x86\_64
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
  - **RPM:**  samba-usershares  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-vfs-iouring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-krb5-locator  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-modules  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 4.17.5-0.amzn2023.0.2
  - **AL2023.0.20230607 version:** 4.17.8-0.amzn2023.0.2

- ** `snakeyaml` **
  - **RPM:**  snakeyaml  / **Architectures:** noarch
  - **RPM:**  snakeyaml-javadoc  / **Architectures:** noarch
  - **AL2023.0.20230517 version:** 1.27-6.amzn2023.0.1
  - **AL2023.0.20230607 version:** 1.27-6.amzn2023.0.2

- ** `sysstat` **
  - **RPM:**  sysstat
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 12.5.6-1.amzn2023.0.2
  - **AL2023.0.20230607 version:** 12.5.6-1.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.0.20230517 version:** 2023.0.20230517-0.amzn2023
  - **AL2023.0.20230607 version:** 2023.0.20230607-0.amzn2023

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 9.0.1403-1.amzn2023.0.1
  - **AL2023.0.20230607 version:** 9.0.1592-1.amzn2023.0.1

- ** `wayland` **
  - **RPM:**  libwayland-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-cursor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-egl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wayland-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wayland-doc  / **Architectures:** noarch
  - **AL2023.0.20230517 version:** 1.19.0-1.amzn2023.0.2
  - **AL2023.0.20230607 version:** 1.22.0-1.amzn2023.0.1

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230517 version:** 4.0.4-1.amzn2023.0.1
  - **AL2023.0.20230607 version:** 4.0.6-1.amzn2023.0.1

## Docker container image
<a name="amis-2023020230607.container-image"></a>

The following packages have been **updated**.
+ `amazon-linux-repo-cdn-2023.0.20230607-0`
+ `curl-minimal-8.0.1-1.amzn2023`
+ `libcap-2.48-2.amzn2023.0.3`
+ `libcurl-minimal-8.0.1-1.amzn2023`
+ `system-release-2023.0.20230607-0`

## Default AMI
<a name="amis-2023020230607.default-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230607-0.amzn2023` |
| `c-ares-1.19.0-1.amzn2023` |
| `cloud-init-22.2.2-1.amzn2023.1.8` |
| `curl-minimal-8.0.1-1.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230607-0` |
| `kernel-tools-6.1.29-47.49.amzn2023` |
| `kernel-6.1.29-47.49.amzn2023` |
| `libcap-2.48-2.amzn2023.0.3` |
| `libcurl-minimal-8.0.1-1.amzn2023` |
| `libldb-2.6.2-1.amzn2023.0.2` |
| `sysstat-12.5.6-1.amzn2023.0.3` |
| `system-release-2023.0.20230607-0` |
| `vim-common-2:9.0.1592-1.amzn2023.0.1` |
| `vim-data-2:9.0.1592-1.amzn2023.0.1` |
| `vim-enhanced-2:9.0.1592-1.amzn2023.0.1` |
| `vim-filesystem-2:9.0.1592-1.amzn2023.0.1` |
| `vim-minimal-2:9.0.1592-1.amzn2023.0.1` |
| `xxd-2:9.0.1592-1.amzn2023.0.1` |
| `microcode_ctl-2:2.1-53.amzn2023.0.1.x86_64` |

## Minimal AMI
<a name="amis-2023020230607.minimal-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230607-0.amzn2023` |
| `cloud-init-22.2.2-1.amzn2023.1.8` |
| `curl-minimal-8.0.1-1.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230607-0.amzn2023` |
| `kernel-6.1.29-47.49.amzn2023` |
| `libcap-2.48-2.amzn2023.0.3` |
| `libcurl-minimal-8.0.1-1.amzn2023` |
| `system-release-2023.0.20230607-0` |
| `vim-data-2:9.0.1592-1.amzn2023.0.1` |
| `vim-minimal-2:9.0.1592-1.amzn2023` |
| `microcode_ctl-2:2.1-53.amzn2023.0.1.x86_64` |
