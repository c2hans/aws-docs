---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ReplicationConfigurationTemplate.html
---

# ReplicationConfigurationTemplate
<a name="API_ReplicationConfigurationTemplate"></a>

## Contents
<a name="API_ReplicationConfigurationTemplate_Contents"></a>

 ** replicationConfigurationTemplateID **   <a name="drs-Type-ReplicationConfigurationTemplate-replicationConfigurationTemplateID"></a>
The Replication Configuration Template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rct-[0-9a-zA-Z]{17}`
Required: Yes

 ** arn **   <a name="drs-Type-ReplicationConfigurationTemplate-arn"></a>
The Replication Configuration Template ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** associateDefaultSecurityGroup **   <a name="drs-Type-ReplicationConfigurationTemplate-associateDefaultSecurityGroup"></a>
Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.
Type: Boolean
Required: No

 ** autoReplicateNewDisks **   <a name="drs-Type-ReplicationConfigurationTemplate-autoReplicateNewDisks"></a>
Whether to allow the AWS replication agent to automatically replicate newly added disks.
Type: Boolean
Required: No

 ** bandwidthThrottling **   <a name="drs-Type-ReplicationConfigurationTemplate-bandwidthThrottling"></a>
Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** createPublicIP **   <a name="drs-Type-ReplicationConfigurationTemplate-createPublicIP"></a>
Whether to create a Public IP for the Recovery Instance by default.
Type: Boolean
Required: No

 ** dataPlaneRouting **   <a name="drs-Type-ReplicationConfigurationTemplate-dataPlaneRouting"></a>
The data plane routing mechanism that will be used for replication.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`
Required: No

 ** defaultLargeStagingDiskType **   <a name="drs-Type-ReplicationConfigurationTemplate-defaultLargeStagingDiskType"></a>
The Staging Disk EBS volume type to be used during replication.
Type: String
Valid Values: `GP2 | GP3 | ST1 | AUTO`
Required: No

 ** ebsEncryption **   <a name="drs-Type-ReplicationConfigurationTemplate-ebsEncryption"></a>
The type of EBS encryption to be used during replication.
Type: String
Valid Values: `DEFAULT | CUSTOM | NONE`
Required: No

 ** ebsEncryptionKeyArn **   <a name="drs-Type-ReplicationConfigurationTemplate-ebsEncryptionKeyArn"></a>
The ARN of the EBS encryption key to be used during replication.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** internetProtocol **   <a name="drs-Type-ReplicationConfigurationTemplate-internetProtocol"></a>
Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** pitPolicy **   <a name="drs-Type-ReplicationConfigurationTemplate-pitPolicy"></a>
The Point in time (PIT) policy to manage snapshots taken during replication.
Type: Array of [PITPolicyRule](API_PITPolicyRule.md) objects
Array Members: Fixed number of 3 items.
Required: No

 ** replicationServerInstanceType **   <a name="drs-Type-ReplicationConfigurationTemplate-replicationServerInstanceType"></a>
The instance type to be used for the replication server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** replicationServersSecurityGroupsIDs **   <a name="drs-Type-ReplicationConfigurationTemplate-replicationServersSecurityGroupsIDs"></a>
The security group IDs that will be used by the replication server.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`
Required: No

 ** stagingAreaSubnetId **   <a name="drs-Type-ReplicationConfigurationTemplate-stagingAreaSubnetId"></a>
The subnet to be used by the replication staging area.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`
Required: No

 ** stagingAreaTags **   <a name="drs-Type-ReplicationConfigurationTemplate-stagingAreaTags"></a>
A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** tags **   <a name="drs-Type-ReplicationConfigurationTemplate-tags"></a>
A set of tags to be associated with the Replication Configuration Template resource.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** useDedicatedReplicationServer **   <a name="drs-Type-ReplicationConfigurationTemplate-useDedicatedReplicationServer"></a>
Whether to use a dedicated Replication Server in the replication staging area.
Type: Boolean
Required: No

## See Also
<a name="API_ReplicationConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ReplicationConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ReplicationConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ReplicationConfigurationTemplate)
