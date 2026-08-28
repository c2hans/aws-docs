---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20250107.html
---

# Amazon Linux 2023 version 2023.6.20250107 release notes
<a name="relnotes-2023.6.20250107"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20250107.

**Topics**
+ [Major updates](#major-updates-2023.6.20250107)
+ [Repository](#amis-2023.6.20250107.repository)
+ [Docker container image](#amis-2023.6.20250107.container-image)
+ [Default AMI](#amis-2023.6.20250107.default-ami)
+ [Minimal AMI](#amis-2023.6.20250107.minimal-ami)
+ [Minimal container image](#amis-2023.6.20250107.minimal-container-ami)
+ [Contact us](#amis-2023.6.20250107.contact-us)

## Major updates
<a name="major-updates-2023.6.20250107"></a>

This release represents an update to the sixth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20250107.repository"></a>

### New packages in AL2023.6.20250107 since AL2023.6.20241212
<a name="new-AL2023.6.20241212-AL2023.6.20250107"></a>

 Comparing AL2023.6.20241212 version 2023.6.20241212 to AL2023.6.20250107 version [2023.6.20250107](#relnotes-2023.6.20250107).

| Package Type | Number of new packages in AL2023.6.20250107 compared to AL2023.6.20241212 |
| --- | --- |
| Source RPMs | 2 |
| Total Binary RPMs | 8 |
|  x86\_64 binary RPMs | 4 |
|  aarch64 binary RPMs | 4 |

New packages in AL2023.6.20250107:

- ** `kdump-utils` **
  - **RPM:**  kdump-utils
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.48-8.amzn2023

- ** `makedumpfile` **
  - **RPM:**  makedumpfile
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.7.6-1.amzn2023

- ** `systemtap` **
  - **RPM:**  systemtap-jupyter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-sdt-dtrace  / **Architectures:** aarch64, x86\_64
  - **Version:** 5.2-1.amzn2023.0.1

### AL2023.6.20250107 upgrades from AL2023.6.20241212
<a name="vercmp-AL2023.6.20241212-AL2023.6.20250107"></a>

 Comparing [2023.6.20241212](relnotes-2023.6.20241212.md) to [2023.6.20250107](#relnotes-2023.6.20250107).

| Package Type | Count |
| --- | --- |
| Source | 15 |
| Total Binary | 216 |
|  noarch binary RPMs | 44 |
|  x86\_64 binary RPMs | 86 |
|  aarch64 binary RPMs | 86 |

The full comparison of RPM package versions is below.

- ** `boost` **
  - **RPM:**  boost  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-atomic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-b2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-build  / **Architectures:** noarch
  - **RPM:**  boost-chrono  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-container  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-context  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-contract  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-coroutine  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-date-time  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-doctools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-examples  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-fiber  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-graph  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-graph-mpich  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-graph-openmpi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-iostreams  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-json  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-locale  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-log  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-math  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-mpich  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-mpich-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-mpich-python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-mpich-python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-nowide  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-numpy3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-openmpi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-openmpi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-openmpi-python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-openmpi-python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-program-options  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-random  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-regex  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-serialization  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-stacktrace  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-system  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-thread  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-timer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-type\_erasure  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-wave  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 1.75.0-4.amzn2023.0.2
  - **AL2023.6.20250107 version:** 1.75.0-4.amzn2023.0.3

- ** `crash` **
  - **RPM:**  crash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  crash-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 8.0.4-2.amzn2023
  - **AL2023.6.20250107 version:** 8.0.5-5.amzn2023

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 1.89.1-1.amzn2023
  - **AL2023.6.20250107 version:** 1.89.2-1.amzn2023

- ** `expat` **
  - **RPM:**  expat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 2.6.3-1.amzn2023.0.1
  - **AL2023.6.20250107 version:** 2.6.3-1.amzn2023.0.2

- ** `haproxy` **
  - **RPM:**  haproxy
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 2.8.3-1.amzn2023
  - **AL2023.6.20250107 version:** 2.8.3-1.amzn2023.0.1

- ** `jackson-databind` **
  - **RPM:**  jackson-databind
  - **Architectures:** noarch
  - **AL2023.6.20241212 version:** 2.11.4-6.amzn2023.0.2
  - **AL2023.6.20250107 version:** 2.11.4-6.amzn2023.0.3

- ** `kexec-tools` **
  - **RPM:**  kexec-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 2.0.23-4.amzn2023.0.4
  - **AL2023.6.20250107 version:** 2.0.29-1.amzn2023.0.1

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 18.20.4-1.amzn2023.0.1
  - **AL2023.6.20250107 version:** 18.20.5-1.amzn2023.0.1

- ** `nodejs20` **
  - **RPM:**  nodejs20  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-docs  / **Architectures:** noarch
  - **RPM:**  nodejs20-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-11.3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 20.18.0-1.amzn2023.0.2
  - **AL2023.6.20250107 version:** 20.18.1-1.amzn2023.0.1

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-snapsafe-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 3.0.8-1.amzn2023.0.16
  - **AL2023.6.20250107 version:** 3.0.8-1.amzn2023.0.18

- ** `perl-Module-ScanDeps` **
  - **RPM:**  perl-Module-ScanDeps  / **Architectures:** noarch
  - **RPM:**  perl-Module-ScanDeps-tests  / **Architectures:** noarch
  - **AL2023.6.20241212 version:** 1.31-1.amzn2023.0.2
  - **AL2023.6.20250107 version:** 1.37-1.amzn2023.0.1

- ** `python-tornado` **
  - **RPM:**  python3-tornado  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-tornado-doc  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 6.1.0-2.amzn2023.0.3
  - **AL2023.6.20250107 version:** 6.1.0-2.amzn2023.0.4

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20241212 version:** 2023.6.20241212-0.amzn2023
  - **AL2023.6.20250107 version:** 2023.6.20250107-0.amzn2023

- ** `systemtap` **
  - **RPM:**  systemtap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-exporter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-initscript  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-virtguest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-sdt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-testsuite  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 4.8-3.amzn2023.0.6
  - **AL2023.6.20250107 version:** 5.2-1.amzn2023.0.1

- ** `tcsh` **
  - **RPM:**  tcsh
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241212 version:** 6.24.07-1.amzn2023
  - **AL2023.6.20250107 version:** 6.24.14-1.amzn2023

## Docker container image
<a name="amis-2023.6.20250107.container-image"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250107-0.amzn2023 |
| expat-2.6.3-1.amzn2023.0.2 |
| openssl-libs-1:3.0.8-1.amzn2023.0.18 |
| system-release-2023.6.20250107-0.amzn2023 |

## Default AMI
<a name="amis-2023.6.20250107.default-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20250107-0.amzn2023 |
| boost-filesystem-1.75.0-4.amzn2023.0.3 |
| boost-system-1.75.0-4.amzn2023.0.3 |
| boost-thread-1.75.0-4.amzn2023.0.3 |
| expat-2.6.3-1.amzn2023.0.2 |
| kernel-livepatch-repo-s3-2023.6.20250107-0.amzn2023 |
| openssl-libs-1:3.0.8-1.amzn2023.0.18 |
| openssl-1:3.0.8-1.amzn2023.0.18 |
| system-release-2023.6.20250107-0.amzn2023 |
| systemtap-runtime-5.2-1.amzn2023.0.1 |
| tcsh-6.24.14-1.amzn2023 |

## Minimal AMI
<a name="amis-2023.6.20250107.minimal-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20250107-0.amzn2023 |
| expat-2.6.3-1.amzn2023.0.2 |
| kernel-livepatch-repo-s3-2023.6.20250107-0.amzn2023 |
| openssl-libs-1:3.0.8-1.amzn2023.0.18 |
| openssl-1:3.0.8-1.amzn2023.0.18 |
| system-release-2023.6.20250107-0.amzn2023 |

## Minimal container image
<a name="amis-2023.6.20250107.minimal-container-ami"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250107-0.amzn2023 |
| openssl-libs-1:3.0.8-1.amzn2023.0.18 |
| system-release-2023.6.20250107-0.amzn2023 |

## Contact us
<a name="amis-2023.6.20250107.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
