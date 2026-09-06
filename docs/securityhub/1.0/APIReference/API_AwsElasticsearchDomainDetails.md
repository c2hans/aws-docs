---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElasticsearchDomainDetails.html
---

# AwsElasticsearchDomainDetails
<a name="API_AwsElasticsearchDomainDetails"></a>

Information about an Elasticsearch domain.

## Contents
<a name="API_AwsElasticsearchDomainDetails_Contents"></a>

 ** AccessPolicies **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-AccessPolicies"></a>
IAM policy document specifying the access policies for the new Elasticsearch domain.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DomainEndpointOptions **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-DomainEndpointOptions"></a>
Additional options for the domain endpoint.
Type: [AwsElasticsearchDomainDomainEndpointOptions](API_AwsElasticsearchDomainDomainEndpointOptions.md) object
Required: No

 ** DomainId **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-DomainId"></a>
Unique identifier for an Elasticsearch domain.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DomainName **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-DomainName"></a>
Name of an Elasticsearch domain.
Domain names are unique across all domains owned by the same account within an AWS Region.
Domain names must start with a lowercase letter and must be between 3 and 28 characters.
Valid characters are a-z (lowercase only), 0-9, and – (hyphen).
Type: String
Pattern: `.*\S.*`
Required: No

 ** ElasticsearchClusterConfig **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-ElasticsearchClusterConfig"></a>
Information about an OpenSearch cluster configuration.
Type: [AwsElasticsearchDomainElasticsearchClusterConfigDetails](API_AwsElasticsearchDomainElasticsearchClusterConfigDetails.md) object
Required: No

 ** ElasticsearchVersion **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-ElasticsearchVersion"></a>
OpenSearch version.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EncryptionAtRestOptions **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-EncryptionAtRestOptions"></a>
Details about the configuration for encryption at rest.
Type: [AwsElasticsearchDomainEncryptionAtRestOptions](API_AwsElasticsearchDomainEncryptionAtRestOptions.md) object
Required: No

 ** Endpoint **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-Endpoint"></a>
Domain-specific endpoint used to submit index, search, and data upload requests to an Elasticsearch domain.
The endpoint is a service URL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Endpoints **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-Endpoints"></a>
The key-value pair that exists if the Elasticsearch domain uses VPC endpoints.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** LogPublishingOptions **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-LogPublishingOptions"></a>
Configures the CloudWatch Logs to publish for the Elasticsearch domain.
Type: [AwsElasticsearchDomainLogPublishingOptions](API_AwsElasticsearchDomainLogPublishingOptions.md) object
Required: No

 ** NodeToNodeEncryptionOptions **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-NodeToNodeEncryptionOptions"></a>
Details about the configuration for node-to-node encryption.
Type: [AwsElasticsearchDomainNodeToNodeEncryptionOptions](API_AwsElasticsearchDomainNodeToNodeEncryptionOptions.md) object
Required: No

 ** ServiceSoftwareOptions **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-ServiceSoftwareOptions"></a>
Information about the status of a domain relative to the latest service software.
Type: [AwsElasticsearchDomainServiceSoftwareOptions](API_AwsElasticsearchDomainServiceSoftwareOptions.md) object
Required: No

 ** VPCOptions **   <a name="securityhub-Type-AwsElasticsearchDomainDetails-VPCOptions"></a>
Information that OpenSearch derives based on `VPCOptions` for the domain.
Type: [AwsElasticsearchDomainVPCOptions](API_AwsElasticsearchDomainVPCOptions.md) object
Required: No

## See Also
<a name="API_AwsElasticsearchDomainDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElasticsearchDomainDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElasticsearchDomainDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElasticsearchDomainDetails)
