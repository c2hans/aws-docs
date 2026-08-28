---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PendingModifiedValues.html
---

# PendingModifiedValues
<a name="API_PendingModifiedValues"></a>

This data type is used as a response element in the `ModifyDBInstance` operation and contains changes that will be applied during the next maintenance window.

## Contents
<a name="API_PendingModifiedValues_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdditionalStorageVolumes.member.N **
The additional storage volume modifications that are pending for the DB instance.
Type: Array of [AdditionalStorageVolume](API_AdditionalStorageVolume.md) objects
Required: No

 ** AllocatedStorage **
The allocated storage size for the DB instance specified in gibibytes (GiB).
Type: Integer
Required: No

 ** AutomationMode **
The automation mode of the RDS Custom DB instance: `full` or `all-paused`. If `full`, the DB instance automates monitoring and instance recovery. If `all-paused`, the instance pauses automation for the duration set by `--resume-full-automation-mode-minutes`.
Type: String
Valid Values: `full | all-paused`
Required: No

 ** BackupRetentionPeriod **
The number of days for which automated backups are retained.
Type: Integer
Required: No

 ** CACertificateIdentifier **
The identifier of the CA certificate for the DB instance.
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.
Type: String
Required: No

 ** DBInstanceClass **
The name of the compute and memory capacity class for the DB instance.
Type: String
Required: No

 ** DBInstanceIdentifier **
The database identifier for the DB instance.
Type: String
Required: No

 ** DBSubnetGroupName **
The DB subnet group for the DB instance.
Type: String
Required: No

 ** DedicatedLogVolume **
Indicates whether the DB instance has a dedicated log volume (DLV) enabled.>
Type: Boolean
Required: No

 ** Engine **
The database engine of the DB instance.
Type: String
Required: No

 ** EngineVersion **
The database engine version.
Type: String
Required: No

 ** IAMDatabaseAuthenticationEnabled **
Indicates whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.
Type: Boolean
Required: No

 ** Iops **
The Provisioned IOPS value for the DB instance.
Type: Integer
Required: No

 ** LicenseModel **
The license model for the DB instance.
Valid values: `license-included` \| `bring-your-own-license` \| `general-public-license` \| `bring-your-own-media`
Type: String
Required: No

 ** MasterUserPassword **
The master credentials for the DB instance.
Type: String
Required: No

 ** MultiAZ **
Indicates whether the Single-AZ DB instance will change to a Multi-AZ deployment.
Type: Boolean
Required: No

 ** MultiTenant **
Indicates whether the DB instance will change to the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).
Type: Boolean
Required: No

 ** PendingCloudwatchLogsExports **
A list of the log types whose configuration is still pending. In other words, these log types are in the process of being activated or deactivated.
Type: [PendingCloudwatchLogsExports](API_PendingCloudwatchLogsExports.md) object
Required: No

 ** Port **
The port for the DB instance.
Type: Integer
Required: No

 ** ProcessorFeatures.ProcessorFeature.N **
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
Type: Array of [ProcessorFeature](API_ProcessorFeature.md) objects
Required: No

 ** ResumeFullAutomationModeTime **
The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation. The minimum value is 60 (default). The maximum value is 1,440.
Type: Timestamp
Required: No

 ** StorageThroughput **
The storage throughput of the DB instance.
Type: Integer
Required: No

 ** StorageType **
The storage type of the DB instance.
Type: String
Required: No

## See Also
<a name="API_PendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/PendingModifiedValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/PendingModifiedValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/PendingModifiedValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
