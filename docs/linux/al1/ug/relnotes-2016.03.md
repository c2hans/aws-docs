---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2016.03.html
---

# AL1 version 2016.03 release notes
<a name="relnotes-2016.03"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes AL1 release notes updates for the 2016.03 release.

## Upgrading to AL1 version 2016.03
<a name="upgrading-2016.03"></a>

We recommend that you upgrade to AL1 version 2016.03 from earlier versions.

Although previous versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new AL1 versions are released, we encourage users to migrate to the latest version of the AMI and to keep their systems updated. In some cases, customers who seek support for an previous version of AL1 through Support might be asked to move to newer versions as part of the support process.

To upgrade to AL1 version 2016.03 from 2011.09 or later, run `sudo yum update`. When the upgrade is complete, reboot your instance.

Remember that the AL1 repository structure is configured to deliver a continuous flow of updates that allow you to roll from one version of AL1 to the next. For more information, see our lock-on-launch FAQ for a discussion of how you can lock an instance (either a new launch or one already running) to a particular version of the AL1 repositories.

## 2016.03.3 point release
<a name="release-2016.03.3"></a>

Released on June 28, 2016

We've added support for the newly launched Elastic Network Adapter (ENA), the next generation network interface for Amazon EC2 instances, including version 0.6.6 of the open source ENA drivers.

## 2016.03.2 point release
<a name="release-2016.03.2"></a>

Released on June 9, 2016

We've updated the base AMI to include all bug fix and security updates that have were available in our repositories since the 2016.03.1 point release.

This point release includes the 4.4.11 kernel.

The Amazon Linux AMI with NVIDIA GRID GPU Driver now includes NVIDIA driver version 352.79 and CUDA 7.5.18.

## 2016.03.1 point release
<a name="release-2016.03.1"></a>

Released on May 4, 2016

We've updated the base AMI to include all bugfix and security updates that have been made available in our repositories since the 2016.03 release.

This point release includes the 4.4.8 kernel.

We've made a number of changes that improve AMI reboot time performance.

## New Features
<a name="new-features-2016.03"></a>

### Kernel 4.4
<a name="kernel-2016.03"></a>

Having spent the past release tracking the 4.1 kernel series, for this release we moved the kernel to version 4.4, which is the most recent long-term stable release kernel.

### SSLv3 protocol disabled by default
<a name="sslv3-2016.03"></a>

The SSLv3 protocol has been disabled by default in OpenSSL in favor of TLS. Server applications that have SSL/TLS protocol lists in their configuration have been updated to exclude SSLv3 by default.

For this release, SSLv3 support has not been entirely removed from any cryptographic libraries, so you can override this decision on an application-by-application basis, where supported.

SSL-related changes to individual applications are described below:

#### Apache: `mod_ssl`, `mod24_ssl`
<a name="apache-sslv3-2016.03"></a>

**Note**
This section applies to Apache 2.2, through the `httpd` and `mod_ssl` packages, and to Apache 2.4, through the `httpd24` and `mod24_ssl` packages.

SSLv3 support in Apache is controlled by the `SSLProtocol` and `SSLProxyProtocol` settings in `/etc/httpd/conf.d/ssl.conf`, part of the `mod_ssl` or `mod24_ssl` packages. If you're performing a new install, or if you're upgrading and you haven't modified `ssl.conf`, you'll get this change automatically. If you're upgrading and you've modified `ssl.conf`, you can add the following lines to `/etc/httpd/conf.d/ssl.conf` and restart `httpd` to ensure you're using TLS.

**Example `ssl.conf` Example**

```
SSLProtocol all -SSLv3
SSLProxyProtocol all -SSLv3
```

If you need to enable SSLv3, you can change `-SSLv3` to `-SSLv2` in those lines and restart `httpd`.

#### Apache: `mod_nss`, `mod24_nss`
<a name="apache-nss-sslv3-2016.03"></a>

**Note**
This section applies to Apache 2.2, through the `httpd` and `mod_nss` packages, and to Apache 2.4, through the `httpd24` and `mod24_nss` packages.

SSLv3 support in `mod_nss` is similar to `mod_ssl` (see previous section) but the relevant configuration option is `NSSProtocol` in `/etc/httpd/conf.d/nss.conf`. In this release, SSLv3 has been removed from this list by default. If you're performing a new install, or if you're upgrading and you haven't modified `nss.conf`, you'll get this change automatically. If you're upgrading and you have modified `nss.conf`, you can add the following line to `/etc/httpd/conf.d/nss.conf` and restart `httpd` to ensure you're using TLS.

**Example `nss.conf` Example**

```
NSSProtocol TLSv1.0,TLSv1.1,TLSv1.2
```

If you need to enable SSLv3, you can add `SSLv3` to that list and restart `httpd`.

#### nginx
<a name="nginx-sslv3-2016.03"></a>

SSLv3 support in `nginx` is controlled by the `ssl_protocols` setting in the `http` and `server` contexts in your configuration. The default (commented) configuration for SSL servers in AL1 now includes an `ssl_protocols` line specifying only TLS, as a suggestion for users setting up a new secure server.

If you're upgrading nginx and want to ensure you only use TLS, include the following line in the server context of your configuration and restart nginx.

**Example nginx configuration enforcing TLS**

```
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
```

If you need to enable SSLv3, you can add `SSLv3` to this line and restart nginx.

#### lighttpd
<a name="lighttpd-sslv3-2016.03"></a>

SSLv3 is disabled by default if not specified in the `lighttpd` configuration file. If you need to enable SSLv3, you can add the following line to `/etc/lighttpd/lighttpd.conf` and restart `lighttpd`.

**Example Enabling SSLv3 in `lighttpd`**

```
ssl.use-sslv3 = "enable"
```

#### tomcat
<a name="tomcat-sslv3-2016.03"></a>

Tomcat uses the JVM for TLS. All versions of OpenJDK in AL1 have SSLv3 support disabled.

#### openldap and 389
<a name="openldap-sslv3-2016.03"></a>

New installations of `openldap` include the parameter `TLSProtocolMin 3.1` in `slapd.conf`, which is used to populate the initial configuration in `cn=config`.

New installations of 389 include the parameter `sslVersionMin: TLS1.0` in `cn=config`.

Users upgrading to this release can change the relevant parameter using `ldapmodify`.

#### dovecot
<a name="dovecot-sslv3-2016.03"></a>

`dovecot` now includes the following line in `/etc/dovecot/conf.d/10-ssl.conf`.

**Example `dovecot` configuration snippet disabling SSLv2 and SSLv3**

```
ssl_protocols = !SSLv2 !SSLv3
```

If you're newly installing `dovecot`, or if you're upgrading and haven't modified `10-ssl.conf`, you'll get this change automatically. If you're upgrading `dovecot` and you have modified `10-ssl.conf`, you can add the line above to `/etc/dovecot/conf.d/10-ssl.conf` and restart `dovecot` to ensure you're using TLS.

If you need to enable SSLv3, remove `!SSLv3` from that line and restart `dovecot`.

#### `postfix`, `sendmail`, `postgresql`, `mysql`, `tomcat`-n`ative`, `haproxy`, `cyrus-imapd`, `stunnel`, `vsftpd`, `fetchmail`
<a name="other-sslv3-2016.03"></a>

These applications inherit their settings from OpenSSL and will no longer use SSLv3.

### DNS resolution retries faster
<a name="dns-2016.03"></a>

The default DNS resolution options were chqnged from two retries with a five second timeout to five retries with a two second timeout.

Retries for DNS resolution in `glibc` are configured to happen faster because the distance to the Amazon EC2 resolvers is known to be short. This is configured in the AMI rather than in a package, so the change is not brought in unexpectedly by a `yum update`.

To apply the same change to existing instances, append the following options to the appropriate configuration files:

1.

   ```
   $ echo 'RES_OPTIONS="timeout:2 attempts:5"' | sudo tee -a /etc/sysconfig/network-scripts/ifcfg-eth0
   ```

1.

   ```
   $ echo 'options timeout:2 attempts:5' | sudo tee -a /etc/resolv.conf
   ```

### NUMA balancing disabled by default
<a name="numa-2016.03"></a>

In this release, NUMA balancing has been disabled by default in the kernel to avoid unexpected performance degradation. This change only affects the following instance types which support NUMA:
+ `cr1.8xlarge`
+ `c3.8xlarge`
+ `r3.8xlarge`
+ `i2.8xlarge`
+ `c4.8xlarge`
+ `d2.8xlarge`
+ `g2.8xlarge`
+ `m4.10xlarge`

If you prefer the previous behavior, you can enable NUMA balancing using sysctl:

1.

   ```
   $ sudo sysctl -w 'kernel.numa_balancing=1'
   ```

1.

   ```
   $ echo 'kernel.numa_balancing = 1' | sudo tee /etc/sysctl.d/50-numa-balancing.conf
   ```

### OpenLDAP 2.4.40
<a name="openldap-2016.03"></a>

OpenLDAP 2.4.40 was in the preview repository since our 2015.09 release. OpenLDAP 2.4.40 is now available in the main repository. In addition to numerous bug fixes and stability enhancements, OpenLDAP now supports the Lightning Memory-Mapped Database (LMDB) format.

### Ruby 2.3
<a name="ruby-2016.03"></a>

Although Ruby 2.0 remains our default Ruby interpreter, we have added `ruby23` packages to this AL1 release. Core rubygems have also been updated.

### Rust 1.9 (preview)
<a name="rust-2016.03"></a>

We continue to track upstream releases of the Rust compiler, and in this release we've included version 1.7. You can install the Rust compiler by running `sudo yum --enablerepo=amzn-preview install rust`.

Update 2016-06-08: Rust 1.9 is now available in our preview repository.

## Fresh packages
<a name="fresh-2016.03"></a>

Many of our packages have been re-synced to newer upstream versions. Some of the more popular packages in 2016.03 are:
+ aalib-1.4.0
+ aws-cli-1.10.33
+ clamav-0.99
+ docker-1.9.1
+ dovecot-2.2.10
+ elfutils-0.163
+ git-2.7.4
+ glibc-2.17-106.167
+ httpd24-2.4.18
+ iproute-4.4.0
+ java-1.7.0-openjdk-1.7.0.101
+ java-1.8.0-openjdk-1.8.0.91
+ kernel-4.4.11
+ lz4-r131
+ mariadb-connector-java-1.3.6
+ mysql55-5.5.46
+ mysql56-5.6.27
+ nmap-6.40
+ nginx-1.8.1
+ openldap-2.4.40
+ php55-5.5.33
+ php56-5.6.19
+ pngcrush-1.8.0
+ postgresql93-9.3.11
+ postgresql94-9.4.6
+ python-boto-2.39.0
+ python-botocore-1.4.23
+ ruby20-2.0.0.648
+ ruby21-2.1.8
+ ruby22-2.2.4
+ ruby23-2.3.0
+ samba-4.2.10
+ systemtap-3.0
+ tomcat7-7.0.68
+ tomcat8-8.0.32

## Supported Instance Types
<a name="instance-types-2016.03"></a>

[This compatibility table](relnotes-2015.09.md#instance-types-2015.09) shows which 2016.03 AMIs launch on each Amazon EC2 instance type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
