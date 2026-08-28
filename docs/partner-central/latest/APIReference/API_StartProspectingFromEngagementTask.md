---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartProspectingFromEngagementTask.html
---

# StartProspectingFromEngagementTask
<a name="API_StartProspectingFromEngagementTask"></a>

Starts a task to convert one or more engagement contexts into new prospecting leads. The task runs asynchronously. To poll for status, use `GetProspectingFromEngagementTask`, or use `ListProspectingFromEngagementTasks` to monitor multiple tasks.

## Request Syntax
<a name="API_StartProspectingFromEngagementTask_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Identifiers": [ "{{string}}" ],
   "TaskName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartProspectingFromEngagementTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_StartProspectingFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-request-Catalog"></a>
Specifies the catalog in which the task is initiated. Specify `AWS` for production environments and `Sandbox` for testing and development purposes.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_StartProspectingFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-request-ClientToken"></a>
A unique, case-sensitive identifier provided by the client to ensure idempotency. Making the same request with the same `ClientToken` returns the same response without creating a duplicate task.
Type: String
Pattern: `.{1,255}`
Required: Yes

 ** [Identifiers](#API_StartProspectingFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-request-Identifiers"></a>
The list of engagement identifiers to include in this prospecting task. Each identifier must correspond to an existing engagement in the specified catalog. Maximum of 100 identifiers per task.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `eng-[0-9a-z]{14}`
Required: Yes

 ** [TaskName](#API_StartProspectingFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-request-TaskName"></a>
A descriptive name for the task. This name helps identify the task in list and get operations. The name must contain 1 to 128 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Syntax
<a name="API_StartProspectingFromEngagementTask_ResponseSyntax"></a>

```
{
   "Identifiers": [ "string" ],
   "Message": "string",
   "ReasonCode": "string",
   "StartTime": "string",
   "TaskArn": "string",
   "TaskId": "string",
   "TaskName": "string",
   "TaskStatus": "string"
}
```

## Response Elements
<a name="API_StartProspectingFromEngagementTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Identifiers](#API_StartProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-response-Identifiers"></a>
The list of engagement identifiers that were accepted into the task queue for processing. This list matches the identifiers provided in the request.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `eng-[0-9a-z]{14}`

 ** [StartTime](#API_StartProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-response-StartTime"></a>
The timestamp indicating when the task was initiated. The format follows ISO 8601 date-time notation.
Type: Timestamp

 ** [TaskName](#API_StartProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-response-TaskName"></a>
The task name from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [TaskStatus](#API_StartProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-response-TaskStatus"></a>
The current status of the task. Possible values: `PENDING` (waiting to run), `IN_PROGRESS` (actively processing), `COMPLETED` (successfully processed), and `FAILED` (unrecoverable error).
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED`

 ** [Message](#API_StartProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-response-Message"></a>
A message providing additional context about the task's current state. When the task fails, this field contains a detailed description of the failure and suggested recovery steps. This field is only populated for tasks in a failed state.
Type: String

 ** [ReasonCode](#API_StartProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-response-ReasonCode"></a>
An enumerated code identifying the reason for task failure. This field is only populated when the task has failed. Use the corresponding `Message` field for a human-readable description of the failure.
Type: String

 ** [TaskArn](#API_StartProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-response-TaskArn"></a>
The Amazon Resource Name (ARN) of the task. The ARN uniquely identifies the task across AWS and can be used for resource-level IAM policies.
Type: String
Pattern: `arn:aws:partnercentral-selling:.*:.*:catalog/.*/prospecting-from-engagement-task/task-[0-9a-z]{14}`

 ** [TaskId](#API_StartProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartProspectingFromEngagementTask-response-TaskId"></a>
The unique identifier assigned to this task. Use this identifier with `GetProspectingFromEngagementTask` to retrieve task details and check status.
Type: String
Pattern: `task-[0-9a-z]{14}`

## Errors
<a name="API_StartProspectingFromEngagementTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** ConflictException **
This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.
Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.
Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.
HTTP Status Code: 400

 ** ThrottlingException **
This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.
This error occurs when there are too many requests sent. Review the provided [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) and retry after the provided delay.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service or business validation rules.
Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.
 ** ErrorList **
A list of issues that were discovered in the submitted request or the resource state.
 ** Reason **
The primary reason for this validation exception to occur.
+  *REQUEST\_VALIDATION\_FAILED:* The request format is not valid.

  Fix: Verify your request payload includes all required fields, uses correct data types and string formats.
+  *BUSINESS\_VALIDATION\_FAILED:* The requested change doesn't pass the business validation rules.

  Fix: Check that your change aligns with the business rules defined by AWS Partner Central.
HTTP Status Code: 400

## See Also
<a name="API_StartProspectingFromEngagementTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/StartProspectingFromEngagementTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
