---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SetDefaultAuthorizer.html
---

# SetDefaultAuthorizer
<a name="API_SetDefaultAuthorizer"></a>

Sets the default authorizer. This will be used if a websocket connection is made without specifying an authorizer.

Requires permission to access the [SetDefaultAuthorizer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_SetDefaultAuthorizer_RequestSyntax"></a>

```
POST /default-authorizer HTTP/1.1
Content-type: application/json

{
   "authorizerName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SetDefaultAuthorizer_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SetDefaultAuthorizer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authorizerName](#API_SetDefaultAuthorizer_RequestSyntax) **   <a name="iot-SetDefaultAuthorizer-request-authorizerName"></a>
The authorizer name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: Yes

## Response Syntax
<a name="API_SetDefaultAuthorizer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authorizerArn": "string",
   "authorizerName": "string"
}
```

## Response Elements
<a name="API_SetDefaultAuthorizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizerArn](#API_SetDefaultAuthorizer_ResponseSyntax) **   <a name="iot-SetDefaultAuthorizer-response-authorizerArn"></a>
The authorizer ARN.
Type: String
Length Constraints: Maximum length of 2048.

 ** [authorizerName](#API_SetDefaultAuthorizer_ResponseSyntax) **   <a name="iot-SetDefaultAuthorizer-response-authorizerName"></a>
The authorizer name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`

## Errors
<a name="API_SetDefaultAuthorizer_Errors"></a>

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

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

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
<a name="API_SetDefaultAuthorizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/SetDefaultAuthorizer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/SetDefaultAuthorizer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SetDefaultAuthorizer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/SetDefaultAuthorizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SetDefaultAuthorizer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/SetDefaultAuthorizer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/SetDefaultAuthorizer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/SetDefaultAuthorizer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/SetDefaultAuthorizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SetDefaultAuthorizer)
