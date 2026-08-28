---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ApiGatewayProxyConfig.html
---

# ApiGatewayProxyConfig
<a name="API_ApiGatewayProxyConfig"></a>

A wrapper object holding the Amazon API Gateway proxy configuration.

## Contents
<a name="API_ApiGatewayProxyConfig_Contents"></a>

 ** ApiGatewayId **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxyConfig-ApiGatewayId"></a>
The resource ID of the API Gateway for the proxy.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: No

 ** EndpointType **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxyConfig-EndpointType"></a>
The type of API Gateway endpoint created.
Type: String
Valid Values: `REGIONAL | PRIVATE`
Required: No

 ** NlbArn **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxyConfig-NlbArn"></a>
The Amazon Resource Name (ARN) of the Network Load Balancer configured by the API Gateway proxy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:elasticloadbalancing:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** NlbName **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxyConfig-NlbName"></a>
The name of the Network Load Balancer that is configured by the API Gateway proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?!internal-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+.*[^-]`
Required: No

 ** ProxyUrl **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxyConfig-ProxyUrl"></a>
The endpoint URL of the API Gateway proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\x38@#/%=~_|]`
Required: No

 ** StageName **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxyConfig-StageName"></a>
The name of the API Gateway stage. The name defaults to `prod`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-a-zA-Z0-9_]*`
Required: No

 ** VpcLinkId **   <a name="migrationhubrefactorspaces-Type-ApiGatewayProxyConfig-VpcLinkId"></a>
The `VpcLink` ID of the API Gateway proxy.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: No

## See Also
<a name="API_ApiGatewayProxyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/ApiGatewayProxyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/ApiGatewayProxyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/ApiGatewayProxyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
