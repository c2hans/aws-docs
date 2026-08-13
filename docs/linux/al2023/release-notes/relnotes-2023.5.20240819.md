---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240819.html
---

# Amazon Linux 2023 version 2023.5.20240819 release notes
<a name="relnotes-2023.5.20240819"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.5.20240819.

**Topics**
+ [Major updates](#major-updates-2023.5.20240819)
+ [Repository](#amis-2023.5.20240819.repository)
+ [Docker container image](#amis-2023.5.20240819.container-image)
+ [Default AMI](#amis-2023.5.20240819.default-ami)
+ [Minimal AMI](#amis-2023.5.20240819.minimal-ami)
+ [Minimal container image](#amis-2023.5.20240819.minimal-container-ami)
+ [Contact us](#amis-2023.5.20240819.contact-us)

## Major updates
<a name="major-updates-2023.5.20240819"></a>

This release represents an update to the fifth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Known Issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.5.20240819.repository"></a>

### New packages in AL2023.5.20240819 since AL2023.5.20240805
<a name="new-AL2023.5.20240805-AL2023.5.20240819"></a>

 Comparing AL2023.5.20240805 version 2023.5.20240805 to AL2023.5.20240819 version [2023.5.20240819](#relnotes-2023.5.20240819).

| Package Type | Number of new packages in AL2023.5.20240819 compared to AL2023.5.20240805 |
| --- | --- |
| Source RPMs | 5 |
| Total Binary RPMs | 27 |
|  noarch binary RPMs | 3 |
|  x86\_64 binary RPMs | 12 |
|  aarch64 binary RPMs | 12 |

New packages in AL2023.5.20240819:

- ** `can-utils` **
  - **RPM:**  can-utils
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2023.03-3.amzn2023

- ** `freerdp` **
  - **RPM:**  freerdp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freerdp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freerdp-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freerdp-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwinpr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwinpr-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.6.3-1.amzn2023

- ** `hwdata` **
  - **RPM:**  hwdata-devel
  - **Architectures:** noarch
  - **Version:** 0.384-1.amzn2023.0.3

- ** `libarchive` **
  - **RPM:**  bsdunzip
  - **Architectures:** aarch64, x86\_64
  - **Version:** 3.7.4-2.amzn2023.0.1

- ** `linux-firmware` **
  - **RPM:**  amd-ucode-firmware
  - **Architectures:** noarch
  - **Version:** 20210208-117.amzn2023.0.6

- ** `meson1` **
  - **RPM:**  meson1
  - **Architectures:** noarch
  - **Version:** 1.4.1-243.amzn2023

- ** `seatd` **
  - **RPM:**  libseat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libseat-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.8.0-2.amzn2023.0.1

- ** `xcb-util-cursor` **
  - **RPM:**  xcb-util-cursor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-cursor-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.1.4-4.amzn2023

### AL2023.5.20240819 upgrades from AL2023.5.20240805
<a name="vercmp-AL2023.5.20240805-AL2023.5.20240819"></a>

 Comparing [2023.5.20240805](relnotes-2023.5.20240805.md) to [2023.5.20240819](#relnotes-2023.5.20240819).

| Package Type | Count |
| --- | --- |
| Source | 19 |
| Total Binary | 373 |
|  noarch binary RPMs | 244 |
|  x86\_64 binary RPMs | 65 |
|  aarch64 binary RPMs | 64 |

The full comparison of RPM package versions is below.

- ** [`amazon-ec2-net-utils`](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html) **
  - **RPM:**  [`amazon-ec2-net-utils`](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html)
  - **Architectures:** noarch
  - **AL2023.5.20240805 version:** 2.4.1-1.amzn2023.0.1
  - **AL2023.5.20240819 version:** 2.5.1-1.amzn2023.0.1

- ** `bind` **
  - **RPM:**  bind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-chroot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-sqlite3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dnssec-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-doc  / **Architectures:** noarch
  - **RPM:**  bind-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-license  / **Architectures:** noarch
  - **RPM:**  bind-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240805 version:** 9.18.28-1.amzn2023.0.1
  - **AL2023.5.20240819 version:** 9.18.28-1.amzn2023.0.2

- ** `distribution-gpg-keys` **
  - **RPM:**  distribution-gpg-keys  / **Architectures:** noarch
  - **RPM:**  distribution-gpg-keys-copr  / **Architectures:** noarch
  - **AL2023.5.20240805 version:** 1.100-1.amzn2023.0.1
  - **AL2023.5.20240819 version:** 1.104-1.amzn2023.0.1

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240805 version:** 1.85.3-1.amzn2023
  - **AL2023.5.20240819 version:** 1.86.0-1.amzn2023

- ** `freeipa` **
  - **RPM:**  freeipa-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipa-client-common  / **Architectures:** noarch
  - **RPM:**  freeipa-client-epn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipa-client-samba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipa-common  / **Architectures:** noarch
  - **RPM:**  freeipa-python-compat  / **Architectures:** noarch
  - **RPM:**  freeipa-selinux  / **Architectures:** noarch
  - **RPM:**  freeipa-selinux-luna  / **Architectures:** noarch
  - **RPM:**  freeipa-selinux-nfast  / **Architectures:** noarch
  - **RPM:**  python3-ipaclient  / **Architectures:** noarch
  - **RPM:**  python3-ipalib  / **Architectures:** noarch
  - **AL2023.5.20240805 version:** 4.12.0-1.amzn2023.0.1
  - **AL2023.5.20240819 version:** 4.12.0-1.amzn2023.0.2

- ** `hwdata` **
  - **RPM:**  hwdata
  - **Architectures:** noarch
  - **AL2023.5.20240805 version:** 0.353-1.amzn2023.0.3
  - **AL2023.5.20240819 version:** 0.384-1.amzn2023.0.3

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
  - **AL2023.5.20240805 version:** 6.1.102-108.177.amzn2023
  - **AL2023.5.20240819 version:** 6.1.102-111.182.amzn2023

- ** `libarchive` **
  - **RPM:**  bsdcat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bsdcpio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bsdtar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libarchive  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libarchive-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240805 version:** 3.5.3-2.amzn2023.0.3
  - **AL2023.5.20240819 version:** 3.7.4-2.amzn2023.0.1

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240805 version:** 15.7-1.amzn2023.0.1
  - **AL2023.5.20240819 version:** 15.8-1.amzn2023.0.1

- ** `linux-firmware` **
  - **RPM:**  iwl1000-firmware  / **Architectures:** noarch
  - **RPM:**  iwl100-firmware  / **Architectures:** noarch
  - **RPM:**  iwl105-firmware  / **Architectures:** noarch
  - **RPM:**  iwl135-firmware  / **Architectures:** noarch
  - **RPM:**  iwl2000-firmware  / **Architectures:** noarch
  - **RPM:**  iwl2030-firmware  / **Architectures:** noarch
  - **RPM:**  iwl3160-firmware  / **Architectures:** noarch
  - **RPM:**  iwl3945-firmware  / **Architectures:** noarch
  - **RPM:**  iwl4965-firmware  / **Architectures:** noarch
  - **RPM:**  iwl5000-firmware  / **Architectures:** noarch
  - **RPM:**  iwl5150-firmware  / **Architectures:** noarch
  - **RPM:**  iwl6000-firmware  / **Architectures:** noarch
  - **RPM:**  iwl6000g2a-firmware  / **Architectures:** noarch
  - **RPM:**  iwl6000g2b-firmware  / **Architectures:** noarch
  - **RPM:**  iwl6050-firmware  / **Architectures:** noarch
  - **RPM:**  iwl7260-firmware  / **Architectures:** noarch
  - **RPM:**  libertas-sd8686-firmware  / **Architectures:** noarch
  - **RPM:**  libertas-sd8787-firmware  / **Architectures:** noarch
  - **RPM:**  libertas-usb8388-firmware  / **Architectures:** noarch
  - **RPM:**  libertas-usb8388-olpc-firmware  / **Architectures:** noarch
  - **RPM:**  linux-firmware  / **Architectures:** noarch
  - **RPM:**  linux-firmware-whence  / **Architectures:** noarch
  - **RPM:**  liquidio-firmware  / **Architectures:** noarch
  - **RPM:**  netronome-firmware  / **Architectures:** noarch
  - **AL2023.5.20240805 version:** 39.31.5.1-117.amzn2023.0.5
  - **AL2023.5.20240819 version:** 39.31.5.1-117.amzn2023.0.6

- ** `meson` **
  - **RPM:**  meson
  - **Architectures:** noarch
  - **AL2023.5.20240805 version:** 0.62.2-205.amzn2023.0.2
  - **AL2023.5.20240819 version:** 0.63.3-1.amzn2023.0.2

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2023.5.20240805 version:** 2.1-53.amzn2023.0.7
  - **AL2023.5.20240819 version:** 2.1-53.amzn2023.0.8

- ** `p7zip` **
  - **RPM:**  p7zip  / **Architectures:** aarch64, x86\_64
  - **RPM:**  p7zip-doc  / **Architectures:** noarch
  - **RPM:**  p7zip-plugins  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240805 version:** 16.02-20.amzn2023.0.5
  - **AL2023.5.20240819 version:** 16.02-20.amzn2023.0.6

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
  - **AL2023.5.20240805 version:** 15.7-1.amzn2023.0.1
  - **AL2023.5.20240819 version:** 15.8-1.amzn2023.0.1

- ** `ruby3.2` **
  - **RPM:**  ruby3.2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-bundled-gems  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-default-gems  / **Architectures:** noarch
  - **RPM:**  ruby3.2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-doc  / **Architectures:** noarch
  - **RPM:**  ruby3.2-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-bigdecimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-bundler  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-io-console  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-irb  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-json  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-minitest  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-power\_assert  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-psych  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-rake  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rbs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-rdoc  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rexml  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rss  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygems  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygems-devel  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-test-unit  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-typeprof  / **Architectures:** noarch
  - **AL2023.5.20240805 version:** 3.2.2-180.amzn2023.0.2
  - **AL2023.5.20240819 version:** 3.2.2-180.amzn2023.0.3

- ** `stress` **
  - **RPM:**  stress
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240805 version:** 1.0.4-28.amzn2023.0.2
  - **AL2023.5.20240819 version:** 1.0.7-2.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.5.20240805 version:** 2023.5.20240805-0.amzn2023
  - **AL2023.5.20240819 version:** 2023.5.20240819-0.amzn2023

- ** `tpm2-tss` **
  - **RPM:**  tpm2-tss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tpm2-tss-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tpm2-tss-fapi  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240805 version:** 4.0.1-6.amzn2023
  - **AL2023.5.20240819 version:** 4.0.2-1.amzn2023

- ** `wayland-protocols` **
  - **RPM:**  wayland-protocols-devel
  - **Architectures:** noarch
  - **AL2023.5.20240805 version:** 1.25-1.amzn2023.0.2
  - **AL2023.5.20240819 version:** 1.36-1.amzn2023.0.1

## Docker container image
<a name="amis-2023.5.20240819.container-image"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240819-0.amzn2023` |
| `libarchive-3.7.4-2.amzn2023.0.1` |
| `system-release-2023.5.20240819-0.amzn2023` |

## Default AMI
<a name="amis-2023.5.20240819.default-ami"></a>

|  |
| --- |
| `amazon-ec2-net-utils-2.5.1-1.amzn2023.0.1` |
| `amazon-linux-repo-s3-2023.5.20240819-0.amzn2023` |
| `bind-libs-32:9.18.28-1.amzn2023.0.2` |
| `bind-license-32:9.18.28-1.amzn2023.0.2` |
| `bind-utils-32:9.18.28-1.amzn2023.0.2` |
| `hwdata-0.384-1.amzn2023.0.3` |
| `kernel-livepatch-repo-s3-2023.5.20240819-0.amzn2023` |
| `kernel-tools-6.1.102-111.182.amzn2023` |
| `kernel-6.1.102-111.182.amzn2023` |
| `libarchive-3.7.4-2.amzn2023.0.1` |
| `microcode_ctl-2:2.1-53.amzn2023.0.8` |
| `system-release-2023.5.20240819-0.amzn2023` |

## Minimal AMI
<a name="amis-2023.5.20240819.minimal-ami"></a>

|  |
| --- |
| `amazon-ec2-net-utils-2.5.1-1.amzn2023.0.1` |
| `amazon-linux-repo-s3-2023.5.20240819-0.amzn2023` |
| `hwdata-0.384-1.amzn2023.0.3` |
| `kernel-livepatch-repo-s3-2023.5.20240819-0.amzn2023` |
| `kernel-6.1.102-111.182.amzn2023` |
| `libarchive-3.7.4-2.amzn2023.0.1` |
| `system-release-2023.5.20240819-0.amzn2023` |

## Minimal container image
<a name="amis-2023.5.20240819.minimal-container-ami"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240819-0.amzn2023` |
| `libarchive-3.7.4-2.amzn2023.0.1` |
| `system-release-2023.5.20240819-0.amzn2023` |

## Contact us
<a name="amis-2023.5.20240819.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
