---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ApiGatewayProxySummary.html
---

# ApiGatewayProxySummary
<a name="API_ApiGatewayProxySummary"></a>

A wrapper object holding the Amazon API Gateway proxy summary.

## Contents
<a name="API_ApiGatewayProxySummary_Contents"></a>

 ** ApiGatewayId **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxySummary-ApiGatewayId"></a>
The resource ID of the API Gateway for the proxy.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: No

 ** EndpointType **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxySummary-EndpointType"></a>
The type of API Gateway endpoint created.
Type: String
Valid Values: `REGIONAL | PRIVATE`
Required: No

 ** NlbArn **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxySummary-NlbArn"></a>
The Amazon Resource Name (ARN) of the Network Load Balancer configured by the API Gateway proxy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:elasticloadbalancing:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** NlbName **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxySummary-NlbName"></a>
The name of the Network Load Balancer that is configured by the API Gateway proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?!internal-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+.*[^-]`
Required: No

 ** ProxyUrl **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxySummary-ProxyUrl"></a>
The endpoint URL of the API Gateway proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\x38@#/%=~_|]`
Required: No

 ** StageName **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxySummary-StageName"></a>
The name of the API Gateway stage. The name defaults to `prod`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-a-zA-Z0-9_]*`
Required: No

 ** VpcLinkId **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxySummary-VpcLinkId"></a>
The `VpcLink` ID of the API Gateway proxy.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: No

## See Also
<a name="API_ApiGatewayProxySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/ApiGatewayProxySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/ApiGatewayProxySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/ApiGatewayProxySummary)
