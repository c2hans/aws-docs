---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/deprecated-al2027.html
---

# Deprecated in AL2027
<a name="deprecated-al2027"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

Functionality deprecated in AL2027 is likely to be removed in a future version of Amazon Linux. Moving off deprecated functionality now reduces the work of migrating to the next version. This section is updated over the lifetime of AL2027 as the Linux ecosystem evolves.

**Topics**
+ [EOL packages are deprecated](#deprecated-eol-packages)

## EOL packages are deprecated
<a name="deprecated-eol-packages"></a>

Each package in AL2027 has an associated support timeline, which you can query with the `dnf supportinfo` command. For more information, see [Getting package support information](manage-updates.md#dnf-support-info-plugin). Where a package's support ends before the end of the major version of Amazon Linux, assume that the package is deprecated and will not be present in the next major version of Amazon Linux.

**Note**
During the preview period, the support timelines reflect the preview terms. Support statements for GA will be published before the public release.
