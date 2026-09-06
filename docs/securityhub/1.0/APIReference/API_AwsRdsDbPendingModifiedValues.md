---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbPendingModifiedValues.html
---

# AwsRdsDbPendingModifiedValues
<a name="API_AwsRdsDbPendingModifiedValues"></a>

Changes to a DB instance that are currently pending.

## Contents
<a name="API_AwsRdsDbPendingModifiedValues_Contents"></a>

 ** AllocatedStorage **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-AllocatedStorage"></a>
The new value of the allocated storage for the DB instance.
Type: Integer
Required: No

 ** BackupRetentionPeriod **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-BackupRetentionPeriod"></a>
The new backup retention period for the DB instance.
Type: Integer
Required: No

 ** CaCertificateIdentifier **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-CaCertificateIdentifier"></a>
The new CA certificate identifier for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbInstanceClass **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-DbInstanceClass"></a>
The new DB instance class for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbInstanceIdentifier **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-DbInstanceIdentifier"></a>
The new DB instance identifier for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbSubnetGroupName **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-DbSubnetGroupName"></a>
The name of the new subnet group for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EngineVersion **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-EngineVersion"></a>
The new engine version for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Iops **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-Iops"></a>
The new provisioned IOPS value for the DB instance.
Type: Integer
Required: No

 ** LicenseModel **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-LicenseModel"></a>
The new license model value for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MasterUserPassword **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-MasterUserPassword"></a>
The new master user password for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MultiAZ **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-MultiAZ"></a>
Indicates that a single Availability Zone DB instance is changing to a multiple Availability Zone deployment.
Type: Boolean
Required: No

 ** PendingCloudWatchLogsExports **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-PendingCloudWatchLogsExports"></a>
A list of log types that are being enabled or disabled.
Type: [AwsRdsPendingCloudWatchLogsExports](API_AwsRdsPendingCloudWatchLogsExports.md) object
Required: No

 ** Port **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-Port"></a>
The new port for the DB instance.
Type: Integer
Required: No

 ** ProcessorFeatures **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-ProcessorFeatures"></a>
Processor features that are being updated.
Type: Array of [AwsRdsDbProcessorFeature](API_AwsRdsDbProcessorFeature.md) objects
Required: No

 ** StorageType **   <a name="securityhub-Type-AwsRdsDbPendingModifiedValues-StorageType"></a>
The new storage type for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbPendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbPendingModifiedValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbPendingModifiedValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbPendingModifiedValues)
