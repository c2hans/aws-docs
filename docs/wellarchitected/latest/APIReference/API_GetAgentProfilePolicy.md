---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentProfilePolicy.html
---

# GetAgentProfilePolicy
<a name="API_GetAgentProfilePolicy"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Retrieves the resource-based policy attached to an Agent Profile. Only the profile owner can call this operation.

## Request Syntax
<a name="API_GetAgentProfilePolicy_RequestSyntax"></a>

```
GET /api/v1/agent-profiles/{{profileArn}}/policy HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentProfilePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileArn](#API_GetAgentProfilePolicy_RequestSyntax) **   <a name="wellarchitected-GetAgentProfilePolicy-request-uri-profileArn"></a>
The ARN of the Agent Profile whose policy to retrieve.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_GetAgentProfilePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentProfilePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": "string",
   "profileArn": "string"
}
```

## Response Elements
<a name="API_GetAgentProfilePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_GetAgentProfilePolicy_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfilePolicy-response-policy"></a>
The IAM resource-based policy document in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

 ** [profileArn](#API_GetAgentProfilePolicy_ResponseSyntax) **   <a name="wellarchitected-GetAgentProfilePolicy-response-profileArn"></a>
The ARN of the Agent Profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`

## Errors
<a name="API_GetAgentProfilePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetAgentProfilePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetAgentProfilePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetAgentProfilePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetAgentProfilePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetAgentProfilePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetAgentProfilePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetAgentProfilePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetAgentProfilePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetAgentProfilePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetAgentProfilePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetAgentProfilePolicy)
