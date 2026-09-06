---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/naming-and-versioning.html
---

# Naming and versioning
<a name="naming-and-versioning"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 provides a minor release every three months during standard support. Each release is identified by an increment from 0 to N. The value 0 refers to the original major release for that iteration. All releases will be called Amazon Linux 2027. When the next version of Amazon Linux is released, AL2027 will enter the maintenance phase and receive security updates and critical bug fixes.

For example, minor releases of AL2027 have the following format:
+ `2027.0.20260903`
+ `2027.1.20261203`
+ `2027.2.20270303`

The corresponding AL2027 AMIs have the following format:
+ `al2027-preview-ami-2027.0.20260903.0-kernel-7.1-x86_64`
+ `al2027-preview-ami-2027.1.20261203.0-kernel-7.1-x86_64`
+ `al2027-preview-ami-minimal-2027.0.20260903.0-kernel-7.1-arm64`

Within a specific minor version, regular AMI releases occur with a timestamp of the date of the AMI release.
+ `al2027-preview-ami-2027.0.20260903.0-kernel-7.1-x86_64`
+ `al2027-preview-ami-2027.0.20261012.0-kernel-7.1-x86_64`
+ `al2027-preview-ami-2027.0.20261120.0-kernel-7.1-x86_64`

To identify an Amazon Linux instance, read the Common Platform Enumeration (CPE) string from `/etc/system-release-cpe`. Then split the string into its fields and read the platform and version values. On AL2027, the CPE string has the following form:

```
cpe:2.3:o:amazon:amazon_linux:2027:2027.0.20260903
```

AL2027 also provides two files for platform identification:
+ `/etc/amazon-linux-release` points to the same file as `/etc/system-release`
+ `/etc/amazon-linux-release-cpe` points to the same file as `/etc/system-release-cpe`

These two files indicate that an instance is Amazon Linux. There is no need to read a file or split the string into fields, unless you want to know the specific platform and version values. For all identification methods and examples, see [Identifying Amazon Linux instances and versions](identifying.md).
