---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentGoal.html
---

# CreateAgentGoal
<a name="API_CreateAgentGoal"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Creates an optimization goal associated with a profile. Goals define specific targets and objectives for the optimization process.

## Request Syntax
<a name="API_CreateAgentGoal_RequestSyntax"></a>

```
POST /api/v1/agent-profiles/{{profileArn}}/goals HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "pillars": [ "{{string}}" ],
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAgentGoal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileArn](#API_CreateAgentGoal_RequestSyntax) **   <a name="wellarchitected-CreateAgentGoal-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the profile to associate the goal with.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_CreateAgentGoal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAgentGoal_RequestSyntax) **   <a name="wellarchitected-CreateAgentGoal-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_CreateAgentGoal_RequestSyntax) **   <a name="wellarchitected-CreateAgentGoal-request-description"></a>
A description of the goal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: No

 ** [pillars](#API_CreateAgentGoal_RequestSyntax) **   <a name="wellarchitected-CreateAgentGoal-request-pillars"></a>
The AWS Well-Architected Framework pillars to associate with this goal.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

 ** [title](#API_CreateAgentGoal_RequestSyntax) **   <a name="wellarchitected-CreateAgentGoal-request-title"></a>
The title of the goal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: Yes

## Response Syntax
<a name="API_CreateAgentGoal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "goal": {
      "createdAt": "string",
      "createdBy": "string",
      "description": "string",
      "id": "string",
      "lastModifiedAt": "string",
      "lastModifiedBy": "string",
      "pillars": [ "string" ],
      "profileArn": "string",
      "title": "string"
   }
}
```

## Response Elements
<a name="API_CreateAgentGoal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [goal](#API_CreateAgentGoal_ResponseSyntax) **   <a name="wellarchitected-CreateAgentGoal-response-goal"></a>
The created goal summary.
Type: [GoalSummary](API_GoalSummary.md) object

## Errors
<a name="API_CreateAgentGoal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

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
<a name="API_CreateAgentGoal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateAgentGoal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateAgentGoal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateAgentGoal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateAgentGoal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateAgentGoal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateAgentGoal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateAgentGoal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateAgentGoal)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateAgentGoal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateAgentGoal)
