---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_VpcEndpoint.html
---

# VpcEndpoint
<a name="API_VpcEndpoint"></a>

The connection endpoint for connecting to an Amazon OpenSearch Service domain through a proxy.

## Contents
<a name="API_VpcEndpoint_Contents"></a>

 ** DomainArn **   <a name="opensearchservice-Type-VpcEndpoint-DomainArn"></a>
The Amazon Resource Name (ARN) of the domain associated with the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
Required: No

 ** Endpoint **   <a name="opensearchservice-Type-VpcEndpoint-Endpoint"></a>
The connection endpoint ID for connecting to the domain.
Type: String
Pattern: `^[A-Za-z0-9\-\.]+$`
Required: No

 ** Status **   <a name="opensearchservice-Type-VpcEndpoint-Status"></a>
The current status of the endpoint.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED`
Required: No

 ** VpcEndpointId **   <a name="opensearchservice-Type-VpcEndpoint-VpcEndpointId"></a>
The unique identifier of the endpoint.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 256.
Pattern: `^aos-[a-zA-Z0-9]*$`
Required: No

 ** VpcEndpointOwner **   <a name="opensearchservice-Type-VpcEndpoint-VpcEndpointOwner"></a>
The creator of the endpoint.
Type: String
Pattern: `^[0-9]+$`
Required: No

 ** VpcOptions **   <a name="opensearchservice-Type-VpcEndpoint-VpcOptions"></a>
Options to specify the subnets and security groups for an Amazon OpenSearch Service VPC endpoint.
Type: [VPCDerivedInfo](API_VPCDerivedInfo.md) object
Required: No

## See Also
<a name="API_VpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/VpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/VpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/VpcEndpoint)
