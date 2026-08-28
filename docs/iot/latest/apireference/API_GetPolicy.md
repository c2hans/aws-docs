---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetPolicy.html
---

# GetPolicy
<a name="API_GetPolicy"></a>

Gets information about the specified policy with the policy document of the default version.

Requires permission to access the [GetPolicy](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetPolicy_RequestSyntax"></a>

```
GET /policies/{{policyName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyName](#API_GetPolicy_RequestSyntax) **   <a name="iot-GetPolicy-request-uri-policyName"></a>
The name of the policy.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Request Body
<a name="API_GetPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDate": number,
   "defaultVersionId": "string",
   "generationId": "string",
   "lastModifiedDate": number,
   "policyArn": "string",
   "policyDocument": "string",
   "policyName": "string"
}
```

## Response Elements
<a name="API_GetPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_GetPolicy_ResponseSyntax) **   <a name="iot-GetPolicy-response-creationDate"></a>
The date the policy was created.
Type: Timestamp

 ** [defaultVersionId](#API_GetPolicy_ResponseSyntax) **   <a name="iot-GetPolicy-response-defaultVersionId"></a>
The default policy version ID.
Type: String
Pattern: `[0-9]+`

 ** [generationId](#API_GetPolicy_ResponseSyntax) **   <a name="iot-GetPolicy-response-generationId"></a>
The generation ID of the policy.
Type: String

 ** [lastModifiedDate](#API_GetPolicy_ResponseSyntax) **   <a name="iot-GetPolicy-response-lastModifiedDate"></a>
The date the policy was last modified.
Type: Timestamp

 ** [policyArn](#API_GetPolicy_ResponseSyntax) **   <a name="iot-GetPolicy-response-policyArn"></a>
The policy ARN.
Type: String

 ** [policyDocument](#API_GetPolicy_ResponseSyntax) **   <a name="iot-GetPolicy-response-policyDocument"></a>
The JSON document that describes the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 404600.
Pattern: `[\s\S]*`

 ** [policyName](#API_GetPolicy_ResponseSyntax) **   <a name="iot-GetPolicy-response-policyName"></a>
The policy name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`

## Errors
<a name="API_GetPolicy_Errors"></a>

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
<a name="API_GetPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
