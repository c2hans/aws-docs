---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_UpgradeTarget.html
---

# UpgradeTarget
<a name="API_UpgradeTarget"></a>

The version of the database engine that an instance can be upgraded to.

## Contents
<a name="API_UpgradeTarget_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AutoUpgrade **
A value that indicates whether the target version is applied to any source DB instances that have `AutoMinorVersionUpgrade` set to `true`.
Type: Boolean
Required: No

 ** Description **
The version of the database engine that an instance can be upgraded to.
Type: String
Required: No

 ** Engine **
The name of the upgrade target database engine.
Type: String
Required: No

 ** EngineVersion **
The version number of the upgrade target database engine.
Type: String
Required: No

 ** IsMajorVersionUpgrade **
A value that indicates whether a database engine is upgraded to a major version.
Type: Boolean
Required: No

## See Also
<a name="API_UpgradeTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/UpgradeTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/UpgradeTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/UpgradeTarget)
