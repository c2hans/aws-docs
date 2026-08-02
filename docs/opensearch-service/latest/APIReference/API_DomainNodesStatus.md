---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DomainNodesStatus.html
---

# DomainNodesStatus
<a name="API_DomainNodesStatus"></a>

Container for information about nodes on the domain.

## Contents
<a name="API_DomainNodesStatus_Contents"></a>

 ** AvailabilityZone **   <a name="opensearchservice-Type-DomainNodesStatus-AvailabilityZone"></a>
The Availability Zone of the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Required: No

 ** InstanceType **   <a name="opensearchservice-Type-DomainNodesStatus-InstanceType"></a>
The instance type information of the node.
Type: String
Valid Values: `m3.medium.search | m3.large.search | m3.xlarge.search | m3.2xlarge.search | m4.large.search | m4.xlarge.search | m4.2xlarge.search | m4.4xlarge.search | m4.10xlarge.search | m5.large.search | m5.xlarge.search | m5.2xlarge.search | m5.4xlarge.search | m5.12xlarge.search | m5.24xlarge.search | r5.large.search | r5.xlarge.search | r5.2xlarge.search | r5.4xlarge.search | r5.12xlarge.search | r5.24xlarge.search | c5.large.search | c5.xlarge.search | c5.2xlarge.search | c5.4xlarge.search | c5.9xlarge.search | c5.18xlarge.search | t3.nano.search | t3.micro.search | t3.small.search | t3.medium.search | t3.large.search | t3.xlarge.search | t3.2xlarge.search | or1.medium.search | or1.large.search | or1.xlarge.search | or1.2xlarge.search | or1.4xlarge.search | or1.8xlarge.search | or1.12xlarge.search | or1.16xlarge.search | ultrawarm1.medium.search | ultrawarm1.large.search | ultrawarm1.xlarge.search | t2.micro.search | t2.small.search | t2.medium.search | r3.large.search | r3.xlarge.search | r3.2xlarge.search | r3.4xlarge.search | r3.8xlarge.search | i2.xlarge.search | i2.2xlarge.search | d2.xlarge.search | d2.2xlarge.search | d2.4xlarge.search | d2.8xlarge.search | c4.large.search | c4.xlarge.search | c4.2xlarge.search | c4.4xlarge.search | c4.8xlarge.search | r4.large.search | r4.xlarge.search | r4.2xlarge.search | r4.4xlarge.search | r4.8xlarge.search | r4.16xlarge.search | i3.large.search | i3.xlarge.search | i3.2xlarge.search | i3.4xlarge.search | i3.8xlarge.search | i3.16xlarge.search | r6g.large.search | r6g.xlarge.search | r6g.2xlarge.search | r6g.4xlarge.search | r6g.8xlarge.search | r6g.12xlarge.search | m6g.large.search | m6g.xlarge.search | m6g.2xlarge.search | m6g.4xlarge.search | m6g.8xlarge.search | m6g.12xlarge.search | c6g.large.search | c6g.xlarge.search | c6g.2xlarge.search | c6g.4xlarge.search | c6g.8xlarge.search | c6g.12xlarge.search | r6gd.large.search | r6gd.xlarge.search | r6gd.2xlarge.search | r6gd.4xlarge.search | r6gd.8xlarge.search | r6gd.12xlarge.search | r6gd.16xlarge.search | t4g.small.search | t4g.medium.search`
Required: No

 ** NodeId **   <a name="opensearchservice-Type-DomainNodesStatus-NodeId"></a>
The ID of the node.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 40.
Required: No

 ** NodeStatus **   <a name="opensearchservice-Type-DomainNodesStatus-NodeStatus"></a>
Indicates if the node is active or in standby.
Type: String
Valid Values: `Active | StandBy | NotAvailable`
Required: No

 ** NodeType **   <a name="opensearchservice-Type-DomainNodesStatus-NodeType"></a>
Indicates whether the nodes is a data, master, or UltraWarm node.
Type: String
Valid Values: `Data | Ultrawarm | Master | Warm`
Required: No

 ** StorageSize **   <a name="opensearchservice-Type-DomainNodesStatus-StorageSize"></a>
The storage size of the node, in GiB.
Type: String
Required: No

 ** StorageType **   <a name="opensearchservice-Type-DomainNodesStatus-StorageType"></a>
Indicates if the node has EBS or instance storage.
Type: String
Required: No

 ** StorageVolumeType **   <a name="opensearchservice-Type-DomainNodesStatus-StorageVolumeType"></a>
If the nodes has EBS storage, indicates if the volume type is gp2 or gp3. Only applicable for data nodes.
Type: String
Valid Values: `standard | gp2 | io1 | gp3`
Required: No

## See Also
<a name="API_DomainNodesStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DomainNodesStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DomainNodesStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DomainNodesStatus)
