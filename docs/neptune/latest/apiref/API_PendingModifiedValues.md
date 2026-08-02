---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_PendingModifiedValues.html
---

# PendingModifiedValues
<a name="API_PendingModifiedValues"></a>

This data type is used as a response element in the [ModifyDBInstance](API_ModifyDBInstance.md) action.

## Contents
<a name="API_PendingModifiedValues_Contents"></a>

 ** AllocatedStorage **
 Contains the new `AllocatedStorage` size for the DB instance that will be applied or is currently being applied.
Type: Integer
Required: No

 ** BackupRetentionPeriod **
Specifies the pending number of days for which automated backups are retained.
Type: Integer
Required: No

 ** CACertificateIdentifier **
Specifies the identifier of the CA certificate for the DB instance.
Type: String
Required: No

 ** DBInstanceClass **
 Contains the new `DBInstanceClass` for the DB instance that will be applied or is currently being applied.
Type: String
Required: No

 ** DBInstanceIdentifier **
 Contains the new `DBInstanceIdentifier` for the DB instance that will be applied or is currently being applied.
Type: String
Required: No

 ** DBSubnetGroupName **
The new DB subnet group for the DB instance.
Type: String
Required: No

 ** EngineVersion **
Indicates the database engine version.
Type: String
Required: No

 ** Iops **
Specifies the new Provisioned IOPS value for the DB instance that will be applied or is currently being applied.
Type: Integer
Required: No

 ** LicenseModel **
Not supported by Neptune.
Type: String
Required: No

 ** MasterUserPassword **
Not supported by Neptune.
Type: String
Required: No

 ** MultiAZ **
Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.
Type: Boolean
Required: No

 ** PendingCloudwatchLogsExports **
This `PendingCloudwatchLogsExports` structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.
Type: [PendingCloudwatchLogsExports](API_PendingCloudwatchLogsExports.md) object
Required: No

 ** Port **
Specifies the pending port for the DB instance.
Type: Integer
Required: No

 ** StorageType **
Not applicable. In Neptune the storage type is managed at the DB Cluster level.
Type: String
Required: No

## See Also
<a name="API_PendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/PendingModifiedValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/PendingModifiedValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/PendingModifiedValues)
