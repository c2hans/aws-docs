---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateAuthorizer.html
---

# CreateAuthorizer
<a name="API_CreateAuthorizer"></a>

Creates an authorizer.

Requires permission to access the [CreateAuthorizer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateAuthorizer_RequestSyntax"></a>

```
POST /authorizer/{{authorizerName}} HTTP/1.1
Content-type: application/json

{
   "authorizerFunctionArn": "{{string}}",
   "enableCachingForHttp": {{boolean}},
   "signingDisabled": {{boolean}},
   "status": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "tokenKeyName": "{{string}}",
   "tokenSigningPublicKeys": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAuthorizer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [authorizerName](#API_CreateAuthorizer_RequestSyntax) **   <a name="iot-CreateAuthorizer-request-uri-authorizerName"></a>
The authorizer name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: Yes

## Request Body
<a name="API_CreateAuthorizer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authorizerFunctionArn](#API_CreateAuthorizer_RequestSyntax) **   <a name="iot-CreateAuthorizer-request-authorizerFunctionArn"></a>
The ARN of the authorizer's Lambda function.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\s\S]*`
Required: Yes

 ** [enableCachingForHttp](#API_CreateAuthorizer_RequestSyntax) **   <a name="iot-CreateAuthorizer-request-enableCachingForHttp"></a>
When `true`, the result from the authorizer’s Lambda function is cached for clients that use persistent HTTP connections. The results are cached for the time specified by the Lambda function in `refreshAfterInSeconds`. This value does not affect authorization of clients that use MQTT connections.
The default value is `false`.
Type: Boolean
Required: No

 ** [signingDisabled](#API_CreateAuthorizer_RequestSyntax) **   <a name="iot-CreateAuthorizer-request-signingDisabled"></a>
Specifies whether AWS IoT validates the token signature in an authorization request.
Type: Boolean
Required: No

 ** [status](#API_CreateAuthorizer_RequestSyntax) **   <a name="iot-CreateAuthorizer-request-status"></a>
The status of the create authorizer request.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** [tags](#API_CreateAuthorizer_RequestSyntax) **   <a name="iot-CreateAuthorizer-request-tags"></a>
Metadata which can be used to manage the custom authorizer.
For URI Request parameters use format: ...key1=value1&key2=value2...
For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."
For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [tokenKeyName](#API_CreateAuthorizer_RequestSyntax) **   <a name="iot-CreateAuthorizer-request-tokenKeyName"></a>
The name of the token key used to extract the token from the HTTP headers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [tokenSigningPublicKeys](#API_CreateAuthorizer_RequestSyntax) **   <a name="iot-CreateAuthorizer-request-tokenSigningPublicKeys"></a>
The public keys used to verify the digital signature returned by your custom authentication service.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Maximum length of 5120.
Value Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_CreateAuthorizer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authorizerArn": "string",
   "authorizerName": "string"
}
```

## Response Elements
<a name="API_CreateAuthorizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizerArn](#API_CreateAuthorizer_ResponseSyntax) **   <a name="iot-CreateAuthorizer-response-authorizerArn"></a>
The authorizer ARN.
Type: String
Length Constraints: Maximum length of 2048.

 ** [authorizerName](#API_CreateAuthorizer_ResponseSyntax) **   <a name="iot-CreateAuthorizer-response-authorizerName"></a>
The authorizer's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`

## Errors
<a name="API_CreateAuthorizer_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_CreateAuthorizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateAuthorizer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateAuthorizer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateAuthorizer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateAuthorizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateAuthorizer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateAuthorizer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateAuthorizer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateAuthorizer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateAuthorizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateAuthorizer)
