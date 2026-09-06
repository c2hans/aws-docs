---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/release-cadence.html
---

# Release cadence
<a name="release-cadence"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 follows the same release cadence model as AL2023. AL2027 will be supported until 2032. There are two phases of support:
+ **Standard support** – During this phase, the release receives quarterly minor version updates with new features, security updates, and bug fixes.
+ **Maintenance** – During this phase, the release receives only security updates and critical bug fixes. These updates are published as soon as they are available.

## Major and minor releases
<a name="major-minor-releases"></a>

With every Amazon Linux release (major version, minor version, or a security release), we release a new AMI.
+ **Major version release** – Includes new features and improvements in security and performance across the stack. The improvements might include major changes to the kernel, toolchain, glibc, OpenSSL, and other system libraries and utilities. Major releases of Amazon Linux are based in part on the current version of the upstream Fedora Linux distribution. AWS might add or replace specific packages from other non-Fedora upstreams. For more information, see [Relationship to Fedora](relationship-to-fedora.md).
+ **Minor version release** – A quarterly update that includes security updates, bug fixes, and new features and packages. Each minor version is a cumulative list of updates that includes security and bug fixes in addition to new features and packages. These releases might include the latest language runtimes and other popular software packages.

## Consuming new releases
<a name="consuming-new-releases"></a>

Updates are provided through a combination of new AMI releases and corresponding new repository versions. By default, a new AMI and the repository version that it points to are coupled: each release is locked to its own repository version. You can point your running Amazon EC2 instances to newer repository versions over time to apply updates in place, or you can update by launching new instances from the latest AMIs. For more information, see [Deterministic upgrades through versioned repositories on AL2027](deterministic-upgrades.md).

## Long-term support policy
<a name="long-term-support-policy"></a>

Amazon Linux provides updates for all of your packages and maintains compatibility within a major version for your applications that are built on Amazon Linux. Core packages such as the glibc library, OpenSSL, OpenSSH, and the DNF5 package manager receive support for the lifetime of the major AL2027 release. Packages that are not part of the core packages are supported based on their specific upstream sources. You can see the support status and dates of individual packages by running the following command.

```
$ sudo dnf supportinfo --pkg {{packagename}}
```

You can get information on all currently installed packages by running the following command.

```
$ sudo dnf supportinfo --show installed
```

**Note**
During the preview, the support timeline reported for each package extends only to the end of the preview period. Support timelines for the AL2027 releases will be published with the public releases.

For all plugin commands, output formats, and configuration, see [Query package support with the AL2027 support info plugin](dnf-supportinfo-plugin.md).

The full list of core packages is finalized during the preview. If you want to see more packages included as core packages, tell us. We evaluate all feedback as we receive it. Provide feedback through your designated AWS representative or file an issue in the `amazon-linux-2027` repo on GitHub.
