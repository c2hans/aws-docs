---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.3.20240122.html
---

# Amazon Linux 2023 version 2023.3.20240122 release notes
<a name="relnotes-2023.3.20240122"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.3.20240122 release

## Major updates
<a name="major-updates-2023.3.20240122"></a>

This release represents an update to the [third quarterly release](https://aws.amazon.com/about-aws/whats-new/2023/12/amazon-linux-kvm-vmware-images-al2023-3/) of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.3.20240122)
+ [Repository](#amis-2023.3.20240122.repository)
+ [Docker container image](#amis-2023.3.20240122.container-image)
+ [Default AMI](#amis-2023.3.20240122.default-ami)
+ [Minimal AMI](#amis-2023.3.20240122.minimal-ami)
+ [Minimal container image](#amis-2023.3.20240122.minimal-container-ami)

## Repository
<a name="amis-2023.3.20240122.repository"></a>

### AL2023.3.20240122 upgrades from AL2023.3.20240117
<a name="vercmp-AL2023.3.20240117-AL2023.3.20240122"></a>

 Comparing [2023.3.20240117](relnotes-2023.3.20240117.md) to [2023.3.20240122](#relnotes-2023.3.20240122).

| Package Type | Count |
| --- | --- |
| Source | 17 |
| Total Binary | 210 |
|  noarch binary RPMs | 56 |
|  x86\_64 binary RPMs | 77 |
|  aarch64 binary RPMs | 77 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 1.300028.1-1.amzn2023
  - **AL2023.3.20240122 version:** 1.300032.3-1.amzn2023

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 1.7.2-1.amzn2023.0.4
  - **AL2023.3.20240122 version:** 1.7.11-1.amzn2023.0.1

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 1.3.4-0.amzn2023
  - **AL2023.3.20240122 version:** 1.3.5-0.amzn2023

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
  - **AL2023.3.20240117 version:** 6.0.25-1.amzn2023.0.1
  - **AL2023.3.20240122 version:** 6.0.26-1.amzn2023.0.1

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 1.79.2-1.amzn2023
  - **AL2023.3.20240122 version:** 1.80.0-1.amzn2023

- ** [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-1.8.0-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 1.8.0\_402.b06-1.amzn2023
  - **AL2023.3.20240122 version:** 1.8.0\_402.b08-1.amzn2023

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
  - **AL2023.3.20240117 version:** 6.1.66-93.164.amzn2023
  - **AL2023.3.20240122 version:** 6.1.72-96.166.amzn2023

- ** `keyutils` **
  - **RPM:**  keyutils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  keyutils-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  keyutils-libs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 1.6.3-1.amzn2023
  - **AL2023.3.20240122 version:** 1.6.3-1.amzn2023.0.1

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
  - **AL2023.3.20240117 version:** 4.35.0-5.amzn2023.0.3
  - **AL2023.3.20240122 version:** 4.35.0-5.amzn2023.0.4

- ** `perl-Spreadsheet-ParseExcel` **
  - **RPM:**  perl-Spreadsheet-ParseExcel
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 0.6500-28.amzn2023.0.2
  - **AL2023.3.20240122 version:** 0.6500-28.amzn2023.0.3

- ** `postfix` **
  - **RPM:**  postfix  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postfix-cdb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postfix-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postfix-lmdb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postfix-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postfix-pcre  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postfix-perl-scripts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postfix-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postfix-sqlite  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 3.7.2-4.amzn2023.0.4
  - **AL2023.3.20240122 version:** 3.7.2-4.amzn2023.0.5

- ** `python-pycryptodomex` **
  - **RPM:**  python3-pycryptodomex  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pycryptodomex-selftest  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 3.11.0-1.amzn2023.0.2
  - **AL2023.3.20240122 version:** 3.11.0-1.amzn2023.0.3

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
  - **AL2023.3.20240117 version:** 1.68.2-1.amzn2023.0.2
  - **AL2023.3.20240122 version:** 1.68.2-1.amzn2023.0.3

- ** `sqlite` **
  - **RPM:**  lemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-analyzer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-doc  / **Architectures:** noarch
  - **RPM:**  sqlite-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-tcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 3.40.0-1.amzn2023.0.3
  - **AL2023.3.20240122 version:** 3.40.0-1.amzn2023.0.4

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.3.20240117 version:** 2023.3.20240117-0.amzn2023
  - **AL2023.3.20240122 version:** 2023.3.20240122-0.amzn2023

- ** `tzdata` **
  - **RPM:**  tzdata  / **Architectures:** noarch
  - **RPM:**  tzdata-java  / **Architectures:** noarch
  - **AL2023.3.20240117 version:** 2023c-1.amzn2023.0.1
  - **AL2023.3.20240122 version:** 2023d-1.amzn2023.0.1

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240117 version:** 4.0.8-2.amzn2023.0.3
  - **AL2023.3.20240122 version:** 4.0.8-2.amzn2023.0.4

## Docker container image
<a name="amis-2023.3.20240122.container-image"></a>
+ `amazon-linux-repo-cdn-2023.3.20240122-0.amzn2023.noarch`
+ `keyutils-libs-1.6.3-1.amzn2023.0.1.x86_64`
+ `sqlite-libs-3.40.0-1.amzn2023.0.4.x86_64`
+ `system-release-2023.3.20240122-0.amzn2023.noarch`
+ `tzdata-2023d-1.amzn2023.0.1.noarch`

## Default AMI
<a name="amis-2023.3.20240122.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20240122-0.amzn2023.noarch` |
| `kernel-livepatch-repo-s3-2023.3.20240122-0.amzn2023.noarch` |
| `kernel-tools-6.1.72-96.166.amzn2023.x86_64` |
| `kernel-6.1.72-96.166.amzn2023.x86_64` |
| `keyutils-libs-1.6.3-1.amzn2023.0.1.x86_64` |
| `keyutils-1.6.3-1.amzn2023.0.1.x86_64` |
| `nspr-4.35.0-5.amzn2023.0.4.x86_64` |
| `nss-softokn-freebl-3.90.0-3.amzn2023.0.4.x86_64` |
| `nss-softokn-3.90.0-3.amzn2023.0.4.x86_64` |
| `nss-sysinit-3.90.0-3.amzn2023.0.4.x86_64` |
| `nss-util-3.90.0-3.amzn2023.0.4.x86_64` |
| `nss-3.90.0-3.amzn2023.0.4.x86_64` |
| `sqlite-libs-3.40.0-1.amzn2023.0.4.x86_64` |
| `system-release-2023.3.20240122-0.amzn2023.noarch` |
| `tzdata-2023d-1.amzn2023.0.1.noarch` |

## Minimal AMI
<a name="amis-2023.3.20240122.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.3.20240122-0.amzn2023.noarch`
+ `kernel-livepatch-repo-s3-2023.3.20240122-0.amzn2023.noarch`
+ `kernel-6.1.72-96.166.amzn2023.x86_64`
+ `keyutils-libs-1.6.3-1.amzn2023.0.1.x86_64`
+ `sqlite-libs-3.40.0-1.amzn2023.0.4.x86_64`
+ `system-release-2023.3.20240122-0.amzn2023.noarch`
+ `tzdata-2023d-1.amzn2023.0.1.noarch`

## Minimal container image
<a name="amis-2023.3.20240122.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.3.20240122-0.amzn2023.noarch`
+ `keyutils-libs-1.6.3-1.amzn2023.0.1.x86_64`
+ `sqlite-libs-3.40.0-1.amzn2023.0.4.x86_64`
+ `system-release-2023.3.20240122-0.amzn2023.noarch`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
