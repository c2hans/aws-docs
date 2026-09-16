---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListOpportunityFromEngagementTasks.html
---

# ListOpportunityFromEngagementTasks
<a name="API_ListOpportunityFromEngagementTasks"></a>

Lists all in-progress, completed, or failed opportunity creation tasks from engagements that were initiated by the caller's account.

## Request Syntax
<a name="API_ListOpportunityFromEngagementTasks_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ContextIdentifier": [ "{{string}}" ],
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
<a name="API_ListOpportunityFromEngagementTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListOpportunityFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-request-Catalog"></a>
Specifies the catalog related to the request. Valid values are `AWS` for production environments and `Sandbox` for testing or development purposes. The catalog determines which environment the task data is retrieved from.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ContextIdentifier](#API_ListOpportunityFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-request-ContextIdentifier"></a>
Filters tasks by the identifiers of the engagement contexts associated with the opportunity creation. Use this to find tasks related to specific contextual information within engagements that are being converted to opportunities.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `[1-9][0-9]*`
Required: No

 ** [EngagementIdentifier](#API_ListOpportunityFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-request-EngagementIdentifier"></a>
Filters tasks by the identifiers of the engagements from which opportunities are being created. Use this to find all opportunity creation tasks associated with a specific engagement.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `(arn:.*|eng-[0-9a-z]{14})`
Required: No

 ** [MaxResults](#API_ListOpportunityFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-request-MaxResults"></a>
Specifies the maximum number of results to return in a single page of the response. Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListOpportunityFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-request-NextToken"></a>
The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages.
Type: String
Pattern: `(?s).{1,2048}`
Required: No

 ** [OpportunityIdentifier](#API_ListOpportunityFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-request-OpportunityIdentifier"></a>
Filters tasks by the identifiers of the opportunities they created or are associated with. Use this to find tasks related to specific opportunity creation processes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `O[0-9]{1,19}`
Required: No

 ** [Sort](#API_ListOpportunityFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-request-Sort"></a>
 Defines the sorting parameters for listing tasks. This structure allows for specifying the field to sort by and the order of sorting.
Type: [ListTasksSortBase](API_ListTasksSortBase.md) object
Required: No

 ** [TaskIdentifier](#API_ListOpportunityFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-request-TaskIdentifier"></a>
Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. Provide the task ID to get details about a particular opportunity creation task.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `(arn:.*|task-[0-9a-z]{13})`
Required: No

 ** [TaskStatus](#API_ListOpportunityFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-request-TaskStatus"></a>
Filters the tasks based on their current status. This allows you to focus on tasks in specific states. Valid values are `COMPLETE` for tasks that have finished successfully, `INPROGRESS` for tasks that are currently running, and `FAILED` for tasks that have encountered an error and failed to complete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`
Required: No

## Response Syntax
<a name="API_ListOpportunityFromEngagementTasks_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TaskSummaries": [
      {
         "ContextId": "string",
         "EngagementId": "string",
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
<a name="API_ListOpportunityFromEngagementTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOpportunityFromEngagementTasks_ResponseSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-response-NextToken"></a>
A token used for pagination to retrieve the next page of results. If there are more results available, this field will contain a token that can be used in a subsequent API call to retrieve the next page. If there are no more results, this field will be null or an empty string.
Type: String

 ** [TaskSummaries](#API_ListOpportunityFromEngagementTasks_ResponseSyntax) **   <a name="AWSPartnerCentral-ListOpportunityFromEngagementTasks-response-TaskSummaries"></a>
An array of `ListOpportunityFromEngagementTaskSummary` objects, each representing a task that matches the specified filters. The array may be empty if no tasks match the criteria.
Type: Array of [ListOpportunityFromEngagementTaskSummary](API_ListOpportunityFromEngagementTaskSummary.md) objects

## Errors
<a name="API_ListOpportunityFromEngagementTasks_Errors"></a>

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
<a name="API_ListOpportunityFromEngagementTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTasks)
