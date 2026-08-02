---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElasticsearchDomainElasticsearchClusterConfigDetails.html
---

# AwsElasticsearchDomainElasticsearchClusterConfigDetails
<a name="API_AwsElasticsearchDomainElasticsearchClusterConfigDetails"></a>

details about the configuration of an OpenSearch cluster.

## Contents
<a name="API_AwsElasticsearchDomainElasticsearchClusterConfigDetails_Contents"></a>

 ** DedicatedMasterCount **   <a name="securityhub-Type-AwsElasticsearchDomainElasticsearchClusterConfigDetails-DedicatedMasterCount"></a>
The number of instances to use for the master node. If this attribute is specified, then `DedicatedMasterEnabled` must be `true`.
Type: Integer
Required: No

 ** DedicatedMasterEnabled **   <a name="securityhub-Type-AwsElasticsearchDomainElasticsearchClusterConfigDetails-DedicatedMasterEnabled"></a>
Whether to use a dedicated master node for the Elasticsearch domain. A dedicated master node performs cluster management tasks, but doesn't hold data or respond to data upload requests.
Type: Boolean
Required: No

 ** DedicatedMasterType **   <a name="securityhub-Type-AwsElasticsearchDomainElasticsearchClusterConfigDetails-DedicatedMasterType"></a>
The hardware configuration of the computer that hosts the dedicated master node. A sample value is `m3.medium.elasticsearch`. If this attribute is specified, then `DedicatedMasterEnabled` must be `true`.
For a list of valid values, see [Supported instance types in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html) in the *Amazon OpenSearch Service Developer Guide*.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceCount **   <a name="securityhub-Type-AwsElasticsearchDomainElasticsearchClusterConfigDetails-InstanceCount"></a>
The number of data nodes to use in the Elasticsearch domain.
Type: Integer
Required: No

 ** InstanceType **   <a name="securityhub-Type-AwsElasticsearchDomainElasticsearchClusterConfigDetails-InstanceType"></a>
The instance type for your data nodes. For example, `m3.medium.elasticsearch`.
For a list of valid values, see [Supported instance types in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html) in the *Amazon OpenSearch Service Developer Guide*.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ZoneAwarenessConfig **   <a name="securityhub-Type-AwsElasticsearchDomainElasticsearchClusterConfigDetails-ZoneAwarenessConfig"></a>
Configuration options for zone awareness. Provided if `ZoneAwarenessEnabled` is `true`.
Type: [AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails](API_AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails.md) object
Required: No

 ** ZoneAwarenessEnabled **   <a name="securityhub-Type-AwsElasticsearchDomainElasticsearchClusterConfigDetails-ZoneAwarenessEnabled"></a>
Whether to enable zone awareness for the Elasticsearch domain. When zone awareness is enabled, OpenSearch allocates the cluster's nodes and replica index shards across Availability Zones in the same Region. This prevents data loss and minimizes downtime if a node or data center fails.
Type: Boolean
Required: No

## See Also
<a name="API_AwsElasticsearchDomainElasticsearchClusterConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElasticsearchDomainElasticsearchClusterConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElasticsearchDomainElasticsearchClusterConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElasticsearchDomainElasticsearchClusterConfigDetails)
