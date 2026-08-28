---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20220831.html
---

# Amazon Linux 2023 version 2022.0.20220831 release notes
<a name="relnotes-2022.0.20220831"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20220831"></a>

Amazon Linux 2022 includes the following major updates.
+ There have been some changes to the build flags that will propagate throughout the packages over the next few months.
+ Starting with [AL2023 version 2022.0.20220728](relnotes-2022.0.20220728.md), SELinux was switched from an enforcing to a permissive mode by default. You can change SELinux settings to enforced mode via command line by running the `setenforce` command.

Upcoming Changes in future Release Candidate AMIs and repos.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.
+ The kernel package will see changes to improve aspects of security and performance, and, while core functionality will be maintained, some unused or deprecated features may be removed in future Release Candidates.

**Java Ecosystem**
+ The `maven`, `xmvn`, and `javapackages-tools` should function as expected, but the versions present in this release have not yet been rebuilt after a bootstrap phase. These packages will be re-built without the use of `javapackages-bootstrap` before General Availability.

**Known Issues**
+ There is a known issue by which enabling FIPS mode with `update-crypto-policies --set FIPS` will result in a non functional system. This will be addressed in a future release.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2022.html).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2022/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about Amazon Linux 2022 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2022/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2022/issues/new/choose).

If you just have questions about Amazon Linux 2022, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2022/discussions). Feedback on Amazon Linux 2022 can also be provided through your designated AWS representative.

## Major since the first Tech Preview
<a name="major-changes-20220831"></a>
+ Kernel updated from 5.10 to 5.15
+ OpenSSL updated from 1.1 to 3.0
+ AWS CLI updated to AWS CLI v2
+ AWS Tools found in AL2 have been added to the repositories like `ecs-agent`, `aws-cfn-bootstrap`, `aws-kinesis-agent`, `ec2-instance-connect`, and other tools.
+ `rsyslog` is no longer installed by default, and thus the `system-journald` is the way `syslog` works, with `journalctl` as the client that can look at logs.
+ The default `curl` is part of the `curl-minimal` package, which supports the most popular protocols. You can switch to the full-featured `curl` if needed by running `dnf install --allowerasing curl-full libcurl-full`
+ The default `gnupg` is a minimal one, which is limited in functionality, but has the minimal code needed to GPG verify RPMs, and brings a minimal number of packages into AMIs and container images. If you need full `gnupg` functionality, you can get the full `gnupg` by running `dnf install --allowerasing gnupg2-full`
+ Curation of packages - As part of the development cycle, we have curated the list of packages available in the repositories. This involved removing a number of packages that were no longer needed due to dependencies. Some package may be re-added to the repository as we work through customer requests.
+ Language run-times were updated and some runtimes like Ruby were name-spaced allowing newer versions to be added in the future without removing the current ones from the repositories.

**Repository**

This update Amazon Linux 2022 repository and AMI includes the following new packages.
+ `bpftrace-0.15.0-1.amzn2022`
+ `kernel-libbpf-5.15.57-30.131.amzn2022`
+ `kernel-libbpf-devel-5.15.57-30.131.amzn2022`
+ `kernel-libbpf-static-5.15.57-30.131.amzn2022`
+ `libbpf-tools-0.24.0-2.amzn2022.0.1`
+ `mpdecimal-2.5.1-3.amzn2022`
+ `mpdecimal-devel-2.5.1-3.amzn2022`
+ `mpdecimal-doc-2.5.1-3.amzn2022`

The repository includes the following packages that were updated since the last release.

|  |
| --- |
| `bcc-0.24.0-2.amzn2022.0.1` |
| `bcc-devel-0.24.0-2.amzn2022.0.1` |
| `bcc-doc-0.24.0-2.amzn2022.0.1` |
| `bcc-tools-0.24.0-2.amzn2022.0.1` |
| `bpftool-5.15.57-30.131.amzn2022` |
| `chrony-4.2-7.amzn2022.0.2` |
| `cloud-init-22.2.2-1.amzn2022.1.2` |
| `kernel-5.15.57-30.131.amzn2022` |
| `kernel-devel-5.15.57-30.131.amzn2022` |
| `kernel-headers-5.15.57-30.131.amzn2022` |
| `kernel-tools-5.15.57-30.131.amzn2022` |
| `kernel-tools-devel-5.15.57-30.131.amzn2022` |
| `microcode_ctl-2.1-53.amzn2022` |
| `perf-5.15.57-30.131.amzn2022` |
| `python3-bcc-0.24.0-2.amzn2022.0.1` |
| `python3-perf-5.15.57-30.131.amzn2022` |
| `sysctl-defaults-1.0-3.amzn2022` |
| `systemd-250.7-1.amzn2022.0.6` |
| `systemd-container-250.7-1.amzn2022.0.6` |
| `systemd-devel-250.7-1.amzn2022.0.6` |
| `systemd-journal-remote-250.7-1.amzn2022.0.6` |
| `systemd-libs-250.7-1.amzn2022.0.6` |
| `systemd-networkd-250.7-1.amzn2022.0.6` |
| `systemd-oomd-defaults-250.7-1.amzn2022.0.6` |
| `systemd-pam-250.7-1.amzn2022.0.6` |
| `systemd-resolved-250.7-1.amzn2022.0.6` |
| `systemd-rpm-macros-250.7-1.amzn2022.0.6` |
| `systemd-standalone-sysusers-250.7-1.amzn2022.0.6` |
| `systemd-standalone-tmpfiles-250.7-1.amzn2022.0.6` |
| `systemd-tests-250.7-1.amzn2022.0.6` |
| `systemd-udev-250.7-1.amzn2022.0.6` |
| `system-release-2022.0.20220831-0.amzn2022` |
| `tzdata-2022c-1.amzn2022.0.1` |
| `tzdata-java-2022c-1.amzn2022.0.1` |

## AMIs
<a name="amis-2022020220831"></a>

Docker Container image
+ `system-release-2022.0.20220831-0.amzn2022.noarch`
+ `tzdata-2022c-1.amzn2022.0.1.noarch`

Default AMI

|  |
| --- |
| `chrony-4.2-7.amzn2022.0.2.aarch64` |
| ` chrony-4.2-7.amzn2022.0.2.x86_64` |
| ` cloud-init-22.2.2-1.amzn2022.1.2.noarch` |
| ` kernel-5.15.57-30.131.amzn2022.aarch64` |
| ` kernel-5.15.57-30.131.amzn2022.x86_64` |
| ` kernel-tools-5.15.57-30.131.amzn2022.aarch64` |
| ` kernel-tools-5.15.57-30.131.amzn2022.x86_64` |
| ` microcode_ctl-2.1-53.amzn2022.x86_64` |
| ` sysctl-defaults-1.0-3.amzn2022.noarch` |
| ` systemd-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-libs-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-libs-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-networkd-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-networkd-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-pam-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-pam-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-resolved-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-resolved-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-udev-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-udev-250.7-1.amzn2022.0.6.x86_64` |
| ` system-release-2022.0.20220831-0.amzn2022.noarch` |
| ` tzdata-2022c-1.amzn2022.0.1.noarch` |

Minimal AMI

|  |
| --- |
| `chrony-4.2-7.amzn2022.0.2.aarch64` |
| ` chrony-4.2-7.amzn2022.0.2.x86_64` |
| ` cloud-init-22.2.2-1.amzn2022.1.2.noarch` |
| ` kernel-5.15.57-30.131.amzn2022.aarch64` |
| ` kernel-5.15.57-30.131.amzn2022.x86_64` |
| ` microcode_ctl-2.1-53.amzn2022.x86_64` |
| ` sysctl-defaults-1.0-3.amzn2022.noarch` |
| ` system-release-2022.0.20220831-0.amzn2022.noarch` |
| ` systemd-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-libs-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-libs-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-networkd-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-networkd-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-pam-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-pam-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-resolved-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-resolved-250.7-1.amzn2022.0.6.x86_64` |
| ` systemd-udev-250.7-1.amzn2022.0.6.aarch64` |
| ` systemd-udev-250.7-1.amzn2022.0.6.x86_64` |
| ` tzdata-2022c-1.amzn2022.0.1.noarch` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
