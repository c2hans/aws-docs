---
source_url: https://docs.aws.amazon.com/linux/al1/ug/deprecated.html
---

# Deprecated functionality in AL1
<a name="deprecated"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and AL2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

 This section describes functionality, such as features and packages, that are no longer available in AL1 and will not be added to AL2.

 For information about AL1 functionality that was discontinued in earlier releases, see [AL1 release notes](relnotes.md).

 For information about packages that had an EOL date earlier than the EOL of AL1, see [AL1 package support status](support-info-by-package.md).

## `compat-` packages
<a name="deprecated-compat"></a>

 Any packages in AL1 with the prefix of `compat-` are provided for binary compatibility with earlier binaries that have not yet been rebuilt for modern versions of the package. Each new major version of Amazon Linux will not carry forward any `compat-` package from prior releases.

 All `compat-` packages in a release of Amazon Linux (such as AL1) are discontinued, and not present in the subsequent version (AL2). We strongly recommend that software is rebuilt against updated versions of the libraries.
