---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ClusterConfig.html
---

# ClusterConfig
<a name="API_ClusterConfig"></a>

Container for the cluster configuration of an OpenSearch Service domain. For more information, see [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html).

## Contents
<a name="API_ClusterConfig_Contents"></a>

 ** ColdStorageOptions **   <a name="opensearchservice-Type-ClusterConfig-ColdStorageOptions"></a>
Container for cold storage configuration options.
Type: [ColdStorageOptions](API_ColdStorageOptions.md) object
Required: No

 ** DedicatedMasterCount **   <a name="opensearchservice-Type-ClusterConfig-DedicatedMasterCount"></a>
Number of dedicated master nodes in the cluster. This number must be greater than 2 and not 4, otherwise you receive a validation exception.
Type: Integer
Required: No

 ** DedicatedMasterEnabled **   <a name="opensearchservice-Type-ClusterConfig-DedicatedMasterEnabled"></a>
Indicates whether dedicated master nodes are enabled for the cluster.`True` if the cluster will use a dedicated master node.`False` if the cluster will not.
Type: Boolean
Required: No

 ** DedicatedMasterType **   <a name="opensearchservice-Type-ClusterConfig-DedicatedMasterType"></a>
OpenSearch Service instance type of the dedicated master nodes in the cluster.
Type: String
Valid Values: `m3.medium.search | m3.large.search | m3.xlarge.search | m3.2xlarge.search | m4.large.search | m4.xlarge.search | m4.2xlarge.search | m4.4xlarge.search | m4.10xlarge.search | m5.large.search | m5.xlarge.search | m5.2xlarge.search | m5.4xlarge.search | m5.12xlarge.search | m5.24xlarge.search | r5.large.search | r5.xlarge.search | r5.2xlarge.search | r5.4xlarge.search | r5.12xlarge.search | r5.24xlarge.search | c5.large.search | c5.xlarge.search | c5.2xlarge.search | c5.4xlarge.search | c5.9xlarge.search | c5.18xlarge.search | t3.nano.search | t3.micro.search | t3.small.search | t3.medium.search | t3.large.search | t3.xlarge.search | t3.2xlarge.search | or1.medium.search | or1.large.search | or1.xlarge.search | or1.2xlarge.search | or1.4xlarge.search | or1.8xlarge.search | or1.12xlarge.search | or1.16xlarge.search | ultrawarm1.medium.search | ultrawarm1.large.search | ultrawarm1.xlarge.search | t2.micro.search | t2.small.search | t2.medium.search | r3.large.search | r3.xlarge.search | r3.2xlarge.search | r3.4xlarge.search | r3.8xlarge.search | i2.xlarge.search | i2.2xlarge.search | d2.xlarge.search | d2.2xlarge.search | d2.4xlarge.search | d2.8xlarge.search | c4.large.search | c4.xlarge.search | c4.2xlarge.search | c4.4xlarge.search | c4.8xlarge.search | r4.large.search | r4.xlarge.search | r4.2xlarge.search | r4.4xlarge.search | r4.8xlarge.search | r4.16xlarge.search | i3.large.search | i3.xlarge.search | i3.2xlarge.search | i3.4xlarge.search | i3.8xlarge.search | i3.16xlarge.search | r6g.large.search | r6g.xlarge.search | r6g.2xlarge.search | r6g.4xlarge.search | r6g.8xlarge.search | r6g.12xlarge.search | m6g.large.search | m6g.xlarge.search | m6g.2xlarge.search | m6g.4xlarge.search | m6g.8xlarge.search | m6g.12xlarge.search | c6g.large.search | c6g.xlarge.search | c6g.2xlarge.search | c6g.4xlarge.search | c6g.8xlarge.search | c6g.12xlarge.search | r6gd.large.search | r6gd.xlarge.search | r6gd.2xlarge.search | r6gd.4xlarge.search | r6gd.8xlarge.search | r6gd.12xlarge.search | r6gd.16xlarge.search | t4g.small.search | t4g.medium.search`
Required: No

 ** InstanceCount **   <a name="opensearchservice-Type-ClusterConfig-InstanceCount"></a>
Number of data nodes in the cluster. This number must be greater than 1, otherwise you receive a validation exception.
Type: Integer
Required: No

 ** InstanceType **   <a name="opensearchservice-Type-ClusterConfig-InstanceType"></a>
Instance type of data nodes in the cluster.
Type: String
Valid Values: `m3.medium.search | m3.large.search | m3.xlarge.search | m3.2xlarge.search | m4.large.search | m4.xlarge.search | m4.2xlarge.search | m4.4xlarge.search | m4.10xlarge.search | m5.large.search | m5.xlarge.search | m5.2xlarge.search | m5.4xlarge.search | m5.12xlarge.search | m5.24xlarge.search | r5.large.search | r5.xlarge.search | r5.2xlarge.search | r5.4xlarge.search | r5.12xlarge.search | r5.24xlarge.search | c5.large.search | c5.xlarge.search | c5.2xlarge.search | c5.4xlarge.search | c5.9xlarge.search | c5.18xlarge.search | t3.nano.search | t3.micro.search | t3.small.search | t3.medium.search | t3.large.search | t3.xlarge.search | t3.2xlarge.search | or1.medium.search | or1.large.search | or1.xlarge.search | or1.2xlarge.search | or1.4xlarge.search | or1.8xlarge.search | or1.12xlarge.search | or1.16xlarge.search | ultrawarm1.medium.search | ultrawarm1.large.search | ultrawarm1.xlarge.search | t2.micro.search | t2.small.search | t2.medium.search | r3.large.search | r3.xlarge.search | r3.2xlarge.search | r3.4xlarge.search | r3.8xlarge.search | i2.xlarge.search | i2.2xlarge.search | d2.xlarge.search | d2.2xlarge.search | d2.4xlarge.search | d2.8xlarge.search | c4.large.search | c4.xlarge.search | c4.2xlarge.search | c4.4xlarge.search | c4.8xlarge.search | r4.large.search | r4.xlarge.search | r4.2xlarge.search | r4.4xlarge.search | r4.8xlarge.search | r4.16xlarge.search | i3.large.search | i3.xlarge.search | i3.2xlarge.search | i3.4xlarge.search | i3.8xlarge.search | i3.16xlarge.search | r6g.large.search | r6g.xlarge.search | r6g.2xlarge.search | r6g.4xlarge.search | r6g.8xlarge.search | r6g.12xlarge.search | m6g.large.search | m6g.xlarge.search | m6g.2xlarge.search | m6g.4xlarge.search | m6g.8xlarge.search | m6g.12xlarge.search | c6g.large.search | c6g.xlarge.search | c6g.2xlarge.search | c6g.4xlarge.search | c6g.8xlarge.search | c6g.12xlarge.search | r6gd.large.search | r6gd.xlarge.search | r6gd.2xlarge.search | r6gd.4xlarge.search | r6gd.8xlarge.search | r6gd.12xlarge.search | r6gd.16xlarge.search | t4g.small.search | t4g.medium.search`
Required: No

 ** MultiAZWithStandbyEnabled **   <a name="opensearchservice-Type-ClusterConfig-MultiAZWithStandbyEnabled"></a>
A boolean that indicates whether a multi-AZ domain is turned on with a standby AZ. For more information, see [Configuring a multi-AZ domain in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html).
Type: Boolean
Required: No

 ** NodeOptions **   <a name="opensearchservice-Type-ClusterConfig-NodeOptions"></a>
List of node options for the domain.
Type: Array of [NodeOption](API_NodeOption.md) objects
Required: No

 ** WarmCount **   <a name="opensearchservice-Type-ClusterConfig-WarmCount"></a>
The number of warm nodes in the cluster.
Type: Integer
Required: No

 ** WarmEnabled **   <a name="opensearchservice-Type-ClusterConfig-WarmEnabled"></a>
Whether to enable warm storage for the cluster.
Type: Boolean
Required: No

 ** WarmType **   <a name="opensearchservice-Type-ClusterConfig-WarmType"></a>
The instance type for the cluster's warm nodes.
Type: String
Valid Values: `ultrawarm1.medium.search | ultrawarm1.large.search | ultrawarm1.xlarge.search`
Required: No

 ** ZoneAwarenessConfig **   <a name="opensearchservice-Type-ClusterConfig-ZoneAwarenessConfig"></a>
Container for zone awareness configuration options. Only required if `ZoneAwarenessEnabled` is `true`.
Type: [ZoneAwarenessConfig](API_ZoneAwarenessConfig.md) object
Required: No

 ** ZoneAwarenessEnabled **   <a name="opensearchservice-Type-ClusterConfig-ZoneAwarenessEnabled"></a>
Indicates whether multiple Availability Zones are enabled. For more information, see [Configuring a multi-AZ domain in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html).
Type: Boolean
Required: No

## See Also
<a name="API_ClusterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ClusterConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ClusterConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ClusterConfig)
