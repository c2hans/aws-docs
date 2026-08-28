---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/naming-and-versioning.html
---

# Naming and versioning
<a name="naming-and-versioning"></a>

AL2023 provides a minor release every three months during the two years of standard support. Each release is identified by an increment from 0 to N. 0 refers to the original major release for that iteration. All releases will be called Amazon Linux 2023. When the next version of Amazon Linux is released, AL2023 will enter extended support and receive updates for security updates and critical bug fixes.

For example, minor releases of AL2023 have the following format:
+ `2023.0.20230301`
+ `2023.1.20230601`
+ `2023.2.20230901`

The corresponding AL2023 AMIs have the following format:
+ `al2023-ami-2023.0.20230301.0-kernel-6.1-x86_64`
+ `al2023-ami-2023.1.20230601.0-kernel-6.1-x86_64`
+ `al2023-ami-2023.2.20230901.0-kernel-6.1-x86_64`

Within a specific minor version, regular AMI releases occur with a timestamp of the date of the AMI release.
+ `al2023-ami-2023.0.20230301.0-kernel-6.1-x86_64`
+ `al2023-ami-2023.0.20230410.0-kernel-6.1-x86_64`
+ `al2023-ami-2023.0.20230520.0-kernel-6.1-x86_64`

The recommended method for identifying an AL2 or AL2023 instance starts with reading the Common Platform Enumeration (CPE) string from `/etc/system-release-cpe`. Then, split the string into its fields. Finally, read the platform and version values.

AL2023 also introduces new files for platform identification:
+  `/etc/amazon-linux-release` symlinks to `/etc/system-release`
+  `/etc/amazon-linux-release-cpe` symlinks to `/etc/system-release-cpe`

These two files indicate that an instance is Amazon Linux. There's no need to read a file or split the string into fields, unless you want to know the specific platform and version values.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
