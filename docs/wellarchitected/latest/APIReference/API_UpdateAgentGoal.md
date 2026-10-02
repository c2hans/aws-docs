---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentGoal.html
---

# UpdateAgentGoal
<a name="API_UpdateAgentGoal"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Updates the pillars and title of an existing goal associated with a profile.

## Request Syntax
<a name="API_UpdateAgentGoal_RequestSyntax"></a>

```
PUT /api/v1/agent-profiles/{{profileArn}}/goals/{{id}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "pillars": [ "{{string}}" ],
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAgentGoal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateAgentGoal_RequestSyntax) **   <a name="wellarchitected-UpdateAgentGoal-request-uri-id"></a>
The unique identifier of the goal to update.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [profileArn](#API_UpdateAgentGoal_RequestSyntax) **   <a name="wellarchitected-UpdateAgentGoal-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the profile containing the goal to update.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_UpdateAgentGoal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateAgentGoal_RequestSyntax) **   <a name="wellarchitected-UpdateAgentGoal-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_UpdateAgentGoal_RequestSyntax) **   <a name="wellarchitected-UpdateAgentGoal-request-description"></a>
A description of the goal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: No

 ** [pillars](#API_UpdateAgentGoal_RequestSyntax) **   <a name="wellarchitected-UpdateAgentGoal-request-pillars"></a>
The updated pillars for the goal. Pillars define the optimization focus areas such as cost, performance, resilience, and operational excellence.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: No

 ** [title](#API_UpdateAgentGoal_RequestSyntax) **   <a name="wellarchitected-UpdateAgentGoal-request-title"></a>
The updated title for the goal. Maximum length of 1000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: No

## Response Syntax
<a name="API_UpdateAgentGoal_ResponseSyntax"></a>

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
<a name="API_UpdateAgentGoal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [goal](#API_UpdateAgentGoal_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentGoal-response-goal"></a>
The updated goal summary.
Type: [GoalSummary](API_GoalSummary.md) object

## Errors
<a name="API_UpdateAgentGoal_Errors"></a>

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
<a name="API_UpdateAgentGoal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateAgentGoal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateAgentGoal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateAgentGoal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateAgentGoal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateAgentGoal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateAgentGoal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateAgentGoal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateAgentGoal)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateAgentGoal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateAgentGoal)
