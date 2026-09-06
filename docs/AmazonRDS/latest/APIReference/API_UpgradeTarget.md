---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_UpgradeTarget.html
---

# UpgradeTarget
<a name="API_UpgradeTarget"></a>

The version of the database engine that a DB instance can be upgraded to.

## Contents
<a name="API_UpgradeTarget_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AutoUpgrade **
Indicates whether the target version is applied to any source DB instances that have `AutoMinorVersionUpgrade` set to true.
This parameter is dynamic, and is set by RDS.
Type: Boolean
Required: No

 ** Description **
The version of the database engine that a DB instance can be upgraded to.
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
Indicates whether upgrading to the target version requires upgrading the major version of the database engine.
Type: Boolean
Required: No

 ** SupportedEngineModes.member.N **
A list of the supported DB engine modes for the target engine version.
Type: Array of strings
Required: No

 ** SupportsBabelfish **
Indicates whether you can use Babelfish for Aurora PostgreSQL with the target engine version.
Type: Boolean
Required: No

 ** SupportsGlobalDatabases **
Indicates whether you can use Aurora global databases with the target engine version.
Type: Boolean
Required: No

 ** SupportsIntegrations **
Indicates whether the DB engine version supports zero-ETL integrations with Amazon Redshift.
Type: Boolean
Required: No

 ** SupportsLimitlessDatabase **
Indicates whether the DB engine version supports Aurora Limitless Database.
Type: Boolean
Required: No

 ** SupportsLocalWriteForwarding **
Indicates whether the target engine version supports forwarding write operations from reader DB instances to the writer DB instance in the DB cluster. By default, write operations aren't allowed on reader DB instances.
Valid for: Aurora DB clusters only
Type: Boolean
Required: No

 ** SupportsParallelQuery **
Indicates whether you can use Aurora parallel query with the target engine version.
Type: Boolean
Required: No

## See Also
<a name="API_UpgradeTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/UpgradeTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/UpgradeTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/UpgradeTarget)
