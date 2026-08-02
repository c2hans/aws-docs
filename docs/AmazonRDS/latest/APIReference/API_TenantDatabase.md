---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_TenantDatabase.html
---

# TenantDatabase
<a name="API_TenantDatabase"></a>

A tenant database in the DB instance. This data type is an element in the response to the `DescribeTenantDatabases` action.

## Contents
<a name="API_TenantDatabase_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CharacterSetName **
The character set of the tenant database.
Type: String
Required: No

 ** DBInstanceIdentifier **
The ID of the DB instance that contains the tenant database.
Type: String
Required: No

 ** DbiResourceId **
The AWS Region-unique, immutable identifier for the DB instance.
Type: String
Required: No

 ** DeletionProtection **
Specifies whether deletion protection is enabled for the DB instance.
Type: Boolean
Required: No

 ** MasterUsername **
The master username of the tenant database.
Type: String
Required: No

 ** MasterUserSecret **
Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.*
Type: [MasterUserSecret](API_MasterUserSecret.md) object
Required: No

 ** NcharCharacterSetName **
The `NCHAR` character set name of the tenant database.
Type: String
Required: No

 ** PendingModifiedValues **
Information about pending changes for a tenant database.
Type: [TenantDatabasePendingModifiedValues](API_TenantDatabasePendingModifiedValues.md) object
Required: No

 ** Status **
The status of the tenant database.
Type: String
Required: No

 ** TagList.Tag.N **
A list of tags.
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TenantDatabaseARN **
The Amazon Resource Name (ARN) for the tenant database.
Type: String
Required: No

 ** TenantDatabaseCreateTime **
The creation time of the tenant database.
Type: Timestamp
Required: No

 ** TenantDatabaseResourceId **
The AWS Region-unique, immutable identifier for the tenant database.
Type: String
Required: No

 ** TenantDBName **
The database name of the tenant database.
Type: String
Required: No

## See Also
<a name="API_TenantDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/TenantDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/TenantDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/TenantDatabase)
