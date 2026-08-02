---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2011.02.html
---

# Amazon Linux 1 (AL1) version 2011.02 (Beta) release notes
<a name="relnotes-2011.02"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2011.02 (Beta) release.

## Major Changes
<a name="major-changes-2011.02"></a>
+ Default compiler upgraded from GCC 4.1 to GCC 4.4
+ The AMI kernel is now based on 2.6.35.11 release
+ HVM AMI released to support `cc1.4xlarge` and `cg1.4xlarge` instance types
+ Default filesystem type for the AMI root filesystem has been changed from `ext3` to `ext4`
+ The Amazon Linux 1 (AL1) is using `upstart` instead of `sysvinit` when booting
+ The default Yum configuration on Amazon Linux 1 (AL1) enables fail-over access to neighboring regions in case the repository in the local region is not accessible

## Upgrading from older Amazon Linux 1 (AL1) version 2010.x releases
<a name="upgrading-2011.02"></a>

For the 2011.x Amazon Linux AMI releases we have changed the layout of the Yum repositories to make it easier to manage updates. Due to this change, upgrading from older Amazon Linux 2010.x releases is handled by an upgrade script provided in the latest version of the system-release-2010.11 package. To get the script, please first upgrade to the latest version of the system-release package:

```
$ sudo yum upgrade system-release
```

This command will upgrade your system-release package (or tell you if you already have the latest version). This should give you access to the upgrade script, which is located in /usr/sbin/distro-upgrade.sh. To upgrade your Amazon Linux AMI to the latest package set, you will need to run this script and reboot your instance afterwards. To run the script, please use:

```
$ sudo /usr/sbin/distro-upgrade.sh
```

This command will attempt to check whether your system can be upgraded and report back to you a list of changes that are about to be performed. Please inspect the list of changes, and if you don't notice any particular problems, run the script again by giving it the `--I-agree` flag, so it can proceed with the system upgrade:

```
$ sudo /usr/sbin/distro-upgrade.sh --I-agree
```

This will upgrade your existing package set to the latest versions and prepare your system to boot into the new kernel, once you issue a reboot command. The 2011.x series of Amazon Linux 1 (AL1) introduce updated versions of system libraries and a new init subsystem. Since the old init and reboot binaries are no longer available after the upgrade, in order to reboot the instance you will need to use the `/sbin/reboot -f` command:

```
$ sudo /sbin/reboot -f
```

## Package Updates
<a name="package-updates-2011.02"></a>

### New packages
<a name="new-packages-2011.02"></a>
+ `GeoIP-1.4.6-3.3.amzn1` - C library for country/city/organization to IP address or hostname mapping
+ `OpenIPMI-2.0.16-12.7.amzn1` - IPMI (Intelligent Platform Management Interface) library and tools
+ `PyYAML-3.09-5.0.amzn1` - YAML parser and emitter for Python
+ `SOAPpy-0.11.6-11.4.amzn1` - Full-featured SOAP library for Python
+ `amtu-1.0.8-8.6.amzn1` - Abstract Machine Test Utility (AMTU)
+ `arpwatch-2.1a15-14.2.amzn1` - Network monitoring tools for tracking IP addresses on a network
+ `aws-scripts-ses-2010.12.01-1.2.amzn1` - AWS ses scripts
+ `batik-1.7-6.3.5.amzn1` - Scalable Vector Graphics for Java
+ `blktrace-1.0.1-3.1.4.amzn1` - Utilities for performing block layer IO tracing in the Linux kernel
+ `cdrkit-1.1.9-11.4.amzn1` - A collection of CD/DVD utilities
+ `cloog-0.15.7-1.2.5.amzn1` - The Chunky Loop Generator
+ `cronie-1.4.4-2.4.amzn1` - Cron daemon for executing programs at set times
+ `cyrus-imapd-2.3.16-6.2.amzn1` - A high-performance mail server with IMAP, POP3, NNTP and SIEVE support
+ `dejavu-fonts-2.30-2.4.amzn1` - DejaVu fonts
+ `deltarpm-3.5-0.5.20090913git.4.amzn1` - Create deltas between rpms
+ `dirmngr-1.0.3-4.2.amzn1` - Client for Managing/Downloading CRLs
+ `docbook-simple-1.1-8.4.amzn1` - Simplified DocBook is a small subset of the DocBook XML DTD
+ `docbook-slides-3.4.0-9.4.amzn1` - DocBook Slides document type and stylesheets
+ `dvipdfm-0.13.2d-41.1.7.amzn1` - A DVI to PDF translator
+ `dvipng-1.11-3.2.4.amzn1` - Converts DVI files to PNG/GIF format
+ `emacs-auctex-11.85-10.2.amzn1` - Enhanced TeX modes for Emacs
+ `fontpackages-1.41-1.1.2.amzn1` - Common directory and macro definitions used by font packages
+ `fop-0.95-4.2.5.amzn1` - XSL-driven print formatter
+ `glpk-4.40-1.1.4.amzn1` - GNU Linear Programming Kit
+ `gnome-doc-utils-0.18.1-1.4.amzn1` - Documentation utilities for GNOME
+ `gprolog-1.3.1-6.4.amzn1` - GNU Prolog is a free Prolog compiler
+ `grubby-7.0.15-2.4.amzn1` - Command line tool for updating bootloader configs
+ `gsl-1.13-4.3.amzn1` - The GNU Scientific Library for numerical analysis
+ `gtk-doc-1.11-5.1.6.amzn1` - API documentation generation tool for GTK\+ and GNOME
+ `hardlink-1.0-10.4.amzn1` - Create a tree of hardlinks
+ `hunspell-1.2.8-16.2.amzn1` - A spell checker and morphological analyzer library
+ `isomd5sum-1.0.6-1.2.amzn1` - Utilities for working with md5sum implanted in ISO images
+ `jasper-1.900.1-15.4.amzn1` - Implementation of the JPEG-2000 standard, Part 1
+ `java-1.5.0-gcj-1.5.0.0-29.1.12.amzn1` - JPackage runtime compatibility layer for GCJ
+ `kbd-1.15-11.4.amzn1` - Tools for configuring the console (keyboard, virtual terminals, etc.)
+ `lapack-3.2.1-4.3.amzn1` - Numerical linear algebra package libraries
+ `libao-0.8.8-7.1.6.amzn1` - Cross Platform Audio Output Library
+ `libdbi-0.8.3-3.1.3.amzn1` - Database Independent Abstraction Layer for C
+ `libdbi-drivers-0.8.3-5.1.3.amzn1` - Database-specific drivers for libdbi
+ `libnetfilter_conntrack-0.0.100-2.2.amzn1` - Netfilter conntrack userspace library
+ `libnfnetlink-1.0.0-1.2.amzn1` - Netfilter netlink userspace library
+ `libnih-1.0.1-6.4.amzn1` - Lightweight application development library
+ `libproxy-0.3.0-1.5.amzn1` - A library handling all the details of proxy configuration
+ `libspiro-20071029-3.1.2.amzn1` - Library to simplify the drawing of beautiful curves
+ `libtasn1-2.3-3.amzn1` - The ASN.1 library used in GNUTLS
+ `libuninameslist-20080409-3.1.2.amzn1` - A library providing Unicode character names and annotations
+ `libyaml-0.1.3-1.0.amzn1` - YAML 1.1 parser and emitter written in C
+ `lslk-1.29-23.3.amzn1` - A lock file lister
+ `lzo-2.03-3.1.2.amzn1` - Data compression library with very fast (de)compression
+ `m17n-contrib-1.1.10-3.4.amzn1` - Contributed multilingualization datafiles for m17n-lib
+ `m17n-lib-1.5.5-2.6.amzn1` - Multilingual text library
+ `mod_auth_pgsql-2.0.3-10.1.5.amzn1` - Basic authentication for the Apache HTTP Server using a PostgreSQL database
+ `mod_proxy_html-3.1.2-7.0.amzn1` - Output filter to rewrite HTML links in a proxy situation
+ `mod_python-3.2.10-1.7.amzn1` - An embedded Python interpreter for the Apache Web server.
+ `mrtg-2.16.2-5.3.amzn1` - Multi Router Traffic Grapher
+ `mysql-connector-odbc-5.1.5r1144-7.5.amzn1` - ODBC driver for MySQL
+ `nash-6.0.93-2.11.amzn1` - nash is not another shell
+ `nss_compat_ossl-0.9.6-1.4.amzn1` - Source-level compatibility library for OpenSSL to NSS porting
+ `oniguruma-5.9.1-3.1.2.amzn1` - Regular expressions library
+ `openjpeg-1.3-7.4.amzn1` - OpenJPEG command line tools
+ `opensm-3.3.5-1.5.amzn1` - OpenIB InfiniBand Subnet Manager and management utilities
+ `openvpn-2.1.1-2.0.amzn1` - A full-featured SSL VPN solution
+ `openvpn-auth-ldap-2.0.3-3.0.amzn1` - OpenVPN plugin for LDAP authentication
+ `perl-Font-AFM-1.20-3.1.4.amzn1` - Perl interface to Adobe Font Metrics files
+ `perl-HTML-Format-2.04-11.1.4.amzn1` - HTML formatter modules
+ `perl-Makefile-DOM-0.004-1.1.4.amzn1` - Simple DOM parser for Makefiles
+ `perl-Makefile-Parser-0.211-1.1.5.amzn1` - Simple parser for Makefiles
+ `perl-XML-Filter-BufferText-1.01-8.4.amzn1` - Filter to put all characters() in one event
+ `perl-XML-LibXSLT-1.70-1.1.4.amzn1` - Interface to the gnome libxslt library
+ `perl-XML-SAX-Writer-0.50-8.4.amzn1` - SAX2 Writer
+ `perl-XML-Twig-3.34-1.2.amzn1` - A perl module for processing huge XML documents in tree mode
+ `pexpect-2.3-6.3.amzn1` - Pure Python Expect-like module
+ `php-pecl-apc-3.1.3p1-1.2.4.amzn1` - APC caches and optimizes PHP intermediate code
+ `php-pecl-memcache-3.0.4-3.2.4.amzn1` - Extension to work with the Memcached caching daemon
+ `pkcs11-helper-1.07-5.2.amzn1` - A library for using PKCS\#11 providers
+ `pl-5.7.11-6.4.amzn1` - SWI-Prolog - Edinburgh compatible Prolog compiler
+ `poppler-data-0.4.0-1.4.amzn1` - Encoding files
+ `ppl-0.10.2-11.5.amzn1` - The Parma Polyhedra Library: a library of numerical abstractions
+ `pptp-1.7.2-8.1.1.amzn1` - Point-to-Point Tunneling Protocol (PPTP) Client
+ `publican-1.6-1.6.amzn1` - Common files and scripts for publishing with DocBook XML
+ `pycairo-1.8.6-2.1.5.amzn1` - Python bindings for the cairo library
+ `python-decorator-3.0.1-3.1.4.amzn1` - Module to simplify usage of decorators
+ `python-fpconst-0.7.3-6.1.4.amzn1` - Python module for handling IEEE 754 floating point special values
+ `python-memcached-1.43-5.3.4.amzn1` - A Python memcached client library
+ `python-nose-0.10.4-3.1.4.amzn1` - A discovery-based unittest extension for Python
+ `python-paste-1.7.4-1.4.amzn1` - Tools for using a Web Server Gateway Interface stack
+ `python-twisted-8.2.0-3.1.2.amzn1` - Event-based framework for internet applications
+ `python-twisted-conch-8.2.0-3.2.3.amzn1` - SSH and SFTP protocol implementation together with clients and servers
+ `python-twisted-core-8.2.0-4.2.amzn1` - Asynchronous networking framework written in Python
+ `python-twisted-lore-8.2.0-3.2.2.amzn1` - Documentation generator with HTML and LaTeX support
+ `python-twisted-mail-8.2.0-3.2.2.amzn1` - SMTP, IMAP and POP protocol implementation together with clients and servers
+ `python-twisted-names-8.2.0-3.2.2.amzn1` - Twisted DNS implementation
+ `python-twisted-news-8.2.0-3.2.2.amzn1` - NNTP protocol implementation with client and server
+ `python-twisted-runner-8.2.0-3.2.2.amzn1` - Twisted Runner process management library and inetd replacement
+ `python-twisted-web-8.2.0-3.2.2.amzn1` - Twisted web client and server, programmable in Python
+ `python-twisted-words-8.2.0-3.2.2.amzn1` - Twisted Instant Messaging implementations
+ `python-zope-filesystem-1-5.2.amzn1` - Python-Zope Libraries Base Filesystem
+ `python-zope-interface-3.5.2-2.1.4.amzn1` - Zope 3 Interface Infrastructure
+ `rarian-0.8.1-5.1.5.amzn1` - Documentation meta-data library
+ `rdma-1.0-9.4.amzn1` - Infiniband/iWARP Kernel Module Initializer
+ `re2c-0.12.1-2.0.amzn1` - Tool for generating C-based recognizers from regular expressions
+ `rkhunter-1.3.8-3.0.amzn1` - A host-based tool to scan for rootkits, backdoors and local exploits
+ `rpmlint-0.94-2.5.amzn1` - Tool for checking common errors in RPM packages
+ `ruby-mysql-2.8.2-1.3.amzn1` - A Ruby interface to MySQL
+ `sinjdoc-0.5-9.1.6.amzn1` - Documentation generator for Java source code
+ `squashfs-tools-4.0-3.3.amzn1` - Utility for the creation of squashfs filesystems
+ `star-1.5-9.3.amzn1` - An archiving tool with ACL support
+ `teckit-2.5.1-4.1.4.amzn1` - Conversion library and mapping compiler
+ `texlive-2007-56.7.amzn1` - Binaries for the TeX formatting system
+ `texlive-texmf-2007-35.4.amzn1` - Architecture independent parts of the TeX formatting system
+ `texlive-texmf-errata-2007-7.1.4.amzn1` - Errata for texlive-texmf
+ `tokyocabinet-1.4.33-6.4.amzn1` - A modern implementation of a DBM
+ `upstart-0.6.5-6.1.5.amzn1` - An event-driven init system
+ `urlview-0.9-7.4.amzn1` - URL extractor/launcher
+ `vlock-1.3-31.3.amzn1` - A program which locks one or more virtual consoles
+ `vorbis-tools-1.2.0-7.6.amzn1` - The Vorbis General Audio Compression Codec tools
+ `vpnc-0.5.3-8.0.amzn1` - IPSec VPN client compatible with Cisco equipment
+ `xdelta-1.1.4-8.3.amzn1` - A binary file delta generator and an RCS replacement library
+ `xferstats-2.16-21.3.amzn1` - Compiles information about file transfers from logfiles
+ `xmlgraphics-commons-1.3.1-1.1.4.amzn1` - XML Graphics Commons
+ `yap-5.1.3-2.1.4.amzn1` - High-performance Prolog Compiler

### Compatibility Packages
<a name="compatibility-packages-2011.02"></a>
+ `automake14` and `automake16` - A GNU tool for automatically creating Makefiles
+ `compat-audit` - User space tools for 2.6 kernel auditing
+ `compat-expat` - A library for parsing XML.
+ `compat-readline` - A library for editing typed command lines.
+ `gcc41` - Version 4.1 of the GNU Compiler suite (GCC)

### Removed Packages
<a name="removed-packages-2011.02"></a>

These packages have been deprecated by similar functionality offered by other packages and as a result are no longer supported/maintained in this beta release of Amazon Linux 1 (AL1):
+ `cairo-java`
+ `glib`
+ `glib-java`
+ `pdksh`
+ `wireless-tools`
+ `exim`

### Obsoleted Packages
<a name="obsoleted-packages-2011.02"></a>
+ `java-1.4.2-gcj-compat` is obsoleted by `java-1.5.0-gcj`
+ `sysklogd` is obsoleted by `rsyslog`
+ `anacron` and `vixie-cron` are obsoleted by `cronie`
+ `portmap` is obsoleted by `rpcbind`
+ `dhcpv6` and `libdhcp` are obsoleted by the updated `dhcp` package
+ `sysvinit` replaced by `upstart`

### Updated Packages
<a name="updated-packages-2011.02"></a>

Due to the GCC upgrade, most packages have been recompiled with the newer compiler. In addition, the following package changes have been updated to newer versions in the process:
+ `ImageMagick-6.5.4.7`
+ `MAKEDEV-3.24`
+ `MySQL-python-1.2.3`
+ `PyXML-0.8.4`
+ `Xaw3d-1.5E`
+ `a2ps-4.14`
+ `acl-2.2.49`
+ `acpid-1.0.10`
+ `adaptx-0.9.13`
+ `aide-0.14`
+ `alsa-lib-1.0.21`
+ `alsa-utils-1.0.21`
+ `amanda-2.6.1p2`
+ `ant-1.7.1`
+ `ant-contrib-1.0`
+ `antlr-2.7.7`
+ `apache-tomcat-apis-0.1`
+ `apr-1.3.9`
+ `apr-util-1.3.9`
+ `arptables_jf-0.0.8`
+ `asciidoc-8.4.5`
+ `aspell-0.60.6`
+ `at-3.1.10`
+ `attr-2.4.44`
+ `audit-2.0.4`
+ `authconfig-6.1.4`
+ `autoconf-2.63`
+ `autofs-5.0.5`
+ `automake-1.11.1`
+ `automake14-1.4p6`
+ `avahi-0.6.16`
+ `avalon-framework-4.1.4`
+ `avalon-logkit-1.2`
+ `aws-apitools-as-1.0.33.1`
+ `aws-apitools-common-1.0.0`
+ `aws-apitools-ec2-1.3.62308`
+ `aws-apitools-elb-1.0.10.0`
+ `aws-apitools-iam-1.2.0`
+ `aws-apitools-mon-1.0.9.5`
+ `aws-apitools-rds-1.3.003`
+ `axis-1.2.1`
+ `babel-0.9.4`
+ `basesystem-10.0`
+ `bash-4.1.2`
+ `bc-1.06.95`
+ `bcel-5.2`
+ `bea-stax-1.2.0`
+ `bind-9.7.0`
+ `binutils-2.20.51.0.2`
+ `bison-2.4.1`
+ `boost-1.41.0`
+ `bridge-utils-1.2`
+ `bsf-2.4.0`
+ `bsh-1.3.0`
+ `byacc-1.9.20070509`
+ `bzip2-1.0.6`
+ `bzr-2.1.2`
+ `ca-certificates-2010.63`
+ `cacti-0.8.7g`
+ `cairo-1.8.8`
+ `castor-0.9.5`
+ `celt051-0.5.1.3`
+ `check-0.9.8`
+ `checkpolicy-2.0.22`
+ `chkconfig-1.3.47`
+ `chrpath-0.13`
+ `classpathx-jaf-1.0`
+ `classpathx-mail-1.1.2`
+ `cloud-init-0.5.15`
+ `cmake-2.6.4`
+ `compat-libcap1-1.10`
+ `conman-0.2.5`
+ `coreutils-8.4`
+ `corosync-1.2.3`
+ `cpio-2.6`
+ `cpuspeed-1.5`
+ `cracklib-2.8.16`
+ `crash-5.1.2`
+ `createrepo-0.9.8`
+ `crontabs-1.10`
+ `crypto-utils-2.4.1`
+ `cryptsetup-luks-1.1.2`
+ `cscope-15.6`
+ `ctags-5.8`
+ `cups-1.4.2`
+ `curl-7.19.7`
+ `cvs-1.11.23`
+ `cvsps-2.2`
+ `cyrus-sasl-2.1.23`
+ `db4-4.7.25`
+ `dbus-1.2.24`
+ `dbus-glib-0.86`
+ `dbus-python-0.83.0`
+ `dejagnu-1.4.4`
+ `dev86-0.16.17`
+ `device-mapper-multipath-0.4.9`
+ `dhcp-4.1.1`
+ `dialog-1.1`
+ `diffstat-1.51`
+ `diffutils-2.8.1`
+ `dmidecode-2.10`
+ `dmraid-1.0.0.rc16`
+ `dnsmasq-2.48`
+ `docbook-dtds-1.0`
+ `docbook-style-dsssl-1.79`
+ `docbook-style-xsl-1.75.2`
+ `docbook-utils-0.6.14`
+ `dos2unix-3.1`
+ `dosfstools-3.0.9`
+ `dovecot-2.0`
+ `doxygen-1.6.1`
+ `dstat-0.7.0`
+ `dump-0.4`
+ `e2fsprogs-1.41.12`
+ `ecj-3.4.2`
+ `ecryptfs-utils-82`
+ `ed-1.1`
+ `edac-utils-0.9`
+ `efax-0.9a`
+ `elfutils-0.148`
+ `elinks-0.12`
+ `emacs-23.1`
+ `enscript-1.6.4`
+ `ethtool-6`
+ `expat-2.0.1`
+ `expect-5.44.1.15`
+ `fakechroot-2.9`
+ `fakeroot-1.12.2`
+ `fetchmail-6.3.17`
+ `file-5.05`
+ `filesystem-2.4.30`
+ `findutils-4.4.2`
+ `finger-0.17`
+ `fipscheck-1.2.0`
+ `flac-1.2.1`
+ `flex-2.5.35`
+ `fontconfig-2.8.0`
+ `freeglut-2.6.0`
+ `freeradius-2.1.9`
+ `freetds-0.82`
+ `freetype-2.3.11`
+ `ftp-0.17`
+ `fuse-2.8.3`
+ `gamin-0.1.10`
+ `gawk-3.1.7`
+ `gc-7.1`
+ `gcc-4.4.4`
+ `gd-2.0.35`
+ `gdb-7.1`
+ `gdbm-1.8.0`
+ `geronimo-specs-1.0`
+ `gettext-0.17`
+ `ghostscript-8.70`
+ `ghostscript-fonts-5.50`
+ `giflib-4.1.6`
+ `git-1.7.2.5`
+ `glib2-2.22.5`
+ `glibc-2.12`
+ `gmp-4.3.1`
+ `gnu-efi-3.0g`
+ `gnupg2-2.0.14`
+ `gnuplot-4.2.6`
+ `gnutls-2.8.5`
+ `gperf-3.0.3`
+ `gpgme-1.1.8`
+ `gpm-1.20.6`
+ `graphviz-2.26.0`
+ `grep-2.6.3`
+ `groff-1.18.1.4`
+ `grub-0.97`
+ `guile-1.8.7`
+ `gzip-1.3.12`
+ `hal-0.5.14`
+ `hdparm-9.16`
+ `help2man-1.36.4`
+ `hesiod-3.1.0`
+ `hmaccalc-0.9.12`
+ `hsqldb-1.8.0.10`
+ `ht2html-2.0`
+ `htdig-3.2.0`
+ `html2ps-1.0`
+ `httpd-2.2.16`
+ `hwdata-0.233`
+ `iasl-20090123`
+ `icu-4.2.1`
+ `imake-1.0.2`
+ `indent-2.2.10`
+ `initscripts-9.03.17`
+ `intltool-0.41.0`
+ `iproute-2.6.32`
+ `iptables-1.4.7`
+ `iptraf-3.0.1`
+ `iptstate-2.2.2`
+ `iputils-20071127`
+ `irqbalance-0.55`
+ `iso-codes-3.16`
+ `jadetex-3.13`
+ `jakarta-commons-beanutils-1.8.3`
+ `jakarta-commons-codec-1.4`
+ `jakarta-commons-daemon-1.0.4`
+ `jakarta-commons-discovery-0.4`
+ `jakarta-commons-el-1.0`
+ `jakarta-commons-io-1.4`
+ `jakarta-commons-lang-2.4`
+ `jakarta-commons-logging-1.0.4`
+ `jakarta-commons-net-2.0`
+ `jakarta-commons-pool-1.5.5`
+ `jakarta-oro-2.0.8`
+ `jakarta-taglibs-standard-1.1.1`
+ `java-1.6.0-openjdk-1.6.0.0`
+ `java_cup-0.10k`
+ `javacc-4.1`
+ `jdepend-2.9`
+ `jdom-1.1.1`
+ `jlex-1.2.6`
+ `jline-0.9.94`
+ `jpackage-utils-1.7.5`
+ `jrefactory-2.8.9`
+ `jsch-0.1.41`
+ `jss-4.2.6`
+ `jtidy-1.0`
+ `junit-3.8.2`
+ `jwhois-4.0`
+ `jython-2.2.1`
+ `jzlib-1.0.7`
+ `kernel-2.6.35.11`
+ `keyutils-1.4`
+ `krb5-1.8.2`
+ `ksh-20100621`
+ `latex2html-2008`
+ `lcms-1.19`
+ `ldapjdk-4.18`
+ `less-436`
+ `lftp-4.0.9`
+ `libICE-1.0.6`
+ `libIDL-0.8.13`
+ `libSM-1.1.0`
+ `libX11-1.3`
+ `libXau-1.0.5`
+ `libXaw-1.0.6`
+ `libXcomposite-0.4.1`
+ `libXcursor-1.1.10`
+ `libXdamage-1.1.2`
+ `libXdmcp-1.0.3`
+ `libXevie-1.0.2`
+ `libXext-1.1`
+ `libXfixes-4.0.4`
+ `libXfont-1.4.1`
+ `libXft-2.1.13`
+ `libXi-1.3`
+ `libXinerama-1.1`
+ `libXmu-1.0.5`
+ `libXp-1.0.0`
+ `libXpm-3.5.8`
+ `libXrandr-1.3.0`
+ `libXrender-0.9.5`
+ `libXres-1.0.4`
+ `libXt-1.0.7`
+ `libXtst-1.0.99.2`
+ `libXv-1.0.5`
+ `libXvMC-1.0.4`
+ `libXxf86dga-1.1.1`
+ `libXxf86misc-1.0.2`
+ `libXxf86vm-1.1.0`
+ `libaio-0.3.107`
+ `libart_lgpl-2.3.20`
+ `libassuan-1.0.5`
+ `libatomic_ops-1.2`
+ `libc-client-2007e`
+ `libcap-2.16`
+ `libcap-ng-0.6.4`
+ `libdaemon-0.14`
+ `libdmx-1.1.0`
+ `libdrm-2.4.20`
+ `libdv-1.0.0`
+ `libedit-2.11`
+ `libevent-1.4.13`
+ `libexif-0.6.16`
+ `libfontenc-1.0.5`
+ `libgcrypt-1.4.5`
+ `libgpg-error-1.7`
+ `libgssglue-0.1`
+ `libhbaapi-2.2`
+ `libhbalinux-1.0.10`
+ `libhugetlbfs-2.8`
+ `libibcm-1.0.5`
+ `libibcommon-1.2.0`
+ `libibmad-1.3.4`
+ `libibumad-1.3.4`
+ `libibverbs-1.1.4`
+ `libidn-1.18`
+ `libieee1284-0.2.11`
+ `libjpeg-6b`
+ `libksba-1.0.5`
+ `libmthca-1.0.5`
+ `libnl-1.1`
+ `libogg-1.1.4`
+ `libpcap-1.0.0`
+ `libpciaccess-0.10.9`
+ `libpng-1.2.44`
+ `librdmacm-1.0.10`
+ `libreadline-java-0.8.0`
+ `libselinux-2.0.98`
+ `libsemanage-2.0.43`
+ `libsepol-2.0.41`
+ `libsmi-0.4.8`
+ `libsoup-2.28.2`
+ `libssh2-1.2.2`
+ `libthai-0.1.12`
+ `libtiff-3.9.4`
+ `libtirpc-0.2.1`
+ `libtool-2.2.10`
+ `libuser-0.56.13`
+ `libutempter-1.1.5`
+ `libvorbis-1.2.3`
+ `libwmf-0.2.8.4`
+ `libwvstreams-4.6`
+ `libxcb-1.6`
+ `libxkbfile-1.0.6`
+ `libxklavier-4.0`
+ `libxml2-2.7.6`
+ `libxslt-1.1.26`
+ `lighttpd-1.4.28`
+ `linuxdoc-tools-0.9.65`
+ `lksctp-tools-1.0.10`
+ `lockdev-1.0.1`
+ `log4cpp-1.0`
+ `log4j-1.2.16`
+ `logrotate-3.7.8`
+ `logwatch-7.3.6`
+ `lsof-4.82`
+ `lsscsi-0.23`
+ `ltrace-0.5`
+ `lua-5.1.4`
+ `lucene-2.3.1`
+ `lvm2-2.02.66`
+ `lynx-2.8.6`
+ `m17n-db-1.5.5`
+ `m2crypto-0.20.2`
+ `m4-1.4.13`
+ `mailcap-2.1.31`
+ `mailman-2.1.12`
+ `mailx-12.4`
+ `make-3.81`
+ `man-1.6f`
+ `man-pages-3.22`
+ `man-pages-fr-3.23`
+ `man-pages-ja-20100115`
+ `mc-4.7.0.2`
+ `mcelog-1.0pre3`
+ `mcpp-2.7.2`
+ `mcstrans-0.3.1`
+ `mdadm-3.1.3`
+ `meanwhile-1.1.0`
+ `memcached-1.4.4`
+ `mercurial-1.7.3`
+ `mesa-7.7`
+ `mgetty-1.1.36`
+ `microcode_ctl-1.17`
+ `mingetty-1.08`
+ `mkbootdisk-1.5.5`
+ `mlocate-0.22.2`
+ `mod_auth_kerb-5.4`
+ `mod_auth_mysql-3.0.0`
+ `mod_authz_ldap-0.26`
+ `mod_nss-1.0.8`
+ `mod_perl-2.0.4`
+ `mod_security-2.5.12`
+ `mod_wsgi-3.2`
+ `module-init-tools-3.9`
+ `monit-5.1.1`
+ `mozldap-6.0.5`
+ `mpfr-2.4.1`
+ `mpich2-1.2.1`
+ `mtools-4.0.12`
+ `mtr-0.75`
+ `munin-1.4.5`
+ `mutt-1.5.20`
+ `mx4j-3.0.1`
+ `mysql-5.1.52`
+ `mysql-connector-java-5.1.12`
+ `nagios-3.2.2`
+ `nagios-plugins-1.4.15`
+ `nano-2.0.9`
+ `nasm-2.07`
+ `nc-1.84`
+ `ncompress-4.2.4`
+ `ncurses-5.7`
+ `neon-0.29.5`
+ `neon0.25-0.25.5`
+ `net-snmp-5.5`
+ `net-tools-1.60`
+ `netpbm-10.47.05`
+ `newt-0.52.11`
+ `nfs-utils-1.2.2`
+ `nfs-utils-lib-1.1.5`
+ `nfs4-acl-tools-0.3.3`
+ `nginx-0.8.53`
+ `nmap-5.21`
+ `nrpe-2.12`
+ `nspr-4.8.6`
+ `nss-3.12.8`
+ `nss-pam-ldapd-0.7.5`
+ `nss-softokn-3.12.8`
+ `nss-util-3.12.8`
+ `nss_db-2.2.3`
+ `ntp-4.2.4p8`
+ `numactl-2.0.3`
+ `openais-1.1.1`
+ `openjade-1.3.2`
+ `openldap-2.4.19`
+ `openmotif-2.3.3`
+ `openmpi-1.4.1`
+ `opensp-1.5.2`
+ `openssh-5.3p1`
+ `openssl-1.0.0a`
+ `openssl097a-0.9.7a`
+ `openssl098e-0.9.8e`
+ `openswan-2.6.32`
+ `oprofile-0.9.6`
+ `pam-1.1.1`
+ `pam_krb5-2.3.11`
+ `pam_ldap-185`
+ `pam_passwdqc-1.0.5`
+ `pango-1.28.1`
+ `paps-0.6.8`
+ `parted-2.1`
+ `passwd-0.77`
+ `patch-2.6`
+ `patchutils-0.3.1`
+ `pax-3.4`
+ `pciutils-3.1.4`
+ `pcre-7.8`
+ `pcsc-lite-1.5.2`
+ `perl-5.10.1`
+ `perl-Algorithm-Diff-1.1902`
+ `perl-AppConfig-1.66`
+ `perl-Archive-Any-0.0932`
+ `perl-Archive-Zip-1.30`
+ `perl-Array-Diff-0.05002`
+ `perl-Authen-SASL-2.13`
+ `perl-B-Keywords-1.09`
+ `perl-BSD-Resource-1.29.03`
+ `perl-Bit-Vector-7.1`
+ `perl-Business-ISBN-2.05`
+ `perl-Business-ISBN-Data-20081208`
+ `perl-CPAN-DistnameInfo-0.09`
+ `perl-CSS-Tiny-1.15`
+ `perl-Cache-Memcached-1.28`
+ `perl-Carp-Clan-6.03`
+ `perl-Class-Accessor-0.31`
+ `perl-Class-C3-0.22`
+ `perl-Class-C3-XS-0.13`
+ `perl-Class-Data-Inheritable-0.08`
+ `perl-Class-Inspector-1.24`
+ `perl-Class-Singleton-1.4`
+ `perl-Class-Trigger-0.13`
+ `perl-Clone-0.31`
+ `perl-Config-General-2.44`
+ `perl-Config-Simple-4.59`
+ `perl-Config-Tiny-2.12`
+ `perl-Convert-ASN1-0.22`
+ `perl-Convert-BinHex-1.119`
+ `perl-Crypt-OpenSSL-Bignum-0.04`
+ `perl-Crypt-OpenSSL-RSA-0.25`
+ `perl-Crypt-OpenSSL-Random-0.04`
+ `perl-Crypt-PasswdMD5-1.3`
+ `perl-Crypt-SSLeay-0.57`
+ `perl-DBD-CSV-0.22`
+ `perl-DBD-MySQL-4.013`
+ `perl-DBD-SQLite-1.27`
+ `perl-DBD-XBase-0.241`
+ `perl-DBI-1.609`
+ `perl-DBIx-Simple-1.32`
+ `perl-Data-OptList-0.104`
+ `perl-Data-Section-0.101620`
+ `perl-Date-Calc-6.3`
+ `perl-Date-Manip-5.54`
+ `perl-DateTime-0.5300`
+ `perl-DateTime-Format-DateParse-0.04`
+ `perl-DateTime-Format-Mail-0.3001`
+ `perl-DateTime-Format-W3CDTF-0.04`
+ `perl-Devel-Cover-0.65`
+ `perl-Devel-Cycle-1.10`
+ `perl-Devel-Leak-0.03`
+ `perl-Devel-StackTrace-1.22`
+ `perl-Devel-Symdump-2.08`
+ `perl-Digest-BubbleBabble-0.01`
+ `perl-Digest-HMAC-1.01`
+ `perl-Digest-SHA1-2.12`
+ `perl-Email-Date-Format-1.002`
+ `perl-Encode-Detect-1.01`
+ `perl-Error-0.17015`
+ `perl-Exception-Class-1.29`
+ `perl-ExtUtils-MakeMaker-Coverage-0.05`
+ `perl-File-Copy-Recursive-0.38`
+ `perl-File-Find-Rule-0.30`
+ `perl-File-Find-Rule-Perl-1.09`
+ `perl-File-HomeDir-0.86`
+ `perl-File-MMagic-1.27`
+ `perl-File-Remove-1.42`
+ `perl-File-Slurp-9999.13`
+ `perl-File-Which-1.09`
+ `perl-File-pushd-1.00`
+ `perl-Font-TTF-0.45`
+ `perl-FreezeThaw-0.45`
+ `perl-Frontier-RPC-0.07b4p1`
+ `perl-GSSAPI-0.26`
+ `perl-HTML-Lint-2.06`
+ `perl-HTML-Parser-3.64`
+ `perl-HTML-Tagset-3.20`
+ `perl-HTML-Template-2.9`
+ `perl-HTML-Tree-3.23`
+ `perl-Hook-LexWrap-0.22`
+ `perl-IO-Capture-0.05`
+ `perl-IO-Multiplex-1.10`
+ `perl-IO-Socket-INET6-2.56`
+ `perl-IO-Socket-SSL-1.31`
+ `perl-IO-String-1.08`
+ `perl-IO-stringy-2.110`
+ `perl-IPC-ShareLite-0.13`
+ `perl-IPC-SharedCache-1.3`
+ `perl-Image-Base-1.07`
+ `perl-Image-Info-1.28`
+ `perl-Image-Size-3.2`
+ `perl-Image-Xbm-1.08`
+ `perl-Image-Xpm-1.09`
+ `perl-JSON-2.15`
+ `perl-LDAP-0.40`
+ `perl-List-MoreUtils-0.22`
+ `perl-Locale-Maketext-Gettext-1.27`
+ `perl-Locale-PO-0.21`
+ `perl-Log-Dispatch-2.22`
+ `perl-Log-Dispatch-FileRotate-1.19`
+ `perl-Log-Log4perl-1.24`
+ `perl-MIME-Lite-3.027`
+ `perl-MIME-Types-1.28`
+ `perl-MIME-tools-5.427`
+ `perl-MRO-Compat-0.11`
+ `perl-Mail-DKIM-0.37`
+ `perl-Mail-Sender-0.8.16`
+ `perl-Mail-Sendmail-0.79`
+ `perl-MailTools-2.04`
+ `perl-Module-CPANTS-Analyse-0.85`
+ `perl-Module-ExtractUse-0.23`
+ `perl-Module-Find-0.08`
+ `perl-Module-Info-0.31`
+ `perl-Module-Install-0.91`
+ `perl-Module-ScanDeps-0.95`
+ `perl-Net-DNS-0.65`
+ `perl-Net-IP-1.25`
+ `perl-Net-Jabber-2.0`
+ `perl-Net-SMTP-SSL-1.01`
+ `perl-Net-SNMP-5.2.0`
+ `perl-Net-SSLeay-1.35`
+ `perl-Net-Server-0.97`
+ `perl-Net-Telnet-3.03`
+ `perl-Net-XMPP-1.02`
+ `perl-NetAddr-IP-4.027`
+ `perl-Newt-1.08`
+ `perl-Number-Compare-0.01`
+ `perl-Object-Deadly-0.09`
+ `perl-PAR-Dist-0.46`
+ `perl-PDF-Reuse-0.35`
+ `perl-PPI-1.206`
+ `perl-PPI-HTML-1.07`
+ `perl-Package-Generator-0.103`
+ `perl-PadWalker-1.9`
+ `perl-Params-Util-1.00`
+ `perl-Params-Validate-0.92`
+ `perl-Parse-RecDescent-1.962.2`
+ `perl-Parse-Yapp-1.05`
+ `perl-Perl-Critic-1.105`
+ `perl-Perl-MinimumVersion-1.20`
+ `perl-Perlilog-0.3`
+ `perl-Pod-Coverage-0.20`
+ `perl-Pod-POM-0.25`
+ `perl-Pod-Spell-1.01`
+ `perl-Pod-Strip-1.02`
+ `perl-Probe-Perl-0.01`
+ `perl-RRD-Simple-1.44`
+ `perl-Readonly-1.03`
+ `perl-Readonly-XS-1.05`
+ `perl-SGMLSpm-1.03ii`
+ `perl-SNMP_Session-1.12`
+ `perl-SOAP-Lite-0.710.10`
+ `perl-SQL-Statement-1.27`
+ `perl-Socket6-0.23`
+ `perl-Software-License-0.101410`
+ `perl-Spiffy-0.30`
+ `perl-String-CRC32-1.4`
+ `perl-String-Format-1.15`
+ `perl-Sub-Exporter-0.982`
+ `perl-Sub-Install-0.925`
+ `perl-Sub-Name-0.04`
+ `perl-Sub-Uplevel-0.2002`
+ `perl-Syntax-Highlight-Engine-Kate-0.04`
+ `perl-Taint-Runtime-0.03`
+ `perl-Task-Weaken-1.02`
+ `perl-TeX-Hyphen-0.140`
+ `perl-Template-Toolkit-2.22`
+ `perl-TermReadKey-2.30`
+ `perl-Test-Base-0.58`
+ `perl-Test-CPAN-Meta-0.13`
+ `perl-Test-ClassAPI-1.06`
+ `perl-Test-Deep-0.106`
+ `perl-Test-Differences-0.4801`
+ `perl-Test-Exception-0.27`
+ `perl-Test-Kwalitee-1.01`
+ `perl-Test-Manifest-1.22`
+ `perl-Test-MinimumVersion-0.011`
+ `perl-Test-NoWarnings-0.084`
+ `perl-Test-Object-0.07`
+ `perl-Test-Output-0.12`
+ `perl-Test-Perl-Critic-1.02`
+ `perl-Test-Pod-1.40`
+ `perl-Test-Pod-Coverage-1.08`
+ `perl-Test-Prereq-1.037`
+ `perl-Test-Script-1.06`
+ `perl-Test-Spelling-0.11`
+ `perl-Test-SubCalls-1.09`
+ `perl-Test-Taint-1.04`
+ `perl-Test-Tester-0.107`
+ `perl-Test-Warn-0.21`
+ `perl-Test-YAML-Meta-0.16`
+ `perl-Test-YAML-Valid-0.04`
+ `perl-Text-Autoformat-1.14.0`
+ `perl-Text-CSV_XS-0.72`
+ `perl-Text-Diff-1.37`
+ `perl-Text-Glob-0.08`
+ `perl-Text-Iconv-1.7`
+ `perl-Text-PDF-0.29a`
+ `perl-Text-Reform-1.12.2`
+ `perl-Text-Template-1.45`
+ `perl-Text-Unidecode-0.04`
+ `perl-Tie-IxHash-1.21`
+ `perl-Time-modules-2006.0814`
+ `perl-TimeDate-1.16`
+ `perl-Tree-DAG_Node-1.06`
+ `perl-UNIVERSAL-can-1.15`
+ `perl-UNIVERSAL-isa-1.03`
+ `perl-UNIVERSAL-require-0.13`
+ `perl-URI-1.40`
+ `perl-Unicode-Map8-0.12`
+ `perl-Unicode-String-2.09`
+ `perl-WWW-Curl-4.09`
+ `perl-XML-DOM-1.44`
+ `perl-XML-DOM-XPath-0.14`
+ `perl-XML-Dumper-0.81`
+ `perl-XML-Grove-0.46alpha`
+ `perl-XML-LibXML-1.70`
+ `perl-XML-NamespaceSupport-1.10`
+ `perl-XML-Parser-2.36`
+ `perl-XML-RSS-1.45`
+ `perl-XML-RegExp-0.03`
+ `perl-XML-SAX-0.96`
+ `perl-XML-Simple-2.18`
+ `perl-XML-Stream-1.22`
+ `perl-XML-TokeParser-0.05`
+ `perl-XML-TreeBuilder-3.09`
+ `perl-XML-Writer-0.606`
+ `perl-XML-XPath-1.13`
+ `perl-XML-XPathEngine-0.12`
+ `perl-YAML-0.70`
+ `perl-YAML-LibYAML-0.33`
+ `perl-YAML-Syck-1.07`
+ `perl-YAML-Tiny-1.40`
+ `perl-libintl-1.20`
+ `perl-libwww-perl-5.833`
+ `perl-libxml-perl-0.08`
+ `perl-prefork-1.04`
+ `perltidy-20090616`
+ `php-5.3.5`
+ `php-pear-1.9.0`
+ `pigz-2.1.6`
+ `pinentry-0.7.6`
+ `pinfo-0.6.9`
+ `pixman-0.18.4`
+ `pkgconfig-0.23`
+ `plpa-1.3.2`
+ `pm-utils-1.2.5`
+ `policycoreutils-2.0.82`
+ `poppler-0.12.4`
+ `popt-1.13`
+ `portreserve-0.0.4`
+ `postfix-2.6.6`
+ `postgresql-8.4.7`
+ `postgresql-jdbc-8.4.701`
+ `postgresql-odbc-08.04.0200`
+ `ppp-2.4.5`
+ `prelink-0.4.3`
+ `procmail-3.22`
+ `procps-3.2.8`
+ `psacct-6.3.2`
+ `psmisc-22.6`
+ `psutils-1.17`
+ `pth-2.0.7`
+ `pyOpenSSL-0.10`
+ `pygobject2-2.20.0`
+ `pygpgme-0.1`
+ `pyparted-3.4`
+ `python-boto-1.9b`
+ `python-cheetah-2.4.1`
+ `python-configobj-4.6.0`
+ `python-dateutil-1.4.1`
+ `python-decoratortools-1.7`
+ `python-dmidecode-3.10.12`
+ `python-docutils-0.6`
+ `python-epdb-0.11`
+ `python-imaging-1.1.6`
+ `python-iniparse-0.3.1`
+ `python-jinja2-2.2.1`
+ `python-krbV-1.0.13`
+ `python-ldap-2.3.10`
+ `python-markdown-2.0.1`
+ `python-paramiko-1.7.5`
+ `python-pycurl-7.19.0`
+ `python-pygments-1.1.1`
+ `python-setuptools-0.6.10`
+ `python-sphinx-0.6.6`
+ `python-urlgrabber-3.9.1`
+ `python-yaml-3.05`
+ `python24-2.4.6`
+ `python26-2.6.6`
+ `quota-3.17`
+ `radiusclient-ng-0.5.6`
+ `rcs-5.7`
+ `rdate-1.4`
+ `rdist-6.1.5`
+ `readahead-1.5.6`
+ `readline-6.0`
+ `regexp-1.5`
+ `rhino-1.7`
+ `rng-utils-2.0`
+ `rootfiles-8.1`
+ `rpcbind-0.2.0`
+ `rpm-4.8.0`
+ `rpmdevtools-7.8`
+ `rrdtool-1.3.8`
+ `rsh-0.17`
+ `rsync-3.0.6`
+ `rsyslog-4.6.2`
+ `ruby-1.8.7.330`
+ `rubygems-1.3.7`
+ `saxon-6.5.5`
+ `screen-4.0.3`
+ `sed-4.2.1`
+ `selinux-policy-3.7.19`
+ `sendmail-8.14.4`
+ `setools-3.3.7`
+ `setserial-2.17`
+ `setup-2.8.14`
+ `sg3_utils-1.28`
+ `sgml-common-0.6.3`
+ `sgpio-1.2.0.10`
+ `shadow-utils-4.1.4.2`
+ `shared-mime-info-0.70`
+ `sharutils-4.7`
+ `slang-2.2.1`
+ `sos-2.2`
+ `spamassassin-3.3.1`
+ `spawn-fcgi-1.6.3`
+ `speex-1.2`
+ `splint-3.1.1`
+ `sqlite-3.6.20`
+ `squid-3.1.4`
+ `strace-4.5.20`
+ `stunnel-4.29`
+ `subversion-1.6.15`
+ `sudo-1.7.2p2`
+ `svrcore-4.0.4`
+ `swig-2.0.1`
+ `symlinks-1.4`
+ `sysfsutils-2.1.0`
+ `syslinux-3.86`
+ `sysstat-9.0.4`
+ `system-release-2011.02`
+ `systemtap-1.2`
+ `sysvinit-2.87`
+ `t1lib-5.1.2`
+ `talk-0.17`
+ `tar-1.23`
+ `tcl-8.5.7`
+ `tcp_wrappers-7.6`
+ `tcpdump-4.0.0`
+ `tcsh-6.17`
+ `telnet-0.17`
+ `texinfo-4.13a`
+ `tftp-0.49`
+ `tidy-0.99.0`
+ `time-1.7`
+ `tmpwatch-2.9.16`
+ `tomcat6-6.0.32`
+ `traceroute-2.0.14`
+ `transfig-3.2.5`
+ `tree-1.5.3`
+ `ttmkfdir-3.0.9`
+ `tunctl-1.5`
+ `tzdata-2010l`
+ `udev-147`
+ `udftools-1.0.0b3`
+ `unix2dos-2.2`
+ `unixODBC-2.2.14`
+ `unzip-6.0`
+ `urw-fonts-2.4`
+ `usbutils-0.86`
+ `usermode-1.102`
+ `ustr-1.0.4`
+ `util-linux-ng-2.17.2`
+ `uuid-1.6.1`
+ `valgrind-3.5.0`
+ `vconfig-1.9`
+ `velocity-1.4`
+ `vim-7.2.411`
+ `vsftpd-2.2.2`
+ `w3m-0.5.2`
+ `watchdog-5.5`
+ `werken-xpath-0.9.4`
+ `wget-1.12`
+ `which-2.19`
+ `wireshark-1.2.13`
+ `words-3.0`
+ `wpa_supplicant-0.6.8`
+ `ws-commons-util-1.0.1`
+ `wsdl4j-1.5.2`
+ `x86info-1.25`
+ `xalan-j2-2.7.0`
+ `xcb-proto-1.6`
+ `xdoclet-1.2.3`
+ `xerces-j2-2.7.1`
+ `xfsprogs-3.1.3`
+ `xhtml2fo-style-xsl-20051222`
+ `xinetd-2.3.14`
+ `xjavadoc-1.1`
+ `xkeyboard-config-1.6`
+ `xml-commons-apis-1.3.04`
+ `xml-commons-resolver-1.1`
+ `xmlrpc-c-1.22.04`
+ `xmltex-20020625`
+ `xmlto-0.0.23`
+ `xorg-x11-apps-7.4`
+ `xorg-x11-font-utils-7.2`
+ `xorg-x11-fonts-7.2`
+ `xorg-x11-proto-devel-7.4`
+ `xorg-x11-server-1.7.7`
+ `xorg-x11-server-utils-7.4`
+ `xorg-x11-util-macros-1.4.1`
+ `xorg-x11-utils-7.4`
+ `xorg-x11-xauth-1.0.2`
+ `xorg-x11-xbitmaps-1.0.1`
+ `xorg-x11-xdm-1.1.6`
+ `xorg-x11-xkb-utils-7.4`
+ `xorg-x11-xtrans-devel-1.2.2`
+ `xrestop-0.4`
+ `xz-4.999.9`
+ `yp-tools-2.9`
+ `ypbind-1.20.4`
+ `ypserv-2.19`
+ `yum-3.2.27`
+ `yum-metadata-parser-1.1.2`
+ `yum-utils-1.1.26`
+ `zip-3.0`
+ `zlib-1.2.3`
+ `zsh-4.3.10`
