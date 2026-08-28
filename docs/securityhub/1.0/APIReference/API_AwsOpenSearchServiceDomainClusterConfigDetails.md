---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsOpenSearchServiceDomainClusterConfigDetails.html
---

# AwsOpenSearchServiceDomainClusterConfigDetails
<a name="API_AwsOpenSearchServiceDomainClusterConfigDetails"></a>

Details about the configuration of an OpenSearch cluster.

## Contents
<a name="API_AwsOpenSearchServiceDomainClusterConfigDetails_Contents"></a>

 ** DedicatedMasterCount **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-DedicatedMasterCount"></a>
The number of instances to use for the master node. If this attribute is specified, then `DedicatedMasterEnabled` must be `true`.
Type: Integer
Required: No

 ** DedicatedMasterEnabled **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-DedicatedMasterEnabled"></a>
Whether to use a dedicated master node for the OpenSearch domain. A dedicated master node performs cluster management tasks, but does not hold data or respond to data upload requests.
Type: Boolean
Required: No

 ** DedicatedMasterType **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-DedicatedMasterType"></a>
The hardware configuration of the computer that hosts the dedicated master node.
If this attribute is specified, then `DedicatedMasterEnabled` must be `true`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceCount **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-InstanceCount"></a>
The number of data nodes to use in the OpenSearch domain.
Type: Integer
Required: No

 ** InstanceType **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-InstanceType"></a>
The instance type for your data nodes.
For a list of valid values, see [Supported instance types in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html) in the *Amazon OpenSearch Service Developer Guide*.
Type: String
Pattern: `.*\S.*`
Required: No

 ** WarmCount **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-WarmCount"></a>
The number of UltraWarm instances.
Type: Integer
Required: No

 ** WarmEnabled **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-WarmEnabled"></a>
Whether UltraWarm is enabled.
Type: Boolean
Required: No

 ** WarmType **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-WarmType"></a>
The type of UltraWarm instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ZoneAwarenessConfig **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-ZoneAwarenessConfig"></a>
Configuration options for zone awareness. Provided if `ZoneAwarenessEnabled` is `true`.
Type: [AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails](API_AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails.md) object
Required: No

 ** ZoneAwarenessEnabled **   <a name="securityhub-Type-AwsOpenSearchServiceDomainClusterConfigDetails-ZoneAwarenessEnabled"></a>
Whether to enable zone awareness for the OpenSearch domain. When zone awareness is enabled, OpenSearch Service allocates the cluster's nodes and replica index shards across Availability Zones (AZs) in the same Region. This prevents data loss and minimizes downtime if a node or data center fails.
Type: Boolean
Required: No

## See Also
<a name="API_AwsOpenSearchServiceDomainClusterConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsOpenSearchServiceDomainClusterConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsOpenSearchServiceDomainClusterConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsOpenSearchServiceDomainClusterConfigDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
