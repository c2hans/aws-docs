---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20220928.html
---

# Amazon Linux 2023 version 2022.0.20220928 release notes
<a name="relnotes-2022.0.20220928"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20220928"></a>

Amazon Linux 2022 includes the following major updates.
+ There have been some changes to the build flags that will propagate throughout the packages over the next few months.
+ Starting with [AL2023 version 2022.0.20220728](relnotes-2022.0.20220728.md), SELinux was switched from an enforcing to a permissive mode by default. You can change SELinux settings to enforced mode via command line by running the `setenforce` command.

Upcoming Changes in future Release Candidate AMIs and repos.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.
+ The kernel package will see changes to improve aspects of security and performance, and, while core functionality will be maintained, some unused or deprecated features may be removed in future Release Candidates.

**Java Ecosystem**
+ The `maven`, `xmvn`, and `javapackages-tools` should function as expected, but the versions present in this release have not yet been rebuilt after a bootstrap phase. These packages will be re-built without the use of `javapackages-bootstrap` before General Availability.

**Known Issues**
+ There is a known issue by which enabling FIPS mode with `update-crypto-policies —set FIPS` will result in a non functional system. This will be addressed in a future release.

**Security Updates**
+ For information on the CVEs addressed in this release, please refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2022.html).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2022/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about Amazon Linux 2022 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2022/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2022/issues/new/choose).

If you just have questions about Amazon Linux 2022, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2022/discussions). Feedback on Amazon Linux 2022 can also be provided through your designated AWS representative.

## Major changes since the first Tech Preview release
<a name="major-changes-20220928"></a>
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
+ `abseil-cpp-20210324.2-5.amzn2022.0.1`
+ `adcli-0.9.1-10.amzn2022.0.1`
+ `alsa-plugins-1.2.7.1-1.amzn2022.0.1`
+ `alsa-utils-1.2.7-1.amzn2022.0.1`
+ `mlocate-0.26-350.amzn2022`
+ `python3.10-3.10.4-1.amzn2022.0.1`
+ `re2-20211101-3.amzn2022`
+ `realmd-0.17.0-9.amzn2022.0.1`

The repository includes the following packages that were updated since the last release.

|  |
| --- |
| `alsa-lib-1.2.7.2-1.amzn2022` |
| `amazon-rpm-config-221-13.amzn2022` |
| `annobin-10.76-1.amzn2022.0.3` |
| `automake-1.16.5-9.amzn2022.0.1` |
| `aws-kinesis-agent-2.0.8-2.amzn2022` |
| `bind-9.16.27-1.amzn2022` |
| `clamav-0.103.7-1.amzn2022.0.1` |
| `clang-14.0.5-2.amzn2022.0.3` |
| `cloud-init-22.2.2-1.amzn2022.1.4` |
| `cppcheck-2.7.4-2.amzn2022.0.1` |
| `dnf-4.12.0-2.amzn2022.0.1` |
| `dracut-055-6.amzn2022.0.4` |
| `ecs-init-1.63.1-1.amzn2022` |
| `fio-3.32-2.amzn2022.0.1` |
| `gcc-11.3.1-2.amzn2022.0.6` |
| `gdb-12.1-5.amzn2022` |
| `giflib-5.2.1-9.amzn2022` |
| `glib2-2.73.2-678.amzn2022` |
| `gmp-6.2.1-2.amzn2022` |
| `gobject-introspection-1.73.0-2.amzn2022` |
| `golang-1.19.1-1.amzn2022.0.1` |
| `golang-github-cpuguy83-md2man-2.0.2-20.amzn2022` |
| `golist-0.10.1-11.amzn2022` |
| `go-rpm-macros-3.1.0-30.amzn2022` |
| `grep-3.8-1.amzn2022.0.1` |
| `highlight-4.2-2.amzn2022.0.1` |
| `kpatch-0.9.4-7.amzn2022` |
| `liblognorm-2.0.6-1.amzn2022.0.1` |
| `lz4-1.9.4-1.amzn2022` |
| `mcstrans-3.2-3.amzn2022.0.1` |
| `ocaml-4.13.1-4.amzn2022` |
| `ocaml-findlib-1.9.3-2.amzn2022.0.1` |
| `ocaml-labltk-8.06.11-3.amzn2022.0.1` |
| `ocaml-ocamlbuild-0.14.0-32.amzn2022.0.1` |
| `ocaml-srpm-macros-6-6.amzn2022` |
| `ocaml-zarith-1.12-5.amzn2022.0.1` |
| `pkgconf-1.7.3-7.amzn2022.0.1` |
| `pygobject3-3.42.2-2.amzn2022` |
| `qpdf-10.6.3-4.amzn2022.0.1` |
| `R-4.1.3-1.amzn2022.0.1` |
| `rpm-4.16.1.3-12.amzn2022.0.2` |
| `ruby3.1-3.1.2-169.amzn2022.0.1` |
| `sendmail-8.17.1-5.amzn2022.0.2` |
| `slang-2.3.2-9.amzn2022.0.1` |
| `systemd-250.8-1.amzn2022.0.1` |
| `system-release-2022.0.20220928-0.amzn2022` |
| `vim-9.0.327-1.amzn2022.0.1` |
| `vsftpd-3.0.5-1.amzn2022` |
| `wget-1.21.3-1.amzn2022` |
| `wireshark-3.6.7-1.amzn2022.0.2` |

## AMIs
<a name="amis-2022020220928"></a>

Docker Container image

|  |
| --- |
| ` dnf-4.12.0-2.amzn2022.0.1.noarch` |
| ` dnf-data-4.12.0-2.amzn2022.0.1.noarch` |
| ` glib2-2.73.2-678.amzn2022.aarch64` |
| ` glib2-2.73.2-678.amzn2022.x86_64` |
| ` gmp-6.2.1-2.amzn2022.aarch64` |
| ` gmp-6.2.1-2.amzn2022.x86_64` |
| ` grep-3.8-1.amzn2022.0.1.aarch64` |
| ` grep-3.8-1.amzn2022.0.1.x86_64` |
| ` libgcc-11.3.1-2.amzn2022.0.6.aarch64` |
| ` libgcc-11.3.1-2.amzn2022.0.6.x86_64` |
| ` libgomp-11.3.1-2.amzn2022.0.6.aarch64` |
| ` libgomp-11.3.1-2.amzn2022.0.6.x86_64` |
| ` libstdc-11.3.1-2.amzn2022.0.6.aarch64` |
| ` libstdc-11.3.1-2.amzn2022.0.6.x86_64` |
| ` lz4-libs-1.9.4-1.amzn2022.aarch64` |
| ` lz4-libs-1.9.4-1.amzn2022.x86_64` |
| `- pcre-8.44-3.amzn2022.1.aarch64` |
| `- pcre-8.44-3.amzn2022.1.x86_64` |
| ` python3-dnf-4.12.0-2.amzn2022.0.1.noarch` |
| ` python3-rpm-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` python3-rpm-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-build-libs-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-build-libs-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-libs-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-libs-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-sign-libs-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-sign-libs-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` system-release-2022.0.20220928-0.amzn2022.noarch` |
| ` vim-data-9.0.327-1.amzn2022.0.1.noarch` |
| ` vim-minimal-9.0.327-1.amzn2022.0.1.aarch64` |
| ` vim-minimal-9.0.327-1.amzn2022.0.1.x86_64` |
| ` yum-4.12.0-2.amzn2022.0.1.noarch` |

Default AMI

|  |
| --- |
| ` bind-libs-9.16.27-1.amzn2022.aarch64` |
| ` bind-libs-9.16.27-1.amzn2022.x86_64` |
| ` bind-license-9.16.27-1.amzn2022.noarch` |
| ` bind-utils-9.16.27-1.amzn2022.aarch64` |
| ` bind-utils-9.16.27-1.amzn2022.x86_64` |
| ` cloud-init-22.2.2-1.amzn2022.1.4.noarch` |
| ` dnf-4.12.0-2.amzn2022.0.1.noarch` |
| ` dnf-data-4.12.0-2.amzn2022.0.1.noarch` |
| ` dracut-055-6.amzn2022.0.4.aarch64` |
| ` dracut-055-6.amzn2022.0.4.x86_64` |
| ` dracut-config-generic-055-6.amzn2022.0.4.aarch64` |
| ` dracut-config-generic-055-6.amzn2022.0.4.x86_64` |
| ` glib2-2.73.2-678.amzn2022.aarch64` |
| ` glib2-2.73.2-678.amzn2022.x86_64` |
| ` gmp-6.2.1-2.amzn2022.aarch64` |
| ` gmp-6.2.1-2.amzn2022.x86_64` |
| ` grep-3.8-1.amzn2022.0.1.aarch64` |
| ` grep-3.8-1.amzn2022.0.1.x86_64` |
| ` kpatch-runtime-0.9.4-7.amzn2022.noarch` |
| ` libgcc-11.3.1-2.amzn2022.0.6.aarch64` |
| ` libgcc-11.3.1-2.amzn2022.0.6.x86_64` |
| ` libgomp-11.3.1-2.amzn2022.0.6.aarch64` |
| ` libgomp-11.3.1-2.amzn2022.0.6.x86_64` |
| ` libpkgconf-1.7.3-7.amzn2022.0.1.aarch64` |
| ` libpkgconf-1.7.3-7.amzn2022.0.1.x86_64` |
| ` libstdc-11.3.1-2.amzn2022.0.6.aarch64` |
| ` libstdc-11.3.1-2.amzn2022.0.6.x86_64` |
| ` lz4-libs-1.9.4-1.amzn2022.aarch64` |
| ` lz4-libs-1.9.4-1.amzn2022.x86_64` |
| `- pcre-8.44-3.amzn2022.1.aarch64` |
| `- pcre-8.44-3.amzn2022.1.x86_64` |
| ` pkgconf-1.7.3-7.amzn2022.0.1.aarch64` |
| ` pkgconf-1.7.3-7.amzn2022.0.1.x86_64` |
| ` pkgconf-m4-1.7.3-7.amzn2022.0.1.noarch` |
| ` pkgconf-pkg-config-1.7.3-7.amzn2022.0.1.aarch64` |
| ` pkgconf-pkg-config-1.7.3-7.amzn2022.0.1.x86_64` |
| ` python3-dnf-4.12.0-2.amzn2022.0.1.noarch` |
| ` python3-rpm-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` python3-rpm-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-build-libs-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-build-libs-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-libs-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-libs-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-plugin-selinux-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-plugin-selinux-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-sign-libs-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-sign-libs-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` slang-2.3.2-9.amzn2022.0.1.aarch64` |
| ` slang-2.3.2-9.amzn2022.0.1.x86_64` |
| ` systemd-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-libs-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-libs-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-networkd-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-networkd-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-pam-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-pam-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-resolved-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-resolved-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-udev-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-udev-250.8-1.amzn2022.0.1.x86_64` |
| ` system-release-2022.0.20220928-0.amzn2022.noarch` |
| ` vim-common-9.0.327-1.amzn2022.0.1.aarch64` |
| ` vim-common-9.0.327-1.amzn2022.0.1.x86_64` |
| ` vim-data-9.0.327-1.amzn2022.0.1.noarch` |
| ` vim-enhanced-9.0.327-1.amzn2022.0.1.aarch64` |
| ` vim-enhanced-9.0.327-1.amzn2022.0.1.x86_64` |
| ` vim-filesystem-9.0.327-1.amzn2022.0.1.noarch` |
| ` vim-minimal-9.0.327-1.amzn2022.0.1.aarch64` |
| ` vim-minimal-9.0.327-1.amzn2022.0.1.x86_64` |
| ` wget-1.21.3-1.amzn2022.aarch64` |
| ` wget-1.21.3-1.amzn2022.x86_64` |
| ` yum-4.12.0-2.amzn2022.0.1.noarch` |

Minimal AMI

|  |
| --- |
| ` cloud-init-22.2.2-1.amzn2022.1.4.noarch` |
| ` dnf-4.12.0-2.amzn2022.0.1.noarch` |
| ` dnf-data-4.12.0-2.amzn2022.0.1.noarch` |
| ` dracut-055-6.amzn2022.0.4.aarch64` |
| ` dracut-055-6.amzn2022.0.4.x86_64` |
| ` dracut-config-generic-055-6.amzn2022.0.4.aarch64` |
| ` dracut-config-generic-055-6.amzn2022.0.4.x86_64` |
| ` glib2-2.73.2-678.amzn2022.aarch64` |
| ` glib2-2.73.2-678.amzn2022.x86_64` |
| ` gmp-6.2.1-2.amzn2022.aarch64` |
| ` gmp-6.2.1-2.amzn2022.x86_64` |
| ` grep-3.8-1.amzn2022.0.1.aarch64` |
| ` grep-3.8-1.amzn2022.0.1.x86_64` |
| ` libgcc-11.3.1-2.amzn2022.0.6.aarch64` |
| ` libgcc-11.3.1-2.amzn2022.0.6.x86_64` |
| ` libgomp-11.3.1-2.amzn2022.0.6.aarch64` |
| ` libgomp-11.3.1-2.amzn2022.0.6.x86_64` |
| ` libstdc-11.3.1-2.amzn2022.0.6.aarch64` |
| ` libstdc-11.3.1-2.amzn2022.0.6.x86_64` |
| ` lz4-libs-1.9.4-1.amzn2022.aarch64` |
| ` lz4-libs-1.9.4-1.amzn2022.x86_64` |
| `- pcre-8.44-3.amzn2022.1.aarch64` |
| `- pcre-8.44-3.amzn2022.1.x86_64` |
| ` python3-dnf-4.12.0-2.amzn2022.0.1.noarch` |
| ` python3-rpm-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` python3-rpm-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-build-libs-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-build-libs-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-libs-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-libs-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-plugin-selinux-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-plugin-selinux-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` rpm-sign-libs-4.16.1.3-12.amzn2022.0.2.aarch64` |
| ` rpm-sign-libs-4.16.1.3-12.amzn2022.0.2.x86_64` |
| ` systemd-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-libs-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-libs-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-networkd-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-networkd-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-pam-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-pam-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-resolved-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-resolved-250.8-1.amzn2022.0.1.x86_64` |
| ` systemd-udev-250.8-1.amzn2022.0.1.aarch64` |
| ` systemd-udev-250.8-1.amzn2022.0.1.x86_64` |
| ` system-release-2022.0.20220928-0.amzn2022.noarch` |
| ` vim-data-9.0.327-1.amzn2022.0.1.noarch` |
| ` vim-minimal-9.0.327-1.amzn2022.0.1.aarch64` |
| ` vim-minimal-9.0.327-1.amzn2022.0.1.x86_64` |
| ` yum-4.12.0-2.amzn2022.0.1.noarch` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
