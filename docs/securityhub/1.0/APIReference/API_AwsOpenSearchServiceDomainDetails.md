---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsOpenSearchServiceDomainDetails.html
---

# AwsOpenSearchServiceDomainDetails
<a name="API_AwsOpenSearchServiceDomainDetails"></a>

Information about an Amazon OpenSearch Service domain.

## Contents
<a name="API_AwsOpenSearchServiceDomainDetails_Contents"></a>

 ** AccessPolicies **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-AccessPolicies"></a>
IAM policy document that specifies the access policies for the OpenSearch Service domain.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AdvancedSecurityOptions **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-AdvancedSecurityOptions"></a>
Specifies options for fine-grained access control.
Type: [AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails](API_AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails.md) object
Required: No

 ** Arn **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-Arn"></a>
The ARN of the OpenSearch Service domain.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterConfig **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-ClusterConfig"></a>
Details about the configuration of an OpenSearch cluster.
Type: [AwsOpenSearchServiceDomainClusterConfigDetails](API_AwsOpenSearchServiceDomainClusterConfigDetails.md) object
Required: No

 ** DomainEndpoint **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-DomainEndpoint"></a>
The domain endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DomainEndpointOptions **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-DomainEndpointOptions"></a>
Additional options for the domain endpoint.
Type: [AwsOpenSearchServiceDomainDomainEndpointOptionsDetails](API_AwsOpenSearchServiceDomainDomainEndpointOptionsDetails.md) object
Required: No

 ** DomainEndpoints **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-DomainEndpoints"></a>
The domain endpoints. Used if the OpenSearch domain resides in a VPC.
This is a map of key-value pairs. The key is always `vpc`. The value is the endpoint.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** DomainName **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-DomainName"></a>
The name of the endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EncryptionAtRestOptions **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-EncryptionAtRestOptions"></a>
Details about the configuration for encryption at rest.
Type: [AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails](API_AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails.md) object
Required: No

 ** EngineVersion **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-EngineVersion"></a>
The version of the domain engine.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-Id"></a>
The identifier of the domain.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LogPublishingOptions **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-LogPublishingOptions"></a>
Configures the CloudWatch Logs to publish for the OpenSearch domain.
Type: [AwsOpenSearchServiceDomainLogPublishingOptionsDetails](API_AwsOpenSearchServiceDomainLogPublishingOptionsDetails.md) object
Required: No

 ** NodeToNodeEncryptionOptions **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-NodeToNodeEncryptionOptions"></a>
Details about the configuration for node-to-node encryption.
Type: [AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails](API_AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails.md) object
Required: No

 ** ServiceSoftwareOptions **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-ServiceSoftwareOptions"></a>
Information about the status of a domain relative to the latest service software.
Type: [AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails](API_AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails.md) object
Required: No

 ** VpcOptions **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDetails-VpcOptions"></a>
Information that OpenSearch Service derives based on `VPCOptions` for the domain.
Type: [AwsOpenSearchServiceDomainVpcOptionsDetails](API_AwsOpenSearchServiceDomainVpcOptionsDetails.md) object
Required: No

## See Also
<a name="API_AwsOpenSearchServiceDomainDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsOpenSearchServiceDomainDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsOpenSearchServiceDomainDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsOpenSearchServiceDomainDetails)
