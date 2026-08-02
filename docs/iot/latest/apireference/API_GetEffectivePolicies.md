---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetEffectivePolicies.html
---

# GetEffectivePolicies
<a name="API_GetEffectivePolicies"></a>

Gets a list of the policies that have an effect on the authorization behavior of the specified device when it connects to the AWS IoT device gateway.

Requires permission to access the [GetEffectivePolicies](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetEffectivePolicies_RequestSyntax"></a>

```
POST /effective-policies?thingName={{thingName}} HTTP/1.1
Content-type: application/json

{
   "cognitoIdentityPoolId": "{{string}}",
   "principal": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetEffectivePolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingName](#API_GetEffectivePolicies_RequestSyntax) **   <a name="iot-GetEffectivePolicies-request-uri-thingName"></a>
The thing name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Request Body
<a name="API_GetEffectivePolicies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cognitoIdentityPoolId](#API_GetEffectivePolicies_RequestSyntax) **   <a name="iot-GetEffectivePolicies-request-cognitoIdentityPoolId"></a>
The Cognito identity pool ID.
Type: String
Required: No

 ** [principal](#API_GetEffectivePolicies_RequestSyntax) **   <a name="iot-GetEffectivePolicies-request-principal"></a>
The principal. Valid principals are CertificateArn (arn:aws:iot:*region*:*accountId*:cert/*certificateId*), thingGroupArn (arn:aws:iot:*region*:*accountId*:thinggroup/*groupName*) and CognitoId (*region*:*id*).
Type: String
Required: No

## Response Syntax
<a name="API_GetEffectivePolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "effectivePolicies": [
      {
         "policyArn": "string",
         "policyDocument": "string",
         "policyName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetEffectivePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [effectivePolicies](#API_GetEffectivePolicies_ResponseSyntax) **   <a name="iot-GetEffectivePolicies-response-effectivePolicies"></a>
The effective policies.
Type: Array of [EffectivePolicy](API_EffectivePolicy.md) objects

## Errors
<a name="API_GetEffectivePolicies_Errors"></a>

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
<a name="API_GetEffectivePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetEffectivePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetEffectivePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetEffectivePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetEffectivePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetEffectivePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetEffectivePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetEffectivePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetEffectivePolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetEffectivePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetEffectivePolicies)
