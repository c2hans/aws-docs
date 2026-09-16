---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePolicy.html
---

# CreatePolicy
<a name="API_CreatePolicy"></a>

Creates an AWS IoT policy.

The created policy is the default version for the policy. This operation creates a policy version with a version identifier of **1** and sets **1** as the policy's default version.

Requires permission to access the [CreatePolicy](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreatePolicy_RequestSyntax"></a>

```
POST /policies/{{policyName}} HTTP/1.1
Content-type: application/json

{
   "policyDocument": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreatePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyName](#API_CreatePolicy_RequestSyntax) **   <a name="iot-CreatePolicy-request-uri-policyName"></a>
The policy name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Request Body
<a name="API_CreatePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policyDocument](#API_CreatePolicy_RequestSyntax) **   <a name="iot-CreatePolicy-request-policyDocument"></a>
The JSON document that describes the policy. **policyDocument** must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 404600.
Pattern: `[\s\S]*`
Required: Yes

 ** [tags](#API_CreatePolicy_RequestSyntax) **   <a name="iot-CreatePolicy-request-tags"></a>
Metadata which can be used to manage the policy.
For URI Request parameters use format: ...key1=value1&key2=value2...
For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."
For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreatePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policyArn": "string",
   "policyDocument": "string",
   "policyName": "string",
   "policyVersionId": "string"
}
```

## Response Elements
<a name="API_CreatePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyArn](#API_CreatePolicy_ResponseSyntax) **   <a name="iot-CreatePolicy-response-policyArn"></a>
The policy ARN.
Type: String

 ** [policyDocument](#API_CreatePolicy_ResponseSyntax) **   <a name="iot-CreatePolicy-response-policyDocument"></a>
The JSON document that describes the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 404600.
Pattern: `[\s\S]*`

 ** [policyName](#API_CreatePolicy_ResponseSyntax) **   <a name="iot-CreatePolicy-response-policyName"></a>
The policy name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`

 ** [policyVersionId](#API_CreatePolicy_ResponseSyntax) **   <a name="iot-CreatePolicy-response-policyVersionId"></a>
The policy version ID.
Type: String
Pattern: `[0-9]+`

## Errors
<a name="API_CreatePolicy_Errors"></a>

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
<a name="API_CreatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreatePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreatePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreatePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreatePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreatePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreatePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreatePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreatePolicy)
