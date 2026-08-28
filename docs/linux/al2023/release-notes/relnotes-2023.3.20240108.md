---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.3.20240108.html
---

# Amazon Linux 2023 version 2023.3.20240108 release notes
<a name="relnotes-2023.3.20240108"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.3.20240108 release.

## Major updates
<a name="major-updates-2023.3.20240108"></a>

This release represents an update to the [third quarterly release](https://aws.amazon.com/about-aws/whats-new/2023/12/amazon-linux-kvm-vmware-images-al2023-3/) of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.3.20240108)
+ [Repository](#amis-2023.3.20240108.repository)
+ [Docker container image](#amis-2023.3.20240108.container-image)
+ [Default AMI](#amis-2023.3.20240108.default-ami)
+ [Minimal AMI](#amis-2023.3.20240108.minimal-ami)
+ [Minimal container image](#amis-2023.3.20240108.minimal-container-ami)

## Repository
<a name="amis-2023.3.20240108.repository"></a>

### New packages in AL2023.3.20240108 since AL2023.3.20231218
<a name="new-AL2023.3.20231218-AL2023.3.20240108"></a>

 Comparing AL2023.3.20231218 version 2023.3.20231218 to AL2023.3.20240108 version [2023.3.20240108](#relnotes-2023.3.20240108).

| Package Type | Number of new packages in AL2023.3.20240108 compared to AL2023.3.20231218 |
| --- | --- |
| Source RPMs | 0 |
| Total Binary RPMs | 2 |
|  x86\_64 binary RPMs | 1 |
|  aarch64 binary RPMs | 1 |

New packages in AL2023.3.20240108:

- ** `kernel` **
  - **RPM:**  kernel-modules-extra-common
  - **Architectures:** aarch64, x86\_64
  - **Version:** 6.1.66-93.164.amzn2023

### AL2023.3.20240108 upgrades from AL2023.3.20231218
<a name="vercmp-AL2023.3.20231218-AL2023.3.20240108"></a>

 Comparing [2023.3.20231218](relnotes-2023.3.20231218.md) to [2023.3.20240108](#relnotes-2023.3.20240108).

| Package Type | Count |
| --- | --- |
| Source | 23 |
| Total Binary | 316 |
|  noarch binary RPMs | 152 |
|  x86\_64 binary RPMs | 82 |
|  aarch64 binary RPMs | 82 |

The full comparison of RPM package versions is below.

- ** [`amazon-linux-sb-keys`](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html) **
  - **RPM:**  [`amazon-linux-sb-keys`](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html)
  - **Architectures:** noarch
  - **AL2023.3.20231218 version:** 2023.1-1.amzn2023.0.4
  - **AL2023.3.20240108 version:** 2023.1-1.amzn2023.0.5

- ** `ansible-core` **
  - **RPM:**  ansible-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ansible-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 2.15.3-1.amzn2023.0.1
  - **AL2023.3.20240108 version:** 2.15.3-1.amzn2023.0.2

- ** `bluez` **
  - **RPM:**  bluez  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-deprecated  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-hid2hci  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-libs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-mesh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-obexd  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 5.62-2.amzn2023.0.4
  - **AL2023.3.20240108 version:** 5.62-2.amzn2023.0.5

- ** `bouncycastle` **
  - **RPM:**  bouncycastle  / **Architectures:** noarch
  - **RPM:**  bouncycastle-javadoc  / **Architectures:** noarch
  - **RPM:**  bouncycastle-mail  / **Architectures:** noarch
  - **RPM:**  bouncycastle-pg  / **Architectures:** noarch
  - **RPM:**  bouncycastle-pkix  / **Architectures:** noarch
  - **RPM:**  bouncycastle-tls  / **Architectures:** noarch
  - **RPM:**  bouncycastle-util  / **Architectures:** noarch
  - **AL2023.3.20231218 version:** 1.70-4.amzn2023.0.3
  - **AL2023.3.20240108 version:** 1.70-4.amzn2023.0.4

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 1.3.3-0.amzn2023
  - **AL2023.3.20240108 version:** 1.3.4-0.amzn2023

- ** [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal) **
  - **RPM:**  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcurl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 8.3.0-1.amzn2023.0.2
  - **AL2023.3.20240108 version:** 8.5.0-1.amzn2023.0.1

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 1.79.1-1.amzn2023
  - **AL2023.3.20240108 version:** 1.79.2-1.amzn2023

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
  - **AL2023.3.20231218 version:** 9.56.1-7.amzn2023.0.4
  - **AL2023.3.20240108 version:** 9.56.1-7.amzn2023.0.5

- ** `gnutls` **
  - **RPM:**  gnutls  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-dane  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 3.8.0-376.amzn2023.0.2
  - **AL2023.3.20240108 version:** 3.8.0-377.amzn2023.0.3

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.3.20231218 version:** 1.20.10-1.amzn2023.0.1
  - **AL2023.3.20240108 version:** 1.20.12-1.amzn2023.0.1

- ** `grpc` **
  - **RPM:**  grpc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-data  / **Architectures:** noarch
  - **RPM:**  grpc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-doc  / **Architectures:** noarch
  - **RPM:**  grpc-plugins  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 1.56.2-10.amzn2023
  - **AL2023.3.20240108 version:** 1.60.0-10.amzn2023

- ** `iperf3` **
  - **RPM:**  iperf3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iperf3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 3.11-1.amzn2023.0.4
  - **AL2023.3.20240108 version:** 3.16-1.amzn2023

- ** `jtidy` **
  - **RPM:**  jtidy  / **Architectures:** noarch
  - **RPM:**  jtidy-javadoc  / **Architectures:** noarch
  - **AL2023.3.20231218 version:** 1.0-0.38.20100930svn1125.amzn2023.0.1
  - **AL2023.3.20240108 version:** 1.0-0.38.20100930svn1125.amzn2023.0.2

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 6.1.66-91.160.amzn2023
  - **AL2023.3.20240108 version:** 6.1.66-93.164.amzn2023

- ** `libssh` **
  - **RPM:**  libssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libssh-config  / **Architectures:** noarch
  - **RPM:**  libssh-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 0.10.5-1.amzn2023.0.2
  - **AL2023.3.20240108 version:** 0.10.6-1.amzn2023.0.1

- ** `ncurses` **
  - **RPM:**  ncurses  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-base  / **Architectures:** noarch
  - **RPM:**  ncurses-c\+\+-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-compat-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-term  / **Architectures:** noarch
  - **AL2023.3.20231218 version:** 6.2-4.20200222.amzn2023.0.4
  - **AL2023.3.20240108 version:** 6.2-4.20200222.amzn2023.0.5

- ** `p7zip` **
  - **RPM:**  p7zip  / **Architectures:** aarch64, x86\_64
  - **RPM:**  p7zip-doc  / **Architectures:** noarch
  - **RPM:**  p7zip-plugins  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 16.02-20.amzn2023.0.4
  - **AL2023.3.20240108 version:** 16.02-20.amzn2023.0.5

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
  - **AL2023.3.20231218 version:** 15.4-1.amzn2023.0.1
  - **AL2023.3.20240108 version:** 15.5-1.amzn2023.0.1

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 5.8-1.amzn2023.0.3
  - **AL2023.3.20240108 version:** 5.8-1.amzn2023.0.4

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.3.20231218 version:** 2023.3.20231218-0.amzn2023
  - **AL2023.3.20240108 version:** 2023.3.20240108-0.amzn2023

- ** `tar` **
  - **RPM:**  tar
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 1.34-1.amzn2023.0.3
  - **AL2023.3.20240108 version:** 1.34-1.amzn2023.0.4

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.3.20231218 version:** 9.0.82-1.amzn2023.0.1
  - **AL2023.3.20240108 version:** 9.0.82-1.amzn2023.0.2

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xxd  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20231218 version:** 9.0.2120-1.amzn2023
  - **AL2023.3.20240108 version:** 9.0.2153-1.amzn2023

## Docker container image
<a name="amis-2023.3.20240108.container-image"></a>
+ `amazon-linux-repo-cdn-2023.3.20240108-0.amzn2023.noarch`
+ `curl-minimal-8.5.0-1.amzn2023.0.1.x86_64`
+ `libcurl-minimal-8.5.0-1.amzn2023.0.1.x86_64`
+ `ncurses-base-6.2-4.20200222.amzn2023.0.5.noarch`
+ `ncurses-libs-6.2-4.20200222.amzn2023.0.5.x86_64`
+ `system-release-2023.3.20240108-0.amzn2023.noarch`

## Default AMI
<a name="amis-2023.3.20240108.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20240108-0.amzn2023.noarch` |
| `amazon-linux-sb-keys-2023.1-1.amzn2023.0.5.noarch` |
| `curl-minimal-8.5.0-1.amzn2023.0.1.x86_64` |
| `dnf-utils-4.1.0-1.amzn2023.0.3.noarch` |
| `gnutls-3.8.0-377.amzn2023.0.3.x86_64` |
| `kernel-livepatch-repo-s3-2023.3.20240108-0.amzn2023.noarch` |
| `kernel-tools-6.1.66-93.164.amzn2023.x86_64` |
| `kernel-6.1.66-93.164.amzn2023.x86_64` |
| `libcurl-minimal-8.5.0-1.amzn2023.0.1.x86_64` |
| `ncurses-base-6.2-4.20200222.amzn2023.0.5.noarch` |
| `ncurses-libs-6.2-4.20200222.amzn2023.0.5.x86_64` |
| `ncurses-6.2-4.20200222.amzn2023.0.5.x86_64` |
| `system-release-2023.3.20240108-0.amzn2023.noarch` |
| `tar-2:1.34-1.amzn2023.0.4.x86_64` |
| `vim-common-2:9.0.2153-1.amzn2023.x86_64` |
| `vim-data-2:9.0.2153-1.amzn2023.noarch` |
| `vim-enhanced-2:9.0.2153-1.amzn2023.x86_64` |
| `vim-filesystem-2:9.0.2153-1.amzn2023.noarch` |
| `vim-minimal-2:9.0.2153-1.amzn2023.x86_64` |
| `xxd-2:9.0.2153-1.amzn2023.x86_64` |

## Minimal AMI
<a name="amis-2023.3.20240108.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20240108-0.amzn2023.noarch` |
| `amazon-linux-sb-keys-2023.1-1.amzn2023.0.5.noarch` |
| `curl-minimal-8.5.0-1.amzn2023.0.1.x86_64` |
| `gnutls-3.8.0-377.amzn2023.0.3.x86_64` |
| `kernel-livepatch-repo-s3-2023.3.20240108-0.amzn2023.noarch` |
| `kernel-6.1.66-93.164.amzn2023.x86_64` |
| `libcurl-minimal-8.5.0-1.amzn2023.0.1.x86_64` |
| `ncurses-base-6.2-4.20200222.amzn2023.0.5.noarch` |
| `ncurses-libs-6.2-4.20200222.amzn2023.0.5.x86_64` |
| `ncurses-6.2-4.20200222.amzn2023.0.5.x86_64` |
| `system-release-2023.3.20240108-0.amzn2023.noarch` |
| `tar-2:1.34-1.amzn2023.0.4.x86_64` |
| `vim-data-2:9.0.2153-1.amzn2023.noarch` |
| `vim-minimal-2:9.0.2153-1.amzn2023.x86_64` |

## Minimal container image
<a name="amis-2023.3.20240108.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.3.20240108-0.amzn2023.noarch`
+ `curl-minimal-8.5.0-1.amzn2023.0.1.x86_64`
+ `libcurl-minimal-8.5.0-1.amzn2023.0.1.x86_64`
+ `ncurses-base-6.2-4.20200222.amzn2023.0.5.noarch`
+ `ncurses-libs-6.2-4.20200222.amzn2023.0.5.x86_64`
+ `system-release-2023.3.20240108-0.amzn2023.noarch`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
