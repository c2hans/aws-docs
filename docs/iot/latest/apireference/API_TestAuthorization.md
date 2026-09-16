---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TestAuthorization.html
---

# TestAuthorization
<a name="API_TestAuthorization"></a>

Tests if a specified principal is authorized to perform an AWS IoT action on a specified resource. Use this to test and debug the authorization behavior of devices that connect to the AWS IoT device gateway.

Requires permission to access the [TestAuthorization](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_TestAuthorization_RequestSyntax"></a>

```
POST /test-authorization?clientId={{clientId}} HTTP/1.1
Content-type: application/json

{
   "authInfos": [
      {
         "actionType": "{{string}}",
         "resources": [ "{{string}}" ]
      }
   ],
   "cognitoIdentityPoolId": "{{string}}",
   "policyNamesToAdd": [ "{{string}}" ],
   "policyNamesToSkip": [ "{{string}}" ],
   "principal": "{{string}}"
}
```

## URI Request Parameters
<a name="API_TestAuthorization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientId](#API_TestAuthorization_RequestSyntax) **   <a name="iot-TestAuthorization-request-uri-clientId"></a>
The MQTT client ID.

## Request Body
<a name="API_TestAuthorization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authInfos](#API_TestAuthorization_RequestSyntax) **   <a name="iot-TestAuthorization-request-authInfos"></a>
A list of authorization info objects. Simulating authorization will create a response for each `authInfo` object in the list.
Type: Array of [AuthInfo](API_AuthInfo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [cognitoIdentityPoolId](#API_TestAuthorization_RequestSyntax) **   <a name="iot-TestAuthorization-request-cognitoIdentityPoolId"></a>
The Cognito identity pool ID.
Type: String
Required: No

 ** [policyNamesToAdd](#API_TestAuthorization_RequestSyntax) **   <a name="iot-TestAuthorization-request-policyNamesToAdd"></a>
When testing custom authorization, the policies specified here are treated as if they are attached to the principal being authorized.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

 ** [policyNamesToSkip](#API_TestAuthorization_RequestSyntax) **   <a name="iot-TestAuthorization-request-policyNamesToSkip"></a>
When testing custom authorization, the policies specified here are treated as if they are not attached to the principal being authorized.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

 ** [principal](#API_TestAuthorization_RequestSyntax) **   <a name="iot-TestAuthorization-request-principal"></a>
The principal. Valid principals are CertificateArn (arn:aws:iot:*region*:*accountId*:cert/*certificateId*) and CognitoId (*region*:*id*).
Type: String
Required: No

## Response Syntax
<a name="API_TestAuthorization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authResults": [
      {
         "allowed": {
            "policies": [
               {
                  "policyArn": "string",
                  "policyName": "string"
               }
            ]
         },
         "authDecision": "string",
         "authInfo": {
            "actionType": "string",
            "resources": [ "string" ]
         },
         "denied": {
            "explicitDeny": {
               "policies": [
                  {
                     "policyArn": "string",
                     "policyName": "string"
                  }
               ]
            },
            "implicitDeny": {
               "policies": [
                  {
                     "policyArn": "string",
                     "policyName": "string"
                  }
               ]
            }
         },
         "missingContextValues": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_TestAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authResults](#API_TestAuthorization_ResponseSyntax) **   <a name="iot-TestAuthorization-response-authResults"></a>
The authentication results.
Type: Array of [AuthResult](API_AuthResult.md) objects

## Errors
<a name="API_TestAuthorization_Errors"></a>

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
<a name="API_TestAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/TestAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/TestAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TestAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/TestAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TestAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/TestAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/TestAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/TestAuthorization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/TestAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TestAuthorization)
