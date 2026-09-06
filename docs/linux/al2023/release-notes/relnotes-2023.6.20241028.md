---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241028.html
---

# Amazon Linux 2023 version 2023.6.20241028 release notes
<a name="relnotes-2023.6.20241028"></a>

**Note**
 This release was recalled due to a bug introduced in the `nodejs` package.
 The [AL2023.6.20241031](relnotes-2023.6.20241031.md) release was subsequently released with a fix for this issue. The release notes for [AL2023.6.20241031](relnotes-2023.6.20241031.md) include the other changes that were present in the 2023.6.20241028 release.

 Moving from this release to [2023.6.20241031](relnotes-2023.6.20241031.md) is only needed if affected by the `nodejs` package issue.

 Upgrades from this release to future AL2023 releases is no different than normal. Recalling an AL2023 release involves directing customers away from updating to the recalled release, and instead directing updates to the next release (in this case, to [2023.6.20241031](relnotes-2023.6.20241031.md)).

## Repository
<a name="amis-2023.6.20241028.repository"></a>

### New packages in AL2023.6.20241028 since AL2023.6.20241010
<a name="new-AL2023.6.20241010-AL2023.6.20241028"></a>

 Comparing AL2023.6.20241010 version 2023.6.20241010 to AL2023.6.20241028 version [2023.6.20241028](#relnotes-2023.6.20241028).

| Package Type | Number of new packages in AL2023.6.20241028 compared to AL2023.6.20241010 |
| --- | --- |
| Source RPMs | 4 |
| Total Binary RPMs | 23 |
|  noarch binary RPMs | 1 |
|  x86\_64 binary RPMs | 11 |
|  aarch64 binary RPMs | 11 |

New packages in AL2023.6.20241028:

- ** `cjose` **
  - **RPM:**  cjose  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cjose-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.6.2.2-6.amzn2023

- ** [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  java-17-amazon-corretto-debugsymbols
  - **Architectures:** aarch64, x86\_64
  - **Version:** 17.0.13\+11-1.amzn2023.1

- ** [`java-21-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  java-21-amazon-corretto-debugsymbols
  - **Architectures:** aarch64, x86\_64
  - **Version:** 21.0.5\+11-1.amzn2023.1

- ** [`java-23-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-23-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-23-amazon-corretto-debugsymbols  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-23-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-23-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-23-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-23-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **Version:** 23.0.1\+8-1.amzn2023.1

- ** `mod_auth_openidc` **
  - **RPM:**  mod\_auth\_openidc
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.4.15-3.amzn2023

- ** `nvidia-release` **
  - **RPM:**  nvidia-release
  - **Architectures:** noarch
  - **Version:** 2023-1.amzn2023

### AL2023.6.20241028 upgrades from AL2023.6.20241010
<a name="vercmp-AL2023.6.20241010-AL2023.6.20241028"></a>

 Comparing [2023.6.20241010](relnotes-2023.6.20241010.md) to [2023.6.20241028](#relnotes-2023.6.20241028).

| Package Type | Count |
| --- | --- |
| Source | 22 |
| Total Binary | 283 |
|  noarch binary RPMs | 116 |
|  x86\_64 binary RPMs | 84 |
|  aarch64 binary RPMs | 83 |

The full comparison of RPM package versions is below.

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 3.3.859.0-1.amzn2023
  - **AL2023.6.20241028 version:** 3.3.987.0-1.amzn2023

- ** `aws-nitro-enclaves-cli` **
  - **RPM:**  aws-nitro-enclaves-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-integration-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 1.3.3-0.amzn2023
  - **AL2023.6.20241028 version:** 1.3.4-0.amzn2023

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 1.87.0-1.amzn2023
  - **AL2023.6.20241028 version:** 1.87.1-1.amzn2023

- ** `flatpak` **
  - **RPM:**  flatpak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-selinux  / **Architectures:** noarch
  - **RPM:**  flatpak-session-helper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 1.15.4-3.amzn2023.0.2
  - **AL2023.6.20241028 version:** 1.15.10-1.amzn2023.0.1

- ** [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-1.8.0-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 1.8.0\_422.b05-1.amzn2023
  - **AL2023.6.20241028 version:** 1.8.0\_432.b06-1.amzn2023

- ** [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 11.0.24\+8-1.amzn2023
  - **AL2023.6.20241028 version:** 11.0.25\+9-1.amzn2023

- ** [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 17.0.12\+7-1.amzn2023.1
  - **AL2023.6.20241028 version:** 17.0.13\+11-1.amzn2023.1

- ** [`java-21-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-21-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-21-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-21-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-21-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-21-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 21.0.4\+7-1.amzn2023.1
  - **AL2023.6.20241028 version:** 21.0.5\+11-1.amzn2023.1

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
  - **AL2023.6.20241010 version:** 6.1.112-122.189.amzn2023
  - **AL2023.6.20241028 version:** 6.1.112-124.190.amzn2023

- ** `libarchive` **
  - **RPM:**  bsdcat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bsdcpio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bsdtar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bsdunzip  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libarchive  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libarchive-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 3.7.4-2.amzn2023.0.1
  - **AL2023.6.20241028 version:** 3.7.4-2.amzn2023.0.2

- ** `lustre-client` **
  - **RPM:**  lustre-client
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 2.15.3-3.amzn2023
  - **AL2023.6.20241028 version:** 2.15.4-7.amzn2023

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2023.6.20241010 version:** 2.1-53.amzn2023.0.8
  - **AL2023.6.20241028 version:** 2.1-53.amzn2023.0.9

- ** `nginx` **
  - **RPM:**  nginx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-all-modules  / **Architectures:** noarch
  - **RPM:**  nginx-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-filesystem  / **Architectures:** noarch
  - **RPM:**  nginx-mod-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-image-filter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-xslt-filter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-mail  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-stream  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 1.24.0-1.amzn2023.0.4
  - **AL2023.6.20241028 version:** 1.26.2-1.amzn2023.0.1

- ** `nodejs20` **
  - **RPM:**  nodejs20  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-docs  / **Architectures:** noarch
  - **RPM:**  nodejs20-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-11.3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 20.12.2-1.amzn2023.0.2
  - **AL2023.6.20241028 version:** 20.18.0-1.amzn2023.0.1

- ** `openssh` **
  - **RPM:**  openssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-keycat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_ssh\_agent\_auth  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 8.7p1-8.amzn2023.0.12
  - **AL2023.6.20241028 version:** 8.7p1-8.amzn2023.0.13

- ** `poppler` **
  - **RPM:**  poppler  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-cpp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib-doc  / **Architectures:** noarch
  - **RPM:**  poppler-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 22.08.0-3.amzn2023.0.4
  - **AL2023.6.20241028 version:** 22.08.0-3.amzn2023.0.5

- ** `python3.11-setuptools` **
  - **RPM:**  python3.11-setuptools  / **Architectures:** noarch
  - **RPM:**  python3.11-setuptools-wheel  / **Architectures:** noarch
  - **AL2023.6.20241010 version:** 65.5.1-2.amzn2023.0.5
  - **AL2023.6.20241028 version:** 65.5.1-2.amzn2023.0.6

- ** `python-twisted` **
  - **RPM:**  python3-twisted  / **Architectures:** noarch
  - **RPM:**  python3-twisted\+tls  / **Architectures:** noarch
  - **AL2023.6.20241010 version:** 22.4.0-126.amzn2023.0.3
  - **AL2023.6.20241028 version:** 22.4.0-127.amzn2023.0.4

- ** `python-urllib3` **
  - **RPM:**  python3-urllib3
  - **Architectures:** noarch
  - **AL2023.6.20241010 version:** 1.25.10-5.amzn2023.0.3
  - **AL2023.6.20241028 version:** 1.25.10-5.amzn2023.0.4

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
  - **AL2023.6.20241010 version:** 3.2.2-180.amzn2023.0.3
  - **AL2023.6.20241028 version:** 3.2.2-180.amzn2023.0.4

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241010 version:** 6.6-1.amzn2023.0.4
  - **AL2023.6.20241028 version:** 6.7-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20241010 version:** 2023.6.20241010-0.amzn2023
  - **AL2023.6.20241028 version:** 2023.6.20241028-0.amzn2023

## Contact us
<a name="amis-2023.6.20241028.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
