---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteVpcEndpointDetail.html
---

# DeleteVpcEndpointDetail
<a name="API_DeleteVpcEndpointDetail"></a>

Deletion details for an OpenSearch Serverless-managed interface endpoint.

## Contents
<a name="API_DeleteVpcEndpointDetail_Contents"></a>

 ** id **   <a name="opensearchserverless-Type-DeleteVpcEndpointDetail-id"></a>
The unique identifier of the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpce-[0-9a-z]*`
Required: No

 ** name **   <a name="opensearchserverless-Type-DeleteVpcEndpointDetail-name"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** status **   <a name="opensearchserverless-Type-DeleteVpcEndpointDetail-status"></a>
The current status of the endpoint deletion process.
Type: String
Valid Values: `PENDING | DELETING | ACTIVE | FAILED`
Required: No

## See Also
<a name="API_DeleteVpcEndpointDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/DeleteVpcEndpointDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/DeleteVpcEndpointDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/DeleteVpcEndpointDetail)
