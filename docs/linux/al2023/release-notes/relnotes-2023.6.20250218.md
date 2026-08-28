---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20250218.html
---

# Amazon Linux 2023 version 2023.6.20250218 release notes
<a name="relnotes-2023.6.20250218"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20250218.

**Topics**
+ [Major updates](#major-updates-2023.6.20250218)
+ [Repository](#amis-2023.6.20250218.repository)
+ [Docker container image](#amis-2023.6.20250218.container-image)
+ [Default AMI](#amis-2023.6.20250218.default-ami)
+ [Minimal AMI](#amis-2023.6.20250218.minimal-ami)
+ [Minimal container image](#amis-2023.6.20250218.minimal-container-ami)
+ [Contact us](#amis-2023.6.20250218.contact-us)

## Major updates
<a name="major-updates-2023.6.20250218"></a>

This release represents an update to the sixth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ To better support multiple versions of NodeJS, we are progressively migrating our NodeJS packages to use the `alternatives` system. This will allow multiple versions of NodeJS to be concurrently installed, and provide a single command to select which NodeJS configuration and binaries are used. To support this change, there are changes to the paths for the NodeJS binaries, globally installed NodeJS modules, and configuration files. Existing globally installed modules will be preserved across the update. This change will be non-disruptive for the majority of customers.

  This release contains this change to the nodejs package (NodeJS 18).

**Known issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20250218.repository"></a>

### New packages in AL2023.6.20250218 since AL2023.6.20250211
<a name="new-AL2023.6.20250211-AL2023.6.20250218"></a>

 Comparing AL2023.6.20250211 version 2023.6.20250211 to AL2023.6.20250218 version [2023.6.20250218](#relnotes-2023.6.20250218).

| Package Type | Number of new packages in AL2023.6.20250218 compared to AL2023.6.20250211 |
| --- | --- |
| Source RPMs | 2 |
| Total Binary RPMs | 8 |
|  noarch binary RPMs | 2 |
|  x86\_64 binary RPMs | 3 |
|  aarch64 binary RPMs | 3 |

New packages in AL2023.6.20250218:

- ** `librsvg2` **
  - **RPM:**  rsvg-pixbuf-loader
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.59.2-317.amzn2023

- ** `pam_radius` **
  - **RPM:**  pam\_radius
  - **Architectures:** aarch64, x86\_64
  - **Version:** 3.0.0-2.amzn2023.0.1

- ** [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html) **
  - **RPM:**  rust-std-static-wasm32-wasip1  / **Architectures:** noarch
  - **RPM:**  rust-toolset-srpm-macros  / **Architectures:** noarch
  - **Version:** 1.84.0-4.amzn2023.0.1

- ** `rust-cargo-c` **
  - **RPM:**  cargo-c
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.9.32-3.amzn2023.0.2

### AL2023.6.20250218 upgrades from AL2023.6.20250211
<a name="vercmp-AL2023.6.20250211-AL2023.6.20250218"></a>

 Comparing [2023.6.20250211](relnotes-2023.6.20250211.md) to [2023.6.20250218](#relnotes-2023.6.20250218).

| Package Type | Count |
| --- | --- |
| Source | 29 |
| Total Binary | 391 |
|  noarch binary RPMs | 112 |
|  x86\_64 binary RPMs | 141 |
|  aarch64 binary RPMs | 138 |

The full comparison of RPM package versions is below.

- ** [`amazon-ec2-net-utils`](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html) **
  - **RPM:**  [`amazon-ec2-net-utils`](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html)
  - **Architectures:** noarch
  - **AL2023.6.20250211 version:** 2.5.2-1.amzn2023.0.1
  - **AL2023.6.20250218 version:** 2.5.4-1.amzn2023.0.1

- ** `ansible-core` **
  - **RPM:**  ansible-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ansible-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 2.15.3-1.amzn2023.0.7
  - **AL2023.6.20250218 version:** 2.15.3-1.amzn2023.0.8

- ** `apr` **
  - **RPM:**  apr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 1.7.5-1.amzn2023.0.2
  - **AL2023.6.20250218 version:** 1.7.5-1.amzn2023.0.4

- ** `aws-nitro-enclaves-cli` **
  - **RPM:**  aws-nitro-enclaves-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-integration-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 1.3.4-0.amzn2023
  - **AL2023.6.20250218 version:** 1.4.0-0.amzn2023

- ** `dnf` **
  - **RPM:**  dnf  / **Architectures:** noarch
  - **RPM:**  dnf-automatic  / **Architectures:** noarch
  - **RPM:**  dnf-data  / **Architectures:** noarch
  - **RPM:**  python3-dnf  / **Architectures:** noarch
  - **RPM:**  yum  / **Architectures:** noarch
  - **AL2023.6.20250211 version:** 4.14.0-1.amzn2023.0.5
  - **AL2023.6.20250218 version:** 4.14.0-1.amzn2023.0.6

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 25.0.6-1.amzn2023.0.2
  - **AL2023.6.20250218 version:** 25.0.8-1.amzn2023.0.1

- ** `dotnet8.0` **
  - **RPM:**  aspnetcore-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 8.0.11-1.amzn2023
  - **AL2023.6.20250218 version:** 8.0.12-1.amzn2023

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 1.89.3-1.amzn2023
  - **AL2023.6.20250218 version:** 1.90.0-1.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** v1.29.9.0-1.amzn2023
  - **AL2023.6.20250218 version:** v1.29.12.0-1.amzn2023

- ** `emacs` **
  - **RPM:**  emacs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-filesystem  / **Architectures:** noarch
  - **RPM:**  emacs-lucid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-nox  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-terminal  / **Architectures:** noarch
  - **AL2023.6.20250211 version:** 28.2-3.amzn2023.0.8
  - **AL2023.6.20250218 version:** 28.2-3.amzn2023.0.9

- ** `ghostscript` **
  - **RPM:**  ghostscript  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-doc  / **Architectures:** noarch
  - **RPM:**  ghostscript-gtk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-tools-dvipdf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-tools-fonts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-tools-printing  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-x11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 9.56.1-7.amzn2023.0.11
  - **AL2023.6.20250218 version:** 9.56.1-7.amzn2023.0.12

- ** `git-lfs` **
  - **RPM:**  git-lfs
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 3.4.0-77.amzn2023.0.3
  - **AL2023.6.20250218 version:** 3.4.0-78.amzn2023.0.4

- ** `grub2` **
  - **RPM:**  grub2-common  / **Architectures:** noarch
  - **RPM:**  grub2-efi-aa64  / **Architectures:** aarch64
  - **RPM:**  grub2-efi-aa64-cdboot  / **Architectures:** aarch64
  - **RPM:**  grub2-efi-aa64-ec2  / **Architectures:** aarch64
  - **RPM:**  grub2-efi-aa64-modules  / **Architectures:** noarch
  - **RPM:**  grub2-efi-x64  / **Architectures:** x86\_64
  - **RPM:**  grub2-efi-x64-cdboot  / **Architectures:** x86\_64
  - **RPM:**  grub2-efi-x64-ec2  / **Architectures:** x86\_64
  - **RPM:**  grub2-efi-x64-modules  / **Architectures:** noarch
  - **RPM:**  grub2-emu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-emu-modules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-pc  / **Architectures:** x86\_64
  - **RPM:**  grub2-pc-modules  / **Architectures:** noarch
  - **RPM:**  grub2-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-tools-efi  / **Architectures:** x86\_64
  - **RPM:**  grub2-tools-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-tools-minimal  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 2.06-61.amzn2023.0.12
  - **AL2023.6.20250218 version:** 2.06-61.amzn2023.0.14

- ** `gsl` **
  - **RPM:**  gsl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gsl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 2.6-4.amzn2023.0.4
  - **AL2023.6.20250218 version:** 2.6-4.amzn2023.0.5

- ** `harfbuzz` **
  - **RPM:**  harfbuzz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  harfbuzz-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  harfbuzz-icu  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 7.0.0-2.amzn2023.0.1
  - **AL2023.6.20250218 version:** 7.0.0-2.amzn2023.0.2

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
  - **AL2023.6.20250211 version:** 6.1.127-135.201.amzn2023
  - **AL2023.6.20250218 version:** 6.1.128-136.201.amzn2023

- ** `libglvnd` **
  - **RPM:**  libglvnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-core-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-egl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-gles  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-glx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-opengl  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 1.7.0-4.amzn2023.0.1
  - **AL2023.6.20250218 version:** 1.7.0-4.amzn2023.0.2

- ** `librsvg2` **
  - **RPM:**  librsvg2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 2.54.6-1.amzn2023.0.2
  - **AL2023.6.20250218 version:** 2.59.2-317.amzn2023

- ** `libxml2` **
  - **RPM:**  libxml2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libxml2  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 2.10.4-1.amzn2023.0.7
  - **AL2023.6.20250218 version:** 2.10.4-1.amzn2023.0.8

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2023.6.20250211 version:** 2.1-53.amzn2023.0.10
  - **AL2023.6.20250218 version:** 2.1-53.amzn2023.0.11

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
  - **AL2023.6.20250211 version:** 1.26.2-1.amzn2023.0.1
  - **AL2023.6.20250218 version:** 1.26.3-1.amzn2023.0.1

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 18.20.5-1.amzn2023.0.1
  - **AL2023.6.20250218 version:** 18.20.6-1.amzn2023.0.1

- ** `openldap` **
  - **RPM:**  openldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-compat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-servers  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 2.4.57-6.amzn2023.0.6
  - **AL2023.6.20250218 version:** 2.4.57-6.amzn2023.0.7

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
  - **RPM:**  php8.1-zip  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 8.1.29-1.amzn2023.0.2
  - **AL2023.6.20250218 version:** 8.1.31-1.amzn2023.0.1

- ** [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html) **
  - **RPM:**  cargo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clippy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html)  / **Architectures:** aarch64, x86\_64
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
  - **RPM:**  rust-toolset  / **Architectures:** noarch
  - **AL2023.6.20250211 version:** 1.68.2-1.amzn2023.0.6
  - **AL2023.6.20250218 version:** 1.84.0-4.amzn2023.0.1

- ** `soci-snapshotter` **
  - **RPM:**  soci-snapshotter
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 0.8.0-1.amzn2023.0.1
  - **AL2023.6.20250218 version:** 0.9.0-1.amzn2023.0.1

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 6.7-1.amzn2023.0.1
  - **AL2023.6.20250218 version:** 6.13-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20250211 version:** 2023.6.20250211-0.amzn2023
  - **AL2023.6.20250218 version:** 2023.6.20250218-0.amzn2023

- ** `zziplib` **
  - **RPM:**  zziplib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zziplib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zziplib-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250211 version:** 0.13.72-1.amzn2023.0.3
  - **AL2023.6.20250218 version:** 0.13.78-1.amzn2023

## Docker container image
<a name="amis-2023.6.20250218.container-image"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250218-0.amzn2023 |
| dnf-data-4.14.0-1.amzn2023.0.6 |
| dnf-4.14.0-1.amzn2023.0.6 |
| libxml2-2.10.4-1.amzn2023.0.8 |
| python3-dnf-4.14.0-1.amzn2023.0.6 |
| system-release-2023.6.20250218-0.amzn2023 |
| yum-4.14.0-1.amzn2023.0.6 |

## Default AMI
<a name="amis-2023.6.20250218.default-ami"></a>

|  |
| --- |
| amazon-ec2-net-utils-2.5.4-1.amzn2023.0.1 |
| amazon-linux-repo-s3-2023.6.20250218-0.amzn2023 |
| dnf-data-4.14.0-1.amzn2023.0.6 |
| dnf-4.14.0-1.amzn2023.0.6 |
| grub2-common-1:2.06-61.amzn2023.0.14 |
| grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.14 |
| grub2-pc-modules-1:2.06-61.amzn2023.0.14 |
| grub2-tools-minimal-1:2.06-61.amzn2023.0.14 |
| grub2-tools-1:2.06-61.amzn2023.0.14 |
| kernel-libbpf-6.1.128-136.201.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20250218-0.amzn2023 |
| kernel-tools-6.1.128-136.201.amzn2023 |
| kernel-6.1.128-136.201.amzn2023 |
| libxml2-2.10.4-1.amzn2023.0.8 |
| microcode\_ctl-2:2.1-53.amzn2023.0.11 |
| openldap-2.4.57-6.amzn2023.0.7 |
| python3-dnf-4.14.0-1.amzn2023.0.6 |
| rust-toolset-srpm-macros-1.84.0-4.amzn2023.0. |
| system-release-2023.6.20250218-0.amzn2023 |
| yum-4.14.0-1.amzn2023.0.6 |

## Minimal AMI
<a name="amis-2023.6.20250218.minimal-ami"></a>

|  |
| --- |
| amazon-ec2-net-utils-2.5.4-1.amzn2023.0.1 |
| amazon-linux-repo-s3-2023.6.20250218-0.amzn2023 |
| dnf-data-4.14.0-1.amzn2023.0.6 |
| dnf-4.14.0-1.amzn2023.0.6 |
| grub2-common-1:2.06-61.amzn2023.0.14 |
| grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.14 |
| grub2-pc-modules-1:2.06-61.amzn2023.0.14 |
| grub2-tools-minimal-1:2.06-61.amzn2023.0.14 |
| grub2-tools-1:2.06-61.amzn2023.0.14 |
| kernel-libbpf-6.1.128-136.201.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20250218-0.amzn2023 |
| kernel-6.1.128-136.201.amzn2023 |
| libxml2-2.10.4-1.amzn2023.0.8 |
| openldap-2.4.57-6.amzn2023.0.7 |
| python3-dnf-4.14.0-1.amzn2023.0.6 |
| system-release-2023.6.20250218-0.amzn2023 |
| yum-4.14.0-1.amzn2023.0.6 |

## Minimal container image
<a name="amis-2023.6.20250218.minimal-container-ami"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250218-0.amzn2023 |
| dnf-data-4.14.0-1.amzn2023.0.6 |
| libxml2-2.10.4-1.amzn2023.0.8 |
| system-release-2023.6.20250218-0.amzn2023 |

## Contact us
<a name="amis-2023.6.20250218.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
