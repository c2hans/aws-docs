---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241010.html
---

# Amazon Linux 2023 version 2023.6.20241010 release notes
<a name="relnotes-2023.6.20241010"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20241010.

**Topics**
+ [Major updates](#major-updates-2023.6.20241010)
+ [Repository](#amis-2023.6.20241010.repository)
+ [Docker container image](#amis-2023.6.20241010.container-image)
+ [Default AMI](#amis-2023.6.20241010.default-ami)
+ [Minimal AMI](#amis-2023.6.20241010.minimal-ami)
+ [Minimal container image](#amis-2023.6.20241010.minimal-container-ami)
+ [Contact us](#amis-2023.6.20241010.contact-us)

## Major updates
<a name="major-updates-2023.6.20241010"></a>

This release represents an update to the sixth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ The crash package was updated to version 8.0.4-2 to address an incompatibility with kernel-6.1.109-118.189 and newer. If you are using the recommended options to update Amazon Linux 2023, such as booting into an updated AMI or using the dnf upgrade feature, you will automatically receive an updated, compatible crash package. If you install security updates only and want to continue to use the crash utility, you must upgrade it to crash-8.0.4-2 or later.
+ The iproute2 package was updated to version 6.10.
+  The X11 subsystem received a major update, as well as the additon of `xterm`. Using a headless X11 server such as `Xvfb`, it is possible to use automated testing tools for graphical applications on AL2023. For running graphical applications on AL2023, remote X11 continues to be supported, enabling running graphical applications on AL2023, and having a local X11 Server be used as a display. The reference compositor for Wayland, `weston` was also added, including RDP support. Using the RDP functionality of `weston` needs to have a suitable security model layered on top of it. AL2023 does not currently include `Xwayland` to run X11 applications under Wayland.
+ PostgreSQL version 16 was added ([requested on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/516)).
+ The `mod_security` security module for the Apache HTTP Server was added ([requested on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/429)).
+ Tomcat version 10 was added ([requested on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/546)), along with `tomcat_native` (also [requested on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/568)).
+ `microdnf` (used in the [Minimal Container Image](https://docs.aws.amazon.com/linux/al2023/ug/minimal-container.html)) has been updated to version 3.10 ([requested on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/595)).
+ OpenVPN has been added ([requested on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/79)).
+ The `fail2ban` package has been added ([requested on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/383)).
+ [Finch](https://runfinch.com/), an open source tool for local container development, has been added to AL2023, along with `soci-snapshotter`. Finch is also available for developers on macOS (Intel and Apple Silicon), and Windows.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20241010.repository"></a>

### New packages in AL2023.6.20241010 since AL2023.5.20241001
<a name="new-AL2023.5.20241001-AL2023.6.20241010"></a>

 Comparing AL2023.5.20241001 version 2023.5.20241001 to AL2023.6.20241010 version [2023.6.20241010](#relnotes-2023.6.20241010).

| Package Type | Number of new packages in AL2023.6.20241010 compared to AL2023.5.20241001 |
| --- | --- |
| Source RPMs | 47 |
| Total Binary RPMs | 170 |
|  noarch binary RPMs | 26 |
|  x86\_64 binary RPMs | 72 |
|  aarch64 binary RPMs | 72 |

New packages in AL2023.6.20241010:

- ** `catch1` **
  - **RPM:**  catch1-devel
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.12.2-16.amzn2023

- ** `edid-decode` **
  - **RPM:**  edid-decode
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0-68.20240130git7a27b339.amzn2023

- ** `fail2ban` **
  - **RPM:**  fail2ban  / **Architectures:** noarch
  - **RPM:**  fail2ban-all  / **Architectures:** noarch
  - **RPM:**  fail2ban-firewalld  / **Architectures:** noarch
  - **RPM:**  fail2ban-mail  / **Architectures:** noarch
  - **RPM:**  fail2ban-selinux  / **Architectures:** noarch
  - **RPM:**  fail2ban-sendmail  / **Architectures:** noarch
  - **RPM:**  fail2ban-server  / **Architectures:** noarch
  - **RPM:**  fail2ban-systemd  / **Architectures:** noarch
  - **RPM:**  fail2ban-tests  / **Architectures:** noarch
  - **Version:** 1.1.0-1.amzn2023.0.1

- ** `iceauth` **
  - **RPM:**  iceauth
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.9-7.amzn2023

- ** `ipmitool` **
  - **RPM:**  bmc-snmp-proxy  / **Architectures:** noarch
  - **RPM:**  exchange-bmc-os-info  / **Architectures:** noarch
  - **RPM:**  ipmievd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ipmitool  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.8.19-7.amzn2023

- ** `iproute` **
  - **RPM:**  iproute-doc
  - **Architectures:** aarch64, x86\_64
  - **Version:** 6.10.0-319.amzn2023.0.1

- ** `libxcvt` **
  - **RPM:**  cvt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxcvt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxcvt-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.1.2-6.amzn2023

- ** `mod_security` **
  - **RPM:**  mod\_security  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_security-mlogc  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.9.7-6.amzn2023.0.1

- ** `mod_security_crs` **
  - **RPM:**  mod\_security\_crs
  - **Architectures:** noarch
  - **Version:** 4.2.0-1.amzn2023.0.1

- ** `netplan` **
  - **RPM:**  netplan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netplan-default-backend-networkd  / **Architectures:** noarch
  - **RPM:**  netplan-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netplan-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-netplan  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.1-1.amzn2023

- ** `openvpn` **
  - **RPM:**  openvpn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openvpn-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.6.12-1.amzn2023.0.1

- ** `PEGTL` **
  - **RPM:**  PEGTL-devel
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.8.3-9.amzn2023

- ** `postgresql16` **
  - **RPM:**  postgresql16  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-contrib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-llvmjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-plperl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-plpython3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-pltcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-private-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-private-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-test-rpm-macros  / **Architectures:** noarch
  - **RPM:**  postgresql16-upgrade  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-upgrade-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 16.4-1.amzn2023.0.1

- ** `python-cpio` **
  - **RPM:**  python3-cpio
  - **Architectures:** noarch
  - **Version:** 0.1-49.amzn2023

- ** `python-inotify` **
  - **RPM:**  python3-inotify
  - **Architectures:** noarch
  - **Version:** 0.9.6-34.amzn2023

- ** `runfinch-finch` **
  - **RPM:**  runfinch-finch
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.0-1.amzn2023.0.1

- ** `sessreg` **
  - **RPM:**  sessreg
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.2-9.amzn2023

- ** `soci-snapshotter` **
  - **RPM:**  soci-snapshotter
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.7.0-1.amzn2023.0.2

- ** `tomcat10` **
  - **RPM:**  tomcat10  / **Architectures:** noarch
  - **RPM:**  tomcat10-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat10-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat10-el-5.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat10-jsp-3.1-api  / **Architectures:** noarch
  - **RPM:**  tomcat10-lib  / **Architectures:** noarch
  - **RPM:**  tomcat10-servlet-6.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat10-webapps  / **Architectures:** noarch
  - **Version:** 10.1.29-1.amzn2023.0.1

- ** `tomcat-native` **
  - **RPM:**  tomcat-native
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.0.8-4.amzn2023.0.1

- ** `usbguard` **
  - **RPM:**  usbguard  / **Architectures:** aarch64, x86\_64
  - **RPM:**  usbguard-dbus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  usbguard-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  usbguard-notifier  / **Architectures:** aarch64, x86\_64
  - **RPM:**  usbguard-selinux  / **Architectures:** noarch
  - **RPM:**  usbguard-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.3-4.amzn2023

- ** `weston` **
  - **RPM:**  weston  / **Architectures:** aarch64, x86\_64
  - **RPM:**  weston-demo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  weston-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  weston-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  weston-session  / **Architectures:** noarch
  - **Version:** 13.0.3-2.amzn2023.0.2

- ** `xdpyinfo` **
  - **RPM:**  xdpyinfo
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.3-5.amzn2023

- ** `xdriinfo` **
  - **RPM:**  xdriinfo
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.7-4.amzn2023

- ** `xev` **
  - **RPM:**  xev
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.2.4-8.amzn2023

- ** `xeyes` **
  - **RPM:**  xeyes
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.0-3.amzn2023

- ** `xfd` **
  - **RPM:**  xfd
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.2-2.amzn2023

- ** `xfontsel` **
  - **RPM:**  xfontsel
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.1-25.amzn2023

- ** `xgamma` **
  - **RPM:**  xgamma
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.7-3.amzn2023

- ** `xhost` **
  - **RPM:**  xhost
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.9-6.amzn2023

- ** `xinput` **
  - **RPM:**  xinput
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.6.4-2.amzn2023

- ** `xisxwayland` **
  - **RPM:**  xisxwayland
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2-4.amzn2023

- ** `xkill` **
  - **RPM:**  xkill
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.6-5.amzn2023

- ** `xlsatoms` **
  - **RPM:**  xlsatoms
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.4-4.amzn2023

- ** `xlsclients` **
  - **RPM:**  xlsclients
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.4-8.amzn2023

- ** `xlsfonts` **
  - **RPM:**  xlsfonts
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.7-6.amzn2023

- ** `xmodmap` **
  - **RPM:**  xmodmap
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.11-6.amzn2023

- ** `xprop` **
  - **RPM:**  xprop
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.2.7-1.amzn2023

- ** `xrandr` **
  - **RPM:**  xrandr
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.5.2-5.amzn2023

- ** `xrdb` **
  - **RPM:**  xrdb
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.2.2-3.amzn2023.0.1

- ** `xrefresh` **
  - **RPM:**  xrefresh
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.7-14.amzn2023

- ** `xset` **
  - **RPM:**  xset
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.2.5-5.amzn2023

- ** `xsetroot` **
  - **RPM:**  xsetroot
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.2-10.amzn2023

- ** `xstdcmap` **
  - **RPM:**  xstdcmap
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.4-10.amzn2023

- ** `xterm` **
  - **RPM:**  xterm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xterm-resize  / **Architectures:** aarch64, x86\_64
  - **Version:** 394-1.amzn2023.0.1

- ** `xvinfo` **
  - **RPM:**  xvinfo
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.4-5.amzn2023

- ** `xwininfo` **
  - **RPM:**  xwininfo
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.5-8.amzn2023

### AL2023.6.20241010 upgrades from AL2023.5.20241001
<a name="vercmp-AL2023.5.20241001-AL2023.6.20241010"></a>

 Comparing [2023.5.20241001](relnotes-2023.5.20241001.md) to [2023.6.20241010](#relnotes-2023.6.20241010).

| Package Type | Count |
| --- | --- |
| Source | 94 |
| Total Binary | 710 |
|  noarch binary RPMs | 236 |
|  x86\_64 binary RPMs | 237 |
|  aarch64 binary RPMs | 237 |

The full comparison of RPM package versions is below.

- ** `amazon-ecr-credential-helper` **
  - **RPM:**  amazon-ecr-credential-helper
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.7.1-4.amzn2023
  - **AL2023.6.20241010 version:** 0.9.0-1.amzn2023

- ** [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 2.0.4-1.amzn2023
  - **AL2023.6.20241010 version:** 2.1.0-1.amzn2023

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 3.3.380.0-1.amzn2023
  - **AL2023.6.20241010 version:** 3.3.859.0-1.amzn2023

- ** `aws-cfn-bootstrap` **
  - **RPM:**  aws-cfn-bootstrap
  - **Architectures:** noarch
  - **AL2023.5.20241001 version:** 2.0-30.amzn2023
  - **AL2023.6.20241010 version:** 2.0-31.amzn2023

- ** `aws-kinesis-agent` **
  - **RPM:**  aws-kinesis-agent
  - **Architectures:** noarch
  - **AL2023.5.20241001 version:** 2.0.8-2.amzn2023
  - **AL2023.6.20241010 version:** 2.0.9-3.amzn2023

- ** `aws-nitro-enclaves-acm` **
  - **RPM:**  aws-nitro-enclaves-acm
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.2.0-2.amzn2023
  - **AL2023.6.20241010 version:** 1.4.0-1.amzn2023

- ** `bdftopcf` **
  - **RPM:**  bdftopcf
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1-2.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.1-3.amzn2023.0.1

- ** `bubblewrap` **
  - **RPM:**  bubblewrap
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.7.0-2.amzn2023.0.1
  - **AL2023.6.20241010 version:** 0.10.0-1.amzn2023.0.1

- ** `c-ares` **
  - **RPM:**  c-ares  / **Architectures:** aarch64, x86\_64
  - **RPM:**  c-ares-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.19.0-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 1.19.1-1.amzn2023.0.1

- ** `clamav` **
  - **RPM:**  clamav  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-data  / **Architectures:** noarch
  - **RPM:**  clamav-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-doc  / **Architectures:** noarch
  - **RPM:**  clamav-filesystem  / **Architectures:** noarch
  - **RPM:**  clamav-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-milter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-update  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamd  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.103.11-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 0.103.12-1.amzn2023.0.1

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.7.20-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 1.7.22-1.amzn2023.0.2

- ** `cups-filters` **
  - **RPM:**  cups-filters  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filters-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filters-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.28.16-3.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.28.16-3.amzn2023.0.3

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.86.3-1.amzn2023
  - **AL2023.6.20241010 version:** 1.87.0-1.amzn2023

- ** `fonttosfnt` **
  - **RPM:**  fonttosfnt
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.2.2-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.2.3-3.amzn2023.0.1

- ** `gdb` **
  - **RPM:**  gdb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdb-doc  / **Architectures:** noarch
  - **RPM:**  gdb-gdbserver  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdb-headless  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdb-minimal  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 12.1-5.amzn2023.0.3
  - **AL2023.6.20241010 version:** 12.1-5.amzn2023.0.4

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 1.22.5-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 1.22.7-1.amzn2023.0.1

- ** `iproute` **
  - **RPM:**  iproute  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iproute-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iproute-tc  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 5.10.0-2.amzn2023.0.5
  - **AL2023.6.20241010 version:** 6.10.0-319.amzn2023.0.1

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
  - **AL2023.5.20241001 version:** 6.1.109-118.189.amzn2023
  - **AL2023.6.20241010 version:** 6.1.112-122.189.amzn2023

- ** `libdmx` **
  - **RPM:**  libdmx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdmx-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.4-10.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.5-3.amzn2023.0.3

- ** `libdrm` **
  - **RPM:**  drm-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdrm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdrm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 2.4.110-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 2.4.123-1.amzn2023.0.1

- ** `libfontenc` **
  - **RPM:**  libfontenc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfontenc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.3-15.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.7-3.amzn2023.0.1

- ** `libgcrypt` **
  - **RPM:**  libgcrypt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgcrypt-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.10.2-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 1.10.2-1.amzn2023.0.2

- ** `libglvnd` **
  - **RPM:**  libglvnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-core-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-egl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-gles  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-glx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-opengl  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.3.4-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.7.0-4.amzn2023.0.1

- ** `libICE` **
  - **RPM:**  libICE  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libICE-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.0.10-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.1-3.amzn2023.0.1

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 15.8-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 16.4-1.amzn2023.0.1

- ** `libSM` **
  - **RPM:**  libSM  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libSM-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.2.3-8.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.2.4-3.amzn2023.0.1

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 4.4.0-4.amzn2023.0.18
  - **AL2023.6.20241010 version:** 4.4.0-4.amzn2023.0.19

- ** `libva` **
  - **RPM:**  libva  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libva-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 2.11.0-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 2.21.0-3.amzn2023.0.2

- ** `libvdpau` **
  - **RPM:**  libvdpau  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvdpau-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvdpau-docs  / **Architectures:** noarch
  - **RPM:**  libvdpau-trace  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.4-4.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.5-6.amzn2023.0.1

- ** `libX11` **
  - **RPM:**  libX11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libX11-common  / **Architectures:** noarch
  - **RPM:**  libX11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libX11-xcb  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.7.2-3.amzn2023.0.4
  - **AL2023.6.20241010 version:** 1.8.10-2.amzn2023.0.1

- ** `libXau` **
  - **RPM:**  libXau  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXau-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.0.9-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.0.11-6.amzn2023.0.1

- ** `libXaw` **
  - **RPM:**  libXaw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXaw-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.0.13-17.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.0.15-3.amzn2023.0.1

- ** `libxcb` **
  - **RPM:**  libxcb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxcb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxcb-doc  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 1.13.1-7.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.17.0-1.amzn2023.0.1

- ** `libXcomposite` **
  - **RPM:**  libXcomposite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXcomposite-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.4.5-5.amzn2023.0.2
  - **AL2023.6.20241010 version:** 0.4.6-3.amzn2023.0.1

- ** `libXcursor` **
  - **RPM:**  libXcursor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXcursor-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.2.0-5.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.2.1-7.amzn2023.0.1

- ** `libXdamage` **
  - **RPM:**  libXdamage  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXdamage-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.5-5.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.6-3.amzn2023.0.1

- ** `libXdmcp` **
  - **RPM:**  libXdmcp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXdmcp-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.3-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.4-3.amzn2023.0.1

- ** `libXext` **
  - **RPM:**  libXext  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXext-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.3.4-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.3.6-1.amzn2023.0.1

- ** `libXfixes` **
  - **RPM:**  libXfixes  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXfixes-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 6.0.0-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 6.0.1-3.amzn2023.0.1

- ** `libXfont2` **
  - **RPM:**  libXfont2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXfont2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 2.0.3-10.amzn2023.0.2
  - **AL2023.6.20241010 version:** 2.0.7-1.amzn2023.0.1

- ** `libXft` **
  - **RPM:**  libXft  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXft-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 2.3.3-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 2.3.8-6.amzn2023.0.1

- ** `libXi` **
  - **RPM:**  libXi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXi-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.7.10-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.8.2-1.amzn2023.0.1

- ** `libXinerama` **
  - **RPM:**  libXinerama  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXinerama-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.4-8.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.5-6.amzn2023.0.1

- ** `libxkbcommon` **
  - **RPM:**  libxkbcommon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxkbcommon-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxkbcommon-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxkbcommon-x11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxkbcommon-x11-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.3.0-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.6.0-2.amzn2023.0.1

- ** `libxkbfile` **
  - **RPM:**  libxkbfile  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxkbfile-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.0-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.3-1.amzn2023.0.1

- ** `libXmu` **
  - **RPM:**  libXmu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXmu-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.3-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.2.1-1.amzn2023.0.1

- ** `libXpm` **
  - **RPM:**  libXpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXpm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 3.5.15-2.amzn2023.0.3
  - **AL2023.6.20241010 version:** 3.5.17-3.amzn2023.0.1

- ** `libXrandr` **
  - **RPM:**  libXrandr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXrandr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.5.2-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.5.4-3.amzn2023.0.1

- ** `libXrender` **
  - **RPM:**  libXrender  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXrender-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.9.10-14.amzn2023.0.2
  - **AL2023.6.20241010 version:** 0.9.11-6.amzn2023.0.1

- ** `libXres` **
  - **RPM:**  libXres  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXres-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.2.0-12.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.2.2-3.amzn2023.0.1

- ** `libXScrnSaver` **
  - **RPM:**  libXScrnSaver  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXScrnSaver-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.2.3-8.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.2.4-3.amzn2023.0.1

- ** `libxshmfence` **
  - **RPM:**  libxshmfence  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxshmfence-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.3-8.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.3.2-3.amzn2023.0.1

- ** `libXt` **
  - **RPM:**  libXt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXt-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.2.0-4.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.3.0-3.amzn2023.0.1

- ** `libXtst` **
  - **RPM:**  libXtst  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXtst-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.2.3-14.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.2.5-1.amzn2023.0.1

- ** `libXv` **
  - **RPM:**  libXv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXv-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.0.11-14.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.0.12-3.amzn2023.0.1

- ** `libXxf86dga` **
  - **RPM:**  libXxf86dga  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXxf86dga-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.5-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.6-3.amzn2023.0.1

- ** `libXxf86vm` **
  - **RPM:**  libXxf86vm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXxf86vm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.4-16.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.5-6.amzn2023.0.1

- ** `mesa` **
  - **RPM:**  mesa-dri-drivers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libd3d  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libd3d-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libEGL  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libEGL-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libgbm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libgbm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libGL  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libglapi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libGL-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOpenCL  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOpenCL-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOSMesa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOSMesa-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libxatracker  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libxatracker-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-omx-drivers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-va-drivers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-vdpau-drivers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-vulkan-drivers  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 22.3.3-1140.amzn2023.0.3
  - **AL2023.6.20241010 version:** 24.1.7-1251.amzn2023.0.2

- ** `microdnf` **
  - **RPM:**  microdnf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  microdnf-dnf  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 3.8.1-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 3.10.0-2.amzn2023.0.1

- ** `mkfontscale` **
  - **RPM:**  mkfontscale
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.2.1-2.amzn2023.0.3
  - **AL2023.6.20241010 version:** 1.2.2-6.amzn2023.0.1

- ** `nerdctl` **
  - **RPM:**  nerdctl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.7.6-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.7.7-1.amzn2023.0.1

- ** `oath-toolkit` **
  - **RPM:**  liboath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liboath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liboath-doc  / **Architectures:** noarch
  - **RPM:**  libpskc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpskc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpskc-doc  / **Architectures:** noarch
  - **RPM:**  oathtool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_oath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pskctool  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 2.6.9-2.amzn2023
  - **AL2023.6.20241010 version:** 2.6.12-1.amzn2023.0.1

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-snapsafe-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 3.0.8-1.amzn2023.0.14
  - **AL2023.6.20241010 version:** 3.0.8-1.amzn2023.0.16

- ** `orc` **
  - **RPM:**  orc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  orc-compiler  / **Architectures:** aarch64, x86\_64
  - **RPM:**  orc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  orc-doc  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 0.4.31-4.amzn2023.0.3
  - **AL2023.6.20241010 version:** 0.4.31-4.amzn2023.0.4

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
  - **AL2023.5.20241001 version:** 8.2.21-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 8.2.23-1.amzn2023.0.1

- ** `pixman` **
  - **RPM:**  pixman  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pixman-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.40.0-3.amzn2023.0.3
  - **AL2023.6.20241010 version:** 0.43.4-1.amzn2023.0.4

- ** `postgresql-odbc` **
  - **RPM:**  postgresql-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql-odbc-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 13.01.0000-5.amzn2023.0.1
  - **AL2023.6.20241010 version:** 13.02.0000-1.amzn2023.0.1

- ** `python3.11-pip` **
  - **RPM:**  python3.11-pip  / **Architectures:** noarch
  - **RPM:**  python3.11-pip-wheel  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 22.3.1-2.amzn2023.0.2
  - **AL2023.6.20241010 version:** 22.3.1-2.amzn2023.0.3

- ** `python-dns` **
  - **RPM:**  python3-dns  / **Architectures:** noarch
  - **RPM:**  python3-dns\+dnssec  / **Architectures:** noarch
  - **RPM:**  python3-dns\+idna  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 2.1.0-3.amzn2023.0.3
  - **AL2023.6.20241010 version:** 2.1.0-3.amzn2023.0.4

- ** `python-pip` **
  - **RPM:**  python3-pip  / **Architectures:** noarch
  - **RPM:**  python3-pip-wheel  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 21.3.1-2.amzn2023.0.7
  - **AL2023.6.20241010 version:** 21.3.1-2.amzn2023.0.8

- ** `rgb` (`xorg-x11-server-utils` in AL2023.5.20241001) **
  - **RPM:**  rgb
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.0.6-39.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.0.6-48.amzn2023

- ** `runc` **
  - **RPM:**  runc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1.13-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 1.1.14-1.amzn2023.0.1

- ** `selinux-policy` **
  - **RPM:**  selinux-policy  / **Architectures:** noarch
  - **RPM:**  selinux-policy-devel  / **Architectures:** noarch
  - **RPM:**  selinux-policy-doc  / **Architectures:** noarch
  - **RPM:**  selinux-policy-minimum  / **Architectures:** noarch
  - **RPM:**  selinux-policy-mls  / **Architectures:** noarch
  - **RPM:**  selinux-policy-sandbox  / **Architectures:** noarch
  - **RPM:**  selinux-policy-targeted  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 37.22-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 38.1.45-1.amzn2023.0.1

- ** `setxkbmap` **
  - **RPM:**  setxkbmap
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.3.2-3.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.3.4-3.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 2023.5.20241001-0.amzn2023
  - **AL2023.6.20241010 version:** 2023.6.20241010-0.amzn2023

- ** `unbound` **
  - **RPM:**  python3-unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-anchor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.17.1-1.amzn2023.0.5
  - **AL2023.6.20241010 version:** 1.17.1-1.amzn2023.0.6

- ** `vulkan-headers` **
  - **RPM:**  vulkan-headers
  - **Architectures:** noarch
  - **AL2023.5.20241001 version:** 1.3.224.0-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 1.3.290.0-57.amzn2023.0.1

- ** `vulkan-loader` **
  - **RPM:**  vulkan-loader  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vulkan-loader-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.3.224.0-1.amzn2023.0.1
  - **AL2023.6.20241010 version:** 1.3.290.0-71.amzn2023.0.1

- ** `xcb-proto` **
  - **RPM:**  xcb-proto
  - **Architectures:** noarch
  - **AL2023.5.20241001 version:** 1.14.1-2.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.17.0-1.amzn2023.0.2

- ** `xcb-util` **
  - **RPM:**  xcb-util  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.4.0-17.amzn2023.0.2
  - **AL2023.6.20241010 version:** 0.4.1-5.amzn2023.0.1

- ** `xcb-util-cursor` **
  - **RPM:**  xcb-util-cursor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-cursor-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.1.4-4.amzn2023
  - **AL2023.6.20241010 version:** 0.1.4-4.amzn2023.0.1

- ** `xcb-util-image` **
  - **RPM:**  xcb-util-image  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-image-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.4.0-17.amzn2023.0.2
  - **AL2023.6.20241010 version:** 0.4.1-5.amzn2023.0.1

- ** `xcb-util-keysyms` **
  - **RPM:**  xcb-util-keysyms  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-keysyms-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.4.0-15.amzn2023.0.2
  - **AL2023.6.20241010 version:** 0.4.1-5.amzn2023.0.1

- ** `xcb-util-renderutil` **
  - **RPM:**  xcb-util-renderutil  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-renderutil-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.3.9-18.amzn2023.0.2
  - **AL2023.6.20241010 version:** 0.3.10-5.amzn2023.0.1

- ** `xcb-util-wm` **
  - **RPM:**  xcb-util-wm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-wm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 0.4.1-20.amzn2023.0.2
  - **AL2023.6.20241010 version:** 0.4.2-5.amzn2023.0.1

- ** `xkbcomp` **
  - **RPM:**  xkbcomp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xkbcomp-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.4.4-2.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.4.7-1.amzn2023.0.1

- ** `xkeyboard-config` **
  - **RPM:**  xkeyboard-config  / **Architectures:** noarch
  - **RPM:**  xkeyboard-config-devel  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 2.33-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 2.41-1.amzn2023.0.1

- ** `xorg-x11-fonts` **
  - **RPM:**  xorg-x11-fonts-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-cyrillic  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ethiopic  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-1-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-14-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-14-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-15-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-15-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-1-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-2-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-2-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-9-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-9-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-misc  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-Type1  / **Architectures:** noarch
  - **AL2023.5.20241001 version:** 7.5-31.amzn2023.0.2
  - **AL2023.6.20241010 version:** 7.5-38.amzn2023.0.1

- ** `xorg-x11-font-utils` **
  - **RPM:**  xorg-x11-font-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 7.5-51.amzn2023.0.2
  - **AL2023.6.20241010 version:** 7.5-59.amzn2023.0.1

- ** `xorg-x11-proto-devel` **
  - **RPM:**  xorg-x11-proto-devel
  - **Architectures:** noarch
  - **AL2023.5.20241001 version:** 2021.4-1.amzn2023.0.2
  - **AL2023.6.20241010 version:** 2024.1-2.amzn2023.0.2

- ** `xorg-x11-util-macros` **
  - **RPM:**  xorg-x11-util-macros
  - **Architectures:** noarch
  - **AL2023.5.20241001 version:** 1.19.3-2.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.20.0-4.amzn2023.0.1

- ** `xorg-x11-xauth` **
  - **RPM:**  xorg-x11-xauth
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.1-8.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.2-6.amzn2023.0.1

- ** `xorg-x11-xbitmaps` **
  - **RPM:**  xorg-x11-xbitmaps
  - **Architectures:** noarch
  - **AL2023.5.20241001 version:** 1.1.1-21.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.1.3-2.amzn2023.0.1

- ** `xorg-x11-xinit` **
  - **RPM:**  xorg-x11-xinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-xinit-session  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20241001 version:** 1.4.0-10.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.4.2-2.amzn2023.0.1

- ** `xorg-x11-xtrans-devel` **
  - **RPM:**  xorg-x11-xtrans-devel
  - **Architectures:** noarch
  - **AL2023.5.20241001 version:** 1.4.0-6.amzn2023.0.2
  - **AL2023.6.20241010 version:** 1.4.0-13.amzn2023.0.1

## Docker container image
<a name="amis-2023.6.20241010.container-image"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20241010-0.amzn2023 |
| libgcrypt-1.10.2-1.amzn2023.0.2 |
| openssl-libs-1:3.0.8-1.amzn2023.0.16 |
| python3-pip-wheel-21.3.1-2.amzn2023.0.8 |
| system-release-2023.6.20241010-0.amzn2023 |

## Default AMI
<a name="amis-2023.6.20241010.default-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20241010-0.amzn2023 |
| amazon-ssm-agent-3.3.859.0-1.amzn2023 |
| aws-cfn-bootstrap-2.0-31.amzn2023 |
| c-ares-1.19.1-1.amzn2023.0.1 |
| iproute-6.10.0-319.amzn2023.0.1 |
| kernel-libbpf-6.1.112-122.189.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20241010-0.amzn2023 |
| kernel-tools-6.1.112-122.189.amzn2023 |
| kernel-6.1.112-122.189.amzn2023 |
| libgcrypt-1.10.2-1.amzn2023.0.2 |
| openssl-libs-1:3.0.8-1.amzn2023.0.16 |
| openssl-1:3.0.8-1.amzn2023.0.16 |
| python3-pip-wheel-21.3.1-2.amzn2023.0.8 |
| selinux-policy-targeted-38.1.45-1.amzn2023.0.1 |
| selinux-policy-38.1.45-1.amzn2023.0.1 |
| system-release-2023.6.20241010-0.amzn2023 |

## Minimal AMI
<a name="amis-2023.6.20241010.minimal-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20241010-0.amzn2023 |
| iproute-6.10.0-319.amzn2023.0.1 |
| kernel-libbpf-6.1.112-122.189.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20241010-0.amzn2023 |
| kernel-6.1.112-122.189.amzn2023 |
| libgcrypt-1.10.2-1.amzn2023.0.2 |
| openssl-libs-1:3.0.8-1.amzn2023.0.16 |
| openssl-1:3.0.8-1.amzn2023.0.16 |
| python3-pip-wheel-21.3.1-2.amzn2023.0.8 |
| selinux-policy-targeted-38.1.45-1.amzn2023.0.1 |
| selinux-policy-38.1.45-1.amzn2023.0.1 |
| system-release-2023.6.20241010-0.amzn2023 |

## Minimal container image
<a name="amis-2023.6.20241010.minimal-container-ami"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20241010-0.amzn2023 |
| libgcrypt-1.10.2-1.amzn2023.0.2 |
| microdnf-dnf-3.10.0-2.amzn2023.0.1 |
| microdnf-3.10.0-2.amzn2023.0.1 |
| openssl-libs-1:3.0.8-1.amzn2023.0.16 |
| system-release-2023.6.20241010-0.amzn2023 |

## Contact us
<a name="amis-2023.6.20241010.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
