---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePolicyVersion.html
---

# CreatePolicyVersion
<a name="API_CreatePolicyVersion"></a>

Creates a new version of the specified AWS IoT policy. To update a policy, create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must use [DeletePolicyVersion](API_DeletePolicyVersion.md) to delete an existing version before you create a new one.

Optionally, you can set the new version as the policy's default version. The default version is the operative version (that is, the version that is in effect for the certificates to which the policy is attached).

Requires permission to access the [CreatePolicyVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreatePolicyVersion_RequestSyntax"></a>

```
POST /policies/{{policyName}}/version?setAsDefault={{setAsDefault}} HTTP/1.1
Content-type: application/json

{
   "policyDocument": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePolicyVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyName](#API_CreatePolicyVersion_RequestSyntax) **   <a name="iot-CreatePolicyVersion-request-uri-policyName"></a>
The policy name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** [setAsDefault](#API_CreatePolicyVersion_RequestSyntax) **   <a name="iot-CreatePolicyVersion-request-uri-setAsDefault"></a>
Specifies whether the policy version is set as the default. When this parameter is true, the new policy version becomes the operative version (that is, the version that is in effect for the certificates to which the policy is attached).

## Request Body
<a name="API_CreatePolicyVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policyDocument](#API_CreatePolicyVersion_RequestSyntax) **   <a name="iot-CreatePolicyVersion-request-policyDocument"></a>
The JSON document that describes the policy. Minimum length of 1. Maximum length of 2048, excluding whitespace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 404600.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_CreatePolicyVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "isDefaultVersion": boolean,
   "policyArn": "string",
   "policyDocument": "string",
   "policyVersionId": "string"
}
```

## Response Elements
<a name="API_CreatePolicyVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [isDefaultVersion](#API_CreatePolicyVersion_ResponseSyntax) **   <a name="iot-CreatePolicyVersion-response-isDefaultVersion"></a>
Specifies whether the policy version is the default.
Type: Boolean

 ** [policyArn](#API_CreatePolicyVersion_ResponseSyntax) **   <a name="iot-CreatePolicyVersion-response-policyArn"></a>
The policy ARN.
Type: String

 ** [policyDocument](#API_CreatePolicyVersion_ResponseSyntax) **   <a name="iot-CreatePolicyVersion-response-policyDocument"></a>
The JSON document that describes the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 404600.
Pattern: `[\s\S]*`

 ** [policyVersionId](#API_CreatePolicyVersion_ResponseSyntax) **   <a name="iot-CreatePolicyVersion-response-policyVersionId"></a>
The policy version ID.
Type: String
Pattern: `[0-9]+`

## Errors
<a name="API_CreatePolicyVersion_Errors"></a>

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

 ** MalformedPolicyException **
The policy documentation is not valid.
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

 ** VersionsLimitExceededException **
The number of policy versions exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_CreatePolicyVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreatePolicyVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreatePolicyVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreatePolicyVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreatePolicyVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreatePolicyVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreatePolicyVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreatePolicyVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreatePolicyVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreatePolicyVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreatePolicyVersion)
