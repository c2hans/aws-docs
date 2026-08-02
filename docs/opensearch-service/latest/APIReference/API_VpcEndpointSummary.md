---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_VpcEndpointSummary.html
---

# VpcEndpointSummary
<a name="API_VpcEndpointSummary"></a>

Summary information for an Amazon OpenSearch Service-managed VPC endpoint.

## Contents
<a name="API_VpcEndpointSummary_Contents"></a>

 ** DomainArn **   <a name="opensearchservice-Type-VpcEndpointSummary-DomainArn"></a>
The Amazon Resource Name (ARN) of the domain associated with the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
Required: No

 ** Status **   <a name="opensearchservice-Type-VpcEndpointSummary-Status"></a>
The current status of the endpoint.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED`
Required: No

 ** VpcEndpointId **   <a name="opensearchservice-Type-VpcEndpointSummary-VpcEndpointId"></a>
The unique identifier of the endpoint.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 256.
Pattern: `^aos-[a-zA-Z0-9]*$`
Required: No

 ** VpcEndpointOwner **   <a name="opensearchservice-Type-VpcEndpointSummary-VpcEndpointOwner"></a>
The creator of the endpoint.
Type: String
Required: No

## See Also
<a name="API_VpcEndpointSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/VpcEndpointSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/VpcEndpointSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/VpcEndpointSummary)
