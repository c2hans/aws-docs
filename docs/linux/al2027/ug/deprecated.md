---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/deprecated.html
---

# Deprecated functionality in AL2027
<a name="deprecated"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

This chapter covers functionality that was present in AL2023 and is removed in AL2027, and functionality that remains in AL2027 but is deprecated. Understanding both helps you migrate to AL2027 and prepare for future versions of Amazon Linux.

Functionality deprecated in AL1 or AL2 and removed in earlier versions remains unavailable in AL2027. For that history, see [Deprecated functionality in AL2023](https://docs.aws.amazon.com/linux/al2023/ug/deprecated.html).

**Topics**
+ [`compat-` library packages](#deprecated-compat)
+ [Deprecated in AL2023](deprecated-al2023.md)
+ [Deprecated in AL2027](deprecated-al2027.md)

## `compat-` library packages
<a name="deprecated-compat"></a>

Packages with the `compat-` prefix provide binary compatibility with binaries built against older library versions. Each major version of Amazon Linux does not carry forward the `compat-` library packages of prior releases, and any it introduces are deprecated from the start. Rebuild software against the current library versions rather than relying on `compat-` packages.
