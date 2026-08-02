---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20250123.html
---

# Amazon Linux 2023 version 2023.6.20250123 release notes
<a name="relnotes-2023.6.20250123"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20250123.

**Topics**
+ [Major updates](#major-updates-2023.6.20250123)
+ [Repository](#amis-2023.6.20250123.repository)
+ [Docker container image](#amis-2023.6.20250123.container-image)
+ [Default AMI](#amis-2023.6.20250123.default-ami)
+ [Minimal AMI](#amis-2023.6.20250123.minimal-ami)
+ [Minimal container image](#amis-2023.6.20250123.minimal-container-ami)
+ [Contact us](#amis-2023.6.20250123.contact-us)

## Major updates
<a name="major-updates-2023.6.20250123"></a>

This release represents an update to the sixth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.
+ A change to the ansible-core package introduced an issue that causes the `ansible-playbook` command to throw an error when executed. This issue will be resolved in the next AL2023 update.

  **Work-Around** - Customers affected by this change can restore the previous `ansible-playbook` behavior until the next update is released by downgrading the `anisble-core` package using the command `sudo dnf install ansible-core-2.15.3-1.amzn2023.0.5`

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20250123.repository"></a>

### New packages in AL2023.6.20250123 since AL2023.6.20250115
<a name="new-AL2023.6.20250115-AL2023.6.20250123"></a>

 Comparing AL2023.6.20250115 version 2023.6.20250115 to AL2023.6.20250123 version [2023.6.20250123](#relnotes-2023.6.20250123).

| Package Type | Number of new packages in AL2023.6.20250123 compared to AL2023.6.20250115 |
| --- | --- |
| Source RPMs | 3 |
| Total Binary RPMs | 16 |
|  x86\_64 binary RPMs | 8 |
|  aarch64 binary RPMs | 8 |

New packages in AL2023.6.20250123:

- ** `lasso` **
  - **RPM:**  lasso  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lasso-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-lasso  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-lasso  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.8.2-14.amzn2023

- ** `libtraceevent` **
  - **RPM:**  libtraceevent  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtraceevent-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.8.2-2.amzn2023.0.1

- ** `mod_auth_mellon` **
  - **RPM:**  mod\_auth\_mellon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_auth\_mellon-diagnostics  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.19.0-2.amzn2023

### AL2023.6.20250123 upgrades from AL2023.6.20250115
<a name="vercmp-AL2023.6.20250115-AL2023.6.20250123"></a>

 Comparing [2023.6.20250115](relnotes-2023.6.20250115.md) to [2023.6.20250123](#relnotes-2023.6.20250123).

| Package Type | Count |
| --- | --- |
| Source | 25 |
| Total Binary | 314 |
|  noarch binary RPMs | 208 |
|  x86\_64 binary RPMs | 53 |
|  aarch64 binary RPMs | 53 |

The full comparison of RPM package versions is below.

- ** [https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html)
  - **Architectures:** noarch
  - **AL2023.6.20250115 version:** 2.5.1-1.amzn2023.0.1
  - **AL2023.6.20250123 version:** 2.5.2-1.amzn2023.0.1

- ** `ansible-core` **
  - **RPM:**  ansible-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ansible-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 2.15.3-1.amzn2023.0.4
  - **AL2023.6.20250123 version:** 2.15.3-1.amzn2023.0.6

- ** `aws-cfn-bootstrap` **
  - **RPM:**  aws-cfn-bootstrap
  - **Architectures:** noarch
  - **AL2023.6.20250115 version:** 2.0-31.amzn2023
  - **AL2023.6.20250123 version:** 2.0-32.amzn2023

- ** `chrony` **
  - **RPM:**  amazon-chrony-config  / **Architectures:** noarch
  - **RPM:**  chrony  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 4.3-1.amzn2023.0.4
  - **AL2023.6.20250123 version:** 4.3-1.amzn2023.0.5

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 1.7.23-1.amzn2023.0.1
  - **AL2023.6.20250123 version:** 1.7.25-1.amzn2023.0.1

- ** `crypto-policies` **
  - **RPM:**  crypto-policies  / **Architectures:** noarch
  - **RPM:**  crypto-policies-scripts  / **Architectures:** noarch
  - **AL2023.6.20250115 version:** 20220428-1.gitdfb10ea.amzn2023.0.2
  - **AL2023.6.20250123 version:** 20240828-2.git626aa59.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 1.89.2-1.amzn2023
  - **AL2023.6.20250123 version:** 1.89.3-1.amzn2023

- ** `git` **
  - **RPM:**  git  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-all  / **Architectures:** noarch
  - **RPM:**  git-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-core-doc  / **Architectures:** noarch
  - **RPM:**  git-credential-libsecret  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-cvs  / **Architectures:** noarch
  - **RPM:**  git-daemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-email  / **Architectures:** noarch
  - **RPM:**  git-gui  / **Architectures:** noarch
  - **RPM:**  git-instaweb  / **Architectures:** noarch
  - **RPM:**  gitk  / **Architectures:** noarch
  - **RPM:**  git-p4  / **Architectures:** noarch
  - **RPM:**  git-subtree  / **Architectures:** noarch
  - **RPM:**  git-svn  / **Architectures:** noarch
  - **RPM:**  gitweb  / **Architectures:** noarch
  - **RPM:**  perl-Git  / **Architectures:** noarch
  - **RPM:**  perl-Git-SVN  / **Architectures:** noarch
  - **AL2023.6.20250115 version:** 2.40.1-1.amzn2023.0.3
  - **AL2023.6.20250123 version:** 2.47.1-1.amzn2023.0.2

- ** `gnutls` **
  - **RPM:**  gnutls  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-dane  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 3.8.0-380.amzn2023.0.6
  - **AL2023.6.20250123 version:** 3.8.0-381.amzn2023.0.7

- ** `grpc` **
  - **RPM:**  grpc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-data  / **Architectures:** noarch
  - **RPM:**  grpc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-doc  / **Architectures:** noarch
  - **RPM:**  grpc-plugins  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 1.60.2-10.amzn2023
  - **AL2023.6.20250123 version:** 1.60.2-10.amzn2023.0.1

- ** `iperf3` **
  - **RPM:**  iperf3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iperf3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 3.16-1.amzn2023
  - **AL2023.6.20250123 version:** 3.18-1.amzn2023

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
  - **AL2023.6.20250115 version:** 6.1.119-129.201.amzn2023
  - **AL2023.6.20250123 version:** 6.1.124-134.200.amzn2023

- ** `lustre-client` **
  - **RPM:**  lustre-client
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 2.15.4-7.amzn2023
  - **AL2023.6.20250123 version:** 2.15.6-13.amzn2023

- ** `nerdctl` **
  - **RPM:**  nerdctl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 1.7.7-1.amzn2023.0.1
  - **AL2023.6.20250123 version:** 2.0.2-1.amzn2023.0.1

- ** `openjpeg2` **
  - **RPM:**  openjpeg2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openjpeg2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openjpeg2-devel-docs  / **Architectures:** noarch
  - **RPM:**  openjpeg2-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 2.4.0-11.amzn2023.0.3
  - **AL2023.6.20250123 version:** 2.4.0-11.amzn2023.0.4

- ** `pcsc-lite` **
  - **RPM:**  pcsc-lite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcsc-lite-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcsc-lite-doc  / **Architectures:** noarch
  - **RPM:**  pcsc-lite-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 1.9.1-1.amzn2023.0.3
  - **AL2023.6.20250123 version:** 1.9.1-1.amzn2023.0.4

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 3.12.6-1.amzn2023.0.2
  - **AL2023.6.20250123 version:** 3.12.8-1.amzn2023.0.1

- ** `python-jinja2` **
  - **RPM:**  python3-jinja2
  - **Architectures:** noarch
  - **AL2023.6.20250115 version:** 2.11.3-1.amzn2023.0.4
  - **AL2023.6.20250123 version:** 2.11.3-1.amzn2023.0.5

- ** `redis6` **
  - **RPM:**  redis6  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-doc  / **Architectures:** noarch
  - **AL2023.6.20250115 version:** 6.2.14-2.amzn2023.0.1
  - **AL2023.6.20250123 version:** 6.2.14-2.amzn2023.0.2

- ** `runc` **
  - **RPM:**  runc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 1.1.14-1.amzn2023.0.1
  - **AL2023.6.20250123 version:** 1.2.4-1.amzn2023.0.1

- ** `runfinch-finch` **
  - **RPM:**  runfinch-finch
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250115 version:** 1.4.1-1.amzn2023.0.2
  - **AL2023.6.20250123 version:** 1.6.0-1.amzn2023.0.1

- ** `selinux-policy` **
  - **RPM:**  selinux-policy  / **Architectures:** noarch
  - **RPM:**  selinux-policy-devel  / **Architectures:** noarch
  - **RPM:**  selinux-policy-doc  / **Architectures:** noarch
  - **RPM:**  selinux-policy-minimum  / **Architectures:** noarch
  - **RPM:**  selinux-policy-mls  / **Architectures:** noarch
  - **RPM:**  selinux-policy-sandbox  / **Architectures:** noarch
  - **RPM:**  selinux-policy-targeted  / **Architectures:** noarch
  - **AL2023.6.20250115 version:** 38.1.47-1.amzn2023.0.1
  - **AL2023.6.20250123 version:** 38.1.50-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20250115 version:** 2023.6.20250115-0.amzn2023
  - **AL2023.6.20250123 version:** 2023.6.20250123-0.amzn2023

- ** `tomcat10` **
  - **RPM:**  tomcat10  / **Architectures:** noarch
  - **RPM:**  tomcat10-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat10-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat10-el-5.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat10-jsp-3.1-api  / **Architectures:** noarch
  - **RPM:**  tomcat10-lib  / **Architectures:** noarch
  - **RPM:**  tomcat10-servlet-6.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat10-webapps  / **Architectures:** noarch
  - **AL2023.6.20250115 version:** 10.1.29-1.amzn2023.0.1
  - **AL2023.6.20250123 version:** 10.1.34-1.amzn2023.0.1

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.6.20250115 version:** 9.0.91-1.amzn2023.0.1
  - **AL2023.6.20250123 version:** 9.0.98-1.amzn2023.0.1

## Docker container image
<a name="amis-2023.6.20250123.container-image"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250123-0.amzn2023 |
| crypto-policies-20240828-2.git626aa59.amzn2023.0.1 |
| system-release-2023.6.20250123-0.amzn2023 |

## Default AMI
<a name="amis-2023.6.20250123.default-ami"></a>

|  |
| --- |
| amazon-chrony-config-4.3-1.amzn2023.0.5 |
| amazon-ec2-net-utils-2.5.2-1.amzn2023.0.1 |
| amazon-linux-repo-s3-2023.6.20250123-0.amzn2023 |
| aws-cfn-bootstrap-2.0-32.amzn2023 |
| chrony-4.3-1.amzn2023.0.5 |
| crypto-policies-scripts-20240828-2.git626aa59.amzn2023.0.1 |
| crypto-policies-20240828-2.git626aa59.amzn2023.0.1 |
| gnutls-3.8.0-381.amzn2023.0.7 |
| kernel-libbpf-6.1.124-134.200.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20250123-0.amzn2023 |
| kernel-tools-6.1.124-134.200.amzn2023 |
| kernel-6.1.124-134.200.amzn2023 |
| python3-jinja2-2.11.3-1.amzn2023.0.5 |
| selinux-policy-targeted-38.1.50-1.amzn2023.0.1 |
| selinux-policy-38.1.50-1.amzn2023.0.1 |
| system-release-2023.6.20250123-0.amzn2023 |

## Minimal AMI
<a name="amis-2023.6.20250123.minimal-ami"></a>

|  |
| --- |
| amazon-chrony-config-4.3-1.amzn2023.0.5 |
| amazon-ec2-net-utils-2.5.2-1.amzn2023.0.1 |
| amazon-linux-repo-s3-2023.6.20250123-0.amzn2023 |
| chrony-4.3-1.amzn2023.0.5 |
| crypto-policies-20240828-2.git626aa59.amzn2023.0.1 |
| gnutls-3.8.0-381.amzn2023.0.7 |
| kernel-libbpf-6.1.124-134.200.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20250123-0.amzn2023 |
| kernel-6.1.124-134.200.amzn2023 |
| python3-jinja2-2.11.3-1.amzn2023.0.5 |
| selinux-policy-targeted-38.1.50-1.amzn2023.0.1 |
| selinux-policy-38.1.50-1.amzn2023.0.1 |
| system-release-2023.6.20250123-0.amzn2023 |

## Minimal container image
<a name="amis-2023.6.20250123.minimal-container-ami"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250123-0.amzn2023 |
| crypto-policies-20240828-2.git626aa59.amzn2023.0.1 |
| system-release-2023.6.20250123-0.amzn2023 |

## Contact us
<a name="amis-2023.6.20250123.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
