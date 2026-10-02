---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PutAgentRecommendationPolicy.html
---

# PutAgentRecommendationPolicy
<a name="API_PutAgentRecommendationPolicy"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Attaches or replaces a resource-based policy on an individual Agent Recommendation. The policy controls cross-account access to the recommendation and its child resources such as items and remediations. The recommendation owner or any principal with profile write access on the parent profile can call this operation. The policy must be valid IAM JSON with Allow-only statements and no negation condition operators.

## Request Syntax
<a name="API_PutAgentRecommendationPolicy_RequestSyntax"></a>

```
PUT /api/v1/agent-recommendations/{{recommendationArn}}/policy HTTP/1.1
Content-type: application/json

{
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutAgentRecommendationPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recommendationArn](#API_PutAgentRecommendationPolicy_RequestSyntax) **   <a name="wellarchitected-PutAgentRecommendationPolicy-request-uri-recommendationArn"></a>
The ARN of the Agent Recommendation to attach the policy to.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-recommendation/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_PutAgentRecommendationPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policy](#API_PutAgentRecommendationPolicy_RequestSyntax) **   <a name="wellarchitected-PutAgentRecommendationPolicy-request-policy"></a>
The IAM resource-based policy document in JSON format. Maximum size 50KB.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

## Response Syntax
<a name="API_PutAgentRecommendationPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutAgentRecommendationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAgentRecommendationPolicy_Errors"></a>

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
<a name="API_PutAgentRecommendationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/PutAgentRecommendationPolicy)
