---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_CreateDBInstance.html
---

# CreateDBInstance
<a name="API_CreateDBInstance"></a>

Creates a new DB instance.

## Request Parameters
<a name="API_CreateDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AllocatedStorage **
Not supported by Neptune.
Type: Integer
Required: No

 ** AutoMinorVersionUpgrade **
Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window.
Default: `true`
Type: Boolean
Required: No

 ** AvailabilityZone **
 The EC2 Availability Zone that the DB instance is created in
Default: A random, system-chosen Availability Zone in the endpoint's Amazon Region.
 Example: `us-east-1d`
 Constraint: The AvailabilityZone parameter can't be specified if the MultiAZ parameter is set to `true`. The specified Availability Zone must be in the same Amazon Region as the current endpoint.
Type: String
Required: No

 ** BackupRetentionPeriod **
The number of days for which automated backups are retained.
Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see [CreateDBCluster](API_CreateDBCluster.md).
Default: 1
Constraints:
+ Must be a value from 0 to 35
+ Cannot be set to 0 if the DB instance is a source to Read Replicas
Type: Integer
Required: No

 ** CharacterSetName **
 *(Not supported by Neptune)*
Type: String
Required: No

 ** CopyTagsToSnapshot **
True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.
Type: Boolean
Required: No

 ** DBClusterIdentifier **
The identifier of the DB cluster that the instance will belong to.
For information on creating a DB cluster, see [CreateDBCluster](API_CreateDBCluster.md).
Type: String
Type: String
Required: Yes

 ** DBInstanceClass **
The compute and memory capacity of the DB instance, for example, `db.m4.large`. Not all DB instance classes are available in all Amazon Regions.
Type: String
Required: Yes

 ** DBInstanceIdentifier **
The DB instance identifier. This parameter is stored as a lowercase string.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `mydbinstance`
Type: String
Required: Yes

 ** DBName **
Not supported.
Type: String
Required: No

 ** DBParameterGroupName **
The name of the DB parameter group to associate with this DB instance. If this argument is omitted, the default DBParameterGroup for the specified engine is used.
Constraints:
+ Must be 1 to 255 letters, numbers, or hyphens.
+ First character must be a letter
+ Cannot end with a hyphen or contain two consecutive hyphens
Type: String
Required: No

 **DBSecurityGroups.DBSecurityGroupName.N**
A list of DB security groups to associate with this DB instance.
Default: The default DB security group for the database engine.
Type: Array of strings
Required: No

 ** DBSubnetGroupName **
A DB subnet group to associate with this DB instance.
If there is no DB subnet group, then it is a non-VPC DB instance.
Type: String
Required: No

 ** DeletionProtection **
A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled. See [Deleting a DB Instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html).
DB instances in a DB cluster can be deleted even when deletion protection is enabled in their parent DB cluster.
Type: Boolean
Required: No

 ** Domain **
Specify the Active Directory Domain to create the instance in.
Type: String
Required: No

 ** DomainIAMRoleName **
Specify the name of the IAM role to be used when making API calls to the Directory Service.
Type: String
Required: No

 **EnableCloudwatchLogsExports.member.N**
The list of log types that need to be enabled for exporting to CloudWatch Logs.
Type: Array of strings
Required: No

 ** EnableIAMDatabaseAuthentication **
Not supported by Neptune (ignored).
Type: Boolean
Required: No

 ** EnablePerformanceInsights **
 *(Not supported by Neptune)*
Type: Boolean
Required: No

 ** Engine **
The name of the database engine to be used for this instance.
Valid Values: `neptune`
Type: String
Required: Yes

 ** EngineVersion **
The version number of the database engine to use. Currently, setting this parameter has no effect.
Type: String
Required: No

 ** Iops **
The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.
Type: Integer
Required: No

 ** KmsKeyId **
The Amazon KMS key identifier for an encrypted DB instance.
The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB instance with the same Amazon account that owns the KMS encryption key used to encrypt the new DB instance, then you can use the KMS key alias instead of the ARN for the KM encryption key.
Not applicable. The KMS key identifier is managed by the DB cluster. For more information, see [CreateDBCluster](API_CreateDBCluster.md).
If the `StorageEncrypted` parameter is true, and you do not specify a value for the `KmsKeyId` parameter, then Amazon Neptune will use your default encryption key. Amazon KMS creates the default encryption key for your Amazon account. Your Amazon account has a different default encryption key for each Amazon Region.
Type: String
Required: No

 ** LicenseModel **
License model information for this DB instance.
 Valid values: `license-included` \| `bring-your-own-license` \| `general-public-license`
Type: String
Required: No

 ** MasterUsername **
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
Specifies if the DB instance is a Multi-AZ deployment. You can't set the AvailabilityZone parameter if the MultiAZ parameter is set to true.
Type: Boolean
Required: No

 ** OptionGroupName **
 *(Not supported by Neptune)*
Type: String
Required: No

 ** PerformanceInsightsKMSKeyId **
 *(Not supported by Neptune)*
Type: String
Required: No

 ** Port **
The port number on which the database accepts connections.
Not applicable. The port is managed by the DB cluster. For more information, see [CreateDBCluster](API_CreateDBCluster.md).
 Default: `8182`
Type: Integer
Type: Integer
Required: No

 ** PreferredBackupWindow **
 The daily time range during which automated backups are created.
Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see [CreateDBCluster](API_CreateDBCluster.md).
Type: String
Required: No

 ** PreferredMaintenanceWindow **
The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).
 Format: `ddd:hh24:mi-ddd:hh24:mi`
The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week.
Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
Constraints: Minimum 30-minute window.
Type: String
Required: No

 ** PromotionTier **
A value that specifies the order in which an Read Replica is promoted to the primary instance after a failure of the existing primary instance.
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

 ** StorageEncrypted **
Specifies whether the DB instance is encrypted.
Not applicable. The encryption for DB instances is managed by the DB cluster. For more information, see [CreateDBCluster](API_CreateDBCluster.md).
Default: false
Type: Boolean
Required: No

 ** StorageType **
Not applicable. In Neptune the storage type is managed at the DB Cluster level.
Type: String
Required: No

 **Tags.Tag.N**
The tags to assign to the new instance.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TdeCredentialArn **
The ARN from the key store with which to associate the instance for TDE encryption.
Type: String
Required: No

 ** TdeCredentialPassword **
The password for the given ARN from the key store in order to access the device.
Type: String
Required: No

 ** Timezone **
The time zone of the DB instance.
Type: String
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**
A list of EC2 VPC security groups to associate with this DB instance.
Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see [CreateDBCluster](API_CreateDBCluster.md).
Default: The default EC2 VPC security group for the DB subnet group's VPC.
Type: Array of strings
Required: No

## Response Elements
<a name="API_CreateDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **
Contains the details of an Amazon Neptune DB instance.
This data type is used as a response element in the [DescribeDBInstances](API_DescribeDBInstances.md) action.
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_CreateDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationNotFound **
Specified CIDRIP or EC2 security group is not authorized for the specified DB security group.
Neptune may not also be authorized via IAM to perform necessary actions on your behalf.
HTTP Status Code: 404

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** DBInstanceAlreadyExists **
User already has a DB instance with the given identifier.
HTTP Status Code: 400

 ** DBParameterGroupNotFound **
 *DBParameterGroupName* does not refer to an existing DB parameter group.
HTTP Status Code: 404

 ** DBSecurityGroupNotFound **
 *DBSecurityGroupName* does not refer to an existing DB security group.
HTTP Status Code: 404

 ** DBSubnetGroupDoesNotCoverEnoughAZs **
Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.
HTTP Status Code: 400

 ** DBSubnetGroupNotFoundFault **
 *DBSubnetGroupName* does not refer to an existing DB subnet group.
HTTP Status Code: 404

 ** DomainNotFoundFault **
 *Domain* does not refer to an existing Active Directory Domain.
HTTP Status Code: 404

 ** InstanceQuotaExceeded **
Request would result in user exceeding the allowed number of DB instances.
HTTP Status Code: 400

 ** InsufficientDBInstanceCapacity **
Specified DB instance class is not available in the specified Availability Zone.
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

 ** InvalidSubnet **
The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **
DB subnet group does not cover all Availability Zones after it is created because users' change.
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
Error accessing KMS key.
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
<a name="API_CreateDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/CreateDBInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/CreateDBInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/CreateDBInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/CreateDBInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/CreateDBInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/CreateDBInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/CreateDBInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/CreateDBInstance)
