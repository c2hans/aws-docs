---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.4.20240416.html
---

# Amazon Linux 2023 version 2023.4.20240416 release notes
<a name="relnotes-2023.4.20240416"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.4.20240416 release

## Major updates
<a name="major-updates-2023.4.20240416"></a>

This release represents an update to the fourth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.4.20240416)
+ [Repository](#amis-2023.4.20240416.repository)
+ [Docker container image](#amis-2023.4.20240416.container-image)
+ [Default AMI](#amis-2023.4.20240416.default-ami)
+ [Minimal AMI](#amis-2023.4.20240416.minimal-ami)
+ [Minimal container image](#amis-2023.4.20240416.minimal-container-ami)

## Repository
<a name="amis-2023.4.20240416.repository"></a>

### New packages in AL2023.4.20240416 since AL2023.4.20240401
<a name="new-AL2023.4.20240401-AL2023.4.20240416"></a>

 Comparing AL2023.4.20240401 version 2023.4.20240401 to AL2023.4.20240416 version [2023.4.20240416](#relnotes-2023.4.20240416).

| Package Type | Number of new packages in AL2023.4.20240416 compared to AL2023.4.20240401 |
| --- | --- |
| Source RPMs | 0 |
| Total Binary RPMs | 2 |
|  x86\_64 binary RPMs | 1 |
|  aarch64 binary RPMs | 1 |

New packages in AL2023.4.20240416:

- ** [https://docs.aws.amazon.com/linux/al2023/ug/efs.html](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/efs.html](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.0.0-1.amzn2023

### AL2023.4.20240416 upgrades from AL2023.4.20240401
<a name="vercmp-AL2023.4.20240401-AL2023.4.20240416"></a>

 Comparing [2023.4.20240401](relnotes-2023.4.20240401.md) to [2023.4.20240416](#relnotes-2023.4.20240416).

| Package Type | Count |
| --- | --- |
| Source | 11 |
| Total Binary | 144 |
|  noarch binary RPMs | 60 |
|  x86\_64 binary RPMs | 42 |
|  aarch64 binary RPMs | 42 |

The full comparison of RPM package versions is below.

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240401 version:** 3.2.2303.0-1.amzn2023
  - **AL2023.4.20240416 version:** 3.3.131.0-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240401 version:** 1.82.1-1.amzn2023
  - **AL2023.4.20240416 version:** 1.82.2-1.amzn2023

- ** `emacs` **
  - **RPM:**  emacs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-filesystem  / **Architectures:** noarch
  - **RPM:**  emacs-lucid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-nox  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-terminal  / **Architectures:** noarch
  - **AL2023.4.20240401 version:** 28.2-3.amzn2023.0.6
  - **AL2023.4.20240416 version:** 28.2-3.amzn2023.0.7

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
  - **AL2023.4.20240401 version:** 6.1.82-99.168.amzn2023
  - **AL2023.4.20240416 version:** 6.1.84-99.169.amzn2023

- ** `krb5` **
  - **RPM:**  krb5-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-pkinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-server-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-workstation  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libkadm5  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240401 version:** 1.21-3.amzn2023.0.3
  - **AL2023.4.20240416 version:** 1.21-3.amzn2023.0.4

- ** `libreswan` **
  - **RPM:**  libreswan
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240401 version:** 4.12-3.amzn2023
  - **AL2023.4.20240416 version:** 4.12-3.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240401 version:** 3.11.6-1.amzn2023.0.1
  - **AL2023.4.20240416 version:** 3.11.6-1.amzn2023.0.2

- ** `selinux-policy` **
  - **RPM:**  selinux-policy  / **Architectures:** noarch
  - **RPM:**  selinux-policy-devel  / **Architectures:** noarch
  - **RPM:**  selinux-policy-doc  / **Architectures:** noarch
  - **RPM:**  selinux-policy-minimum  / **Architectures:** noarch
  - **RPM:**  selinux-policy-mls  / **Architectures:** noarch
  - **RPM:**  selinux-policy-sandbox  / **Architectures:** noarch
  - **RPM:**  selinux-policy-targeted  / **Architectures:** noarch
  - **AL2023.4.20240401 version:** 37.22-1.amzn2023.0.1
  - **AL2023.4.20240416 version:** 37.22-1.amzn2023.0.2

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.4.20240401 version:** 2023.4.20240401-0.amzn2023
  - **AL2023.4.20240416 version:** 2023.4.20240416-1.amzn2023

- ** `xorg-x11-server` **
  - **RPM:**  xorg-x11-server-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-source  / **Architectures:** noarch
  - **RPM:**  xorg-x11-server-Xdmx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xephyr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xnest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xorg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xvfb  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240401 version:** 1.20.14-30.amzn2023.0.1
  - **AL2023.4.20240416 version:** 1.20.14-30.amzn2023.0.2

## Docker container image
<a name="amis-2023.4.20240416.container-image"></a>
+ `amazon-linux-repo-cdn-2023.4.20240416-1.amzn2023`
+ `krb5-libs-1.21-3.amzn2023.0.4`
+ `system-release-2023.4.20240416-1.amzn2023`

## Default AMI
<a name="amis-2023.4.20240416.default-ami"></a>
+ `amazon-linux-repo-s3-2023.4.20240416-1.amzn2023`
+ `amazon-ssm-agent-3.3.131.0-1.amzn2023`
+ `kernel-livepatch-repo-s3-2023.4.20240416-1.amzn2023`
+ `kernel-tools-6.1.84-99.169.amzn2023`
+ `kernel-6.1.84-99.169.amzn2023`
+ `krb5-libs-1.21-3.amzn2023.0.4`
+ `selinux-policy-targeted-37.22-1.amzn2023.0.2`
+ `selinux-policy-37.22-1.amzn2023.0.2`
+ `system-release-2023.4.20240416-1.amzn2023`

## Minimal AMI
<a name="amis-2023.4.20240416.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.4.20240416-1.amzn2023`
+ `kernel-livepatch-repo-s3-2023.4.20240416-1.amzn2023`
+ `kernel-6.1.84-99.169.amzn2023`
+ `krb5-libs-1.21-3.amzn2023.0.4`
+ `selinux-policy-targeted-37.22-1.amzn2023.0.2`
+ `selinux-policy-37.22-1.amzn2023.0.2`
+ `system-release-2023.4.20240416-1.amzn2023`

## Minimal container image
<a name="amis-2023.4.20240416.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.4.20240416-1.amzn2023`
+ `krb5-libs-1.21-3.amzn2023.0.4`
+ `system-release-2023.4.20240416-1.amzn2023`
