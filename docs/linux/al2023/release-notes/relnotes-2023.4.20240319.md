---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.4.20240319.html
---

# Amazon Linux 2023 version 2023.4.20240319 release notes
<a name="relnotes-2023.4.20240319"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.4.20240319 release

## Major updates
<a name="major-updates-2023.4.20240319"></a>

This release represents an update to the fourth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

AL2023 includes the following major updates.
+ AL2023.4 updates `sssd` to 2.9.4 and no longer runs this service by default. Existing customer-specific configurations will be preserved and `sssd` will continue to run if any configurations are present.

**Known Issues**
+ A change to hosts module ordering in nsswitch.conf introduced a regression that might cause instance hostname resolution to return multiple IP addresses. The previous hostname resolution behavior will be restored in a future update to the `glibc` package in AL2023.

  **Work-Around** – Customers affected by this change can restore the previous hostname resolution behavior until the next update is released by downgrading the `glibc` package using the command `sudo dnf install glibc-2.34-52.amzn2023.0.7`.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.4.20240319)
+ [Repository](#amis-2023.4.20240319.repository)
+ [Docker container image](#amis-2023.4.20240319.container-image)
+ [Default AMI](#amis-2023.4.20240319.default-ami)
+ [Minimal AMI](#amis-2023.4.20240319.minimal-ami)
+ [Minimal container image](#amis-2023.4.20240319.minimal-container-ami)

## Repository
<a name="amis-2023.4.20240319.repository"></a>

### New packages in AL2023.4.20240319 since AL2023.3.20240312
<a name="new-AL2023.3.20240312-AL2023.4.20240319"></a>

 Comparing AL2023.3.20240312 version 2023.3.20240312 to AL2023.4.20240319 version [2023.4.20240319](#relnotes-2023.4.20240319).

| Package Type | Number of new packages in AL2023.4.20240319 compared to AL2023.3.20240312 |
| --- | --- |
| Source RPMs | 36 |
| Total Binary RPMs | 91 |
|  noarch binary RPMs | 33 |
|  x86\_64 binary RPMs | 29 |
|  aarch64 binary RPMs | 29 |

New packages in AL2023.4.20240319:

- ** `distribution-gpg-keys` **
  - **RPM:**  distribution-gpg-keys  / **Architectures:** noarch
  - **RPM:**  distribution-gpg-keys-copr  / **Architectures:** noarch
  - **Version:** 1.100-1.amzn2023.0.1

- ** `etckeeper` **
  - **RPM:**  etckeeper  / **Architectures:** noarch
  - **RPM:**  etckeeper-dnf  / **Architectures:** noarch
  - **Version:** 1.18.20-1.amzn2023.0.1

- ** `fetchmail` **
  - **RPM:**  fetchmail
  - **Architectures:** aarch64, x86\_64
  - **Version:** 6.4.38-1.amzn2023

- ** `getdns` **
  - **RPM:**  getdns  / **Architectures:** aarch64, x86\_64
  - **RPM:**  getdns-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  getdns-utils  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.7.3-1.amzn2023

- ** `hiredis` **
  - **RPM:**  hiredis  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hiredis-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.2.0-1.amzn2023.0.1

- ** [`hyperv-daemons`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html) **
  - **RPM:**  [`hyperv-daemons`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`hyperv-daemons-license`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** noarch
  - **RPM:**  [`hypervfcopyd`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`hypervkvpd`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`hyperv-tools`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** noarch
  - **RPM:**  hypervvssd  / **Architectures:** aarch64, x86\_64
  - **Version:** 0-0.42.20220731git.amzn2023.0.1

- ** `iperf` **
  - **RPM:**  iperf
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.1.9-2.amzn2023

- ** `lcov` **
  - **RPM:**  lcov
  - **Architectures:** noarch
  - **Version:** 2.0-1.amzn2023

- ** `lustre-client` **
  - **RPM:**  lustre-client
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.15.3-3.amzn2023

- ** `mock` **
  - **RPM:**  mock  / **Architectures:** noarch
  - **RPM:**  mock-filesystem  / **Architectures:** noarch
  - **RPM:**  mock-lvm  / **Architectures:** noarch
  - **RPM:**  mock-rpmautospec  / **Architectures:** noarch
  - **RPM:**  mock-scm  / **Architectures:** noarch
  - **Version:** 5.4-1.amzn2023.0.1

- ** `mock-core-configs` **
  - **RPM:**  mock-core-configs
  - **Architectures:** noarch
  - **Version:** 39.2-1.amzn2023

- ** `openscap` **
  - **RPM:**  openscap-perl
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.9-1.amzn2023.0.1

- ** `pdsh` **
  - **RPM:**  pdsh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pdsh-rcmd-ssh  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.34-4.amzn2023.0.1

- ** `perl-Crypt-OpenSSL-Bignum` **
  - **RPM:**  perl-Crypt-OpenSSL-Bignum
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.09-23.amzn2023

- ** `perl-Crypt-OpenSSL-Random` **
  - **RPM:**  perl-Crypt-OpenSSL-Random
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.15-21.amzn2023

- ** `perl-Crypt-OpenSSL-RSA` **
  - **RPM:**  perl-Crypt-OpenSSL-RSA
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.33-3.amzn2023

- ** `perl-CryptX` **
  - **RPM:**  perl-CryptX  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-CryptX-tests  / **Architectures:** noarch
  - **Version:** 0.080-1.amzn2023

- ** `perl-Digest-BubbleBabble` **
  - **RPM:**  perl-Digest-BubbleBabble
  - **Architectures:** noarch
  - **Version:** 0.02-37.amzn2023

- ** `perl-Encode-Detect` **
  - **RPM:**  perl-Encode-Detect
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.01-44.amzn2023

- ** `perl-Mail-AuthenticationResults` **
  - **RPM:**  perl-Mail-AuthenticationResults
  - **Architectures:** noarch
  - **Version:** 2.20230112-3.amzn2023

- ** `perl-Mail-DKIM` **
  - **RPM:**  perl-Mail-DKIM
  - **Architectures:** noarch
  - **Version:** 1.20230630-1.amzn2023

- ** `perl-Mail-SPF` **
  - **RPM:**  perl-Mail-SPF
  - **Architectures:** noarch
  - **Version:** 2.9.0-32.amzn2023

- ** `perl-Math-BigInt` **
  - **RPM:**  perl-Math-BigInt-tests
  - **Architectures:** noarch
  - **Version:** 1.9998.39-2.amzn2023.0.2

- ** `perl-Module-Install-TestBase` **
  - **RPM:**  perl-Module-Install-TestBase  / **Architectures:** noarch
  - **RPM:**  perl-Module-Install-TestBase-tests  / **Architectures:** noarch
  - **Version:** 0.86-29.amzn2023

- ** `perl-NetAddr-IP` **
  - **RPM:**  perl-NetAddr-IP
  - **Architectures:** aarch64, x86\_64
  - **Version:** 4.079-25.amzn2023

- ** `perl-Net-CIDR-Lite` **
  - **RPM:**  perl-Net-CIDR-Lite
  - **Architectures:** noarch
  - **Version:** 0.22-8.amzn2023

- ** `perl-Net-DNS` **
  - **RPM:**  perl-Net-DNS  / **Architectures:** noarch
  - **RPM:**  perl-Net-DNS-Nameserver  / **Architectures:** noarch
  - **RPM:**  perl-Net-DNS-tests  / **Architectures:** noarch
  - **Version:** 1.39-2.amzn2023

- ** `perl-Net-DNS-Resolver-Mock` **
  - **RPM:**  perl-Net-DNS-Resolver-Mock  / **Architectures:** noarch
  - **RPM:**  perl-Net-DNS-Resolver-Mock-tests  / **Architectures:** noarch
  - **Version:** 1.20230216-2.amzn2023

- ** `perl-Net-DNS-Resolver-Programmable` **
  - **RPM:**  perl-Net-DNS-Resolver-Programmable
  - **Architectures:** noarch
  - **Version:** 0.009-18.amzn2023

- ** `perl-Net-LibIDN2` **
  - **RPM:**  perl-Net-LibIDN2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Net-LibIDN2-tests  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.02-4.amzn2023

- ** [`php8.1`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  php8.1-zip
  - **Architectures:** aarch64, x86\_64
  - **Version:** 8.1.27-1.amzn2023.0.2

- ** `python-backoff` **
  - **RPM:**  python3-backoff
  - **Architectures:** noarch
  - **Version:** 2.2.1-1.amzn2023

- ** `python-poetry-core` **
  - **RPM:**  python3-poetry-core
  - **Architectures:** noarch
  - **Version:** 1.0.7-2.amzn2023.0.1

- ** `python-pyroute2` **
  - **RPM:**  python3-pyroute2
  - **Architectures:** noarch
  - **Version:** 0.7.3-1.amzn2023

- ** `python-rpmautospec-core` **
  - **RPM:**  python3-rpmautospec-core
  - **Architectures:** noarch
  - **Version:** 0.1.4-13.amzn2023

- ** `python-systemd` **
  - **RPM:**  python3-systemd
  - **Architectures:** aarch64, x86\_64
  - **Version:** 235-51.amzn2023.0.2

- ** `python-templated-dictionary` **
  - **RPM:**  python3-templated-dictionary
  - **Architectures:** noarch
  - **Version:** 1.4-1.amzn2023

- ** `smart-restart` **
  - **RPM:**  smart-restart
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.1-1.amzn2023.0.3

- ** `sssd` **
  - **RPM:**  sssd-idp
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.9.4-1.amzn2023.0.1

- ** `tpm2-tools` **
  - **RPM:**  tpm2-tools
  - **Architectures:** aarch64, x86\_64
  - **Version:** 5.5-4.amzn2023.0.1

- ** `tpm2-tss` **
  - **RPM:**  tpm2-tss-fapi
  - **Architectures:** aarch64, x86\_64
  - **Version:** 4.0.1-6.amzn2023

### AL2023.4.20240319 upgrades from AL2023.3.20240312
<a name="vercmp-AL2023.3.20240312-AL2023.4.20240319"></a>

 Comparing [2023.3.20240312](relnotes-2023.3.20240312.md) to [2023.4.20240319](#relnotes-2023.4.20240319).

| Package Type | Count |
| --- | --- |
| Source | 38 |
| Total Binary | 1036 |
|  noarch binary RPMs | 200 |
|  x86\_64 binary RPMs | 418 |
|  aarch64 binary RPMs | 418 |

The full comparison of RPM package versions is below.

- ** `aide` **
  - **RPM:**  aide
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 0.17.4-1.amzn2023.0.2
  - **AL2023.4.20240319 version:** 0.18.6-1.amzn2023.0.1

- ** [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** noarch
  - **AL2023.3.20240312 version:** 1.35.1-1.amzn2023
  - **AL2023.4.20240319 version:** 1.35.2-1.amzn2023

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 3.2.2222.0-1.amzn2023
  - **AL2023.4.20240319 version:** 3.2.2303.0-1.amzn2023

- ** `apache-commons-compress` **
  - **RPM:**  apache-commons-compress  / **Architectures:** noarch
  - **RPM:**  apache-commons-compress-javadoc  / **Architectures:** noarch
  - **AL2023.3.20240312 version:** 1.21-4.amzn2023.0.3
  - **AL2023.4.20240319 version:** 1.21-4.amzn2023.0.4

- ** `c-ares` **
  - **RPM:**  c-ares  / **Architectures:** aarch64, x86\_64
  - **RPM:**  c-ares-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 1.19.0-1.amzn2023
  - **AL2023.4.20240319 version:** 1.19.0-1.amzn2023.0.1

- ** `dnf` **
  - **RPM:**  dnf  / **Architectures:** noarch
  - **RPM:**  dnf-automatic  / **Architectures:** noarch
  - **RPM:**  dnf-data  / **Architectures:** noarch
  - **RPM:**  python3-dnf  / **Architectures:** noarch
  - **RPM:**  yum  / **Architectures:** noarch
  - **AL2023.3.20240312 version:** 4.12.0-2.amzn2023.0.4
  - **AL2023.4.20240319 version:** 4.14.0-1.amzn2023.0.4

- ** `dnf-plugins-core` **
  - **RPM:**  dnf-plugins-core  / **Architectures:** noarch
  - **RPM:**  dnf-utils  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-leaves  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-local  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-modulesync  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-post-transaction-actions  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugins-core  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-show-leaves  / **Architectures:** noarch
  - **RPM:**  python3-dnf-plugin-versionlock  / **Architectures:** noarch
  - **AL2023.3.20240312 version:** 4.1.0-1.amzn2023.0.3
  - **AL2023.4.20240319 version:** 4.3.0-13.amzn2023.0.4

- ** `ec2-utils` **
  - **RPM:**  ec2-utils
  - **Architectures:** noarch
  - **AL2023.3.20240312 version:** 2.1.0-1.amzn2023.0.1
  - **AL2023.4.20240319 version:** 2.2.0-1.amzn2023.0.1

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 1.81.1-1.amzn2023
  - **AL2023.4.20240319 version:** 1.82.0-1.amzn2023

- ** `fontforge` **
  - **RPM:**  fontforge  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fontforge-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fontforge-doc  / **Architectures:** noarch
  - **AL2023.3.20240312 version:** 20201107-3.amzn2023.0.2
  - **AL2023.4.20240319 version:** 20201107-3.amzn2023.0.3

- ** [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html) **
  - **RPM:**  compat-libpthread-nonshared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-all-langpacks  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-benchtests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-doc  / **Architectures:** noarch
  - **RPM:**  glibc-gconv-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-headers-x86  / **Architectures:** noarch
  - **RPM:**  glibc-langpack-aa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-af  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-agr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-am  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-an  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-anp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-as  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ast  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ayc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-az  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-be  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ber  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bhb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bho  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-br  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-brx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-byn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ca  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ce  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-chr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ckb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cmn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-crh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-csb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-da  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-de  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-doi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-dsb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-dv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-dz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-el  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-en  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-eo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-es  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-et  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-eu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fil  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fur  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ga  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gez  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ha  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-he  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hif  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hne  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hsb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ht  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ia  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-id  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ig  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ik  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-is  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-it  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-iu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ja  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ka  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kab  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-km  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ko  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kok  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ks  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ku  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ky  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-li  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lij  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ln  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lzh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mag  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mai  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mfe  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mhr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-miq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mjw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mni  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mnw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ms  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-my  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nds  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ne  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nhn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-niu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nso  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-oc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-om  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-or  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-os  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-pa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-pap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-pl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-pt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-quz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-raj  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ro  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ru  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-rw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sah  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-se  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sgs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-shn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-shs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-si  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-so  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-st  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-szl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ta  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tcy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-te  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-th  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-the  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ti  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tig  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-to  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tpi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-uk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-unm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ur  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-uz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ve  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-vi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-wa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-wae  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-wal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-wo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-xh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-yi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-yo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-yue  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-yuw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-zh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-zu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-locale-source  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-minimal-langpack  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-nss-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnsl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nscd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss\_db  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss\_hesiod  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sysroot-aarch64-fc34-glibc  / **Architectures:** noarch
  - **RPM:**  sysroot-x86\_64-fc34-glibc  / **Architectures:** noarch
  - **AL2023.3.20240312 version:** 2.34-52.amzn2023.0.7
  - **AL2023.4.20240319 version:** 2.34-52.amzn2023.0.8

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.3.20240312 version:** 1.20.12-1.amzn2023.0.1
  - **AL2023.4.20240319 version:** 1.20.12-1.amzn2023.0.2

- ** `javapackages-bootstrap` **
  - **RPM:**  javapackages-bootstrap
  - **Architectures:** noarch
  - **AL2023.3.20240312 version:** 1.5.0^20220105.git9f283b7-3.amzn2023.0.2
  - **AL2023.4.20240319 version:** 1.5.0^20220105.git9f283b7-3.amzn2023.0.3

- ** `jq` **
  - **RPM:**  jq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 1.6-10.amzn2023.0.2
  - **AL2023.4.20240319 version:** 1.7.1-48.amzn2023.0.1

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
  - **AL2023.3.20240312 version:** 6.1.79-99.164.amzn2023
  - **AL2023.4.20240319 version:** 6.1.79-99.167.amzn2023

- ** `libcomps` **
  - **RPM:**  libcomps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcomps-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcomps-doc  / **Architectures:** noarch
  - **RPM:**  python3-libcomps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-libcomps-doc  / **Architectures:** noarch
  - **AL2023.3.20240312 version:** 0.1.18-1.amzn2023.0.2
  - **AL2023.4.20240319 version:** 0.1.20-1.amzn2023

- ** `libdnf` **
  - **RPM:**  libdnf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdnf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-hawkey  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libdnf  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 0.67.0-1.amzn2023.0.5
  - **AL2023.4.20240319 version:** 0.69.0-8.amzn2023.0.5

- ** `librepo` **
  - **RPM:**  librepo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librepo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-librepo  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 1.14.2-1.amzn2023.0.4
  - **AL2023.4.20240319 version:** 1.14.5-2.amzn2023.0.1

- ** `libsndfile` **
  - **RPM:**  libsndfile  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsndfile-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsndfile-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 1.0.31-6.amzn2023.0.2
  - **AL2023.4.20240319 version:** 1.2.2-3.amzn2023.0.1

- ** `libsodium` **
  - **RPM:**  libsodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsodium-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsodium-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 1.0.18-13.amzn2023.0.1
  - **AL2023.4.20240319 version:** 1.0.19-4.amzn2023

- ** `nmap` **
  - **RPM:**  nmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nmap-ncat  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 7.93-1.amzn2023
  - **AL2023.4.20240319 version:** 7.93-4.amzn2023

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 18.18.2-1.amzn2023.0.1
  - **AL2023.4.20240319 version:** 18.18.2-1.amzn2023.0.3

- ** `nodejs20` **
  - **RPM:**  nodejs20  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-docs  / **Architectures:** noarch
  - **RPM:**  nodejs20-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-11.3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 20.11.1-1.amzn2023.0.1
  - **AL2023.4.20240319 version:** 20.11.1-1.amzn2023.0.2

- ** `openscap` **
  - **RPM:**  openscap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-containers  / **Architectures:** noarch
  - **RPM:**  openscap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-engine-sce  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-engine-sce-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-scanner  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 1.3.7-1.amzn2023.0.1
  - **AL2023.4.20240319 version:** 1.3.9-1.amzn2023.0.1

- ** `openssh` **
  - **RPM:**  openssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-keycat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_ssh\_agent\_auth  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 8.7p1-8.amzn2023.0.9
  - **AL2023.4.20240319 version:** 8.7p1-8.amzn2023.0.10

- ** `perl-Math-BigInt` **
  - **RPM:**  perl-Math-BigInt
  - **Architectures:** noarch
  - **AL2023.3.20240312 version:** 1.9998.18-458.amzn2023.0.2
  - **AL2023.4.20240319 version:** 1.9998.39-2.amzn2023.0.2

- ** [`php8.1`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.1`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-xml  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 8.1.27-1.amzn2023.0.1
  - **AL2023.4.20240319 version:** 8.1.27-1.amzn2023.0.2

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-sodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-zip  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 8.2.15-1.amzn2023.0.1
  - **AL2023.4.20240319 version:** 8.2.15-1.amzn2023.0.2

- ** `R` **
  - **RPM:**  libRmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libRmath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libRmath-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-core-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-java-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 4.1.3-1.amzn2023.0.2
  - **AL2023.4.20240319 version:** 4.3.2-1.amzn2023.0.1

- ** `rdma-core` **
  - **RPM:**  ibacm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  infiniband-diags  / **Architectures:** aarch64, x86\_64
  - **RPM:**  infiniband-diags-compat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iwpmd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libibumad  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libibverbs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libibverbs-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librdmacm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librdmacm-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pyverbs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rdma-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rdma-core-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  srp\_daemon  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 37.0-1.amzn2023.0.3
  - **AL2023.4.20240319 version:** 48.0-1.amzn2023.0.1

- ** `rpm` **
  - **RPM:**  python3-rpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-apidocs  / **Architectures:** noarch
  - **RPM:**  rpm-build  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-build-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-cron  / **Architectures:** noarch
  - **RPM:**  rpm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-audit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-fapolicyd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-ima  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-prioreset  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-selinux  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-syslog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-systemd-inhibit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-sign  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-sign-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 4.16.1.3-12.amzn2023.0.6
  - **AL2023.4.20240319 version:** 4.16.1.3-29.amzn2023.0.6

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
  - **AL2023.3.20240312 version:** 1.68.2-1.amzn2023.0.4
  - **AL2023.4.20240319 version:** 1.68.2-1.amzn2023.0.5

- ** `sssd` **
  - **RPM:**  libipa\_hbac  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libipa\_hbac-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_autofs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_certmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_certmap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_idmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_idmap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_nss\_idmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_nss\_idmap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_simpleifp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_simpleifp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_sudo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libipa\_hbac  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libsss\_nss\_idmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-sss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-sssdconfig  / **Architectures:** noarch
  - **RPM:**  python3-sss-murmur  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-ad  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-common-pac  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-dbus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-ipa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-kcm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-krb5  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-krb5-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-nfs-idmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-proxy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-winbind-idmap  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 2.5.0-1.amzn2023.0.3
  - **AL2023.4.20240319 version:** 2.9.4-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.3.20240312 version:** 2023.3.20240312-0.amzn2023
  - **AL2023.4.20240319 version:** 2023.4.20240319-1.amzn2023

- ** `tpm2-tss` **
  - **RPM:**  tpm2-tss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tpm2-tss-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 3.2.2-1.amzn2023
  - **AL2023.4.20240319 version:** 4.0.1-6.amzn2023

- ** `update-motd` **
  - **RPM:**  update-motd
  - **Architectures:** noarch
  - **AL2023.3.20240312 version:** 2.1-1.amzn2023.0.1
  - **AL2023.4.20240319 version:** 2.2-1.amzn2023

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240312 version:** 4.0.8-2.amzn2023.0.4
  - **AL2023.4.20240319 version:** 4.0.8-2.amzn2023.0.5

- ** `zsh` **
  - **RPM:**  zsh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zsh-html  / **Architectures:** noarch
  - **AL2023.3.20240312 version:** 5.8.1-1.amzn2023.0.3
  - **AL2023.4.20240319 version:** 5.9-12.amzn2023

## Docker container image
<a name="amis-2023.4.20240319.container-image"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.4.20240319-1.amzn2023` |
| `dnf-data-4.14.0-1.amzn2023.0.4` |
| `dnf-4.14.0-1.amzn2023.0.4` |
| `glibc-common-2.34-52.amzn2023.0.8` |
| `glibc-minimal-langpack-2.34-52.amzn2023.0.8` |
| `glibc-2.34-52.amzn2023.0.8` |
| `libcomps-0.1.20-1.amzn2023` |
| `libdnf-0.69.0-8.amzn2023.0.5` |
| `librepo-1.14.5-2.amzn2023.0.1` |
| `python3-dnf-4.14.0-1.amzn2023.0.4` |
| `python3-hawkey-0.69.0-8.amzn2023.0.5` |
| `python3-libcomps-0.1.20-1.amzn2023` |
| `python3-libdnf-0.69.0-8.amzn2023.0.5` |
| `python3-rpm-4.16.1.3-29.amzn2023.0.6` |
| `rpm-build-libs-4.16.1.3-29.amzn2023.0.6` |
| `rpm-libs-4.16.1.3-29.amzn2023.0.6` |
| `rpm-sign-libs-4.16.1.3-29.amzn2023.0.6` |
| `rpm-4.16.1.3-29.amzn2023.0.6` |
| `system-release-2023.4.20240319-1.amzn2023` |
| `yum-4.14.0-1.amzn2023.0.4` |

## Default AMI
<a name="amis-2023.4.20240319.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.4.20240319-1.amzn2023` |
| `amazon-ssm-agent-3.2.2303.0-1.amzn2023` |
| `c-ares-1.19.0-1.amzn2023.0.1` |
| `dnf-data-4.14.0-1.amzn2023.0.4` |
| `dnf-plugins-core-4.3.0-13.amzn2023.0.4` |
| `dnf-utils-4.3.0-13.amzn2023.0.4` |
| `dnf-4.14.0-1.amzn2023.0.4` |
| `ec2-utils-2.2.0-1.amzn2023.0.1` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.8` |
| `glibc-common-2.34-52.amzn2023.0.8` |
| `glibc-gconv-extra-2.34-52.amzn2023.0.8` |
| `glibc-locale-source-2.34-52.amzn2023.0.8` |
| `glibc-2.34-52.amzn2023.0.8` |
| `jq-1.7.1-48.amzn2023.0.1` |
| `kernel-livepatch-repo-s3-2023.4.20240319-1.amzn2023` |
| `kernel-tools-6.1.79-99.167.amzn2023` |
| `kernel-6.1.79-99.167.amzn2023` |
| `libcomps-0.1.20-1.amzn2023` |
| `libdnf-0.69.0-8.amzn2023.0.5` |
| `libibverbs-48.0-1.amzn2023.0.1` |
| `librepo-1.14.5-2.amzn2023.0.1` |
| `libsss_certmap-2.9.4-1.amzn2023.0.1` |
| `libsss_idmap-2.9.4-1.amzn2023.0.1` |
| `libsss_nss_idmap-2.9.4-1.amzn2023.0.1` |
| `libsss_sudo-2.9.4-1.amzn2023.0.1` |
| `openssh-clients-8.7p1-8.amzn2023.0.10` |
| `openssh-server-8.7p1-8.amzn2023.0.10` |
| `openssh-8.7p1-8.amzn2023.0.10` |
| `python3-dnf-plugins-core-4.3.0-13.amzn2023.0.4` |
| `python3-dnf-4.14.0-1.amzn2023.0.4` |
| `python3-hawkey-0.69.0-8.amzn2023.0.5` |
| `python3-libcomps-0.1.20-1.amzn2023` |
| `python3-libdnf-0.69.0-8.amzn2023.0.5` |
| `python3-rpm-4.16.1.3-29.amzn2023.0.6` |
| `python3-systemd-235-51.amzn2023.0.2` |
| `rpm-build-libs-4.16.1.3-29.amzn2023.0.6` |
| `rpm-libs-4.16.1.3-29.amzn2023.0.6` |
| `rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.6` |
| `rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.6` |
| `rpm-sign-libs-4.16.1.3-29.amzn2023.0.6` |
| `rpm-4.16.1.3-29.amzn2023.0.6` |
| `sssd-client-2.9.4-1.amzn2023.0.1` |
| `sssd-common-2.9.4-1.amzn2023.0.1` |
| `sssd-kcm-2.9.4-1.amzn2023.0.1` |
| `sssd-nfs-idmap-2.9.4-1.amzn2023.0.1` |
| `system-release-2023.4.20240319-1.amzn2023` |
| `update-motd-2.2-1.amzn2023` |
| `yum-4.14.0-1.amzn2023.0.4` |

## Minimal AMI
<a name="amis-2023.4.20240319.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.4.20240319-1.amzn2023` |
| `dnf-data-4.14.0-1.amzn2023.0.4` |
| `dnf-plugins-core-4.3.0-13.amzn2023.0.4` |
| `dnf-4.14.0-1.amzn2023.0.4` |
| `ec2-utils-2.2.0-1.amzn2023.0.1` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.8` |
| `glibc-common-2.34-52.amzn2023.0.8` |
| `glibc-locale-source-2.34-52.amzn2023.0.8` |
| `glibc-2.34-52.amzn2023.0.8` |
| `jq-1.7.1-48.amzn2023.0.1` |
| `kernel-livepatch-repo-s3-2023.4.20240319-1.amzn2023` |
| `kernel-6.1.79-99.167.amzn2023` |
| `libcomps-0.1.20-1.amzn2023` |
| `libdnf-0.69.0-8.amzn2023.0.5` |
| `librepo-1.14.5-2.amzn2023.0.1` |
| `openssh-clients-8.7p1-8.amzn2023.0.10` |
| `openssh-server-8.7p1-8.amzn2023.0.10` |
| `openssh-8.7p1-8.amzn2023.0.10` |
| `python3-dnf-plugins-core-4.3.0-13.amzn2023.0.4` |
| `python3-dnf-4.14.0-1.amzn2023.0.4` |
| `python3-hawkey-0.69.0-8.amzn2023.0.5` |
| `python3-libcomps-0.1.20-1.amzn2023` |
| `python3-libdnf-0.69.0-8.amzn2023.0.5` |
| `python3-rpm-4.16.1.3-29.amzn2023.0.6` |
| `python3-systemd-235-51.amzn2023.0.2` |
| `rpm-build-libs-4.16.1.3-29.amzn2023.0.6` |
| `rpm-libs-4.16.1.3-29.amzn2023.0.6` |
| `rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.6` |
| `rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.6` |
| `rpm-sign-libs-4.16.1.3-29.amzn2023.0.6` |
| `rpm-4.16.1.3-29.amzn2023.0.6` |
| `system-release-2023.4.20240319-1.amzn2023` |
| `update-motd-2.2-1.amzn2023` |
| `yum-4.14.0-1.amzn2023.0.4` |

## Minimal container image
<a name="amis-2023.4.20240319.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.4.20240319-1.amzn2023`
+ `dnf-data-4.14.0-1.amzn2023.0.4`
+ `glibc-common-2.34-52.amzn2023.0.8`
+ `glibc-minimal-langpack-2.34-52.amzn2023.0.8`
+ `glibc-2.34-52.amzn2023.0.8`
+ `libdnf-0.69.0-8.amzn2023.0.5`
+ `librepo-1.14.5-2.amzn2023.0.1`
+ `rpm-libs-4.16.1.3-29.amzn2023.0.6`
+ `rpm-4.16.1.3-29.amzn2023.0.6`
+ `system-release-2023.4.20240319-1.amzn2023`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
