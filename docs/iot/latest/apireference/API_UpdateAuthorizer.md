---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAuthorizer.html
---

# UpdateAuthorizer
<a name="API_UpdateAuthorizer"></a>

Updates an authorizer.

Requires permission to access the [UpdateAuthorizer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateAuthorizer_RequestSyntax"></a>

```
PUT /authorizer/{{authorizerName}} HTTP/1.1
Content-type: application/json

{
   "authorizerFunctionArn": "{{string}}",
   "enableCachingForHttp": {{boolean}},
   "status": "{{string}}",
   "tokenKeyName": "{{string}}",
   "tokenSigningPublicKeys": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateAuthorizer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [authorizerName](#API_UpdateAuthorizer_RequestSyntax) **   <a name="iot-UpdateAuthorizer-request-uri-authorizerName"></a>
The authorizer name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: Yes

## Request Body
<a name="API_UpdateAuthorizer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authorizerFunctionArn](#API_UpdateAuthorizer_RequestSyntax) **   <a name="iot-UpdateAuthorizer-request-authorizerFunctionArn"></a>
The ARN of the authorizer's Lambda function.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

 ** [enableCachingForHttp](#API_UpdateAuthorizer_RequestSyntax) **   <a name="iot-UpdateAuthorizer-request-enableCachingForHttp"></a>
When `true`, the result from the authorizer’s Lambda function is cached for the time specified in `refreshAfterInSeconds`. The cached result is used while the device reuses the same HTTP connection.
Type: Boolean
Required: No

 ** [status](#API_UpdateAuthorizer_RequestSyntax) **   <a name="iot-UpdateAuthorizer-request-status"></a>
The status of the update authorizer request.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** [tokenKeyName](#API_UpdateAuthorizer_RequestSyntax) **   <a name="iot-UpdateAuthorizer-request-tokenKeyName"></a>
The key used to extract the token from the HTTP headers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [tokenSigningPublicKeys](#API_UpdateAuthorizer_RequestSyntax) **   <a name="iot-UpdateAuthorizer-request-tokenSigningPublicKeys"></a>
The public keys used to verify the token signature.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Maximum length of 5120.
Value Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_UpdateAuthorizer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authorizerArn": "string",
   "authorizerName": "string"
}
```

## Response Elements
<a name="API_UpdateAuthorizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizerArn](#API_UpdateAuthorizer_ResponseSyntax) **   <a name="iot-UpdateAuthorizer-response-authorizerArn"></a>
The authorizer ARN.
Type: String
Length Constraints: Maximum length of 2048.

 ** [authorizerName](#API_UpdateAuthorizer_ResponseSyntax) **   <a name="iot-UpdateAuthorizer-response-authorizerName"></a>
The authorizer name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`

## Errors
<a name="API_UpdateAuthorizer_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

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
<a name="API_UpdateAuthorizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateAuthorizer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateAuthorizer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateAuthorizer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateAuthorizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateAuthorizer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateAuthorizer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateAuthorizer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateAuthorizer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateAuthorizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateAuthorizer)
