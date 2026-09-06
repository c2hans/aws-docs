---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/deprecated.html
---

# Deprecated Functionality in AL2023
<a name="deprecated"></a>

 Functionality deprecated in AL2 and not present in AL2023 is documented here. This is functionality such as features and packages that are present in AL2, but not in AL2023 and will not be added to AL2023. For more information about how the long the functionality is supported in AL2, see [Deprecated functionality in AL2](https://docs.aws.amazon.com/linux/al2/ug/deprecated.html).

 There is also functionality in AL2023 which is deprecated, and will be removed in a future release. This chapter describes what that functionality is, when it no longer supported, and when it will be removed from Amazon Linux. Understanding the deprecated functionality will help you deploy AL2023 as well as prepare for the next major version of Amazon Linux.

**Topics**
+ [`compat-` packages](#deprecated-compat)
+ [Deprecated functionality discontinued in AL1, removed in AL2](deprecated-al1.md)
+ [Functionality deprecated in AL2 and removed in AL2023](deprecated-al2.md)
+ [Deprecated in AL2023](deprecated-al2023.md)

## `compat-` packages
<a name="deprecated-compat"></a>

 Any packages in AL2 with the prefix of `compat-` are provided for binary compatibility with older binaries that have not yet been rebuilt for modern versions of the package. Each new major version of Amazon Linux will not carry forward any `compat-` package from prior releases.

 All `compat-` packages in a release of Amazon Linux (e.g. AL2) are deprecated, and not present in the subsequent version (e.g. AL2023). We strongly recommend that software is rebuilt against updated versions of the libraries.
