---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2015.09.html
---

# Amazon Linux 1 (AL1) version 2015.09 release notes
<a name="relnotes-2015.09"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2015.09 release.

## Upgrading to Amazon Linux 1 (AL1) version 2015.09
<a name="upgrading-2015.09"></a>

Please upgrade to Amazon Linux 1 (AL1) version 2015.09 from earlier versions\!

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux 1 (AL1) versions are released, we encourage users to migrate to the latest version of the AMI and to keep their systems updated. In some cases, customers seeking support for an older version of the Amazon Linux 1 (AL1) through Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux 1 (AL1) version 2015.09 from 2011.09 or later, run `sudo yum update`. When the upgrade is complete, reboot your instance.

Remember that the Amazon Linux 1 (AL1) repository structure is configured to deliver a continuous flow of updates that allow you to roll from one version of the Amazon Linux 1 (AL1) to the next. Please consult our lock-on-launch FAQ for a discussion of how you can lock an instance (either a new launch or already running) to a particular version of the Amazon Linux 1 (AL1) repositories.

## 2015.09.2 point release
<a name="release-2015.09.2"></a>

Released on February 16, 2016

We've updated the base AMI to include all bugfix and security updates that have been made available in our repositories since the 2015.09 release.

This point release includes the 4.1.17 kernel.

## 2015.09.1 point release
<a name="release-2015.09.1"></a>

Released on November 2, 2015

We've updated the base AMI to include all bugfix and security updates that have been made available in our repositories since the 2015.09 release.

This point release includes the 4.1.10 kernel.

## New Features
<a name="new-features-2015.09"></a>

### Kernel 4.1.7
<a name="kernel-2015.09"></a>

Having spent the past year tracking the 3.14 kernel series, for this release we have moved the kernel to version 4.1.7, which is the most recent long-term stable release kernel. Of particular interest to many customers is the support for OverlayFS in the 4.x kernel series.

### Amazon Aurora JDBC driver
<a name="jdbc-2015.09"></a>

We introduced a Java JDBC driver for Amazon Aurora and MariaDB databases. This driver can connect to multiple Aurora nodes, allowing faster fail-over compared to DNS-based fail-over. The package is available via `sudo yum install mariadb-connector-java`.

### Samba
<a name="samba-2015.09"></a>

Based on numerous customer requests and in order to support joining Amazon Linux 1 (AL1) instances to an AWS Directory Service directory, we have added Samba 4.1 to the Amazon Linux 1 (AL1) repositories, available via `sudo yum install samba`.

### PostgreSQL 9.4
<a name="postgresql-2015.09"></a>

Numerous customers have asked for PostgreSQL 9.4 and it is now available in our Amazon Linux 1 (AL1) repositories as a separate package from PostgreSQL 9.2 and 9.3. PostgreSQL 9.4 is available via `sudo yum install postgresql94` and the 2015.09 version of the Amazon Linux 1 (AL1) repositories include PostgreSQL 9.4.4.

### MySQL 5.6
<a name="mysql-2015.09"></a>

A frequent customer request has been MySQL 5.6, and we are pleased to offer it in the 2015.09 repositories as a separate package from MySQL 5.1 and 5.5. MySQL 5.6 is available via `sudo yum install mysql56` and the 2015.09 repositories include MySQL 5.6.26.

### Docker is (still) Go
<a name="docker-2015.09"></a>

We introduced support for Docker and Go in our 2014.03 AMI, and we continue to follow upstream developments in each. The lead-up to the 2015.09 release included an update to Go 1.4 and to Docker 1.7.1.

### CloudHSM CLI
<a name="cloud-hsm-2015.09"></a>

We have added the AWS CloudHSM CLI tools to our repositories, installable via `sudo yum install aws-cloudhsm-cli`. The AWS CloudHSM service uses dedicated Hardware Security Module (HSM) appliances, allowing customers the ability to control the encryption keys and cryptographic operations performed by the HSM.

### PyPy (preview)
<a name="pypy-2015.09"></a>

We already provide Python 2.6, 2.7 (default), and 3.4 in Amazon Linux 1 (AL1), but several customers have also asked for the PyPy implementation of Python. We're pleased to include PyPy 2.4 in our preview repository. PyPy 2.4 is compatible with Python 2.7.8 and is installable via `sudo yum --enablerepo=amzn-preview install pypy`.

### OpenLDAP 2.4.40 (preview)
<a name="openldap-2015.09"></a>

We already provide OpenLDAP 2.4.23 in the main Amazon Linux 1 (AL1) repositories, but customers have asked for a newer version of OpenLDAP. We've included OpenLDAP 2.4.40 in our preview repository, and we will work to integrate it into our main repository in the future. It is installable via `sudo yum --enablerepo=amzn-preview install openldap`.

### Rust 1.3 (preview)
<a name="rust-2015.09"></a>

In our 2015.03 release notes we added an initial preview of the Rust programming language. Upstream development has continued on this language, and we have updated from Rust 1.0 to Rust 1.2 for the 2015.09 release. You can install the Rust compiler by running `sudo yum --enablerepo=amzn-preview install rust`.

Update 2015-09-28: Rust 1.3 is now available in our "Preview" repository.

## Full deprecation of GPU AMIs for the CG1 platform
<a name="gpu-2015.09"></a>

The following is only applicable to the GPU AMIs that we built specifically for the CG1 instance family.

In our 2014.09 release notes we announced that we would no longer produce GPU AMIs, recommending migration to the Graphics AMI and the G2 instance type. Our 2015.03 release notes reinforced this message, as we did not provide a GPU AMI for that release though we did still provide package updates in the GPU repository.

A full year later, we are now no longer producing any GPU package repositories. This means that existing GPU instances using the "latest" releasever will no longer receive updates to NVIDIA or CUDA-related packages and may see errors regarding the GPU repo when using yum. If you update your kernel using the 2015.09 release or later and reboot, you will no longer be able to use the nvidia module.

Our recommendation for all Amazon Linux 1 (AL1) GPU customers is to migrate to the Graphics AMI. The Graphics AMI has newer NVIDIA and CUDA software available and runs on the more powerful G2 instance type. We believe you'll find it more efficient and less expensive than the CG1 instance type.

## System call auditing disabled by default
<a name="audit-2015.09"></a>

In this release, system call auditing has been disabled by default to improve overall system performance. This change is only applied automatically to new instances created from 2015.09 AMIs. See below for instructions on changing existing instances.

If you need system call auditing, please find the following line in `/etc/audit/audit.rules` and remove it or comment it out, then restart the audit daemon.

` -a never,task`

**Example (as root):**

```
$ auditctl -l
LIST_RULES: task,never
$ sed -i.bak -e '/^-a never,task$/ s/^/#/' /etc/audit/audit.rules
$ /etc/init.d/auditd restart
$ auditctl -l
No rules
```

If you want to get the same performance improvement on existing instances, please add the line above to `/etc/audit/audit.rules` and restart the daemon. If you have not made any changes to audit rule files, you can simply move or copy the new default rules file to `/etc/audit/audit.rules`

**Example (as root):**

```
$ auditctl -l
No rules
$ cp -p /etc/audit/rules.d/audit.rules.default /etc/audit/audit.rules
cp: overwrite ‘/etc/audit/audit.rules’? y
$ /etc/init.d/auditd restart
$ auditctl -l
LIST_RULES: task,never
```

## Fresh packages
<a name="fresh-2015.09"></a>

Many of our packages have been re-synced to newer upstream versions. Some of the more popular packages in 2015.09 are:
+ aws-cli-1.8.2
+ bash-4.2.46
+ docker-1.7.1
+ gcc48-4.8.3
+ git-2.4.3
+ glibc-2.17-78.161
+ gnupg2-2.0.28
+ grep-2.20
+ httpd-2.2.31
+ httpd24-2.4.16
+ java-1.7.0-openjdk-1.7.0.85
+ java-1.8.0-openjdk-1.8.0.51
+ jq-1.5
+ kernel-4.1.7
+ llvm-3.6.2
+ mysql55-5.5.45
+ mysql56-5.6.26
+ nginx-1.8.0
+ nss-3.19.1
+ ntp-4.2.6p5
+ openssh-6.6.1p1
+ php54-5.4.45
+ php55-5.5.29
+ php56-5.6.13
+ pngcrush-1.7.85
+ postgresql93-9.3.9
+ postgresql94-9.4.4
+ python-boto-2.38.0
+ python-botocore-1.2.0
+ python-matplotlib-1.2.0
+ python27-2.7.10
+ R-3.2.2
+ ruby20-2.0.0.647
+ ruby21-2.1.7
+ ruby22-2.2.3
+ samba-4.1.12
+ sl-5.02
+ subversion-1.8.13
+ systemtap-2.8
+ tomcat7-7.0.62
+ tomcat8-8.0.23
+ zsh-5.0.2

## Supported Instance Types
<a name="instance-types-2015.09"></a>

| Instance Family | HVM EBS-Backed 64-bit | HVM Instance Store 64-bit | PV EBS-Backed 64-bit | PV Instance Store 64-bit |
| --- | --- | --- | --- | --- |
| t2 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| m4 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| m3 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |
| c4 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| c3 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |
| r3 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| g2 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| i2 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| d2 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
