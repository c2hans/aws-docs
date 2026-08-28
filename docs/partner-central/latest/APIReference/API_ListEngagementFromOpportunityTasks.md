---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementFromOpportunityTasks.html
---

# ListEngagementFromOpportunityTasks
<a name="API_ListEngagementFromOpportunityTasks"></a>

 Lists all in-progress, completed, or failed `EngagementFromOpportunity` tasks that were initiated by the caller's account.

## Request Syntax
<a name="API_ListEngagementFromOpportunityTasks_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "EngagementIdentifier": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OpportunityIdentifier": [ "{{string}}" ],
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   },
   "TaskIdentifier": [ "{{string}}" ],
   "TaskStatus": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListEngagementFromOpportunityTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListEngagementFromOpportunityTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-request-Catalog"></a>
 Specifies the catalog related to the request. Valid values are:
+  AWS: Retrieves the request from the production AWS environment.
+  Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [EngagementIdentifier](#API_ListEngagementFromOpportunityTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-request-EngagementIdentifier"></a>
 Filters tasks by the identifiers of the engagements they created or are associated with.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `(arn:.*|eng-[0-9a-z]{14})`
Required: No

 ** [MaxResults](#API_ListEngagementFromOpportunityTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-request-MaxResults"></a>
 Specifies the maximum number of results to return in a single page of the response.Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListEngagementFromOpportunityTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-request-NextToken"></a>
 The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages.
Type: String
Pattern: `(?s).{1,2048}`
Required: No

 ** [OpportunityIdentifier](#API_ListEngagementFromOpportunityTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-request-OpportunityIdentifier"></a>
 The identifier of the original opportunity associated with this task.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `O[0-9]{1,19}`
Required: No

 ** [Sort](#API_ListEngagementFromOpportunityTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-request-Sort"></a>
 Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes.
Type: [ListTasksSortBase](API_ListTasksSortBase.md) object
Required: No

 ** [TaskIdentifier](#API_ListEngagementFromOpportunityTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-request-TaskIdentifier"></a>
 Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `(arn:.*|task-[0-9a-z]{13})`
Required: No

 ** [TaskStatus](#API_ListEngagementFromOpportunityTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-request-TaskStatus"></a>
 Filters the tasks based on their current status. This allows you to focus on tasks in specific states.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`
Required: No

## Response Syntax
<a name="API_ListEngagementFromOpportunityTasks_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TaskSummaries": [
      {
         "EngagementId": "string",
         "EngagementInvitationId": "string",
         "Message": "string",
         "OpportunityId": "string",
         "ReasonCode": "string",
         "ResourceSnapshotJobId": "string",
         "StartTime": "string",
         "TaskArn": "string",
         "TaskId": "string",
         "TaskStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListEngagementFromOpportunityTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListEngagementFromOpportunityTasks_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-response-NextToken"></a>
 A token used for pagination to retrieve the next page of results. If there are more results available, this field will contain a token that can be used in a subsequent API call to retrieve the next page. If there are no more results, this field will be null or an empty string.
Type: String

 ** [TaskSummaries](#API_ListEngagementFromOpportunityTasks_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagementFromOpportunityTasks-response-TaskSummaries"></a>
 TaskSummaries An array of TaskSummary objects containing details about each task.
Type: Array of [ListEngagementFromOpportunityTaskSummary](API_ListEngagementFromOpportunityTaskSummary.md) objects

## Errors
<a name="API_ListEngagementFromOpportunityTasks_Errors"></a>

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
<a name="API_ListEngagementFromOpportunityTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
