---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230222rc0.html
---

# Amazon Linux 2023 version 2023.0.20230222 (Release Candidate 0) release notes
<a name="relnotes-2023.0.20230222rc0"></a>

This topic includes release notes for a pre-GA version of Amazon Linux 2023 (AL2023). These release notes are for the 2023.0.20230222 Release Candidate 0 version of AL2023.

## Major updates
<a name="major-updates-20230222"></a>

This is an updated Release Candidate (RC) for Amazon Linux 2023 (AL2023), **RC0**. It's the successor of Amazon Linux 2, previously called Amazon Linux 2022.

An RC is a version that is nearly ready for release, but is still being tested. An RC receives only patches and bug fixes leading to the AL2023 Generally Available (GA) release. A GA distribution feature set is stable with no major changes expected between the final RC and the GA versions.

An RC version is not intended for production workloads. It's intended for testing purposes and to help you prepare for migration to AL2023.

Review [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) for more details on the changes since Amazon Linux 2.

AL2023 includes the following major updates.
+ Kernel updated from 5.15 to 6.1
+ This release represents the updated Release Candidate (RC) for AL2023 (previously Amazon Linux 2022). You can use the Release Candidate to test compatibility with your applications or prepare for migration to AL2023.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor.

**Known Issues**
+ Kernel livepatch isn't enabled in AL2023 **RC0**, but it will be enabled before AL2023 GA.
+ AL2023 contains a known issue where customer defined NTP servers via DHCP are not honored.

  **Work-Around** - Configure the NTP servers using a config file in `/etc/chrony.d`
+ Enabling FIPS mode is currently unsupported, and there will be changes to how a FIPS mode enabled system works in upcoming releases.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you just have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-20230222)
+ [Repository](#amis-2023020230222.repository)
+ [Docker container image](#amis-2023020230222.container-image)
+ [Default AMI](#amis-2023020230222.default-ami)
+ [Minimal AMI](#amis-2023020230222.minimal-ami)

## Repository
<a name="amis-2023020230222.repository"></a>

The repository includes the following packages that were **updated** since the last release.

|  |
| --- |
| `cni-plugins-1.2.0-1.amzn2023.0.1.src` |
| `nerdctl-1.1.0-1.amzn2023.0.1.src` |
| `python-tomli-2.0.1-4.amzn2023.src` |
| `python-tomli-w-1.0.0-4.amzn2023.src` |
| `ruby3.2-3.2.0-177.amzn2023.0.1.src` |
| `rubygem-mustache-1.1.1-3.amzn2023.0.1.src` |

The repository includes the following packages that were **removed** since the last release.

|  |
| --- |
| `aws-c-auth-0.6.5-6.amzn2022.0.2.src` |
| `aws-c-cal-0.5.12-7.amzn2022.0.2.src` |
| `aws-c-common-0.6.14-6.amzn2022.0.2.src` |
| `aws-c-compression-0.2.14-5.amzn2022.0.2.src` |
| `aws-c-event-stream-0.2.7-5.amzn2022.0.2.src` |
| `aws-checksums-0.1.12-5.amzn2022.0.2.src` |
| `aws-c-http-0.6.8-6.amzn2022.0.2.src` |
| `aws-c-io-0.10.12-5.amzn2022.0.7.src` |
| `aws-c-mqtt-0.7.8-7.amzn2022.0.2.src` |
| `aws-c-s3-0.1.27-5.amzn2022.0.3.src` |
| `aws-c-sdkutils-0.1.1-5.amzn2022.0.2.src` |
| `linkchecker-9.4.0-12.20191005.d13b3f5.amzn2022.0.2.src` |
| `python3.10-3.10.9-1.amzn2022.0.1.src` |
| `python-beautifulsoup4-4.9.3-2.amzn2022.src` |
| `python-graphviz-1:0.16-2.amzn2022.src` |
| `python-nose-1.3.7-33.amzn2022.src` |
| `python-parameterized-0.7.4-2.amzn2022.0.1.src` |
| `python-soupsieve-2.3.1-23.amzn2022.src` |
| `python-sure-1.4.11-63.amzn2022.src` |
| `python-tempita-0.5.1-29.amzn2022.src` |
| `ruby3.1-3.1.3-173.amzn2022.0.1.src` |
| `rubypick-1.1.1-14.amzn2022.src` |
| `s2n-tls-1.3.24-1.amzn2022.0.2.src` |

The repository includes the following packages that were **updated** since the last release.

|  |
| --- |
| `amazon-cloudwatch-agent-1.247358.0-1.amzn2023.src` |
| `amazon-efs-utils-1.34.5-1.amzn2023.src` |
| `amazon-ssm-agent-3.1.1927.0-1.amzn2023.src` |
| `apache-commons-compress-1.21-4.amzn2023.0.3.src` |
| `apache-commons-lang3-3.12.0-7.amzn2023.0.3.src` |
| `apache-commons-net-3.6-17.amzn2023.0.1.src` |
| `apr-1.7.2-2.amzn2023.0.2.src` |
| `apr-util-1.6.3-1.amzn2023.0.1.src` |
| `atlas-3.10.3-18.amzn2023.0.2.src` |
| `aws-cfn-bootstrap-2.0-23.amzn2023.src` |
| `awscli-2-2.9.19-1.amzn2023.0.1.src` |
| `bcc-0.26.0-1.amzn2023.0.1.src` |
| `bpftrace-0.17.0-1.amzn2023.src` |
| `capstone-4.0.2-9.amzn2023.0.3.src` |
| `cdi-api-2.0.2-6.amzn2023.0.3.src` |
| `clamav-0.103.8-1.amzn2023.0.1.src` |
| `container-selinux-2:2.189.0-289.amzn2023.0.2.src` |
| `curl-7.88.0-1.amzn2023.0.1.src` |
| `dbus-broker-32-1.amzn2023.0.2.src` |
| `ecs-init-1.68.2-1.amzn2023.src` |
| `git-2.39.2-1.amzn2023.0.1.src` |
| `glib2-2.73.2-680.amzn2023.0.3.src` |
| `gnulib-0-43.20220212git.amzn2023.0.2.src` |
| `gnutls-3.7.7-357.amzn2023.0.2.src` |
| `golang-github-cpuguy83-md2man-2.0.2-22.amzn2023.0.2.src` |
| `go-rpm-macros-3.1.0-32.amzn2023.0.2.src` |
| `grpc-1.41.1-9.amzn2023.src` |
| `grub2-1:2.06-61.amzn2023.0.3.src` |
| `gzip-1.12-1.amzn2023.0.1.src` |
| `harfbuzz-7.0.0-2.amzn2023.0.1.src` |
| `htop-3.2.1-87.amzn2023.0.3.src` |
| `ibus-anthy-1.5.14-4.amzn2023.0.1.src` |
| `jansson-2.14-0.amzn2023.src` |
| `jctools-3.3.0-5.amzn2023.0.3.src` |
| `kernel-6.1.12-19.43.amzn2023.src` |
| `libblockdev-2.28-2.amzn2023.0.1.src` |
| `libcgroup-3.0-1.amzn2023.0.1.src` |
| `libdbi-0.9.0-20.amzn2023.0.1.src` |
| `libgcrypt-1.10.1-7.amzn2023.0.1.src` |
| `libjpeg-turbo-2.1.4-2.amzn2023.0.2.src` |
| `libkcapi-1.4.0-105.amzn2023.0.1.src` |
| `libksba-1.6.3-1.amzn2023.0.2.src` |
| `libldb-2.6.1-1.amzn2023.0.2.src` |
| `libtevent-0.13.0-1.amzn2023.0.2.src` |
| `libtirpc-1.3.3-0.amzn2023.src` |
| `libtommath-1.2.0-9.amzn2023.0.1.src` |
| `libuv-1:1.44.1-156.amzn2023.0.2.src` |
| `libXpm-3.5.15-2.amzn2023.0.1.src` |
| `mesa-22.3.3-1140.amzn2023.0.3.src` |
| `meson-0.62.2-205.amzn2023.0.2.src` |
| `mlocate-0.26-351.amzn2023.src` |
| `nodejs-1:18.12.1-1.amzn2023.0.2.src` |
| `ocl-icd-2.3.1-2.amzn2023.0.2.src` |
| `openssl-1:3.0.8-1.amzn2023.0.1.src` |
| `package-notes-0.4-18.amzn2023.0.5.src` |
| `php8.1-8.1.14-1.amzn2023.0.2.src` |
| `plexus-i18n-1.0-0.19.b10.4.amzn2023.0.3.src` |
| `protobuf-3.19.6-1.amzn2023.0.1.src` |
| `pv-1.6.20-63.amzn2023.0.3.src` |
| `python-awscrt-0.16.7-1.amzn2023.0.1.src` |
| `python-certifi-2022.12.07-1.amzn2023.0.1.src` |
| `python-elementpath-2.3.2-2.amzn2023.src` |
| `python-flit-3.7.1-4.amzn2023.0.1.src` |
| `python-progressbar2-3.52.1-23.amzn2023.0.2.src` |
| `python-pytest-cov-3.0.0-67.amzn2023.0.2.src` |
| `python-simplejson-3.17.6-111.amzn2023.0.2.src` |
| `python-twisted-22.4.0-124.amzn2023.0.2.src` |
| `pytz-2022.7.1-1.amzn2023.src` |
| `rsyslog-8.2204.0-3.amzn2023.0.2.src` |
| `rubygem-asciidoctor-2.0.15-3.amzn2023.0.1.src` |
| `rust-packaging-21-88.amzn2023.0.2.src` |
| `rust-srpm-macros-21-42.amzn2023.0.2.src` |
| `samba-2:4.17.5-0.amzn2023.0.2.src` |
| `shadow-utils-2:4.9-12.amzn2023.0.2.src` |
| `shared-mime-info-2.2-2.amzn2023.0.1.src` |
| `spirv-headers-1.5.5-42.amzn2023.0.1.src` |
| `sscg-3.0.1-61.amzn2023.0.2.src` |
| `sudo-1.9.12-1.p2.amzn2023.0.2.src` |
| `swig-4.1.1-4.amzn2023.0.3.src` |
| `systemd-252.4-1161.amzn2023.0.1.src` |
| `system-release-2023.0.20230222-0.amzn2023.src` |
| `systemtap-4.8-3.amzn2023.0.5.src` |
| `tcsh-6.24.07-1.amzn2023.src` |
| `vim-2:9.0.1160-1.amzn2023.0.2.src` |
| `vulkan-headers-1.3.224.0-1.amzn2023.0.1.src` |
| `vulkan-loader-1.3.224.0-1.amzn2023.0.1.src` |
| `xdg-utils-1.1.3-12.amzn2023.0.1.src` |
| `xfsdump-3.1.11-2.amzn2023.0.2.src` |
| `xmlrpc-c-1.51.08-2.amzn2023.0.1.src` |
| `xorg-x11-server-1.20.14-12.amzn2023.0.2.src` |

## Docker container image
<a name="amis-2023020230222.container-image"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-cdn-2023.0.20230222-0.amzn2023.noarch` |
| `curl-minimal-7.88.0-1.amzn2023.0.1.aarch64` |
| `curl-minimal-7.88.0-1.amzn2023.0.1.x86_64` |
| `glib2-2.73.2-680.amzn2023.0.3.aarch64` |
| `glib2-2.73.2-680.amzn2023.0.3.x86_64` |
| `libcurl-minimal-7.88.0-1.amzn2023.0.1.aarch64` |
| `libcurl-minimal-7.88.0-1.amzn2023.0.1.x86_64` |
| `libgcrypt-1.10.1-7.amzn2023.0.1.aarch64` |
| `libgcrypt-1.10.1-7.amzn2023.0.1.x86_64` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.1.aarch64` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.1.x86_64` |
| `system-release-2023.0.20230222-0.amzn2023.noarch` |
| `vim-data-2:9.0.1160-1.amzn2023.0.2.noarch` |
| `vim-minimal-2:9.0.1160-1.amzn2023.0.2.aarch64` |
| `vim-minimal-2:9.0.1160-1.amzn2023.0.2.x86_64` |

## Default AMI
<a name="amis-2023020230222.default-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230222-0.amzn2023.noarch` |
| `amazon-ssm-agent-3.1.1927.0-1.amzn2023.aarch64` |
| `amazon-ssm-agent-3.1.1927.0-1.amzn2023.x86_64` |
| `aws-cfn-bootstrap-2.0-23.amzn2023.noarch` |
| `awscli-2-2.9.19-1.amzn2023.0.1.noarch` |
| `curl-minimal-7.88.0-1.amzn2023.0.1.aarch64` |
| `curl-minimal-7.88.0-1.amzn2023.0.1.x86_64` |
| `dbus-broker-32-1.amzn2023.0.2.aarch64` |
| `dbus-broker-32-1.amzn2023.0.2.x86_64` |
| `glib2-2.73.2-680.amzn2023.0.3.aarch64` |
| `glib2-2.73.2-680.amzn2023.0.3.x86_64` |
| `gnutls-3.7.7-357.amzn2023.0.2.aarch64` |
| `gnutls-3.7.7-357.amzn2023.0.2.x86_64` |
| `go-srpm-macros-3.1.0-32.amzn2023.0.2.noarch` |
| `grub2-common-1:2.06-61.amzn2023.0.3.noarch` |
| `grub2-efi-aa64-ec2-1:2.06-61.amzn2023.0.3.aarch64` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.3.x86_64` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.3.noarch` |
| `grub2-tools-1:2.06-61.amzn2023.0.3.aarch64` |
| `grub2-tools-1:2.06-61.amzn2023.0.3.x86_64` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.3.aarch64` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.3.x86_64` |
| `gzip-1.12-1.amzn2023.0.1.aarch64` |
| `gzip-1.12-1.amzn2023.0.1.x86_64` |
| `jansson-2.14-0.amzn2023.aarch64` |
| `jansson-2.14-0.amzn2023.x86_64` |
| `kernel-6.1.12-19.43.amzn2023.aarch64` |
| `kernel-6.1.12-19.43.amzn2023.x86_64` |
| `kernel-livepatch-repo-s3-2023.0.20230222-0.amzn2023.noarch` |
| `kernel-tools-6.1.12-19.43.amzn2023.aarch64` |
| `kernel-tools-6.1.12-19.43.amzn2023.x86_64` |
| `libcurl-minimal-7.88.0-1.amzn2023.0.1.aarch64` |
| `libcurl-minimal-7.88.0-1.amzn2023.0.1.x86_64` |
| `libgcrypt-1.10.1-7.amzn2023.0.1.aarch64` |
| `libgcrypt-1.10.1-7.amzn2023.0.1.x86_64` |
| `libkcapi-1.4.0-105.amzn2023.0.1.aarch64` |

The following packages have been **removed**.

|  |
| --- |
| `aws-c-auth-libs-0.6.5-6.amzn2023.0.2.aarch64` |
| `aws-c-auth-libs-0.6.5-6.amzn2023.0.2.x86_64` |
| `aws-c-cal-libs-0.5.12-7.amzn2023.0.2.aarch64` |
| `aws-c-cal-libs-0.5.12-7.amzn2023.0.2.x86_64` |
| `aws-c-common-libs-0.6.14-6.amzn2023.0.2.aarch64` |
| `aws-c-common-libs-0.6.14-6.amzn2023.0.2.x86_64` |
| `aws-c-compression-libs-0.2.14-5.amzn2023.0.2.aarch64` |
| `aws-c-compression-libs-0.2.14-5.amzn2023.0.2.x86_64` |
| `aws-c-event-stream-libs-0.2.7-5.amzn2023.0.2.aarch64` |
| `aws-c-event-stream-libs-0.2.7-5.amzn2023.0.2.x86_64` |
| `aws-checksums-libs-0.1.12-5.amzn2023.0.2.aarch64` |
| `aws-checksums-libs-0.1.12-5.amzn2023.0.2.x86_64` |
| `aws-c-http-libs-0.6.8-6.amzn2023.0.2.aarch64` |
| `aws-c-http-libs-0.6.8-6.amzn2023.0.2.x86_64` |
| `aws-c-io-libs-0.10.12-5.amzn2023.0.7.aarch64` |
| `aws-c-io-libs-0.10.12-5.amzn2023.0.7.x86_64` |
| `aws-c-mqtt-libs-0.7.8-7.amzn2023.0.2.aarch64` |
| `aws-c-mqtt-libs-0.7.8-7.amzn2023.0.2.x86_64` |
| `aws-c-s3-libs-0.1.27-5.amzn2023.0.3.aarch64` |
| `aws-c-s3-libs-0.1.27-5.amzn2023.0.3.x86_64` |
| `aws-c-sdkutils-libs-0.1.1-5.amzn2023.0.2.aarch64` |
| `aws-c-sdkutils-libs-0.1.1-5.amzn2023.0.2.x86_64` |
| `s2n-tls-1.3.24-1.amzn2023.0.2.aarch64` |
| `s2n-tls-1.3.24-1.amzn2023.0.2.x86_64` |
| `s2n-tls-libs-1.3.24-1.amzn2023.0.2.aarch64` |
| `s2n-tls-libs-1.3.24-1.amzn2023.0.2.x86_64` |

## Minimal AMI
<a name="amis-2023020230222.minimal-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230222-0.amzn2023.noarch` |
| `awscli-2-2.9.19-1.amzn2023.0.1.noarch` |
| `curl-minimal-7.88.0-1.amzn2023.0.1.aarch64` |
| `curl-minimal-7.88.0-1.amzn2023.0.1.x86_64` |
| `dbus-broker-32-1.amzn2023.0.2.aarch64` |
| `dbus-broker-32-1.amzn2023.0.2.x86_64` |
| `glib2-2.73.2-680.amzn2023.0.3.aarch64` |
| `glib2-2.73.2-680.amzn2023.0.3.x86_64` |
| `gnutls-3.7.7-357.amzn2023.0.2.aarch64` |
| `gnutls-3.7.7-357.amzn2023.0.2.x86_64` |
| `grub2-common-1:2.06-61.amzn2023.0.3.noarch` |
| `grub2-efi-aa64-ec2-1:2.06-61.amzn2023.0.3.aarch64` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.3.x86_64` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.3.noarch` |
| `grub2-tools-1:2.06-61.amzn2023.0.3.aarch64` |
| `grub2-tools-1:2.06-61.amzn2023.0.3.x86_64` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.3.aarch64` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.3.x86_64` |
| `gzip-1.12-1.amzn2023.0.1.aarch64` |
| `gzip-1.12-1.amzn2023.0.1.x86_64` |
| `jansson-2.14-0.amzn2023.aarch64` |
| `jansson-2.14-0.amzn2023.x86_64` |
| `kernel-6.1.12-19.43.amzn2023.aarch64` |
| `kernel-6.1.12-19.43.amzn2023.x86_64` |
| `kernel-livepatch-repo-s3-2023.0.20230222-0.amzn2023.noarch` |
| `libcurl-minimal-7.88.0-1.amzn2023.0.1.aarch64` |
| `libcurl-minimal-7.88.0-1.amzn2023.0.1.x86_64` |
| `libgcrypt-1.10.1-7.amzn2023.0.1.aarch64` |
| `libgcrypt-1.10.1-7.amzn2023.0.1.x86_64` |
| `libkcapi-1.4.0-105.amzn2023.0.1.aarch64` |
| `libkcapi-1.4.0-105.amzn2023.0.1.x86_64` |
| `libkcapi-hmaccalc-1.4.0-105.amzn2023.0.1.aarch64` |
| `libkcapi-hmaccalc-1.4.0-105.amzn2023.0.1.x86_64` |
| `openssl-1:3.0.8-1.amzn2023.0.1.aarch64` |
| `openssl-1:3.0.8-1.amzn2023.0.1.x86_64` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.1.aarch64` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.1.x86_64` |
| `python3-awscrt-0.16.7-1.amzn2023.0.1.aarch64` |
| `python3-awscrt-0.16.7-1.amzn2023.0.1.x86_64` |
| `python3-pytz-2022.7.1-1.amzn2023.noarch` |
| `shadow-utils-2:4.9-12.amzn2023.0.2.aarch64` |
| `shadow-utils-2:4.9-12.amzn2023.0.2.x86_64` |
| `sudo-1.9.12-1.p2.amzn2023.0.2.aarch64` |
| `sudo-1.9.12-1.p2.amzn2023.0.2.x86_64` |
| `systemd-252.4-1161.amzn2023.0.1.aarch64` |
| `systemd-252.4-1161.amzn2023.0.1.x86_64` |
| `systemd-libs-252.4-1161.amzn2023.0.1.aarch64` |
| `systemd-libs-252.4-1161.amzn2023.0.1.x86_64` |
| `systemd-networkd-252.4-1161.amzn2023.0.1.aarch64` |
| `systemd-networkd-252.4-1161.amzn2023.0.1.x86_64` |
| `systemd-pam-252.4-1161.amzn2023.0.1.aarch64` |
| `systemd-pam-252.4-1161.amzn2023.0.1.x86_64` |
| `systemd-resolved-252.4-1161.amzn2023.0.1.aarch64` |
| `systemd-resolved-252.4-1161.amzn2023.0.1.x86_64` |
| `systemd-udev-252.4-1161.amzn2023.0.1.aarch64` |
| `systemd-udev-252.4-1161.amzn2023.0.1.x86_64` |
| `system-release-2023.0.20230222-0.amzn2023.noarch` |
| `vim-data-2:9.0.1160-1.amzn2023.0.2.noarch` |
| `vim-minimal-2:9.0.1160-1.amzn2023.0.2.aarch64` |
| `vim-minimal-2:9.0.1160-1.amzn2023.0.2.x86_64` |

The following packages have been **removed**.

|  |
| --- |
| `aws-c-auth-libs-0.6.5-6.amzn2023.0.2.aarch64` |
| `aws-c-auth-libs-0.6.5-6.amzn2023.0.2.x86_64` |
| `aws-c-cal-libs-0.5.12-7.amzn2023.0.2.aarch64` |
| `aws-c-cal-libs-0.5.12-7.amzn2023.0.2.x86_64` |
| `aws-c-common-libs-0.6.14-6.amzn2023.0.2.aarch64` |
| `aws-c-common-libs-0.6.14-6.amzn2023.0.2.x86_64` |
| `aws-c-compression-libs-0.2.14-5.amzn2023.0.2.aarch64` |
| `aws-c-compression-libs-0.2.14-5.amzn2023.0.2.x86_64` |
| `aws-c-event-stream-libs-0.2.7-5.amzn2023.0.2.aarch64` |
| `aws-c-event-stream-libs-0.2.7-5.amzn2023.0.2.x86_64` |
| `aws-checksums-libs-0.1.12-5.amzn2023.0.2.aarch64` |
| `aws-checksums-libs-0.1.12-5.amzn2023.0.2.x86_64` |
| `aws-c-http-libs-0.6.8-6.amzn2023.0.2.aarch64` |
| `aws-c-http-libs-0.6.8-6.amzn2023.0.2.x86_64` |
| `aws-c-io-libs-0.10.12-5.amzn2023.0.7.aarch64` |
| `aws-c-io-libs-0.10.12-5.amzn2023.0.7.x86_64` |
| `aws-c-mqtt-libs-0.7.8-7.amzn2023.0.2.aarch64` |
| `aws-c-mqtt-libs-0.7.8-7.amzn2023.0.2.x86_64` |
| `aws-c-s3-libs-0.1.27-5.amzn2023.0.3.aarch64` |
| `aws-c-s3-libs-0.1.27-5.amzn2023.0.3.x86_64` |
| `aws-c-sdkutils-libs-0.1.1-5.amzn2023.0.2.aarch64` |
| `aws-c-sdkutils-libs-0.1.1-5.amzn2023.0.2.x86_64` |
| `s2n-tls-1.3.24-1.amzn2023.0.2.aarch64` |
| `s2n-tls-1.3.24-1.amzn2023.0.2.x86_64` |
| `s2n-tls-libs-1.3.24-1.amzn2023.0.2.aarch64` |
| `s2n-tls-libs-1.3.24-1.amzn2023.0.2.x86_64` |
