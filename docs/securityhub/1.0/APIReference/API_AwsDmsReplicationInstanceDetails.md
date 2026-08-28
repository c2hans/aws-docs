---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDmsReplicationInstanceDetails.html
---

# AwsDmsReplicationInstanceDetails
<a name="API_AwsDmsReplicationInstanceDetails"></a>

 Provides details about an AWS Database Migration Service (AWS DMS) replication instance. DMS uses a replication instance to connect to your source data store, read the source data, and format the data for consumption by the target data store.

## Contents
<a name="API_AwsDmsReplicationInstanceDetails_Contents"></a>

 ** AllocatedStorage **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-AllocatedStorage"></a>
 The amount of storage (in gigabytes) that is allocated for the replication instance.
Type: Integer
Required: No

 ** AutoMinorVersionUpgrade **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-AutoMinorVersionUpgrade"></a>
 Indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window.
Type: Boolean
Required: No

 ** AvailabilityZone **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-AvailabilityZone"></a>
 The Availability Zone that the replication instance is created in. The default value is a random, system-chosen Availability Zone in the endpoint's AWS Region, such as `us-east-1d`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EngineVersion **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-EngineVersion"></a>
 The engine version number of the replication instance. If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-KmsKeyId"></a>
 An AWS KMS key identifier that is used to encrypt the data on the replication instance. If you don't specify a value for the `KmsKeyId` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MultiAZ **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-MultiAZ"></a>
 Specifies whether the replication instance is deployed across multiple Availability Zones (AZs). You can't set the `AvailabilityZone` parameter if the `MultiAZ` parameter is set to `true`.
Type: Boolean
Required: No

 ** PreferredMaintenanceWindow **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-PreferredMaintenanceWindow"></a>
 The maintenance window times for the replication instance. Upgrades to the replication instance are performed during this time.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PubliclyAccessible **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-PubliclyAccessible"></a>
 Specifies the accessibility options for the replication instance. A value of `true` represents an instance with a public IP address. A value of `false` represents an instance with a private IP address. The default value is `true`.
Type: Boolean
Required: No

 ** ReplicationInstanceClass **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-ReplicationInstanceClass"></a>
 The compute and memory capacity of the replication instance as defined for the specified replication instance class.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplicationInstanceIdentifier **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-ReplicationInstanceIdentifier"></a>
 The replication instance identifier.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplicationSubnetGroup **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-ReplicationSubnetGroup"></a>
 The subnet group for the replication instance.
Type: [AwsDmsReplicationInstanceReplicationSubnetGroupDetails](API_AwsDmsReplicationInstanceReplicationSubnetGroupDetails.md) object
Required: No

 ** VpcSecurityGroups **   <a name="securityhub-Type-AwsDmsReplicationInstanceDetails-VpcSecurityGroups"></a>
 The virtual private cloud (VPC) security group for the replication instance.
Type: Array of [AwsDmsReplicationInstanceVpcSecurityGroupsDetails](API_AwsDmsReplicationInstanceVpcSecurityGroupsDetails.md) objects
Required: No

## See Also
<a name="API_AwsDmsReplicationInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDmsReplicationInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDmsReplicationInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDmsReplicationInstanceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
