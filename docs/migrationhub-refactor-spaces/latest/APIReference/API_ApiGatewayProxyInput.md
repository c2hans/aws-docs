---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ApiGatewayProxyInput.html
---

# ApiGatewayProxyInput
<a name="API_ApiGatewayProxyInput"></a>

A wrapper object holding the Amazon API Gateway endpoint input.

## Contents
<a name="API_ApiGatewayProxyInput_Contents"></a>

 ** EndpointType **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxyInput-EndpointType"></a>
The type of endpoint to use for the API Gateway proxy. If no value is specified in the request, the value is set to `REGIONAL` by default.
If the value is set to `PRIVATE` in the request, this creates a private API endpoint that is isolated from the public internet. The private endpoint can only be accessed by using Amazon Virtual Private Cloud (Amazon VPC) interface endpoints for the Amazon API Gateway that has been granted access. For more information about creating a private connection with Refactor Spaces and interface endpoint (AWS PrivateLink) availability, see [Access Refactor Spaces using an interface endpoint (AWS PrivateLink)](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/vpc-interface-endpoints.html).
Type: String
Valid Values: `REGIONAL | PRIVATE`
Required: No

 ** StageName **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxyInput-StageName"></a>
The name of the API Gateway stage. The name defaults to `prod`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-a-zA-Z0-9_]*`
Required: No

## See Also
<a name="API_ApiGatewayProxyInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/ApiGatewayProxyInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/ApiGatewayProxyInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/ApiGatewayProxyInput)
