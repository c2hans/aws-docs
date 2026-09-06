---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ReplicationConfigurationTemplate.html
---

# ReplicationConfigurationTemplate
<a name="API_ReplicationConfigurationTemplate"></a>

## Contents
<a name="API_ReplicationConfigurationTemplate_Contents"></a>

 ** replicationConfigurationTemplateID **   <a name="mgn-Type-ReplicationConfigurationTemplate-replicationConfigurationTemplateID"></a>
Replication Configuration template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rct-[0-9a-zA-Z]{17}`
Required: Yes

 ** arn **   <a name="mgn-Type-ReplicationConfigurationTemplate-arn"></a>
Replication Configuration template ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** associateDefaultSecurityGroup **   <a name="mgn-Type-ReplicationConfigurationTemplate-associateDefaultSecurityGroup"></a>
Replication Configuration template associate default Application Migration Service Security group.
Type: Boolean
Required: No

 ** bandwidthThrottling **   <a name="mgn-Type-ReplicationConfigurationTemplate-bandwidthThrottling"></a>
Replication Configuration template bandwidth throttling.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** createPublicIP **   <a name="mgn-Type-ReplicationConfigurationTemplate-createPublicIP"></a>
Replication Configuration template create Public IP.
Type: Boolean
Required: No

 ** dataPlaneRouting **   <a name="mgn-Type-ReplicationConfigurationTemplate-dataPlaneRouting"></a>
Replication Configuration template data plane routing.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`
Required: No

 ** defaultLargeStagingDiskType **   <a name="mgn-Type-ReplicationConfigurationTemplate-defaultLargeStagingDiskType"></a>
Replication Configuration template use default large Staging Disk type.
Type: String
Valid Values: `GP2 | ST1 | GP3`
Required: No

 ** ebsEncryption **   <a name="mgn-Type-ReplicationConfigurationTemplate-ebsEncryption"></a>
Replication Configuration template EBS encryption.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: No

 ** ebsEncryptionKeyArn **   <a name="mgn-Type-ReplicationConfigurationTemplate-ebsEncryptionKeyArn"></a>
Replication Configuration template EBS encryption key ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** internetProtocol **   <a name="mgn-Type-ReplicationConfigurationTemplate-internetProtocol"></a>
Replication Configuration template internet protocol.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** replicationServerInstanceType **   <a name="mgn-Type-ReplicationConfigurationTemplate-replicationServerInstanceType"></a>
Replication Configuration template server instance type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** replicationServersSecurityGroupsIDs **   <a name="mgn-Type-ReplicationConfigurationTemplate-replicationServersSecurityGroupsIDs"></a>
Replication Configuration template server Security Groups IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`
Required: No

 ** stagingAreaSubnetId **   <a name="mgn-Type-ReplicationConfigurationTemplate-stagingAreaSubnetId"></a>
Replication Configuration template Staging Area subnet ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`
Required: No

 ** stagingAreaTags **   <a name="mgn-Type-ReplicationConfigurationTemplate-stagingAreaTags"></a>
Replication Configuration template Staging Area Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** storageConfiguration **   <a name="mgn-Type-ReplicationConfigurationTemplate-storageConfiguration"></a>
Replication Configuration template storage configuration.
Type: [StorageConfiguration](API_StorageConfiguration.md) object
Required: No

 ** storeSnapshotOnLocalZone **   <a name="mgn-Type-ReplicationConfigurationTemplate-storeSnapshotOnLocalZone"></a>
Replication Configuration template store snapshot on local zone.
Type: Boolean
Required: No

 ** tags **   <a name="mgn-Type-ReplicationConfigurationTemplate-tags"></a>
Replication Configuration template Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** useDedicatedReplicationServer **   <a name="mgn-Type-ReplicationConfigurationTemplate-useDedicatedReplicationServer"></a>
Replication Configuration template use Dedicated Replication Server.
Type: Boolean
Required: No

 ** useFipsEndpoint **   <a name="mgn-Type-ReplicationConfigurationTemplate-useFipsEndpoint"></a>
Replication Configuration template use Fips Endpoint.
Type: Boolean
Required: No

## See Also
<a name="API_ReplicationConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ReplicationConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ReplicationConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ReplicationConfigurationTemplate)
