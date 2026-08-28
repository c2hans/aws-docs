---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2011.09.html
---

# Amazon Linux 1 (AL1) version 2011.09 release notes
<a name="relnotes-2011.09"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2011.09 release.

## Upgrading to Amazon Linux 1 (AL1) version 2011.09
<a name="upgrading-2011.09"></a>
+ From Amazon Linux 1 (AL1) version 2011.02, run `sudo yum upgrade`.
+ From Amazon Linux 1 (AL1) version 2010.x, follow [these instructions](relnotes-2011.02.md).

## Major Changes
<a name="major-changes-2011.09"></a>
+ The beta tag has been removed from the Amazon Linux AMI.
+ The [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html) is avaliable to track security and privacy issues with Amazon Linux 1 (AL1).
+ `dracut` is now used to build the kernel `initramfs` images on install instead of `mkinitrd`.
+ `gnupg1` and `gnupg2` can now coexist on the same install and are alternatives-enabled.
+ PHP scripts have the option of using PHP-FPM.
+ Access to the Extra Packages for Enterprise Linux (EPEL 6) repository is configured, though not enabled by default.
+ Message of the Day (`/etc/motd`) lists when updates are available for installed packages.
+ AWS CloudFormation bootstrap scripts are included and can be used in conjunction with metadata defined in your template to install, configure, and start applications and services an instance launch time.

## Frequently Asked Questions
<a name="faq-2011.09"></a>

**How do I enable the primary EPEL 6 repository?**
 Log in to your AMI as root, and modify `/etc/yum.repos.d/epel.repo`. Under the section marked `[epel]`, change `enabled=0` to `enabled=1`.
 To temporarily enable the EPEL 6 repository, use the yum command line option `--enablerepo=epel`.

**Why does it take a long time for SSH to start up when running in a Virtual Private Cloud (VPC) without an Internet Gateway or NAT instance?**
 On boot, the Amazon Linux 1 (AL1) by default will install available security updates from the package repositories before services, such as SSH, start.
 If the AMI cannot access the `yum` repositories, it will timeout and retry multiple times before completing the boot procedure. Possible reasons for this are restrictive firewall settings or VPC settings, which prevent access to the Amazon Linux 1 (AL1) package repositories.
 If you encounter this issue you can either modify your environment so that the Amazon Linux AMI can connect to its package repositories or you can disable the security update on boot.

**To disable the security update on boot from the Amazon EC2 Console:**
+  On the "Advanced Instance Options" page in the Request Instances Wizard, there is a text field for sending the Amazon Linux 1 (AL1) `user-data`. This data can be entered as text, or uploaded as a file. In either case, the data should be:

  ```
  #cloud-config
  repo_upgrade: none
  ```

**To disable the security update on boot from the command line:**
+ Create a text file with the preceding user-data, and pass it to `ec2-run-instances` with the `-f data_file` flag.

**To disable the security update on boot when rebundling the Amazon Linux 1 (AL1):**
+ Modify `/etc/cloud/cloud.cfg` and change `repo_upgrade: security` to `repo_upgrade: none`.

## Known Issues
<a name="known-issues-2011.09"></a>

After using yum to upgrade to Amazon Linux 1 (AL1) version 2011.09, `t1.micro` 32-bit instances fail to reboot.

There is a bug in PV-Grub that affects the handling of memory pages from Xen on 32bit `t1.micro` instances. A new release of PV-Grub has been released to fix this problem. Some manual steps need to be performed to have your instance launch with the new PV-Grub.

As of 2011-11-01, the latest version of the PV-Grub Amazon Kernel Images (AKIs) is 1.02. Find the PV-Grub AKI's for your given region by running: `ec2-describe-images -o amazon --filter "manifest-location=*pv-grub-hd0_1.02-i386*" --region REGION`.

**Currently running instances need to be stopped before replacing the AKI. The following commands point an instance to the new AKI:**

1.

   ```
   $ ec2-stop-instances --region us-east-1 i-#####
   ```

1.

   ```
   $ ec2-modify-instance-attribute --kernel aki-805ea7e9 --region us-east-1 i-#####
   ```

1.

   ```
   $ ec2-start-instances --region us-east-1 i-#####.
   ```

If launching a custom AMI, add a --kernel parameter to the ec2-run-instances command or choose the AKI in the kernel drop-down of the console launch widget.

## Package Updates
<a name="package-updates-2011.09"></a>

### New packages
<a name="new-packages-2011.09"></a>
+ `PyGreSQL-3.8.1-2.2.amzn1.src` - A Python client library for PostgreSQL
+ `atlas-3.8.3-12.4.2.amzn1.src` - Automatically Tuned Linear Algebra Software
+ `augeas-0.7.2-6.2.amzn1.src` - A library for changing configuration files
+ `aws-apitools-cfn-1.0.8-1.2.amzn1.src` - AWS CloudFormation API tools - control cfn instances from the command line
+ `aws-cfn-bootstrap-1.0-3.amzn1.src` - An EC2 bootstrapper for CloudFormation
+ `busybox-1.15.1-11.6.amzn1.src` - Statically linked binary providing simplified versions of system commands
+ `collectd-5.0.0-1.8.amzn1.src` - Statistics collection daemon for filling RRD files
+ `cvs2svn-2.3.0-1.2.amzn1.src` - CVS to Subversion Repository Converter
+ `dash-0.5.5.1-3.1.4.amzn1.src` - Small and fast POSIX-compliant shell
+ `docbook5-schemas-5.0-4.1.2.amzn1.src` - Norman Walsh's schemas (DTD, Relax NG, W3C schema) for Docbook 5.X
+ `docbook5-style-xsl-1.75.2-4.2.amzn1.src` - Norman Walsh's XSL stylesheets for DocBook 5.X
+ `dracut-004-53.10.amzn1.src` - Initramfs generator using udev
+ `epel-release-6-5.2.amzn1.src` - Extra Packages for Enterprise Linux repository configuration
+ `facter-1.5.9-1.4.amzn1.src` - Ruby module for collecting simple facts about a host operating system
+ `foomatic-4.0.4-1.6.amzn1.src` - Database of printers and printer drivers
+ `foomatic-db-4.0-7.20091126.2.amzn1.src` - Database of printers and printer drivers
+ `iotop-0.3.2-3.2.amzn1.src` - Top like utility for I/O
+ `irssi-0.8.15-3.2.amzn1.src` - Modular text mode IRC client with Perl scripting
+ `jemalloc-2.2.1-1.1.amzn1.src` - General-purpose scalable concurrent malloc implementation
+ `kexec-tools-2.0.0-188.6.amzn1.src` - The kexec/kdump userspace component.
+ `latrace-0.5.9-2.2.amzn1.src` - LD\_AUDIT feature frontend for glibc 2.4\+
+ `libEMF-1.0.4-1.2.amzn1.src` - A library for generating Enhanced Metafiles
+ `libcgroup-0.37-2.2.amzn1.src` - Tools and libraries to control and monitor control groups
+ `libconfig-1.3.2-1.1.2.amzn1.src` - C/C\+\+ configuration file library
+ `libffi-3.0.5-3.2.2.amzn1.src` - A portable foreign function interface library
+ `libmemcached-0.31-1.1.4.amzn1.src` - Client library and command line tools for memcached server
+ `libtalloc-2.0.1-1.1.2.amzn1.src` - The talloc library
+ `mod_fcgid-2.3.6-1.2.amzn1.src` - FastCGI interface module for Apache 2
+ `mpage-2.5.6-8.3.amzn1.src` - A tool for printing multiple pages of text on each printed page
+ `netlabel_tools-0.19-7.3.amzn1.src` - Tools to manage the Linux NetLabel subsystem
+ `numpy-1.3.0-6.2.3.amzn1.src` - A fast multidimensional array facility for Python
+ `perl-FCGI-1:0.71-5.0.amzn1.src` - FastCGI Perl bindings
+ `perl-Regexp-Common-2010010201-1.0.amzn1.src` - Regexp::Common Perl module
+ `php-pecl-memcached-1.0.0-1.1.amzn1.src` - Extension to work with the Memcached caching daemon
+ `plotutils-2.5-7.1.2.amzn1.src` - GNU vector and raster graphics utilities and libraries
+ `pssh-2.2.2-2.1.amzn1.src` - Parallel SSH tools
+ `pstoedit-3.45-10.2.amzn1.src` - Translates PostScript and PDF graphics into other vector formats
+ `puppet-2.6.6-1.0.amzn1.src` - A network tool for managing many disparate systems
+ `python-psycopg2-2.0.13-2.2.amzn1.src` - A PostgreSQL database adapter for Python
+ `quilt-0.48-2.1.amzn1.src` - Scripts for working with series of patches
+ `ruby-augeas-0.3.0-2.2.amzn1.src` - Ruby bindings for Augeas
+ `rubygem-flexmock-0.8.6-1.1.2.amzn1.src` - Mock object library for ruby
+ `rubygem-rake-0.8.7-2.1.4.amzn1.src` - Ruby based make-like utility
+ `socat-1.7.1.3-3.4.amzn1.src` - Bidirectional data relay between two data channels ('netcat\+\+')
+ `tetex-tex4ht-1.0.2008_09_16_1413-4.2.amzn1.src` - Translates TeX and LaTeX into HTML or XML\+MathML
+ `units-1.87-7.3.amzn1.src` - A utility for converting amounts from one unit to another
+ `update-motd-1.0-1.2.amzn1.src` - Framework for dynamically generating MOTD
+ `varnish-2.1.5-1.1.amzn1.src` - High-performance HTTP accelerator
+ `xml-stylebook-1.0-0.5.b3_xalan2.svn313293.3.amzn1.src` - Apache XML Stylebook
+ `xmltoman-0.4-4.2.amzn1.src` - Scripts for converting XML to roff or HTML

### Compatibility Packages
<a name="compatibility-packages-2011.09"></a>
+ `compat-ImageMagick-6.2.8.0` - compatibility library for ImageMagick 6.2.8

### Removed Packages
<a name="removed-packages-2011.09"></a>

These packages have been deprecated either due to availability of similar functionality offered by other packages or lack of meaningful functionality in the context of an AMI running in EC2. As a result these packages are no longer supported/maintained in this release of Amazon Linux AMI:
+ `ccid`
+ `edac-utils`
+ `fcoe-utils`
+ `libdrm`
+ `libhbalinux`
+ `libpciaccess`
+ `lm_sensors`
+ `pcsc-lite`
+ `sos`

### Obsoleted Packages
<a name="obsoleted-packages-2011.09"></a>
+ `nash` and `mkinitrd` are obsoleted by `dracut`
+ `python-yaml` has been renamed `PyYAML`

### Updated Packages
<a name="updated-packages-2011.09"></a>

These packages have been updated with security patches, bugfixes, and feature updates.
+ `GeoIP-1.4.8`
+ `PyYAML-3.09`
+ `apr-1.3.9`
+ `audit-2.1`
+ `authconfig-6.1.12`
+ `autofs-5.0.5`
+ `automake-1.11.1`
+ `avahi-0.6.25`
+ `aws-amitools-ec2-1.4.0.1`
+ `aws-apitools-as-1.0.39.0`
+ `aws-apitools-common-1.0.1`
+ `aws-apitools-ec2-1.4.4.2`
+ `aws-apitools-elb-1.0.14.3`
+ `aws-apitools-mon-1.0.12.1`
+ `aws-apitools-rds-1.4.007`
+ `aws-scripts-ses-2011.007.21`
+ `basesystem-10.0`
+ `bash-4.1.2`
+ `beecrypt-4.2.1`
+ `bind-9.7.3`
+ `binutils-2.20.51.0.2`
+ `blktrace-1.0.1`
+ `bsh-1.3.0`
+ `cloud-init-0.5.15`
+ `compat-expat-1.95.8`
+ `coreutils-8.4`
+ `corosync-1.2.3`
+ `cpio-2.10`
+ `cracklib-2.8.16`
+ `crash-5.1.7`
+ `cronie-1.4.4`
+ `cryptsetup-luks-1.2.0`
+ `cups-1.4.2`
+ `curl-7.19.7`
+ `cyrus-imapd-2.3.16`
+ `dbus-1.2.24`
+ `device-mapper-multipath-0.4.9`
+ `dhcp-4.1.1`
+ `dirmngr-1.1.0`
+ `dkim-milter-2.8.3`
+ `dmidecode-2.11`
+ `docbook-utils-0.6.14`
+ `dovecot-2.0.9`
+ `e2fsprogs-1.41.12`
+ `ec2-utils-0.2`
+ `ecryptfs-utils-82`
+ `elfutils-0.152`
+ `emacs-23.1`
+ `fakechroot-2.9`
+ `fipscheck-1.2.0`
+ `freeradius-2.1.10`
+ `freetype-2.3.11`
+ `fuse-2.8.4`
+ `gcc-4.4.5`
+ `gdb-7.2`
+ `get_reference_source-1.1`
+ `ghostscript-8.70`
+ `git-1.7.4.5`
+ `glib2-2.22.5`
+ `glibc-2.12`
+ `gnupg-1.4.11`
+ `gnupg2-2.0.18`
+ `gpgme-1.3.1`
+ `grub-0.97`
+ `grubby-7.0.15`
+ `hal-0.5.14`
+ `hesinfo-3.1.0`
+ `httpd-2.2.21`
+ `hwdata-0.233`
+ `initscripts-9.03.23`
+ `iproute-2.6.32`
+ `iptables-1.4.7`
+ `iputils-20071127`
+ `irqbalance-0.55`
+ `jadetex-3.13`
+ `java-1.6.0-openjdk-1.6.0.0`
+ `jss-4.2.6`
+ `kernel-2.6.35.14`
+ `krb5-1.9`
+ `ksh-20100621`
+ `ldapjdk-4.18`
+ `libXfont-1.4.1`
+ `libassuan-2.0.2`
+ `liberation-fonts-1.05.1.20090721`
+ `libgcrypt-1.4.5`
+ `libgpg-error-1.10`
+ `libgssglue-0.1`
+ `libksba-1.2.0`
+ `libmcrypt-2.5.8`
+ `libnl-1.1`
+ `libpng-1.2.46`
+ `libproxy-0.3.0`
+ `libsoup-2.28.2`
+ `libtasn1-2.3`
+ `libtiff-3.9.4`
+ `libtirpc-0.2.1`
+ `libusb-0.1.12`
+ `lighttpd-1.4.29`
+ `logrotate-3.7.8`
+ `logwatch-7.3.6`
+ `lvm2-2.02.83`
+ `m17n-contrib-1.1.10`
+ `mailman-2.1.12`
+ `man-pages-3.22`
+ `man-pages-ja-20100115`
+ `mcelog-1.0pre3_20101112`
+ `mdadm-3.2.2`
+ `memcached-1.4.6`
+ `mercurial-1.8.4`
+ `mesa-7.10`
+ `microcode_ctl-1.17`
+ `mod_nss-1.0.8`
+ `mod_python-3.2.10`
+ `mod_security-2.5.12`
+ `monit-5.2.5`
+ `munin-1.4.5`
+ `nagios-3.2.3`
+ `nagios-plugins-1.4.15`
+ `neon0.25-0.25.5`
+ `net-snmp-5.5`
+ `net-tools-1.60`
+ `nfs-utils-1.2.3`
+ `nfs-utils-lib-1.1.5`
+ `nginx-0.8.54`
+ `nspr-4.8.7`
+ `nss-3.12.9`
+ `nss-pam-ldapd-0.7.5`
+ `nss-softokn-3.12.9`
+ `nss-util-3.12.9`
+ `ntp-4.2.4p8`
+ `openldap-2.4.23`
+ `openmpi-1.4.3`
+ `openssh-5.3p1`
+ `openssl-1.0.0a`
+ `openswan-2.6.34`
+ `openvpn-2.1.4`
+ `openvpn-auth-ldap-2.0.3`
+ `oprofile-0.9.6`
+ `pam-1.1.1`
+ `pam_krb5-2.3.11`
+ `pam_ldap-185`
+ `pango-1.28.1`
+ `parted-2.1`
+ `passivetex-1.25`
+ `perl-5.10.1`
+ `perl-HTML-Template-2.9`
+ `perl-IO-Multiplex-1.13`
+ `perl-Log-Dispatch-2.27`
+ `perl-Log-Log4perl-1.30`
+ `perl-Mozilla-LDAP-1.5.3`
+ `perl-TermReadKey-2.30`
+ `php-5.3.6`
+ `php-pear-1.9.0`
+ `php-pecl-memcache-3.0.5`
+ `pigz-2.1.6`
+ `pm-utils-1.2.5`
+ `policycoreutils-2.0.83`
+ `postfix-2.6.6`
+ `postgresql-8.4.7`
+ `prelink-0.4.4`
+ `procps-3.2.8`
+ `publican-2.1`
+ `python-boto-2.0`
+ `python-crypto-2.0.1`
+ `python-dmidecode-3.10.12`
+ `python-imaging-1.1.6`
+ `python-krbV-1.0.90`
+ `python-pycurl-7.19.0`
+ `python-urlgrabber-3.9.1`
+ `python24-2.4.6`
+ `python26-2.6.7`
+ `quota-3.17`
+ `re2c-0.13.5`
+ `redhat-lsb-4.0`
+ `rkhunter-1.3.8`
+ `rpm-4.8.0`
+ `rsync-3.0.6`
+ `rsyslog-4.6.2`
+ `ruby-1.8.7.352`
+ `screen-4.0.3`
+ `selinux-policy-3.7.19`
+ `setup-2.8.14`
+ `shadow-utils-4.1.4.2`
+ `splint-3.1.2`
+ `squashfs-tools-4.0`
+ `squid-3.1.10`
+ `subversion-1.6.17`
+ `sudo-1.7.4p5`
+ `swig-2.0.1`
+ `syslinux-4.02`
+ `sysstat-9.0.4`
+ `system-release-2011.09`
+ `systemtap-1.4`
+ `tar-1.23`
+ `tcsh-6.17`
+ `texi2html-1.82`
+ `texlive-2007`
+ `texlive-texmf-2007`
+ `tomcat6-6.0.32`
+ `transfig-3.2.5`
+ `tzdata-2011h`
+ `udev-147`
+ `unifdef-1.334`
+ `upstart-0.6.5`
+ `util-linux-ng-2.17.2`
+ `valgrind-3.6.0`
+ `vim-7.2.411`
+ `vpnc-0.5.3`
+ `vsftpd-2.2.2`
+ `w3m-0.5.2`
+ `watchdog-5.9`
+ `wireshark-1.2.15`
+ `xalan-j2-2.7.0`
+ `xerces-j2-2.7.1`
+ `xhtml1-dtds-1.0`
+ `xinetd-2.3.14`
+ `xmlto-0.0.23`
+ `xorg-x11-server-1.7.7`
+ `xorg-x11-server-utils-7.4`
+ `xorg-x11-utils-7.4`
+ `xorg-x11-xinit-1.0.9`
+ `xterm-253`
+ `ypbind-1.20.4`
+ `yum-3.2.29`
+ `yum-metadata-parser-1.1.2`
+ `yum-utils-1.1.30`
+ `zlib-1.2.3 `

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
