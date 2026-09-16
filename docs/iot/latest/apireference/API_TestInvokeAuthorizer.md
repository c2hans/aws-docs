---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TestInvokeAuthorizer.html
---

# TestInvokeAuthorizer
<a name="API_TestInvokeAuthorizer"></a>

Tests a custom authorization behavior by invoking a specified custom authorizer. Use this to test and debug the custom authorization behavior of devices that connect to the AWS IoT device gateway.

Requires permission to access the [TestInvokeAuthorizer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_TestInvokeAuthorizer_RequestSyntax"></a>

```
POST /authorizer/{{authorizerName}}/test HTTP/1.1
Content-type: application/json

{
   "httpContext": {
      "headers": {
         "{{string}}" : "{{string}}"
      },
      "queryString": "{{string}}"
   },
   "mqttContext": {
      "clientId": "{{string}}",
      "password": {{blob}},
      "username": "{{string}}"
   },
   "tlsContext": {
      "serverName": "{{string}}"
   },
   "token": "{{string}}",
   "tokenSignature": "{{string}}"
}
```

## URI Request Parameters
<a name="API_TestInvokeAuthorizer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [authorizerName](#API_TestInvokeAuthorizer_RequestSyntax) **   <a name="iot-TestInvokeAuthorizer-request-uri-authorizerName"></a>
The custom authorizer name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: Yes

## Request Body
<a name="API_TestInvokeAuthorizer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [httpContext](#API_TestInvokeAuthorizer_RequestSyntax) **   <a name="iot-TestInvokeAuthorizer-request-httpContext"></a>
Specifies a test HTTP authorization request.
Type: [HttpContext](API_HttpContext.md) object
Required: No

 ** [mqttContext](#API_TestInvokeAuthorizer_RequestSyntax) **   <a name="iot-TestInvokeAuthorizer-request-mqttContext"></a>
Specifies a test MQTT authorization request.
Type: [MqttContext](API_MqttContext.md) object
Required: No

 ** [tlsContext](#API_TestInvokeAuthorizer_RequestSyntax) **   <a name="iot-TestInvokeAuthorizer-request-tlsContext"></a>
Specifies a test TLS authorization request.
Type: [TlsContext](API_TlsContext.md) object
Required: No

 ** [token](#API_TestInvokeAuthorizer_RequestSyntax) **   <a name="iot-TestInvokeAuthorizer-request-token"></a>
The token returned by your custom authentication service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\s\S]*`
Required: No

 ** [tokenSignature](#API_TestInvokeAuthorizer_RequestSyntax) **   <a name="iot-TestInvokeAuthorizer-request-tokenSignature"></a>
The signature made with the token and your custom authentication service's private key. This value must be Base-64-encoded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2560.
Pattern: `[A-Za-z0-9+/]+={0,2}`
Required: No

## Response Syntax
<a name="API_TestInvokeAuthorizer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "disconnectAfterInSeconds": number,
   "isAuthenticated": boolean,
   "policyDocuments": [ "string" ],
   "principalId": "string",
   "refreshAfterInSeconds": number
}
```

## Response Elements
<a name="API_TestInvokeAuthorizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [disconnectAfterInSeconds](#API_TestInvokeAuthorizer_ResponseSyntax) **   <a name="iot-TestInvokeAuthorizer-response-disconnectAfterInSeconds"></a>
The number of seconds after which the connection is terminated.
Type: Integer

 ** [isAuthenticated](#API_TestInvokeAuthorizer_ResponseSyntax) **   <a name="iot-TestInvokeAuthorizer-response-isAuthenticated"></a>
True if the token is authenticated, otherwise false.
Type: Boolean

 ** [policyDocuments](#API_TestInvokeAuthorizer_ResponseSyntax) **   <a name="iot-TestInvokeAuthorizer-response-policyDocuments"></a>
IAM policy documents.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 404600.
Pattern: `[\s\S]*`

 ** [principalId](#API_TestInvokeAuthorizer_ResponseSyntax) **   <a name="iot-TestInvokeAuthorizer-response-principalId"></a>
The principal ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`

 ** [refreshAfterInSeconds](#API_TestInvokeAuthorizer_ResponseSyntax) **   <a name="iot-TestInvokeAuthorizer-response-refreshAfterInSeconds"></a>
The number of seconds after which the temporary credentials are refreshed.
Type: Integer

## Errors
<a name="API_TestInvokeAuthorizer_Errors"></a>

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

 ** InvalidResponseException **
The response is invalid.
 ** message **
The message for the exception.
HTTP Status Code: 400

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
<a name="API_TestInvokeAuthorizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/TestInvokeAuthorizer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/TestInvokeAuthorizer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TestInvokeAuthorizer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/TestInvokeAuthorizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TestInvokeAuthorizer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/TestInvokeAuthorizer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/TestInvokeAuthorizer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/TestInvokeAuthorizer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/TestInvokeAuthorizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TestInvokeAuthorizer)
