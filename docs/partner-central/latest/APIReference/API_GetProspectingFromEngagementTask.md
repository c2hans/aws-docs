---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetProspectingFromEngagementTask.html
---

# GetProspectingFromEngagementTask
<a name="API_GetProspectingFromEngagementTask"></a>

Retrieves the details and current status of a prospecting task previously started with `StartProspectingFromEngagementTask` to enable polling for completion and access to per-engagement processing results.

## Request Syntax
<a name="API_GetProspectingFromEngagementTask_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "TaskIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetProspectingFromEngagementTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetProspectingFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-GetProspectingFromEngagementTask-request-Catalog"></a>
Specifies the catalog associated with the task. Specify `AWS` for production environments and `Sandbox` for testing and development purposes. The value must match the catalog used when the task was created.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [TaskIdentifier](#API_GetProspectingFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-GetProspectingFromEngagementTask-request-TaskIdentifier"></a>
The unique identifier of the prospecting task to retrieve. This value is returned in the `TaskId` field of the `StartProspectingFromEngagementTask` response.
Type: String
Pattern: `task-[0-9a-z]{14}`
Required: Yes

## Response Syntax
<a name="API_GetProspectingFromEngagementTask_ResponseSyntax"></a>

```
{
   "EndTime": "string",
   "Engagements": [
      {
         "EngagementContextId": "string",
         "EngagementIdentifier": "string",
         "Message": "string",
         "ReasonCode": "string",
         "Status": "string"
      }
   ],
   "StartTime": "string",
   "TaskArn": "string",
   "TaskId": "string",
   "TaskName": "string"
}
```

## Response Elements
<a name="API_GetProspectingFromEngagementTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Engagements](#API_GetProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-GetProspectingFromEngagementTask-response-Engagements"></a>
An array of `EngagementProspectingResult` entries for each engagement in the task. Each entry contains the processing status. For successfully completed engagements, includes the prospecting context identifier. For failed engagements, includes an error code and message.
Type: Array of [EngagementProspectingResult](API_EngagementProspectingResult.md) objects

 ** [StartTime](#API_GetProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-GetProspectingFromEngagementTask-response-StartTime"></a>
The timestamp indicating when the task was initiated. The format follows ISO 8601 date-time notation.
Type: Timestamp

 ** [TaskArn](#API_GetProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-GetProspectingFromEngagementTask-response-TaskArn"></a>
The Amazon Resource Name (ARN) of the task.
Type: String
Pattern: `arn:aws:partnercentral-selling:.*:.*:catalog/.*/prospecting-from-engagement-task/task-[0-9a-z]{14}`

 ** [TaskId](#API_GetProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-GetProspectingFromEngagementTask-response-TaskId"></a>
The unique identifier of the task.
Type: String
Pattern: `task-[0-9a-z]{14}`

 ** [TaskName](#API_GetProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-GetProspectingFromEngagementTask-response-TaskName"></a>
The descriptive name of the task that you provided when you created it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [EndTime](#API_GetProspectingFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-GetProspectingFromEngagementTask-response-EndTime"></a>
The timestamp indicating when the task finished processing. This field is absent if the task is still in progress. The format follows ISO 8601 date-time notation.
Type: Timestamp

## Errors
<a name="API_GetProspectingFromEngagementTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Reason **
The reason why access was denied for the requested operation.
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
<a name="API_GetProspectingFromEngagementTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetProspectingFromEngagementTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
