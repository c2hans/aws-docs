---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateVpcEndpointDetail.html
---

# UpdateVpcEndpointDetail
<a name="API_UpdateVpcEndpointDetail"></a>

Update details for an OpenSearch Serverless-managed interface endpoint.

## Contents
<a name="API_UpdateVpcEndpointDetail_Contents"></a>

 ** id **   <a name="opensearchserverless-Type-UpdateVpcEndpointDetail-id"></a>
The unique identifier of the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpce-[0-9a-z]*`
Required: No

 ** lastModifiedDate **   <a name="opensearchserverless-Type-UpdateVpcEndpointDetail-lastModifiedDate"></a>
The timestamp of when the endpoint was last modified.
Type: Long
Required: No

 ** name **   <a name="opensearchserverless-Type-UpdateVpcEndpointDetail-name"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** securityGroupIds **   <a name="opensearchserverless-Type-UpdateVpcEndpointDetail-securityGroupIds"></a>
The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+\-]+`
Required: No

 ** status **   <a name="opensearchserverless-Type-UpdateVpcEndpointDetail-status"></a>
The current status of the endpoint update process.
Type: String
Valid Values: `PENDING | DELETING | ACTIVE | FAILED`
Required: No

 ** subnetIds **   <a name="opensearchserverless-Type-UpdateVpcEndpointDetail-subnetIds"></a>
The ID of the subnets from which you access OpenSearch Serverless.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `subnet-([0-9a-f]{8}|[0-9a-f]{17})`
Required: No

## See Also
<a name="API_UpdateVpcEndpointDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateVpcEndpointDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateVpcEndpointDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateVpcEndpointDetail)
