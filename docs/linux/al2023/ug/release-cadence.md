---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/release-cadence.html
---

# Release cadence
<a name="release-cadence"></a>

Amazon Linux 2023 (AL2023) was released in March 2023 and will be supported until June 30, 2029. There are two phases of support:
+ **Standard support** – During this phase, the release receives quarterly minor version updates. The standard support phase ends June 30, 2027.
+ **Maintenance** – During this phase, the release receives only security updates and critical bug ﬁxes. These updates are published as soon as they're available. The maintenance phase ends June 30, 2029.

## Major and minor releases
<a name="major-minor-releases"></a>

With every Amazon Linux release (major version, minor version, or a security release), we release a new Linux Amazon Machine Image (AMI).
+ **Major version release**— Includes new features and improvements in security and performance across the stack. The improvements might include major changes to the kernel, toolchain, Glib C, OpenSSL, and any other system libraries and utilities. Major releases of Amazon Linux are based in part on the current version of the upstream Fedora Linux distribution. AWS might add or replace speciﬁc packages from other non-Fedora upstreams.
+ **Minor version release**— A quarterly update that includes security updates, bug fixes, and new features and packages. Each minor version is a cumulative list of updates that includes security and bug fixes in addition to new features and packages. These releases might include latest language runtimes, such as PHP. They might also include other popular software packages such as Ansible and Docker.

## Consuming new releases
<a name="consuming-new-releases"></a>

Updates are provided through a combination of new Amazon Machine Image (AMI) releases and corresponding new repositories. By default, a new AMI and the repository that it points to are coupled. However, you can point your running Amazon EC2 instances to newer repository versions over time to apply updates on the running instances. You can also update by launching new instances of the latest AMIs.

## Long-term support policy
<a name="long-term-support-policy"></a>

Amazon Linux provides updates for all of your packages and maintains compatibility within a major version for your applications that are built on Amazon Linux. Core packages such as the glibc library, OpenSSL, OpenSSH, and the DNF package manager receive support for the lifetime of the major AL2023 release. Packages that aren't part of the core packages are supported based on their specific upstream sources. You can see the specific support status and dates of individual packages by running the following command.

```
$ sudo dnf supportinfo --pkg {{packagename}}
```

You can get information on all currently installed packages by running the following command.

```
$ sudo dnf supportinfo --show installed
```

The full list of core packages is ﬁnalized during the preview. If you want to see more packages included as core packages, tell us. We evaluate as we are collecting feedback. Feedback on AL2023 can be provided through your designated AWS representative or by filing an issue in the [amazon-linux-2023 repo](https://github.com/amazonlinux/amazon-linux-2023/issues) on GitHub.
