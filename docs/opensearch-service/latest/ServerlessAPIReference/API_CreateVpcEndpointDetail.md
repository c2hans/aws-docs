---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateVpcEndpointDetail.html
---

# CreateVpcEndpointDetail
<a name="API_CreateVpcEndpointDetail"></a>

Creation details for an OpenSearch Serverless-managed interface endpoint. For more information, see [Access Amazon OpenSearch Serverless using an interface endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html).

## Contents
<a name="API_CreateVpcEndpointDetail_Contents"></a>

 ** id **   <a name="opensearchserverless-Type-CreateVpcEndpointDetail-id"></a>
The unique identifier of the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpce-[0-9a-z]*`
Required: No

 ** name **   <a name="opensearchserverless-Type-CreateVpcEndpointDetail-name"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** status **   <a name="opensearchserverless-Type-CreateVpcEndpointDetail-status"></a>
The current status in the endpoint creation process.
Type: String
Valid Values: `PENDING | DELETING | ACTIVE | FAILED`
Required: No

## See Also
<a name="API_CreateVpcEndpointDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CreateVpcEndpointDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CreateVpcEndpointDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CreateVpcEndpointDetail)
