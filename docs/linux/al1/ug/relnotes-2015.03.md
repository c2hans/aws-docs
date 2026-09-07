---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2015.03.html
---

# AL1 version 2015.03 release notes
<a name="relnotes-2015.03"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes AL1 release notes updates for the 2015.03 release.

## Upgrading to AL1 version 2015.03
<a name="upgrading-2015.03"></a>

Please upgrade to AL1 version 2015.03 from earlier versions\!

While previous versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new AL1 versions are released, we recommend users migrate to the latest version of the AMI and keep their systems updated. In some cases, customers seeking support for an previous version of AL1 through Support might be asked to move to newer versions as part of the support process.

To upgrade to AL1 version 2015.03 from 2011.09 or later, run `sudo yum update`. When the upgrade is complete, reboot your instance.

Remember that the AL1 repository structure is configured to deliver a continuous flow of updates that allow you to roll from one version of AL1 to the next. Please consult our lock-on-launch FAQ for a discussion of how you can lock an instance (either a new launch or already running) to a particular version of the AL1 repositories.

## 2015.03.1 point release
<a name="release-2015.03.1"></a>

Released on August 21, 2015

We've updated the base AMI to include all bugfix and security updates that have been made available in our repositories since the 2015.03 release.

This point release includes the 3.14.48 kernel.

We've added `nfs-utils` to the default package set on the AMI to support Amazon Elastic File System.

## New Features
<a name="new-features-2015.03"></a>

### Python 2.7 by default
<a name="python27-2015.03"></a>

Python 2.7 is now used for the core system packages, including `yum` and `cloud-init`.

We've added Python 2.7 support for all of our existing Python 2.6 modules. For a full list, use yum's search command:

```
$ yum search python27
```

```
$ yum search python26
```

`/usr/bin/python` is controlled by alternatives, and can be set to either 2.7 or 2.6:

**Default to 2.7**

```
$ sudo alternatives --set python /usr/bin/python2.7
```

**Default to 2.6**

```
$ sudo alternatives --set python /usr/bin/python2.6
```

For maximum compatibility with EPEL 6, we recommend installing the `python26` package and setting it as your default using the previous command. This will happen automatically when updating from a previous AL1 release.

To simplify the process of installing unpackaged dependencies, `pip` and `virtualenv` are installed by default for Python 2.7 on 2015.03 AMIs. If a module you want is not provided in our repositories (use the search commands above to tell) then you have several options, outlined below.

These examples assume you've installed `python27-pip` and `python27-virtualenv` or that you have started with a 2015.03 AMI where those packages are included by default.

**Example To install a package system-wide without changing your default Python interpreter**

```
$ sudo pip-2.7 install modulename
```

**Example To install a package system-wide after you've changed your default with alternatives**

```
$ sudo pip install modulename
```

**Example To install a package in a virtualenv so that it doesn't impact your system python**

```
$ virtualenv-2.7 myproject && cd myproject
$ source bin/activate
$ pip install modulename
```

### Python 3.4
<a name="python34-2015.03"></a>

As part of our improvements to the Python experience, we've added Python 3.4 to our repositories with the 2015.03 release. Python 3.4 can be managed the same way described above, using `pip` and `virtualenv` to install dependencies.

**Example commands:**

```
$ yum search python34
$ sudo yum install python34-virtualenv
$ sudo alternatives --set python /usr/bin/python3.4
$ virtualenv-3.4 myproject
```

Python 2.6, 2.7, and 3.4 can all be installed on your system simultaneously, with `/usr/bin/python` controlled by `alternatives`. Python 2.7 will remain the version used by system tools.

### Kernel 3.14.35
<a name="kernel-2015.03"></a>

We moved to the long-term-supported 3.14 kernel with our 2014.03 release of AL1, and we continue to track that kernel in 2015.03.

### DKMS support
<a name="dkms-2015.03"></a>

On our G2 AMIs -- AL1 with NVIDIA GRID GPU Driver -- the nvidia package is now DKMS-enabled. Updating to a new kernel will trigger a nvidia module build for both the running kernel and the newly-installed kernel. The modules will be loaded for the running kernel with no need to reboot and will be loaded with a new kernel when you choose to reboot into it.

To see the current state of your DKMS-managed kernel modules run `sudo dkms status`.

### Ruby 2.2
<a name="ruby-2015.03"></a>

While Ruby 2.0 remains our default Ruby interpreter, we have added `ruby22` packages to this AL1 release.

Also, we have updated our versions of Ruby to the latest upstream patch levels:
+ ruby19-1.9.3.551
+ ruby20-2.0.0.643
+ ruby21-2.1.5
+ ruby22-2.2.1

### PHP 5.6
<a name="php-2015.03"></a>

Based on customer requests, PHP 5.6 is now available in the AL1 repositories as `php56`. PHP 5.5 and PHP 5.6 are able to be installed in parallel, and the version in use is controlled by alternatives. It is important to note that PHP 5.6 has the highest priority. If you have both versions installed, PHP 5.6 will be the default.

If you want to ensure that your environment will continue to use PHP 5.5 even after installing PHP 5.6, run `sudo alternatives --set php /usr/bin/php-5.5` or run `sudo alternatives --config php` to set the default interactively.

PHP 5.5 and PHP 5.6 each maintain their own configuration files, so changes made to PHP 5.6 will not be applied to PHP 5.5 (and vice versa).

### Docker 1.5
<a name="docker-2015.03"></a>

It's been a year since we introduced Docker to the AL1 repositories, and we continue to follow the Docker upstream closely. Docker 1.5 is now available. The [upstream release notes](https://docs.docker.com/engine/release-notes/prior-releases/#150-2015-02-10) have much more information about new features in Docker 1.5.

### Puppet 3.7
<a name="puppet-2015.03"></a>

A frequent customer request has been Puppet 3 support in AL1, and it's now available in the repositories as `puppet3`. This addition includes `facter2` and `hiera1`. These new packages all use Ruby 2.0 while the previous Puppet 2 packages (including facter 1) continue to require Ruby 1.8. The Puppet 2 and Puppet 3 packages conflict with each other, as do the facter 1 and facter 2 packages, meaning they cannot be installed at the same time.

### Rust (preview)
<a name="rust-2015.03"></a>

We've included a preview of the Rust programming language with our 2015.03 release. This preview is based on the 2015-03-09 sources with stabilized modules. Rust is scheduled for final release upstream in May 2015, and we plan on packaging Cargo and updating Rust as the release date approaches.

You can install the Rust compiler by running `sudo yum --enablerepo=amzn-preview install rust`.

## Deprecation of 32-bit AMIs
<a name="x86-2015.03"></a>

As announced in our [2014.09 release notes](relnotes-2014.09.md), we are no longer producing new 32-bit AMIs.

We are still producing 32-bit packages for existing customers (those using 32-bit AMIs from 2014.09 and earlier).

New customers should start with 64-bit AMIs, and we encourage existing customers to move to 64-bit as soon as possible.

## Deprecation of GPU AMIs
<a name="gpu-2015.03"></a>

As announced in our 2014.09 release notes, we are no longer producing new "GPU" AMIs for the CG1 instance type.

We are still providing package updates for existing customers (those using GPU AMIs from 2014.09 and earlier)

We recommend that customers migrate to the G2 instance type and the Amazon Linux AMI with NVIDIA GRID GPU Driver.

## Fresh packages
<a name="fresh-2015.03"></a>

Many of our packages have been re-synced to newer upstream versions. Some of the more popular packages in 2015.03 are:
+ aws-cli-1.7.14-1.8
+ bash-4.1.2-15.24
+ curl-7.40.0-1.49
+ docker-1.5.0-1.8
+ fortune-mod-1.99.1-20.3
+ git-2.1.0-1.38
+ glibc-2.17-55.140
+ gnutls-2.8.5-14.13
+ httpd24-2.4.12-1.60
+ java-1.7.0-openjdk-1.7.0.75-2
+ java-1.8.0-openjdk-1.8.0.31-2
+ kernel-3.14.35-28.38
+ mysql55-5.5.42
+ nethack-3.4.3-32.3
+ nginx-1.6.2-1.23
+ nss-3.16.2.3-2.63
+ openssh-6.2p2-8.43
+ openssl-1.0.1k-1.84
+ php54-5.4.38-1.66
+ php55-5.5.22-1.98
+ php56-5.6.6-1.109
+ php-amazon-sdk2-2.7.22-1.2
+ pngcrush-1.7.82-1.8
+ postgresql92-9.2.10
+ postgresql93-9.3.6
+ puppet3-3.7.4-1.11
+ python-boto-2.36.0-1.6
+ python-botocore-0.95.0-1.6
+ python27-2.7.9-4.114
+ python34-3.4.3-1.29
+ rpm-4.11.2-2.63
+ ruby19-1.9.3.551-32.64
+ ruby20-2.0.0.643-1.21
+ ruby21-2.1.5-1.15
+ ruby22-2.2.1-1.4
+ subversion-1.8.10-1.47
+ systemtap-2.5-3.26
+ tomcat6-6.0.43-1.2
+ tomcat7-7.0.59-1.7
+ tomcat8-8.0.20-1.52
+ vim-7.4.160-1.31

## Supported Instance Types
<a name="instance-types-2015.03"></a>

The compatibility table below shows which AL1 flavors are recommended for each Amazon EC2 instance type.

| Instance Family | HVM EBS-Backed 64-bit | HVM Instance Store 64-bit | PV EBS-Backed 64-bit | PV Instance Store 64-bit | HVM (G2) EBS-Backed 64-bit |
| --- | --- | --- | --- | --- | --- |
| t2 | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |  |
| m3 | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |
| c3 | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |
| c4 | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |  |
| r3 | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| g2 |  |  |  |  | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |
| i2 | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| hs1 | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |
| m1 |  |  | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |
| c1 |  |  | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |
| cc2.4xlarge | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| m2 |  |  | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |
| cr1 | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |  |
| hi1 | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |
| t1 |  |  | ![](https://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
