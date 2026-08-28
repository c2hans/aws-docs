---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabase.html
---

# RelationalDatabase
<a name="API_RelationalDatabase"></a>

Describes a database.

## Contents
<a name="API_RelationalDatabase_Contents"></a>

 ** arn **   <a name="Lightsail-Type-RelationalDatabase-arn"></a>
The Amazon Resource Name (ARN) of the database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** backupRetentionEnabled **   <a name="Lightsail-Type-RelationalDatabase-backupRetentionEnabled"></a>
A Boolean value indicating whether automated backup retention is enabled for the database.
Type: Boolean
Required: No

 ** caCertificateIdentifier **   <a name="Lightsail-Type-RelationalDatabase-caCertificateIdentifier"></a>
The certificate associated with the database.
Type: String
Required: No

 ** createdAt **   <a name="Lightsail-Type-RelationalDatabase-createdAt"></a>
The timestamp when the database was created. Formatted in Unix time.
Type: Timestamp
Required: No

 ** engine **   <a name="Lightsail-Type-RelationalDatabase-engine"></a>
The database software (for example, `MySQL`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** engineVersion **   <a name="Lightsail-Type-RelationalDatabase-engineVersion"></a>
The database engine version (for example, `5.7.23`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** hardware **   <a name="Lightsail-Type-RelationalDatabase-hardware"></a>
Describes the hardware of the database.
Type: [RelationalDatabaseHardware](API_RelationalDatabaseHardware.md) object
Required: No

 ** latestRestorableTime **   <a name="Lightsail-Type-RelationalDatabase-latestRestorableTime"></a>
The latest point in time to which the database can be restored. Formatted in Unix time.
Type: Timestamp
Required: No

 ** location **   <a name="Lightsail-Type-RelationalDatabase-location"></a>
The Region name and Availability Zone where the database is located.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** masterDatabaseName **   <a name="Lightsail-Type-RelationalDatabase-masterDatabaseName"></a>
The name of the master database created when the Lightsail database resource is created.
Type: String
Required: No

 ** masterEndpoint **   <a name="Lightsail-Type-RelationalDatabase-masterEndpoint"></a>
The master endpoint for the database.
Type: [RelationalDatabaseEndpoint](API_RelationalDatabaseEndpoint.md) object
Required: No

 ** masterUsername **   <a name="Lightsail-Type-RelationalDatabase-masterUsername"></a>
The master user name of the database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** name **   <a name="Lightsail-Type-RelationalDatabase-name"></a>
The unique name of the database resource in Lightsail.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** parameterApplyStatus **   <a name="Lightsail-Type-RelationalDatabase-parameterApplyStatus"></a>
The status of parameter updates for the database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** pendingMaintenanceActions **   <a name="Lightsail-Type-RelationalDatabase-pendingMaintenanceActions"></a>
Describes the pending maintenance actions for the database.
Type: Array of [PendingMaintenanceAction](API_PendingMaintenanceAction.md) objects
Required: No

 ** pendingModifiedValues **   <a name="Lightsail-Type-RelationalDatabase-pendingModifiedValues"></a>
Describes pending database value modifications.
Type: [PendingModifiedRelationalDatabaseValues](API_PendingModifiedRelationalDatabaseValues.md) object
Required: No

 ** preferredBackupWindow **   <a name="Lightsail-Type-RelationalDatabase-preferredBackupWindow"></a>
The daily time range during which automated backups are created for the database (for example, `16:00-16:30`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** preferredMaintenanceWindow **   <a name="Lightsail-Type-RelationalDatabase-preferredMaintenanceWindow"></a>
The weekly time range during which system maintenance can occur on the database.
In the format `ddd:hh24:mi-ddd:hh24:mi`. For example, `Tue:17:00-Tue:17:30`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** publiclyAccessible **   <a name="Lightsail-Type-RelationalDatabase-publiclyAccessible"></a>
A Boolean value indicating whether the database is publicly accessible.
Type: Boolean
Required: No

 ** relationalDatabaseBlueprintId **   <a name="Lightsail-Type-RelationalDatabase-relationalDatabaseBlueprintId"></a>
The blueprint ID for the database. A blueprint describes the major engine version of a database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** relationalDatabaseBundleId **   <a name="Lightsail-Type-RelationalDatabase-relationalDatabaseBundleId"></a>
The bundle ID for the database. A bundle describes the performance specifications for your database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** resourceType **   <a name="Lightsail-Type-RelationalDatabase-resourceType"></a>
The Lightsail resource type for the database (for example, `RelationalDatabase`).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** secondaryAvailabilityZone **   <a name="Lightsail-Type-RelationalDatabase-secondaryAvailabilityZone"></a>
Describes the secondary Availability Zone of a high availability database.
The secondary database is used for failover support of a high availability database.
Type: String
Required: No

 ** state **   <a name="Lightsail-Type-RelationalDatabase-state"></a>
Describes the current state of the database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** supportCode **   <a name="Lightsail-Type-RelationalDatabase-supportCode"></a>
The support code for the database. Include this code in your email to support when you have questions about a database in Lightsail. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-RelationalDatabase-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_RelationalDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/RelationalDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/RelationalDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/RelationalDatabase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
