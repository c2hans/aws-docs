---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_DatabaseMigrationPreference.html
---

# DatabaseMigrationPreference
<a name="API_DatabaseMigrationPreference"></a>

 Preferences for migrating a database to AWS.

## Contents
<a name="API_DatabaseMigrationPreference_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** heterogeneous **   <a name="migrationhubstrategy-Type-DatabaseMigrationPreference-heterogeneous"></a>
 Indicates whether you are interested in moving from one type of database to another. For example, from SQL Server to Amazon Aurora MySQL-Compatible Edition.
Type: [Heterogeneous](API_Heterogeneous.md) object
Required: No

 ** homogeneous **   <a name="migrationhubstrategy-Type-DatabaseMigrationPreference-homogeneous"></a>
 Indicates whether you are interested in moving to the same type of database into AWS. For example, from SQL Server in your environment to SQL Server on AWS.
Type: [Homogeneous](API_Homogeneous.md) object
Required: No

 ** noPreference **   <a name="migrationhubstrategy-Type-DatabaseMigrationPreference-noPreference"></a>
 Indicated that you do not prefer heterogeneous or homogeneous.
Type: [NoDatabaseMigrationPreference](API_NoDatabaseMigrationPreference.md) object
Required: No

## See Also
<a name="API_DatabaseMigrationPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/DatabaseMigrationPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/DatabaseMigrationPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/DatabaseMigrationPreference)
