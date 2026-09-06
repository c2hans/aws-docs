---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationInstance.html
---

# ReplicationInstance
<a name="API_ReplicationInstance"></a>

Provides information that defines a replication instance.

## Contents
<a name="API_ReplicationInstance_Contents"></a>

 ** AllocatedStorage **   <a name="DMS-Type-ReplicationInstance-AllocatedStorage"></a>
The amount of storage (in gigabytes) that is allocated for the replication instance.
Type: Integer
Required: No

 ** AutoMinorVersionUpgrade **   <a name="DMS-Type-ReplicationInstance-AutoMinorVersionUpgrade"></a>
Boolean value indicating if minor version upgrades will be automatically applied to the instance.
Type: Boolean
Required: No

 ** AvailabilityZone **   <a name="DMS-Type-ReplicationInstance-AvailabilityZone"></a>
The Availability Zone for the instance.
Type: String
Required: No

 ** DnsNameServers **   <a name="DMS-Type-ReplicationInstance-DnsNameServers"></a>
The DNS name servers supported for the replication instance to access your on-premise source or target database.
Type: String
Required: No

 ** EngineVersion **   <a name="DMS-Type-ReplicationInstance-EngineVersion"></a>
The engine version number of the replication instance.
If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.
When modifying a major engine version of an instance, also set `AllowMajorVersionUpgrade` to `true`.
Type: String
Required: No

 ** FreeUntil **   <a name="DMS-Type-ReplicationInstance-FreeUntil"></a>
 The expiration date of the free replication instance that is part of the Free DMS program.
Type: Timestamp
Required: No

 ** InstanceCreateTime **   <a name="DMS-Type-ReplicationInstance-InstanceCreateTime"></a>
The time the replication instance was created.
Type: Timestamp
Required: No

 ** KerberosAuthenticationSettings **   <a name="DMS-Type-ReplicationInstance-KerberosAuthenticationSettings"></a>
Specifies the settings required for kerberos authentication when replicating an instance.
Type: [KerberosAuthenticationSettings](API_KerberosAuthenticationSettings.md) object
Required: No

 ** KmsKeyId **   <a name="DMS-Type-ReplicationInstance-KmsKeyId"></a>
An AWS KMS key identifier that is used to encrypt the data on the replication instance.
If you don't specify a value for the `KmsKeyId` parameter, then AWS DMS uses your default encryption key.
 AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Required: No

 ** MultiAZ **   <a name="DMS-Type-ReplicationInstance-MultiAZ"></a>
 Specifies whether the replication instance is a Multi-AZ deployment. You can't set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to `true`.
Type: Boolean
Required: No

 ** NetworkType **   <a name="DMS-Type-ReplicationInstance-NetworkType"></a>
The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.
Type: String
Required: No

 ** PendingModifiedValues **   <a name="DMS-Type-ReplicationInstance-PendingModifiedValues"></a>
The pending modification values.
Type: [ReplicationPendingModifiedValues](API_ReplicationPendingModifiedValues.md) object
Required: No

 ** PreferredMaintenanceWindow **   <a name="DMS-Type-ReplicationInstance-PreferredMaintenanceWindow"></a>
The maintenance window times for the replication instance. Any pending upgrades to the replication instance are performed during this time.
Type: String
Required: No

 ** PubliclyAccessible **   <a name="DMS-Type-ReplicationInstance-PubliclyAccessible"></a>
 Specifies the accessibility options for the replication instance. A value of `true` represents an instance with a public IP address. A value of `false` represents an instance with a private IP address. The default value is `true`.
Type: Boolean
Required: No

 ** ReplicationInstanceArn **   <a name="DMS-Type-ReplicationInstance-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the replication instance.
Type: String
Required: No

 ** ReplicationInstanceClass **   <a name="DMS-Type-ReplicationInstance-ReplicationInstanceClass"></a>
The compute and memory capacity of the replication instance as defined for the specified replication instance class. It is a required parameter, although a default value is pre-selected in the DMS console.
For more information on the settings and capacities for the available replication instance classes, see [ Selecting the right AWS DMS replication instance for your migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth).
Type: String
Length Constraints: Maximum length of 30.
Required: No

 ** ReplicationInstanceIdentifier **   <a name="DMS-Type-ReplicationInstance-ReplicationInstanceIdentifier"></a>
The replication instance identifier is a required parameter. This parameter is stored as a lowercase string.
Constraints:
+ Must contain 1-63 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `myrepinstance`
Type: String
Required: No

 ** ReplicationInstanceIpv6Addresses **   <a name="DMS-Type-ReplicationInstance-ReplicationInstanceIpv6Addresses"></a>
One or more IPv6 addresses for the replication instance.
Type: Array of strings
Required: No

 ** ReplicationInstancePrivateIpAddress **   <a name="DMS-Type-ReplicationInstance-ReplicationInstancePrivateIpAddress"></a>
 *This member has been deprecated.*
The private IP address of the replication instance.
Type: String
Required: No

 ** ReplicationInstancePrivateIpAddresses **   <a name="DMS-Type-ReplicationInstance-ReplicationInstancePrivateIpAddresses"></a>
One or more private IP addresses for the replication instance.
Type: Array of strings
Required: No

 ** ReplicationInstancePublicIpAddress **   <a name="DMS-Type-ReplicationInstance-ReplicationInstancePublicIpAddress"></a>
 *This member has been deprecated.*
The public IP address of the replication instance.
Type: String
Required: No

 ** ReplicationInstancePublicIpAddresses **   <a name="DMS-Type-ReplicationInstance-ReplicationInstancePublicIpAddresses"></a>
One or more public IP addresses for the replication instance.
Type: Array of strings
Required: No

 ** ReplicationInstanceStatus **   <a name="DMS-Type-ReplicationInstance-ReplicationInstanceStatus"></a>
The status of the replication instance. The possible return values include:
+  `"available"`
+  `"creating"`
+  `"deleted"`
+  `"deleting"`
+  `"failed"`
+  `"modifying"`
+  `"upgrading"`
+  `"rebooting"`
+  `"resetting-master-credentials"`
+  `"storage-full"`
+  `"incompatible-credentials"`
+  `"incompatible-network"`
+  `"maintenance"`
Type: String
Required: No

 ** ReplicationSubnetGroup **   <a name="DMS-Type-ReplicationInstance-ReplicationSubnetGroup"></a>
The subnet group for the replication instance.
Type: [ReplicationSubnetGroup](API_ReplicationSubnetGroup.md) object
Required: No

 ** SecondaryAvailabilityZone **   <a name="DMS-Type-ReplicationInstance-SecondaryAvailabilityZone"></a>
The Availability Zone of the standby replication instance in a Multi-AZ deployment.
Type: String
Required: No

 ** VpcSecurityGroups **   <a name="DMS-Type-ReplicationInstance-VpcSecurityGroups"></a>
The VPC security group for the instance.
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects
Required: No

## See Also
<a name="API_ReplicationInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationInstance)
