---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsApiGatewayV2ApiDetails.html
---

# AwsApiGatewayV2ApiDetails
<a name="API_AwsApiGatewayV2ApiDetails"></a>

Contains information about a version 2 API in Amazon API Gateway.

## Contents
<a name="API_AwsApiGatewayV2ApiDetails_Contents"></a>

 ** ApiEndpoint **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-ApiEndpoint"></a>
The URI of the API.
Uses the format ` <api-id>.execute-api.<region>.amazonaws.com`
The stage name is typically appended to the URI to form a complete path to a deployed API stage.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ApiId **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-ApiId"></a>
The identifier of the API.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ApiKeySelectionExpression **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-ApiKeySelectionExpression"></a>
An API key selection expression. Supported only for WebSocket APIs.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CorsConfiguration **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-CorsConfiguration"></a>
A cross-origin resource sharing (CORS) configuration. Supported only for HTTP APIs.
Type: [AwsCorsConfiguration](API_AwsCorsConfiguration.md) object
Required: No

 ** CreatedDate **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-CreatedDate"></a>
Indicates when the API was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-Description"></a>
A description of the API.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-Name"></a>
The name of the API.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProtocolType **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-ProtocolType"></a>
The API protocol for the API.
Valid values: `WEBSOCKET` \| `HTTP`
Type: String
Pattern: `.*\S.*`
Required: No

 ** RouteSelectionExpression **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-RouteSelectionExpression"></a>
The route selection expression for the API.
For HTTP APIs, must be `${request.method} ${request.path}`. This is the default value for HTTP APIs.
For WebSocket APIs, there is no default value.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Version **   <a name="securityhub-Type-AwsApiGatewayV2ApiDetails-Version"></a>
The version identifier for the API.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsApiGatewayV2ApiDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsApiGatewayV2ApiDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsApiGatewayV2ApiDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsApiGatewayV2ApiDetails)
