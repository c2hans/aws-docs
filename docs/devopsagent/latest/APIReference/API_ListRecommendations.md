---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListRecommendations.html
---

# ListRecommendations
<a name="API_ListRecommendations"></a>

Lists recommendations for the specified agent space

## Request Syntax
<a name="API_ListRecommendations_RequestSyntax"></a>

```
POST /backlog/agent-space/{{agentSpaceId}}/recommendations/list HTTP/1.1
Content-type: application/json

{
   "goalId": "{{string}}",
   "limit": {{number}},
   "nextToken": "{{string}}",
   "priority": "{{string}}",
   "status": "{{string}}",
   "taskId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_ListRecommendations_RequestSyntax) **   <a name="devopsagent-ListRecommendations-request-uri-agentSpaceId"></a>
The unique identifier for the agent space containing the recommendations
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_ListRecommendations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [goalId](#API_ListRecommendations_RequestSyntax) **   <a name="devopsagent-ListRecommendations-request-goalId"></a>
Optional goal ID to filter recommendations by specific goal
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [limit](#API_ListRecommendations_RequestSyntax) **   <a name="devopsagent-ListRecommendations-request-limit"></a>
Maximum number of recommendations to return in a single response
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListRecommendations_RequestSyntax) **   <a name="devopsagent-ListRecommendations-request-nextToken"></a>
Token for retrieving the next page of results
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [priority](#API_ListRecommendations_RequestSyntax) **   <a name="devopsagent-ListRecommendations-request-priority"></a>
Optional priority to filter recommendations by priority level
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: No

 ** [status](#API_ListRecommendations_RequestSyntax) **   <a name="devopsagent-ListRecommendations-request-status"></a>
Optional status to filter recommendations by their current status
Type: String
Valid Values: `PROPOSED | ACCEPTED | REJECTED | CLOSED | COMPLETED | UPDATE_IN_PROGRESS`
Required: No

 ** [taskId](#API_ListRecommendations_RequestSyntax) **   <a name="devopsagent-ListRecommendations-request-taskId"></a>
Optional task ID to filter recommendations by specific task
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_ListRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "recommendations": [
      {
         "additionalContext": "string",
         "agentSpaceArn": "string",
         "content": {
            "spec": "string",
            "summary": "string"
         },
         "createdAt": "string",
         "goalId": "string",
         "goalVersion": number,
         "priority": "string",
         "rankedAt": "string",
         "rankPosition": number,
         "recommendationId": "string",
         "status": "string",
         "taskId": "string",
         "title": "string",
         "updatedAt": "string",
         "version": number
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRecommendations_ResponseSyntax) **   <a name="devopsagent-ListRecommendations-response-nextToken"></a>
Token for retrieving the next page of results, if more results are available
Type: String

 ** [recommendations](#API_ListRecommendations_ResponseSyntax) **   <a name="devopsagent-ListRecommendations-response-recommendations"></a>
List of recommendations matching the request criteria
Type: Array of [Recommendation](API_Recommendation.md) objects

## Errors
<a name="API_ListRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/ListRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/ListRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ListRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/ListRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ListRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/ListRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/ListRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/ListRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/ListRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ListRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
