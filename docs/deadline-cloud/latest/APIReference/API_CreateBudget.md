---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateBudget.html
---

# CreateBudget
<a name="API_CreateBudget"></a>

Creates a budget to set spending thresholds for your rendering activity.

## Request Syntax
<a name="API_CreateBudget_RequestSyntax"></a>

```
POST /2023-10-12/farms/{{farmId}}/budgets HTTP/1.1
X-Amz-Client-Token: {{clientToken}}
Content-type: application/json

{
   "actions": [
      {
         "description": "{{string}}",
         "thresholdPercentage": {{number}},
         "type": "{{string}}"
      }
   ],
   "approximateDollarLimit": {{number}},
   "description": "{{string}}",
   "displayName": "{{string}}",
   "schedule": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "usageTrackingResource": { ... }
}
```

## URI Request Parameters
<a name="API_CreateBudget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_CreateBudget_RequestSyntax) **   <a name="deadlinecloud-CreateBudget-request-clientToken"></a>
The unique token which the server uses to recognize retries of the same request.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [farmId](#API_CreateBudget_RequestSyntax) **   <a name="deadlinecloud-CreateBudget-request-uri-farmId"></a>
The farm ID to include in this budget.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_CreateBudget_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_CreateBudget_RequestSyntax) **   <a name="deadlinecloud-CreateBudget-request-actions"></a>
The budget actions to specify what happens when the budget runs out.
Type: Array of [BudgetActionToAdd](API_BudgetActionToAdd.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** [approximateDollarLimit](#API_CreateBudget_RequestSyntax) **   <a name="deadlinecloud-CreateBudget-request-approximateDollarLimit"></a>
The dollar limit based on consumed usage.
Type: Float
Valid Range: Minimum value of 0.01.
Required: Yes

 ** [description](#API_CreateBudget_RequestSyntax) **   <a name="deadlinecloud-CreateBudget-request-description"></a>
The description of the budget.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** [displayName](#API_CreateBudget_RequestSyntax) **   <a name="deadlinecloud-CreateBudget-request-displayName"></a>
The display name of the budget.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [schedule](#API_CreateBudget_RequestSyntax) **   <a name="deadlinecloud-CreateBudget-request-schedule"></a>
The schedule to associate with this budget.
Type: [BudgetSchedule](API_BudgetSchedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [tags](#API_CreateBudget_RequestSyntax) **   <a name="deadlinecloud-CreateBudget-request-tags"></a>
Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.
Type: String to string map
Required: No

 ** [usageTrackingResource](#API_CreateBudget_RequestSyntax) **   <a name="deadlinecloud-CreateBudget-request-usageTrackingResource"></a>
The queue ID provided to this budget to track usage.
Type: [UsageTrackingResource](API_UsageTrackingResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateBudget_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "budgetId": "string"
}
```

## Response Elements
<a name="API_CreateBudget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [budgetId](#API_CreateBudget_ResponseSyntax) **   <a name="deadlinecloud-CreateBudget-response-budgetId"></a>
The budget ID.
Type: String
Pattern: `budget-[0-9a-f]{32}`

## Errors
<a name="API_CreateBudget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that has been exceeded.
 ** reason **
A string that describes the reason the quota was exceeded.
 ** resourceId **
The identifier of the affected resource.
 ** resourceType **
The type of the affected resource
 ** serviceCode **
Identifies the service that exceeded the quota.
HTTP Status Code: 402

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateBudget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateBudget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/CreateBudget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateBudget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateBudget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateBudget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateBudget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateBudget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateBudget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateBudget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateBudget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
