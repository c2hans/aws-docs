---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBSnapshotTenantDatabase.html
---

# DBSnapshotTenantDatabase
<a name="API_DBSnapshotTenantDatabase"></a>

Contains the details of a tenant database in a snapshot of a DB instance.

## Contents
<a name="API_DBSnapshotTenantDatabase_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CharacterSetName **
The name of the character set of a tenant database.
Type: String
Required: No

 ** DBInstanceIdentifier **
The ID for the DB instance that contains the tenant databases.
Type: String
Required: No

 ** DbiResourceId **
The resource identifier of the source CDB instance. This identifier can't be changed and is unique to an AWS Region.
Type: String
Required: No

 ** DBSnapshotIdentifier **
The identifier for the snapshot of the DB instance.
Type: String
Required: No

 ** DBSnapshotTenantDatabaseARN **
The Amazon Resource Name (ARN) for the snapshot tenant database.
Type: String
Required: No

 ** EngineName **
The name of the database engine.
Type: String
Required: No

 ** MasterUsername **
The master username of the tenant database.
Type: String
Required: No

 ** NcharCharacterSetName **
The `NCHAR` character set name of the tenant database.
Type: String
Required: No

 ** SnapshotType **
The type of DB snapshot.
Type: String
Required: No

 ** TagList.Tag.N **
A list of tags.
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TenantDatabaseCreateTime **
The time the DB snapshot was taken, specified in Coordinated Universal Time (UTC). If you copy the snapshot, the creation time changes.
Type: Timestamp
Required: No

 ** TenantDatabaseResourceId **
The resource ID of the tenant database.
Type: String
Required: No

 ** TenantDBName **
The name of the tenant database.
Type: String
Required: No

## See Also
<a name="API_DBSnapshotTenantDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBSnapshotTenantDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBSnapshotTenantDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBSnapshotTenantDatabase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
