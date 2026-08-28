---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateAuthorizer.html
---

# CreateAuthorizer
<a name="API_CreateAuthorizer"></a>

Adds a new Authorizer resource to an existing RestApi resource.

## Request Syntax
<a name="API_CreateAuthorizer_RequestSyntax"></a>

```
POST /restapis/{{restapi_id}}/authorizers HTTP/1.1
Content-type: application/json

{
   "authorizerCredentials": "{{string}}",
   "authorizerResultTtlInSeconds": {{number}},
   "authorizerUri": "{{string}}",
   "authType": "{{string}}",
   "identitySource": "{{string}}",
   "identityValidationExpression": "{{string}}",
   "name": "{{string}}",
   "providerARNs": [ "{{string}}" ],
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAuthorizer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [restapi\_id](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_CreateAuthorizer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authorizerCredentials](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-authorizerCredentials"></a>
Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.
Type: String
Required: No

 ** [authorizerResultTtlInSeconds](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-authorizerResultTtlInSeconds"></a>
The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.
Type: Integer
Required: No

 ** [authorizerUri](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-authorizerUri"></a>
Specifies the authorizer's Uniform Resource Identifier (URI). For `TOKEN` or `REQUEST` authorizers, this must be a well-formed Lambda function URI, for example, `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations`. In general, the URI has this form `arn:aws:apigateway:{region}:lambda:path/{service_api}`, where `{region}` is the same as the region hosting the Lambda function, `path` indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial `/`. For Lambda functions, this is usually of the form `/2015-03-31/functions/[FunctionARN]/invocations`.
Type: String
Required: No

 ** [authType](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-authType"></a>
Optional customer-defined field, used in OpenAPI imports and exports without functional impact.
Type: String
Required: No

 ** [identitySource](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-identitySource"></a>
The identity source for which authorization is requested. For a `TOKEN` or `COGNITO_USER_POOLS` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is `Auth`, the header mapping expression is `method.request.header.Auth`. For the `REQUEST` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an `Auth` header, a `Name` query string parameter are defined as identity sources, this value is `method.request.header.Auth, method.request.querystring.Name`. These parameters will be used to derive the authorization caching key and to perform runtime validation of the `REQUEST` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
Type: String
Required: No

 ** [identityValidationExpression](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-identityValidationExpression"></a>
A validation expression for the incoming identity token. For `TOKEN` authorizers, this value is a regular expression. For `COGNITO_USER_POOLS` authorizers, API Gateway will match the `aud` field of the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function when there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the `REQUEST` authorizer.
Type: String
Required: No

 ** [name](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-name"></a>
The name of the authorizer.
Type: String
Required: Yes

 ** [providerARNs](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-providerARNs"></a>
A list of the Amazon Cognito user pool ARNs for the `COGNITO_USER_POOLS` authorizer. Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`. For a `TOKEN` or `REQUEST` authorizer, this is not defined.
Type: Array of strings
Required: No

 ** [type](#API_CreateAuthorizer_RequestSyntax) **   <a name="apigw-CreateAuthorizer-request-type"></a>
The authorizer type. Valid values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, and `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Type: String
Valid Values: `TOKEN | REQUEST | COGNITO_USER_POOLS`
Required: Yes

## Response Syntax
<a name="API_CreateAuthorizer_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "authorizerCredentials": "string",
   "authorizerResultTtlInSeconds": number,
   "authorizerUri": "string",
   "authType": "string",
   "id": "string",
   "identitySource": "string",
   "identityValidationExpression": "string",
   "name": "string",
   "providerARNs": [ "string" ],
   "type": "string"
}
```

## Response Elements
<a name="API_CreateAuthorizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [authorizerCredentials](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-authorizerCredentials"></a>
Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.
Type: String

 ** [authorizerResultTtlInSeconds](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-authorizerResultTtlInSeconds"></a>
The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.
Type: Integer

 ** [authorizerUri](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-authorizerUri"></a>
Specifies the authorizer's Uniform Resource Identifier (URI). For `TOKEN` or `REQUEST` authorizers, this must be a well-formed Lambda function URI, for example, `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations`. In general, the URI has this form `arn:aws:apigateway:{region}:lambda:path/{service_api}`, where `{region}` is the same as the region hosting the Lambda function, `path` indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial `/`. For Lambda functions, this is usually of the form `/2015-03-31/functions/[FunctionARN]/invocations`.
Type: String

 ** [authType](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-authType"></a>
Optional customer-defined field, used in OpenAPI imports and exports without functional impact.
Type: String

 ** [id](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-id"></a>
The identifier for the authorizer resource.
Type: String

 ** [identitySource](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-identitySource"></a>
The identity source for which authorization is requested. For a `TOKEN` or `COGNITO_USER_POOLS` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is `Auth`, the header mapping expression is `method.request.header.Auth`. For the `REQUEST` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an `Auth` header, a `Name` query string parameter are defined as identity sources, this value is `method.request.header.Auth`, `method.request.querystring.Name`. These parameters will be used to derive the authorization caching key and to perform runtime validation of the `REQUEST` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
Type: String

 ** [identityValidationExpression](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-identityValidationExpression"></a>
A validation expression for the incoming identity token. For `TOKEN` authorizers, this value is a regular expression. For `COGNITO_USER_POOLS` authorizers, API Gateway will match the `aud` field of the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function when there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the `REQUEST` authorizer.
Type: String

 ** [name](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-name"></a>
The name of the authorizer.
Type: String

 ** [providerARNs](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-providerARNs"></a>
A list of the Amazon Cognito user pool ARNs for the `COGNITO_USER_POOLS` authorizer. Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`. For a `TOKEN` or `REQUEST` authorizer, this is not defined.
Type: Array of strings

 ** [type](#API_CreateAuthorizer_ResponseSyntax) **   <a name="apigw-CreateAuthorizer-response-type"></a>
The authorizer type. Valid values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, and `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Type: String
Valid Values: `TOKEN | REQUEST | COGNITO_USER_POOLS`

## Errors
<a name="API_CreateAuthorizer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

 ** LimitExceededException **
The request exceeded the rate limit. Retry after the specified time period.
HTTP Status Code: 429

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## Examples
<a name="API_CreateAuthorizer_Examples"></a>

### Example: Create a custom authorizer
<a name="API_CreateAuthorizer_Example_1"></a>

This example illustrates one usage of CreateAuthorizer.

#### Sample Request
<a name="API_CreateAuthorizer_Example_1_Request"></a>

```
POST /restapis/mxsmn867vb/authorizers HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T232342Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
"authType": "custom",
"authorizerResultTtlInSeconds": 300,
"authorizerCredentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole",
"authorizerUri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:myApiAuthroizer/invocations",
"identitySource": "method.request.header.CustAuth",
"name": "my-other-cust-auth",
"type": "TOKEN"
}"
```

#### Sample Response
<a name="API_CreateAuthorizer_Example_1_Response"></a>

```
{
"_links": {
  "curies": {
    "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-authorizer-{rel}.html",
    "name": "authorizer",
    "templated": true
  },
  "self": {
    "href": "/restapis/mxsmn867vb/authorizers/4unj71"
  },
  "authorizer:delete": {
    "href": "/restapis/mxsmn867vb/authorizers/4unj71"
  },
  "authorizer:update": {
    "href": "/restapis/mxsmn867vb/authorizers/4unj71"
  }
},
"authType": "custom",
"authorizerCredentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole",
"authorizerResultTtlInSeconds": 300,
"authorizerUri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:myApiAuthroizer/invocations",
"id": "4unj71",
"identitySource": "method.request.header.CustAuth",
"name": "my-other-cust-auth",
"type": "TOKEN"
}
```

## See Also
<a name="API_CreateAuthorizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateAuthorizer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateAuthorizer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateAuthorizer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateAuthorizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateAuthorizer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateAuthorizer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateAuthorizer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateAuthorizer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateAuthorizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateAuthorizer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
