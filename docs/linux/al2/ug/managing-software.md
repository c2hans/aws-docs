---
source_url: https://docs.aws.amazon.com/linux/al2/ug/managing-software.html
---

# Manage software on your AL2 instance
<a name="managing-software"></a>

The base distribution of Amazon Linux contains the software packages and utilities that are required for basic server operations.

This information applies to AL2. For information about AL2023, see [Manage packages and operating system updates in AL2023](https://docs.aws.amazon.com/linux/al2023/ug/managing-repos-os-updates.html) in the *Amazon Linux 2023 User Guide*.

It is important to keep software up to date. Many packages in a Linux distribution are updated frequently to fix bugs, add features, and protect against security exploits. For more information, see [Update instance software on your AL2 instance](install-updates.md).

By default, AL2 instances launch with the following repositories enabled:
+ `amzn2-core`
+ `amzn2extra-docker`

While there are many packages available in these repositories that are updated by AWS, there might be a package that you want to install that is contained in another repository. For more information, see [Add repositories on an AL2 instance](add-repositories.md). For help finding and installing packages in enabled repositories, see [Find and install software packages on an AL2 instance](find-install-software.md).

Not all software is available in software packages stored in repositories; some software must be compiled on an instance from its source code. For more information, see [Prepare to compile software on an AL2 instance](compile-software.md).

AL2 instances manage their software using the yum package manager. The yum package manager can install, remove, and update software, as well as manage all of the dependencies for each package.

**Topics**
+ [Update instance software on your AL2 instance](install-updates.md)
+ [Add repositories on an AL2 instance](add-repositories.md)
+ [Find and install software packages on an AL2 instance](find-install-software.md)
+ [Prepare to compile software on an AL2 instance](compile-software.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
