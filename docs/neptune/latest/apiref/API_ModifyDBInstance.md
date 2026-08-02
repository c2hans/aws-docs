---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ModifyDBInstance.html
---

# ModifyDBInstance
<a name="API_ModifyDBInstance"></a>

Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. To learn what modifications you can make to your DB instance, call [DescribeValidDBInstanceModifications](API_DescribeValidDBInstanceModifications.md) before you call [ModifyDBInstance](#API_ModifyDBInstance).

## Request Parameters
<a name="API_ModifyDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AllocatedStorage **
Not supported by Neptune.
Type: Integer
Required: No

 ** AllowMajorVersionUpgrade **
Indicates that major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.
Type: Boolean
Required: No

 ** ApplyImmediately **
Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the DB instance.
 If this parameter is set to `false`, changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to [RebootDBInstance](API_RebootDBInstance.md), or the next failure reboot.
Default: `false`
Type: Boolean
Required: No

 ** AutoMinorVersionUpgrade **
 Indicates that minor version upgrades are applied automatically to the DB instance during the maintenance window. Changing this parameter doesn't result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to `true` during the maintenance window, and a newer minor version is available, and Neptune has enabled auto patching for that engine version.
Type: Boolean
Required: No

 ** BackupRetentionPeriod **
Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see [ModifyDBCluster](API_ModifyDBCluster.md).
Default: Uses existing setting
Type: Integer
Required: No

 ** CACertificateIdentifier **
Indicates the certificate that needs to be associated with the instance.
Type: String
Required: No

 ** CloudwatchLogsExportConfiguration **
The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB instance or DB cluster.
Type: [CloudwatchLogsExportConfiguration](API_CloudwatchLogsExportConfiguration.md) object
Required: No

 ** CopyTagsToSnapshot **
True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.
Type: Boolean
Required: No

 ** DBInstanceClass **
The new compute and memory capacity of the DB instance, for example, `db.m4.large`. Not all DB instance classes are available in all Amazon Regions.
If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless `ApplyImmediately` is specified as `true` for this request.
Default: Uses existing setting
Type: String
Required: No

 ** DBInstanceIdentifier **
The DB instance identifier. This value is stored as a lowercase string.
Constraints:
+ Must match the identifier of an existing DBInstance.
Type: String
Required: Yes

 ** DBParameterGroupName **
The name of the DB parameter group to apply to the DB instance. Changing this setting doesn't result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. The db instance will NOT be rebooted automatically and the parameter changes will NOT be applied during the next maintenance window.
Default: Uses existing setting
Constraints: The DB parameter group must be in the same DB parameter group family as this DB instance.
Type: String
Required: No

 ** DBPortNumber **
The port number on which the database accepts connections.
The value of the `DBPortNumber` parameter must not match any of the port values specified for options in the option group for the DB instance.
Your database will restart when you change the `DBPortNumber` value regardless of the value of the `ApplyImmediately` parameter.
 Default: `8182`
Type: Integer
Required: No

 **DBSecurityGroups.DBSecurityGroupName.N**
A list of DB security groups to authorize on this DB instance. Changing this setting doesn't result in an outage and the change is asynchronously applied as soon as possible.
Constraints:
+ If supplied, must match existing DBSecurityGroups.
Type: Array of strings
Required: No

 ** DBSubnetGroupName **
The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC.
Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you specify `true` for the `ApplyImmediately` parameter.
Constraints: If supplied, must match the name of an existing DBSubnetGroup.
Example: `mySubnetGroup`
Type: String
Required: No

 ** DeletionProtection **
A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled. See [Deleting a DB Instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html).
Type: Boolean
Required: No

 ** Domain **
Not supported.
Type: String
Required: No

 ** DomainIAMRoleName **
Not supported
Type: String
Required: No

 ** EnableIAMDatabaseAuthentication **
True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
You can enable IAM database authentication for the following database engines
Not applicable. Mapping Amazon IAM accounts to database accounts is managed by the DB cluster. For more information, see [ModifyDBCluster](API_ModifyDBCluster.md).
Default: `false`
Type: Boolean
Required: No

 ** EnablePerformanceInsights **
 *(Not supported by Neptune)*
Type: Boolean
Required: No

 ** EngineVersion **
The version number of the database engine to upgrade to. Currently, setting this parameter has no effect. To upgrade your database engine to the most recent release, use the [ApplyPendingMaintenanceAction](API_ApplyPendingMaintenanceAction.md) API.
Type: String
Required: No

 ** Iops **
The new Provisioned IOPS (I/O operations per second) value for the instance.
Changing this setting doesn't result in an outage and the change is applied during the next maintenance window unless the `ApplyImmediately` parameter is set to `true` for this request.
Default: Uses existing setting
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

 ** MonitoringInterval **
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
If `MonitoringRoleArn` is specified, then you must also set `MonitoringInterval` to a value other than 0.
Valid Values: `0, 1, 5, 10, 15, 30, 60`
Type: Integer
Required: No

 ** MonitoringRoleArn **
The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess`.
If `MonitoringInterval` is set to a value other than 0, then you must supply a `MonitoringRoleArn` value.
Type: String
Required: No

 ** MultiAZ **
Specifies if the DB instance is a Multi-AZ deployment. Changing this parameter doesn't result in an outage and the change is applied during the next maintenance window unless the `ApplyImmediately` parameter is set to `true` for this request.
Type: Boolean
Required: No

 ** NewDBInstanceIdentifier **
 The new DB instance identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot will occur immediately if you set `Apply Immediately` to true, or will occur during the next maintenance window if `Apply Immediately` to false. This value is stored as a lowercase string.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `mydbinstance`
Type: String
Required: No

 ** OptionGroupName **
 *(Not supported by Neptune)*
Type: String
Required: No

 ** PerformanceInsightsKMSKeyId **
 *(Not supported by Neptune)*
Type: String
Required: No

 ** PreferredBackupWindow **
 The daily time range during which automated backups are created if automated backups are enabled.
Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see [ModifyDBCluster](API_ModifyDBCluster.md).
Constraints:
+ Must be in the format hh24:mi-hh24:mi
+ Must be in Universal Time Coordinated (UTC)
+ Must not conflict with the preferred maintenance window
+ Must be at least 30 minutes
Type: String
Required: No

 ** PreferredMaintenanceWindow **
The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn't result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter will cause a reboot of the DB instance. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.
Default: Uses existing setting
Format: ddd:hh24:mi-ddd:hh24:mi
Valid Days: Mon \| Tue \| Wed \| Thu \| Fri \| Sat \| Sun
Constraints: Must be at least 30 minutes
Type: String
Required: No

 ** PromotionTier **
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.
Default: 1
Valid Values: 0 - 15
Type: Integer
Required: No

 ** PubliclyAccessible **
Indicates whether the DB instance is publicly accessible.
When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.
When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.
Type: Boolean
Required: No

 ** StorageType **
Not applicable. In Neptune the storage type is managed at the DB Cluster level.
Type: String
Required: No

 ** TdeCredentialArn **
The ARN from the key store with which to associate the instance for TDE encryption.
Type: String
Required: No

 ** TdeCredentialPassword **
The password for the given ARN from the key store in order to access the device.
Type: String
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**
A list of EC2 VPC security groups to authorize on this DB instance. This change is asynchronously applied as soon as possible.
Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see [ModifyDBCluster](API_ModifyDBCluster.md).
Constraints:
+ If supplied, must match existing VpcSecurityGroupIds.
Type: Array of strings
Required: No

## Response Elements
<a name="API_ModifyDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **
Contains the details of an Amazon Neptune DB instance.
This data type is used as a response element in the [DescribeDBInstances](API_DescribeDBInstances.md) action.
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_ModifyDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationNotFound **
Specified CIDRIP or EC2 security group is not authorized for the specified DB security group.
Neptune may not also be authorized via IAM to perform necessary actions on your behalf.
HTTP Status Code: 404

 ** CertificateNotFound **
 *CertificateIdentifier* does not refer to an existing certificate.
HTTP Status Code: 404

 ** DBInstanceAlreadyExists **
User already has a DB instance with the given identifier.
HTTP Status Code: 400

 ** DBInstanceNotFound **
 *DBInstanceIdentifier* does not refer to an existing DB instance.
HTTP Status Code: 404

 ** DBParameterGroupNotFound **
 *DBParameterGroupName* does not refer to an existing DB parameter group.
HTTP Status Code: 404

 ** DBSecurityGroupNotFound **
 *DBSecurityGroupName* does not refer to an existing DB security group.
HTTP Status Code: 404

 ** DBUpgradeDependencyFailure **
The DB upgrade failed because a resource the DB depends on could not be modified.
HTTP Status Code: 400

 ** DomainNotFoundFault **
 *Domain* does not refer to an existing Active Directory Domain.
HTTP Status Code: 404

 ** InsufficientDBInstanceCapacity **
Specified DB instance class is not available in the specified Availability Zone.
HTTP Status Code: 400

 ** InvalidDBInstanceState **
The specified DB instance is not in the *available* state.
HTTP Status Code: 400

 ** InvalidDBSecurityGroupState **
The state of the DB security group does not allow deletion.
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **
DB subnet group does not cover all Availability Zones after it is created because users' change.
HTTP Status Code: 400

 ** OptionGroupNotFoundFault **
The designated option group could not be found.
HTTP Status Code: 404

 ** ProvisionedIopsNotAvailableInAZFault **
Provisioned IOPS not available in the specified Availability Zone.
HTTP Status Code: 400

 ** StorageQuotaExceeded **
Request would result in user exceeding the allowed amount of storage available across all DB instances.
HTTP Status Code: 400

 ** StorageTypeNotSupported **
 *StorageType* specified cannot be associated with the DB Instance.
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/ModifyDBInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/ModifyDBInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ModifyDBInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/ModifyDBInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ModifyDBInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/ModifyDBInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/ModifyDBInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/ModifyDBInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ModifyDBInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ModifyDBInstance)
