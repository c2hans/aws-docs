---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PutAgentProfilePolicy.html
---

# PutAgentProfilePolicy
<a name="API_PutAgentProfilePolicy"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Attaches or replaces a resource-based policy on an Agent Profile. The policy controls cross-account access to the profile and its child resources such as recommendations, goals, and contexts. Only the profile owner can call this operation. The policy must be valid IAM JSON with Allow-only statements and no negation condition operators.

## Request Syntax
<a name="API_PutAgentProfilePolicy_RequestSyntax"></a>

```
PUT /api/v1/agent-profiles/{{profileArn}}/policy HTTP/1.1
Content-type: application/json

{
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutAgentProfilePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileArn](#API_PutAgentProfilePolicy_RequestSyntax) **   <a name="wellarchitected-PutAgentProfilePolicy-request-uri-profileArn"></a>
The ARN of the Agent Profile to attach the policy to.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_PutAgentProfilePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policy](#API_PutAgentProfilePolicy_RequestSyntax) **   <a name="wellarchitected-PutAgentProfilePolicy-request-policy"></a>
The IAM resource-based policy document in JSON format. Maximum size 50KB.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

## Response Syntax
<a name="API_PutAgentProfilePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutAgentProfilePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAgentProfilePolicy_Errors"></a>

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
<a name="API_PutAgentProfilePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/PutAgentProfilePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/PutAgentProfilePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/PutAgentProfilePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/PutAgentProfilePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/PutAgentProfilePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/PutAgentProfilePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/PutAgentProfilePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/PutAgentProfilePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/PutAgentProfilePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/PutAgentProfilePolicy)
