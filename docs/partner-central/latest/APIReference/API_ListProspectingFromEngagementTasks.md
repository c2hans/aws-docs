---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListProspectingFromEngagementTasks.html
---

# ListProspectingFromEngagementTasks
<a name="API_ListProspectingFromEngagementTasks"></a>

Lists all prospecting tasks initiated by the caller's account. Supports optional filters by task identifier, task name, or start time range. Results can be sorted using configurable options. The response is paginated. Use the `NextToken` value from each response to retrieve subsequent pages.

## Request Syntax
<a name="API_ListProspectingFromEngagementTasks_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   },
   "StartAfter": "{{string}}",
   "StartBefore": "{{string}}",
   "TaskIdentifier": [ "{{string}}" ],
   "TaskName": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListProspectingFromEngagementTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListProspectingFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-request-Catalog"></a>
Specifies the catalog to list tasks from. Specify `AWS` for production environments and `Sandbox` for testing and development purposes.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [MaxResults](#API_ListProspectingFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-request-MaxResults"></a>
The maximum number of results to return in a single page. If additional results exist, the response includes a `NextToken` value for retrieving the next page. If omitted, the API uses a service-defined default page size.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListProspectingFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-request-NextToken"></a>
The pagination token from a previous call to this API. Include this value to retrieve the next page of results. If omitted, the first page is returned.
Type: String
Required: No

 ** [Sort](#API_ListProspectingFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-request-Sort"></a>
Specifies the field and order used to sort the returned tasks. If omitted, tasks are returned in the default sort order.
Type: [ProspectingFromEngagementTaskSort](API_ProspectingFromEngagementTaskSort.md) object
Required: No

 ** [StartAfter](#API_ListProspectingFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-request-StartAfter"></a>
Filters tasks to include only those that started after the specified timestamp. Use this with `StartBefore` to define a start-time range for your query. The format follows ISO 8601 date-time notation.
Type: Timestamp
Required: No

 ** [StartBefore](#API_ListProspectingFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-request-StartBefore"></a>
Filters tasks to include only those that started before the specified timestamp. Use this with `StartAfter` to define a start-time range for your query. The format follows ISO 8601 date-time notation.
Type: Timestamp
Required: No

 ** [TaskIdentifier](#API_ListProspectingFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-request-TaskIdentifier"></a>
Filters the results to include only the tasks with the specified identifiers. Provide up to 10 task IDs to narrow the list to specific tasks. If omitted, tasks are not filtered by identifier.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Pattern: `task-[0-9a-z]{14}`
Required: No

 ** [TaskName](#API_ListProspectingFromEngagementTasks_RequestSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-request-TaskName"></a>
Filters the results to include only tasks with the specified names. Provide up to 10 task names to narrow the list. If omitted, tasks are not filtered by name.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_ListProspectingFromEngagementTasks_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TaskSummaries": [
      {
         "CompletedEngagementCount": number,
         "EndTime": "string",
         "FailedEngagementCount": number,
         "StartTime": "string",
         "TaskArn": "string",
         "TaskId": "string",
         "TaskName": "string",
         "TotalEngagementCount": number
      }
   ]
}
```

## Response Elements
<a name="API_ListProspectingFromEngagementTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TaskSummaries](#API_ListProspectingFromEngagementTasks_ResponseSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-response-TaskSummaries"></a>
Prospecting task summaries matching the specified filters. Each summary includes the task identifier, name, status counters, and timing information. If no tasks match the filter criteria, the list is empty.
Type: Array of [ProspectingTaskSummary](API_ProspectingTaskSummary.md) objects

 ** [NextToken](#API_ListProspectingFromEngagementTasks_ResponseSyntax) **   <a name="AWSPartnerCentral-ListProspectingFromEngagementTasks-response-NextToken"></a>
A pagination token used to retrieve the next page of results. If this field is present, pass its value as `NextToken` in the next call. If absent or empty, there are no further pages.
Type: String
Pattern: `(?s).{1,2048}`

## Errors
<a name="API_ListProspectingFromEngagementTasks_Errors"></a>

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
<a name="API_ListProspectingFromEngagementTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListProspectingFromEngagementTasks)
