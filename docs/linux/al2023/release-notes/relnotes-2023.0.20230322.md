---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230322.html
---

# Amazon Linux 2023 version 2023.0.20230322 release notes
<a name="relnotes-2023.0.20230322"></a>

This topic includes release notes for the second General Availability (GA) version of Amazon Linux 2023 (AL2023). These release notes are for the 2023.0.20230322 version of AL2023.

## Major updates
<a name="major-updates-20230322"></a>

This release represents an update to the General Availability (GA) release of Amazon Linux 2023 (AL2023). AL2023 is the next generation of Amazon Linux. It comes with 5 years of support and brings features like Deterministic Updates, better optimizations for Graviton processors and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

See the [Amazon Linux What's New Post](https://aws.amazon.com/about-aws/whats-new/2023/03/amazon-linux-2023/) for more information about AL2023.

AL2023 includes the following major updates.
+ Systems Manager Patch Manager now supports AL2023.
+ The `Arm64` version of AL2023 is built with a feature called *Pointer Authentication (PAC)*. When run on supported hardware (Graviton 3), the return address for function calls are signed and verified, adding an extra layer of security against a whole category of attacks.
+ Fixed the issue with `gcc` on `aarch64` with patchable function sections which was causing the failure of `kretprobe` event registration and affected related functionality in SystemTap and the `perf` tool.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ Amazon Inspector support for AL2023 will be available in April.
+ When upgrading an instance from AL2023 RC1 or earlier, in order to avoid a boot order issue, you will need to add the following to `/etc/default/grub` before upgrading in order to get the kernel update:

  ```
  GRUB_DEFAULT=saved
  GRUB_UPDATE_DEFAULT_KERNEL=true
  ```
+ `codedeploy` agent does not currently work with AL2023.
+ AL2023 contains a known issue where customer defined `NTP` servers via `DHCP` are not honored.

  **Work-Around** - Configure the NTP servers using a config file in `/etc/chrony.d`
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, please refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).

**Contact us**

If you find a security issue, follow this link to learn [how to contact our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a Github issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you just have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-20230322)
+ [Repository](#amis-2023.0.20230322.repository)
+ [Docker container image](#amis-2023020230322.container-image)
+ [Default AMI](#amis-2023020230322.default-ami)
+ [Minimal AMI](#amis-2023020230322.minimal-ami)

## Repository
<a name="amis-2023.0.20230322.repository"></a>

### New packages in AL2023.0.20230322 since AL2023.0.20230315
<a name="new-AL2023.0.20230315-AL2023.0.20230322"></a>

 Comparing AL2023.0.20230315 version 2023.0.20230315 to AL2023.0.20230322 version [2023.0.20230322](#relnotes-2023.0.20230322).

| Package Type | Number of new packages in AL2023.0.20230322 compared to AL2023.0.20230315 |
| --- | --- |
| Source RPMs | 1 |
| Total Binary RPMs | 2 |
|  x86\_64 binary RPMs | 1 |
|  aarch64 binary RPMs | 1 |

New packages in AL2023.0.20230322:

- ** `trace-cmd` **
  - **RPM:**  trace-cmd
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.7-10.amzn2023.0.1

### AL2023.0.20230322 upgrades from AL2023.0.20230315
<a name="vercmp-AL2023.0.20230315-AL2023.0.20230322"></a>

 Comparing [2023.0.20230315](relnotes-2023.0.20230315.md) to [2023.0.20230322](#relnotes-2023.0.20230322).

| Package Type | Count |
| --- | --- |
| Source | 25 |
| Total Binary | 376 |
|  noarch binary RPMs | 112 |
|  x86\_64 binary RPMs | 135 |
|  aarch64 binary RPMs | 129 |

The full comparison of RPM package versions is below.

- ** `autotrace` **
  - **RPM:**  autotrace  / **Architectures:** aarch64, x86\_64
  - **RPM:**  autotrace-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 0.31.1-62.amzn2023.0.2
  - **AL2023.0.20230322 version:** 0.31.9-86.amzn2023.0.1

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 1.6.8-2.amzn2023.0.3
  - **AL2023.0.20230322 version:** 1.6.8-2.amzn2023.0.4

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 1.1.0-1.amzn2023.0.2
  - **AL2023.0.20230322 version:** 1.1.0-6.amzn2023.0.2

- ** `device-mapper-multipath` **
  - **RPM:**  device-mapper-multipath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-multipath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-multipath-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpartx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdmmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdmmp-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 0.8.7-16.amzn2023.0.1
  - **AL2023.0.20230322 version:** 0.8.7-16.amzn2023.0.2

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 20.10.17-1.amzn2023.0.5
  - **AL2023.0.20230322 version:** 20.10.17-1.amzn2023.0.6

- ** `emacs` **
  - **RPM:**  emacs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-filesystem  / **Architectures:** noarch
  - **RPM:**  emacs-lucid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-nox  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-terminal  / **Architectures:** noarch
  - **AL2023.0.20230315 version:** 28.2-3.amzn2023.0.3
  - **AL2023.0.20230322 version:** 28.2-3.amzn2023.0.4

- ** [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gdb-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-offload-nvptx  / **Architectures:** x86\_64
  - **RPM:**  gcc-plugin-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgcc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgccjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgccjit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgfortran-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgomp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgomp-offload-nvptx  / **Architectures:** x86\_64
  - **RPM:**  libitm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libitm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libitm-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libquadmath  / **Architectures:** x86\_64
  - **RPM:**  libquadmath-devel  / **Architectures:** x86\_64
  - **RPM:**  libquadmath-static  / **Architectures:** x86\_64
  - **RPM:**  libstdc\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libubsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libubsan-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 11.3.1-4.amzn2023.0.2
  - **AL2023.0.20230322 version:** 11.3.1-4.amzn2023.0.3

- ** [https://docs.aws.amazon.com/linux/al2023/ug/go.html](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/go.html](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-race  / **Architectures:** x86\_64
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.0.20230315 version:** 1.19.3-2.amzn2023.0.2
  - **AL2023.0.20230322 version:** 1.19.6-1.amzn2023.0.1

- ** `httpd` **
  - **RPM:**  httpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  httpd-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  httpd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  httpd-filesystem  / **Architectures:** noarch
  - **RPM:**  httpd-manual  / **Architectures:** noarch
  - **RPM:**  httpd-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_lua  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_proxy\_html  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_session  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_ssl  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 2.4.55-1.amzn2023
  - **AL2023.0.20230322 version:** 2.4.56-1.amzn2023

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 6.1.15-28.43.amzn2023
  - **AL2023.0.20230322 version:** 6.1.19-30.43.amzn2023

- ** `keyutils` **
  - **RPM:**  keyutils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  keyutils-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  keyutils-libs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 1.6.1-2.amzn2023.0.2
  - **AL2023.0.20230322 version:** 1.6.3-1.amzn2023

- ** `nmap` **
  - **RPM:**  nmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nmap-ncat  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 7.80-11.amzn2023.0.3
  - **AL2023.0.20230322 version:** 7.93-1.amzn2023

- ** `opensc` **
  - **RPM:**  opensc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 0.22.0-4.amzn2023.0.3
  - **AL2023.0.20230322 version:** 0.23.0-3.amzn2023

- ** `openscap` **
  - **RPM:**  openscap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-containers  / **Architectures:** noarch
  - **RPM:**  openscap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-engine-sce  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-engine-sce-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-scanner  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 1.3.5-2.amzn2023.0.3
  - **AL2023.0.20230322 version:** 1.3.7-1.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
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
  - **RPM:**  php8.1-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-xml  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 8.1.14-1.amzn2023.0.2
  - **AL2023.0.20230322 version:** 8.1.16-1.amzn2023.0.1

- ** `polkit` **
  - **RPM:**  polkit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  polkit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  polkit-docs  / **Architectures:** noarch
  - **RPM:**  polkit-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 0.117-10.amzn2023.0.3
  - **AL2023.0.20230322 version:** 0.117-11.amzn2023

- ** `python-pillow` **
  - **RPM:**  python3-pillow  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-tk  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 9.0.1-6.amzn2023.0.3
  - **AL2023.0.20230322 version:** 9.4.0-2.amzn2023.0.1

- ** `setools` **
  - **RPM:**  python3-setools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  setools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  setools-console  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 4.4.0-9.amzn2023.0.2
  - **AL2023.0.20230322 version:** 4.4.1-1.amzn2023

- ** `sudo` **
  - **RPM:**  sudo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-logsrvd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-python-plugin  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 1.9.12-1.p2.amzn2023.0.3
  - **AL2023.0.20230322 version:** 1.9.13-1.p2.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.0.20230315 version:** 2023.0.20230315-1.amzn2023
  - **AL2023.0.20230322 version:** 2023.0.20230322-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.0.20230315 version:** 9.0.64-1.amzn2023.0.2
  - **AL2023.0.20230322 version:** 9.0.71-1.amzn2023.0.1

- ** `udica` **
  - **RPM:**  udica
  - **Architectures:** noarch
  - **AL2023.0.20230315 version:** 0.2.6-3.amzn2023.0.1
  - **AL2023.0.20230322 version:** 0.2.7-4.amzn2023.0.1

- ** `unbound` **
  - **RPM:**  python3-unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-anchor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 1.16.3-2.amzn2023.0.1
  - **AL2023.0.20230322 version:** 1.17.1-1.amzn2023.0.1

- ** `update-motd` **
  - **RPM:**  update-motd
  - **Architectures:** noarch
  - **AL2023.0.20230315 version:** 2.0-1.amzn2023.0.3
  - **AL2023.0.20230322 version:** 2.1-1.amzn2023

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230315 version:** 9.0.1314-1.amzn2023.0.2
  - **AL2023.0.20230322 version:** 9.0.1367-1.amzn2023.0.1

## Docker container image
<a name="amis-2023020230322.container-image"></a>

The following packages have been **removed**.
+ `amazon-linux-repo-cdn-2023.0.20230315-1.amzn2023`
+ `keyutils-libs-1.6.1-2.amzn2023.0.2`
+ `libgcc-11.3.1-4.amzn2023.0.2`
+ `libgomp-11.3.1-4.amzn2023.0.2`
+ `libstdc++-11.3.1-4.amzn2023.0.2`
+ `system-release-2023.0.20230315-1.amzn2023`

The following packages have been **updated**.
+ `amazon-linux-repo-cdn-2023.0.20230322-0.amzn2023`
+ `keyutils-libs-1.6.3-1.amzn2023`
+ `libgcc-11.3.1-4.amzn2023.0.3`
+ `libgomp-11.3.1-4.amzn2023.0.3`
+ `libstdc++-11.3.1-4.amzn2023.0.3`
+ `system-release-2023.0.20230322-0.amzn2023`

## Default AMI
<a name="amis-2023020230322.default-ami"></a>

The following packages have been **removed**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230315-1.amzn2023-kernel-6.1.15-28.43.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230315-1.amzn2023` |
| `kernel-tools-6.1.15-28.43.amzn2023` |
| `keyutils-1.6.1-2.amzn2023.0.2` |
| `keyutils-libs-1.6.1-2.amzn2023.0.2` |
| `libgcc-11.3.1-4.amzn2023.0.2` |
| `libgomp-11.3.1-4.amzn2023.0.2` |
| `libstdc++-11.3.1-4.amzn2023.0.2` |
| `python3-setools-4.4.0-9.amzn2023.0.2` |
| `sudo-1.9.12-1.p2.amzn2023.0.3` |
| `system-release-2023.0.20230315-1.amzn2023` |
| `update-motd-2.0-1.amzn2023.0.3` |
| `vim-common-2:9.0.1314-1.amzn2023.0.2` |
| `vim-data-2:9.0.1314-1.amzn2023.0.2` |
| `vim-enhanced-2:9.0.1314-1.amzn2023.0.2` |
| `vim-filesystem-2:9.0.1314-1.amzn2023.0.2` |
| `vim-minimal-2:9.0.1314-1.amzn2023.0.2` |

The following packages have been **updated**.

|  |
| --- |
| `acpid-2.0.32-4.amzn2023.0.2` |
| `amazon-linux-repo-s3-2023.0.20230322-0.amzn2023` |
| `ec2-hibinit-agent-1.0.4-0.amzn2023.0.2` |
| `kernel-6.1.19-30.43.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230322-0.amzn2023` |
| `kernel-tools-6.1.19-30.43.amzn2023` |
| `keyutils-1.6.3-1.amzn2023` |
| `keyutils-libs-1.6.3-1.amzn2023` |
| `libgcc-11.3.1-4.amzn2023.0.3` |
| `libgomp-11.3.1-4.amzn2023.0.3` |
| `libstdc-11.3.1-4.amzn2023.0.3` |
| `python3-setools-4.4.1-1.amzn2023` |
| `sudo-1.9.13-1.p2.amzn2023.0.1` |
| `system-release-2023.0.20230322-0.amzn2023` |
| `update-motd-2.1-1.amzn2023` |
| `vim-common-2:9.0.1367-1.amzn2023.0.1` |
| `vim-data-2:9.0.1367-1.amzn2023.0.1` |
| `vim-enhanced-2:9.0.1367-1.amzn2023.0.1` |
| `vim-filesystem-2:9.0.1367-1.amzn2023.0.1` |
| `vim-minimal-2:9.0.1367-1.amzn2023.0.1` |

## Minimal AMI
<a name="amis-2023020230322.minimal-ami"></a>

The following packages have been **removed**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230315-1.amzn2023` |
| `kernel-6.1.15-28.43.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230315-1.amzn2023` |
| `keyutils-libs-1.6.1-2.amzn2023.0.2` |
| `libgcc-11.3.1-4.amzn2023.0.2` |
| `libgomp-11.3.1-4.amzn2023.0.2` |
| `libstdc++-11.3.1-4.amzn2023.0.2` |
| `python3-setools-4.4.0-9.amzn2023.0.2` |
| `sudo-1.9.12-1.p2.amzn2023.0.3` |
| `system-release-2023.0.20230315-1.amzn2023` |
| `update-motd-2.0-1.amzn2023.0.3` |
| `vim-data-2:9.0.1314-1.amzn2023.0.2` |
| `vim-minimal-2:9.0.1314-1.amzn2023.0.2` |

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230322-0.amzn2023` |
| `kernel-6.1.19-30.43.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230322-0.amzn2023` |
| `keyutils-libs-1.6.3-1.amzn2023` |
| `libgcc-11.3.1-4.amzn2023.0.3` |
| `libgomp-11.3.1-4.amzn2023.0.3` |
| `libstdc-11.3.1-4.amzn2023.0.3` |
| `python3-setools-4.4.1-1.amzn2023` |
| `sudo-1.9.13-1.p2.amzn2023.0.1` |
| `system-release-2023.0.20230322-0.amzn2023` |
| `update-motd-2.1-1.amzn2023` |
| `vim-data-2:9.0.1367-1.amzn2023.0.1` |
| `vim-minimal-2:9.0.1367-1.amzn2023.0.1` |
