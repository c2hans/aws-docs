---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationSubnetGroup.html
---

# ReplicationSubnetGroup
<a name="API_ReplicationSubnetGroup"></a>

Describes a subnet group in response to a request by the `DescribeReplicationSubnetGroups` operation.

## Contents
<a name="API_ReplicationSubnetGroup_Contents"></a>

 ** IsReadOnly **   <a name="DMS-Type-ReplicationSubnetGroup-IsReadOnly"></a>
Indicates whether the replication subnet group is read-only. When set to `true`, this subnet group is managed by AWS DMS as part of a zero-ETL integration and cannot be modified or deleted directly. You can only modify or delete read-only subnet groups through their associated zero-ETL integration.
Type: Boolean
Required: No

 ** ReplicationSubnetGroupDescription **   <a name="DMS-Type-ReplicationSubnetGroup-ReplicationSubnetGroupDescription"></a>
A description for the replication subnet group.
Type: String
Required: No

 ** ReplicationSubnetGroupIdentifier **   <a name="DMS-Type-ReplicationSubnetGroup-ReplicationSubnetGroupIdentifier"></a>
The identifier of the replication instance subnet group.
Type: String
Required: No

 ** SubnetGroupStatus **   <a name="DMS-Type-ReplicationSubnetGroup-SubnetGroupStatus"></a>
The status of the subnet group.
Type: String
Required: No

 ** Subnets **   <a name="DMS-Type-ReplicationSubnetGroup-Subnets"></a>
The subnets that are in the subnet group.
Type: Array of [Subnet](API_Subnet.md) objects
Required: No

 ** SupportedNetworkTypes **   <a name="DMS-Type-ReplicationSubnetGroup-SupportedNetworkTypes"></a>
The IP addressing protocol supported by the subnet group. This is used by a replication instance with values such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.
Type: Array of strings
Required: No

 ** VpcId **   <a name="DMS-Type-ReplicationSubnetGroup-VpcId"></a>
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_ReplicationSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationSubnetGroup)
