---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20221019.html
---

# Amazon Linux 2023 version 2022.0.20221019 release notes
<a name="relnotes-2022.0.20221019"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20221019"></a>

Amazon Linux 2022 includes the following major updates.
+ Starting with [AL2023 version 2022.0.20220728](relnotes-2022.0.20220728.md), SELinux was switched from an enforcing to a permissive mode by default. You can change SELinux settings to enforced mode via command line by running the `setenforce` command.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.

**Known Issues**
+ Amazon Linux 2022 contains a known issue where customer defined NTP servers via DHCP are not honored.

  **Work-Around** - Configure the NTP servers using a config file in `/etc/chrony.d`
+ Enabling FIPS mode is currently unsupported, and there will be changes to how a FIPS mode enabled system works in upcoming releases.
+ Installing `collected-java` fails because the Amazon Corretto package doesn't announce that it provides `libjvm.so`. Once the Amazon Corretto package is updated, the `collectd-java` install is expected to work.

  **Work-Around** ‐ Install manually with `rpm —nodeps -i collectd-java-5.12.0-16.amzn2022.0.1.x86_64.rpm`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2022.html).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2022/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about Amazon Linux 2022 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2022/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2022/issues/new/choose).

If you just have questions about Amazon Linux 2022, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2022/discussions). Feedback on Amazon Linux 2022 can also be provided through your designated AWS representative.

## Major changes since the first Tech Preview release
<a name="major-changes-20221019"></a>
+ `Kernel` updated from 5.10 to 5.15
+ `OpenSSL` updated from 1.1 to 3.0
+ AWS CLI updated to AWS CLI v2
+ AWS Tools found in Amazon Linux 2 have been added to the repositories like `ecs-agent`, `aws-cfn-bootstrap`, `aws-kinesis-agent`, `ec2-instance-connect`, and other tools.
+ `rsyslog` is no longer installed by default, and thus the `system-journald` is the way `syslog` works, with `journalctl` as the client that can look at logs.
+ The default `curl` is part of the `curl-minimal` package, which supports the most popular protocols. You can switch to the full-featured `curl` if needed by running `dnf install --allowerasing curl-full libcurl-full`
+ The default `gnupg` is a minimal one, which is limited in functionality, but has the minimal code needed to GPG verify RPMs, and brings a minimal number of packages into AMIs and container images. If you need full `gnupg` functionality, you can get the full `gnupg` by running `dnf install --allowerasing gnupg2-full`
+ **Curation of packages** - As part of the development cycle, we have curated the list of packages available in the repositories. This involved removing a number of packages that were no longer needed due to dependencies. Some package may be re-added to the repository as we work through customer requests.
+ Language run-times were updated and some runtimes like Ruby were name-spaced allowing newer versions to be added in the future without removing the current ones from the repositories.
+ The Java ecosystem is now based on Amazon Corretto 17 rather than OpenJDK 11. Java build tools have been rebuilt to newer versions and run with Amazon Corretto.

**Kernel CONFIG\_HZ changed from `250` to `100` on both `arm64` and `x86`.**

The kernel configuration has been better optimized for memory usage and futher hardened by disabling some functionality unused in Amazon EC2. Notable changes include:
+ Set `NR_CPUS=512` from `8192`
+ Remove several older filesystems and use `ext4`-only
+ Remove some physical adapters not used in Amazon EC2
+ Drop a variety of unused or old network protocols
+ Remove CDROM support
+ Remove PS2 support
+ Remove "media" and `v4l2` support
+ Drop older `NFS`/`CIFS` API versions except `nfsv3`
+ Turn on a few performance-friendly security options
+ Set `PANIC_ON_OOPS` for all hangs
+ Enable `TCMU CONFIG_TCM_USER2` Module
+ Drop unused `arm64` platforms
+ Enable `CONFIG_KEXEC_SIG`
+ Disable `CONFIG_SCHED_CORE and CONFIG_SCHED_SMT` on `arm64`
+ Disable `CONFIG_LDISC_AUTOLOAD`
+ Enable CAKE `qdisc` support `CONFIG_NET_SCH_CAKE`
+ Update Lustre client to `2.12.8`
+ Disable `CONFIG_KSM`

   ‐ `CONFIG_RANDOMIZE_KSTACK_OFFSET_DEFAULT`

   ‐ `CONFIG_GCC_PLUGIN_STACKLEAK`

   ‐ `CONFIG_INIT_ON_ALLOC_DEFAULT_ON`

   ‐ `CONFIG_ZERO_CALL_USED_REGS`

   ‐ `CONFIG_KFENCE`

**Repository**

This update to the Amazon Linux 2022 repository and AMI includes the following new packages.
+ `jackson-annotations-2.11.4-6.amzn2022`
+ `jackson-bom-2.11.4-5.amzn2022`
+ `jackson-core-2.11.4-7.amzn2022`
+ `jackson-databind-2.11.4-6.amzn2022`
+ `jackson-parent-2.11-7.amzn2022`
+ `microdnf-3.8.1-1.amzn2022.0.1`
+ `snakeyaml-1.27-6.amzn2022`

The repository includes the following packages that were updated since the last release.

|  |
| --- |
| `aide-0.17.4-1.amzn2022.0.2` |
| `amazon-ec2-net-utils-2.3.0-1.amzn2022.0.1` |
| `antlr-2.7.7-69.amzn2022.0.1` |
| `aopalliance-1.0-28.amzn2022.0.2` |
| `apache-commons-exec-1.3-22.amzn2022.0.1` |
| `apache-commons-net-3.6-16.amzn2022` |
| `apache-ivy-2.5.0-10.amzn2022.0.1` |
| `args4j-2.33-19.amzn2022` |
| `aws-c-io-0.10.12-5.amzn2022.0.6` |
| `bcel-6.4.1-9.amzn2022.0.1` |
| `bouncycastle-1.70-4.amzn2022.0.1` |
| `bsf-2.4.0-44.amzn2022.0.1` |
| `bsh-2.1.0-5.amzn2022.0.1` |
| `byte-buddy-1.12.0-3.amzn2022.0.3` |
| `byteman-4.0.16-4.amzn2022.0.1` |
| `cloud-init-22.2.2-1.amzn2022.1.6` |
| `codehaus-parent-4-23.amzn2022.0.1` |
| `containerd-1.6.8-1.amzn2022.0.1` |
| `disruptor-3.4.4-3.amzn2022.0.1` |
| `dnf-4.12.0-2.amzn2022.0.3` |
| `dnf-plugin-support-info-1.0-2.amzn2022.0.3` |
| `dom4j-2.0.3-4.amzn2022` |
| `ecj-4.23-1.amzn2022.0.2` |
| `elfutils-0.187-9.amzn2022.0.1` |
| `exec-maven-plugin-3.0.0-4.amzn2022` |
| `fasterxml-oss-parent-41-5.amzn2022.0.1` |
| `freetype-2.11.0-6.amzn2022.0.1` |
| `google-gson-2.9.0-1.amzn2022.0.1` |
| `graphviz-2.44.0-25.amzn2022.0.5` |
| `hawtjni-1.18-4.amzn2022.0.1` |
| `irqbalance-1.9.0-1.amzn2022.0.2` |
| `jakarta-activation-1.2.2-6.amzn2022` |
| `jakarta-el-4.0.0-7.amzn2022` |
| `jakarta-interceptors-2.0.0-5.amzn2022` |
| `jakarta-mail-1.6.5-8.amzn2022` |
| `jakarta-oro-2.0.8-36.amzn2022` |
| `jakarta-saaj-1.4.2-6.amzn2022.0.1` |
| `jakarta-server-pages-2.3.6-7.amzn2022` |
| `janino-3.1.7-1.amzn2022` |
| `jansi1-1.18-11.amzn2022` |
| `jansi-native-1.8-9.amzn2022.0.1` |
| `java-1.8.0-amazon-corretto-1.8.0_352.b08-1.amzn2022` |
| `java-11-amazon-corretto-11.0.17+8-1.amzn2022` |
| `java-17-amazon-corretto-17.0.5+8-1.amzn2022.1` |
| `javacc-7.0.4-11.amzn2022` |
| `javacc-maven-plugin-2.6-35.amzn2022` |
| `javaparser-3.22.0-3.amzn2022` |
| `javassist-3.28.0-4.amzn2022` |
| `jaxb-2.3.5-5.amzn2022.0.1` |
| `jaxb-api-2.3.3-6.amzn2022` |
| `jaxb-dtd-parser-1.5.0-1.amzn2022.0.1` |
| `jaxb-fi-1.2.18-7.amzn2022` |
| `jaxb-istack-commons-3.0.12-3.amzn2022` |
| `jaxb-stax-ex-1.8.3-8.amzn2022` |
| `jaxen-1.2.0-10.amzn2022` |
| `jboss-parent-20-14.amzn2022` |
| `jcip-annotations-1-35.20060626.amzn2022` |
| `jctools-3.3.0-3.amzn2022.0.1` |
| `jdepend-2.9.1-29.amzn2022` |
| `jdependency-2.8.0-1.amzn2022.0.1` |
| `jline2-2.14.6-5.amzn2022` |
| `jna-5.9.0-1.amzn2022.0.1` |
| `jsch-0.1.55-7.amzn2022` |
| `jtidy-1.0-0.38.20100930svn1125.amzn2022` |
| `jzlib-1.1.3-21.amzn2022` |
| `kernel-5.15.73-45.135.amzn2022` |
| `libgcrypt-1.10.1-4.amzn2022` |
| `libidn-1.38-4.amzn2022.0.1` |
| `libstoragemgmt-1.9.4-5.amzn2022.0.1` |
| `libwebp-1.2.4-1.amzn2022.0.1` |
| `log4j-2.17.2-1.amzn2022.0.3` |
| `maven2-2.2.1-70.amzn2022` |
| `maven-archiver-3.5.1-1.amzn2022.0.1` |
| `maven-clean-plugin-3.1.0-10.amzn2022` |
| `maven-doxia-1.9.1-7.amzn2022.0.1` |
| `maven-doxia-sitetools-1.9.2-7.amzn2022` |
| `maven-invoker-3.1.0-3.amzn2022` |
| `maven-invoker-plugin-3.2.1-8.amzn2022` |
| `maven-mapping-3.0.0-16.amzn2022` |
| `maven-reporting-api-3.1.0-1.amzn2022` |
| `maven-reporting-impl-3.1.0-1.amzn2022` |
| `maven-script-interpreter-1.2-11.amzn2022` |
| `maven-shade-plugin-3.2.4-7.amzn2022` |
| `maven-verifier-plugin-1.0-30.amzn2022` |
| `nss-3.83.0-1.amzn2022.0.1` |
| `openmpi-4.1.2-3.amzn2022.0.1` |
| `perl-Graphics-TIFF-18-4.amzn2022.0.1` |
| `php8.1-8.1.7-1.amzn2022.0.4` |
| `plexus-component-api-1.0-0.34.alpha15.amzn2022.0.1` |
| `plexus-i18n-1.0-0.23.b10.4.amzn2022.0.1` |
| `plexus-velocity-1.2-15.amzn2022.0.1` |
| `reflections-0.9.12-10.amzn2022` |
| `regexp-1.5-38.amzn2022` |
| `replacer-1.6-22.amzn2022.0.1` |
| `rhino-1.7.14-3.amzn2022.0.1` |
| `s2n-tls-1.3.24-1.amzn2022.0.2` |
| `spec-version-maven-plugin-1.5-6.amzn2022` |
| `sphinx-2.2.11-24.amzn2022.0.1` |
| `systemd-250.8-1.amzn2022.0.2` |
| `system-release-2022.0.20221019-2.amzn2022` |
| `systemtap-4.7-1.amzn2022.0.3` |
| `tomcat-taglibs-parent-3-18.amzn2022` |
| `tzdata-2022e-1.amzn2022.0.1` |
| `vim-9.0.475-1.amzn2022.0.1` |
| `weld-parent-45-3.amzn2022` |
| `wsdl4j-1.6.3-24.amzn2022` |
| `xalan-j2-2.7.2-12.amzn2022.0.2` |
| `xerces-j2-2.12.1-7.amzn2022` |
| `xml-commons-apis-1.4.01-38.amzn2022` |
| `xml-commons-resolver-1.2-37.amzn2022` |
| `xmlgraphics-commons-2.7-2.amzn2022.0.2` |
| `xmlstreambuffer-1.5.10-5.amzn2022` |
| `z3-4.8.17-1.amzn2022.0.1` |

## AMIs
<a name="amis-2022020221019"></a>

**Docker Container image**

|  |
| --- |
| `amazon-linux-repo-cdn-2022.0.20221019-2.amzn2022` |
| `dnf-4.12.0-2.amzn2022.0.2` |
| `dnf-data-4.12.0-2.amzn2022.0.2` |
| `elfutils-default-yama-scope-0.187-5.amzn2022.0.3` |
| `elfutils-libelf-0.187-5.amzn2022.0.3` |
| `elfutils-libs-0.187-5.amzn2022.0.3` |
| `dnf-4.12.0-2.amzn2022.0.3` |
| `dnf-data-4.12.0-2.amzn2022.0.3` |
| `elfutils-default-yama-scope-0.187-9.amzn2022.0.1` |
| `elfutils-libelf-0.187-9.amzn2022.0.1` |
| `elfutils-libs-0.187-9.amzn2022.0.1` |
| `libgcrypt-1.9.3-3.amzn2022.0.2` |
| `libgcrypt-1.10.1-4.amzn2022` |
| `python3-dnf-4.12.0-2.amzn2022.0.2` |
| `python3-dnf-4.12.0-2.amzn2022.0.3` |
| `system-release-2022.0.20221012-0.amzn2022` |
| `tzdata-2022d-1.amzn2022.0.1` |
| `vim-data-9.0.327-1.amzn2022.0.2` |
| `vim-minimal-9.0.327-1.amzn2022.0.2` |
| `system-release-2022.0.20221019-2.amzn2022` |
| `tzdata-2022e-1.amzn2022.0.1` |
| `vim-data-9.0.475-1.amzn2022.0.1` |
| `vim-minimal-9.0.475-1.amzn2022.0.1` |
| `yum-4.12.0-2.amzn2022.0.2` |
| `yum-4.12.0-2.amzn2022.0.3` |

**Default AMI**

|  |
| --- |
| `amazon-ec2-net-utils-2.2.0-1.amzn2022.0.1` |
| `amazon-ec2-net-utils-2.3.0-1.amzn2022.0.1` |
| `amazon-linux-repo-s3-2022.0.20221019-2.amzn2022` |
| `aws-c-io-libs-0.10.12-5.amzn2022.0.2` |
| `aws-c-io-libs-0.10.12-5.amzn2022.0.6` |
| `cloud-init-22.2.2-1.amzn2022.1.5` |
| `cloud-init-22.2.2-1.amzn2022.1.6` |
| `dnf-4.12.0-2.amzn2022.0.2` |
| `dnf-data-4.12.0-2.amzn2022.0.2` |
| `dnf-4.12.0-2.amzn2022.0.3` |
| `dnf-data-4.12.0-2.amzn2022.0.3` |
| `dnf-plugin-support-info-1.0-2.amzn2022.0.2` |
| `dnf-plugin-support-info-1.0-2.amzn2022.0.3` |
| `elfutils-debuginfod-client-0.187-5.amzn2022.0.3` |
| `elfutils-default-yama-scope-0.187-5.amzn2022.0.3` |
| `elfutils-libelf-0.187-5.amzn2022.0.3` |
| `elfutils-libs-0.187-5.amzn2022.0.3` |
| `elfutils-debuginfod-client-0.187-9.amzn2022.0.1` |
| `elfutils-default-yama-scope-0.187-9.amzn2022.0.1` |
| `elfutils-libelf-0.187-9.amzn2022.0.1` |
| `elfutils-libs-0.187-9.amzn2022.0.1` |
| `irqbalance-1.8.0-2.amzn2022.0.2` |
| `irqbalance-1.9.0-1.amzn2022.0.2` |
| `kernel-5.15.57-30.131.amzn2022` |
| `kernel-tools-5.15.57-30.131.amzn2022` |
| `kernel-5.15.73-45.135.amzn2022` |
| `kernel-tools-5.15.73-45.135.amzn2022` |
| `libgcrypt-1.9.3-3.amzn2022.0.2` |
| `libgcrypt-1.10.1-4.amzn2022` |
| `libstoragemgmt-1.9.2-4.amzn2022.0.1` |
| `libstoragemgmt-1.9.4-5.amzn2022.0.1` |
| `nspr-4.32.0-5.amzn2022.0.1` |
| `nss-3.77.0-2.amzn2022.0.1` |
| `nss-softokn-3.77.0-2.amzn2022.0.1` |
| `nss-softokn-freebl-3.77.0-2.amzn2022.0.1` |
| `nss-sysinit-3.77.0-2.amzn2022.0.1` |
| `nss-util-3.77.0-2.amzn2022.0.1` |
| `3nspr-4.35.0-1.amzn2022.0.1` |
| `nss-3.83.0-1.amzn2022.0.1` |
| `nss-softokn-3.83.0-1.amzn2022.0.1` |
| `nss-softokn-freebl-3.83.0-1.amzn2022.0.1` |
| `nss-sysinit-3.83.0-1.amzn2022.0.1` |
| `nss-util-3.83.0-1.amzn2022.0.1` |
| `python3-dnf-4.12.0-2.amzn2022.0.2` |
| `python3-dnf-4.12.0-2.amzn2022.0.3` |
| `python3-libstoragemgmt-1.9.2-4.amzn2022.0.1` |
| `python3-libstoragemgmt-1.9.4-5.amzn2022.0.1` |
| `s2n-tls-1.3.2-3.amzn2022.0.2` |
| `s2n-tls-libs-1.3.2-3.amzn2022.0.2` |
| `s2n-tls-1.3.24-1.amzn2022.0.2` |
| `s2n-tls-libs-1.3.24-1.amzn2022.0.2` |
| `system-release-2022.0.20221012-0.amzn2022` |
| `systemd-250.8-1.amzn2022.0.1` |
| `systemd-libs-250.8-1.amzn2022.0.1` |
| `systemd-networkd-250.8-1.amzn2022.0.1` |
| `systemd-pam-250.8-1.amzn2022.0.1` |
| `systemd-resolved-250.8-1.amzn2022.0.1` |
| `systemd-udev-250.8-1.amzn2022.0.1` |
| `systemtap-runtime-4.7-1.amzn2022.0.2` |
| `system-release-2022.0.20221019-2.amzn2022` |
| `systemd-250.8-1.amzn2022.0.2` |
| `systemd-libs-250.8-1.amzn2022.0.2` |
| `systemd-networkd-250.8-1.amzn2022.0.2` |
| `systemd-pam-250.8-1.amzn2022.0.2` |
| `systemd-resolved-250.8-1.amzn2022.0.2` |
| `systemd-udev-250.8-1.amzn2022.0.2` |
| `systemtap-runtime-4.7-1.amzn2022.0.3` |
| `tzdata-2022d-1.amzn2022.0.1` |
| `tzdata-2022e-1.amzn2022.0.1` |
| `vim-common-9.0.327-1.amzn2022.0.2` |
| `vim-data-9.0.327-1.amzn2022.0.2` |
| `vim-enhanced-9.0.327-1.amzn2022.0.2` |
| `vim-filesystem-9.0.327-1.amzn2022.0.2` |
| `vim-minimal-9.0.327-1.amzn2022.0.2` |
| `vim-common-9.0.475-1.amzn2022.0.1` |
| `vim-data-9.0.475-1.amzn2022.0.1` |
| `vim-enhanced-9.0.475-1.amzn2022.0.1` |
| `vim-filesystem-9.0.475-1.amzn2022.0.1` |
| `vim-minimal-9.0.475-1.amzn2022.0.1` |
| `yum-4.12.0-2.amzn2022.0.2` |
| `yum-4.12.0-2.amzn2022.0.3` |

**Minimal AMI**

|  |
| --- |
| `amazon-ec2-net-utils-2.2.0-1.amzn2022.0.1` |
| `amazon-ec2-net-utils-2.3.0-1.amzn2022.0.1` |
| `amazon-linux-repo-s3-2022.0.20221019-2.amzn2022` |
| `aws-c-io-libs-0.10.12-5.amzn2022.0.2` |
| `aws-c-io-libs-0.10.12-5.amzn2022.0.6` |
| `cloud-init-22.2.2-1.amzn2022.1.5` |
| `cloud-init-22.2.2-1.amzn2022.1.6` |
| `dnf-4.12.0-2.amzn2022.0.2` |
| `dnf-data-4.12.0-2.amzn2022.0.2` |
| `dnf-4.12.0-2.amzn2022.0.3` |
| `dnf-data-4.12.0-2.amzn2022.0.3` |
| `dnf-plugin-support-info-1.0-2.amzn2022.0.2` |
| `dnf-plugin-support-info-1.0-2.amzn2022.0.3` |
| `elfutils-default-yama-scope-0.187-5.amzn2022.0.3` |
| `elfutils-libelf-0.187-5.amzn2022.0.3` |
| `elfutils-libs-0.187-5.amzn2022.0.3` |
| `elfutils-default-yama-scope-0.187-9.amzn2022.0.1` |
| `elfutils-libelf-0.187-9.amzn2022.0.1` |
| `elfutils-libs-0.187-9.amzn2022.0.1` |
| `irqbalance-1.8.0-2.amzn2022.0.2` |
| `irqbalance-1.9.0-1.amzn2022.0.2` |
| `kernel-5.15.57-30.131.amzn2022` |
| `kernel-5.15.73-45.135.amzn2022` |
| `libgcrypt-1.9.3-3.amzn2022.0.2` |
| `libgcrypt-1.10.1-4.amzn2022` |
