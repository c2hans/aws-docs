---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20231016.html
---

# Amazon Linux 2023 version 2023.2.20231016 release notes
<a name="relnotes-2023.2.20231016"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.2.20231016 release

## Major updates
<a name="major-updates-2023.2.20231016"></a>

This release represents an update to the second quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

AL2023 includes the following major updates.
+ This release includes updated `nghttp2`, `golang`, `dotnet6.0`, `tomcat9`, `nodejs`, and `nginx` packages addressing CVE-2023-44487 and CVE-2023-39325. For more information, see [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.2.20231016)
+ [Repository](#amis-2023.2.20231016.repository)
+ [Docker container image](#amis-2023.2.20231016.container-image)
+ [Default AMI](#amis-2023.2.20231016.default-ami)
+ [Minimal AMI](#amis-2023.2.20231016.minimal-ami)
+ [Minimal container image](#amis-2023.2.20231016.minimal-container-ami)

## Repository
<a name="amis-2023.2.20231016.repository"></a>

### AL2023.2.20231016 upgrades from AL2023.2.20231011
<a name="vercmp-AL2023.2.20231011-AL2023.2.20231016"></a>

 Comparing [2023.2.20231011](relnotes-2023.2.20231011.md) to [2023.2.20231016](#relnotes-2023.2.20231016).

| Package Type | Count |
| --- | --- |
| Source | 7 |
| Total Binary | 144 |
|  noarch binary RPMs | 80 |
|  x86\_64 binary RPMs | 32 |
|  aarch64 binary RPMs | 32 |

The full comparison of RPM package versions is below.

- ** `dotnet6.0` **
  - **RPM:**  aspnetcore-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231011 version:** 6.0.22-1.amzn2023.0.1
  - **AL2023.2.20231016 version:** 6.0.23-1.amzn2023.0.1

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.2.20231011 version:** 1.20.8-1.amzn2023.0.1
  - **AL2023.2.20231016 version:** 1.20.10-1.amzn2023.0.1

- ** `nghttp2` **
  - **RPM:**  libnghttp2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnghttp2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nghttp2  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231011 version:** 1.55.1-1.amzn2023.0.4
  - **AL2023.2.20231016 version:** 1.57.0-1.amzn2023.0.1

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
  - **AL2023.2.20231011 version:** 1.24.0-1.amzn2023.0.1
  - **AL2023.2.20231016 version:** 1.24.0-1.amzn2023.0.2

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231011 version:** 18.17.1-1.amzn2023.0.2
  - **AL2023.2.20231016 version:** 18.18.0-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.2.20231011 version:** 2023.2.20231011-0.amzn2023
  - **AL2023.2.20231016 version:** 2023.2.20231016-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.2.20231011 version:** 9.0.71-1.amzn2023.0.5
  - **AL2023.2.20231016 version:** 9.0.71-1.amzn2023.0.6

## Docker container image
<a name="amis-2023.2.20231016.container-image"></a>
+ `amazon-linux-repo-cdn-2023.2.20231016-0.amzn2023`
+ `libnghttp2-1.57.0-1.amzn2023.0.1`
+ `system-release-2023.2.20231016-0.amzn2023`

## Default AMI
<a name="amis-2023.2.20231016.default-ami"></a>
+ `amazon-linux-repo-s3-2023.2.20231016-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.2.20231016-0.amzn2023`
+ `libnghttp2-1.57.0-1.amzn2023.0.1`
+ `system-release-2023.2.20231016-0.amzn2023`

## Minimal AMI
<a name="amis-2023.2.20231016.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.2.20231016-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.2.20231016-0.amzn2023`
+ `libnghttp2-1.57.0-1.amzn2023.0.1`
+ `system-release-2023.2.20231016-0.amzn2023`

## Minimal container image
<a name="amis-2023.2.20231016.minimal-container-ami"></a>
+ `system-release-2023.2.20231016-0.amzn2023`
+ `amazon-linux-repo-cdn-2023.2.20231016-0.amzn2023`
+ `libnghttp2-1.57.0-1.amzn2023.0.1`
