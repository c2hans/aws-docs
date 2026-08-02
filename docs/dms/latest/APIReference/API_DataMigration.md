---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DataMigration.html
---

# DataMigration
<a name="API_DataMigration"></a>

This object provides information about a AWS DMS data migration.

## Contents
<a name="API_DataMigration_Contents"></a>

 ** DataMigrationArn **   <a name="DMS-Type-DataMigration-DataMigrationArn"></a>
The Amazon Resource Name (ARN) that identifies this replication.
Type: String
Required: No

 ** DataMigrationCidrBlocks **   <a name="DMS-Type-DataMigration-DataMigrationCidrBlocks"></a>
The CIDR blocks of the endpoints for the data migration.
Type: Array of strings
Required: No

 ** DataMigrationCreateTime **   <a name="DMS-Type-DataMigration-DataMigrationCreateTime"></a>
The UTC time when DMS created the data migration.
Type: Timestamp
Required: No

 ** DataMigrationEndTime **   <a name="DMS-Type-DataMigration-DataMigrationEndTime"></a>
The UTC time when data migration ended.
Type: Timestamp
Required: No

 ** DataMigrationName **   <a name="DMS-Type-DataMigration-DataMigrationName"></a>
The user-friendly name for the data migration.
Type: String
Required: No

 ** DataMigrationSettings **   <a name="DMS-Type-DataMigration-DataMigrationSettings"></a>
Specifies CloudWatch settings and selection rules for the data migration.
Type: [DataMigrationSettings](API_DataMigrationSettings.md) object
Required: No

 ** DataMigrationStartTime **   <a name="DMS-Type-DataMigration-DataMigrationStartTime"></a>
The UTC time when DMS started the data migration.
Type: Timestamp
Required: No

 ** DataMigrationStatistics **   <a name="DMS-Type-DataMigration-DataMigrationStatistics"></a>
Provides information about the data migration's run, including start and stop time, latency, and data migration progress.
Type: [DataMigrationStatistics](API_DataMigrationStatistics.md) object
Required: No

 ** DataMigrationStatus **   <a name="DMS-Type-DataMigration-DataMigrationStatus"></a>
The current status of the data migration.
Type: String
Required: No

 ** DataMigrationType **   <a name="DMS-Type-DataMigration-DataMigrationType"></a>
Specifies whether the data migration is full-load only, change data capture (CDC) only, or full-load and CDC.
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: No

 ** LastFailureMessage **   <a name="DMS-Type-DataMigration-LastFailureMessage"></a>
Information about the data migration's most recent error or failure.
Type: String
Required: No

 ** MigrationProjectArn **   <a name="DMS-Type-DataMigration-MigrationProjectArn"></a>
The Amazon Resource Name (ARN) of the data migration's associated migration project.
Type: String
Required: No

 ** PublicIpAddresses **   <a name="DMS-Type-DataMigration-PublicIpAddresses"></a>
The IP addresses of the endpoints for the data migration.
Type: Array of strings
Required: No

 ** ServiceAccessRoleArn **   <a name="DMS-Type-DataMigration-ServiceAccessRoleArn"></a>
The IAM role that the data migration uses to access AWS resources.
Type: String
Required: No

 ** SourceDataSettings **   <a name="DMS-Type-DataMigration-SourceDataSettings"></a>
Specifies information about the data migration's source data provider.
Type: Array of [SourceDataSetting](API_SourceDataSetting.md) objects
Required: No

 ** StopReason **   <a name="DMS-Type-DataMigration-StopReason"></a>
The reason the data migration last stopped.
Type: String
Required: No

 ** TargetDataSettings **   <a name="DMS-Type-DataMigration-TargetDataSettings"></a>
Specifies information about the data migration's target data provider.
Type: Array of [TargetDataSetting](API_TargetDataSetting.md) objects
Required: No

## See Also
<a name="API_DataMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DataMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DataMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DataMigration)
