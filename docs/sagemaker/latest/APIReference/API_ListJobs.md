---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListJobs.html
---

# ListJobs
<a name="API_ListJobs"></a>

Lists jobs in a specified category. You can filter results by creation time, last modified time, name, and status. Results are sorted by the field you specify in `SortBy`. Use pagination to retrieve large result sets efficiently.

The following operations are related to `ListJobs`:
+  `CreateJob`
+  `DescribeJob`

## Request Syntax
<a name="API_ListJobs_RequestSyntax"></a>

```
{
   "JobCategory": "{{string}}",
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobCategory](#API_ListJobs_RequestSyntax) **   <a name="sagemaker-ListJobs-request-JobCategory"></a>
The category of jobs to list.
Type: String
Valid Values: `AgentRFT | AgentRFTEvaluation`
Required: Yes

 ** [MaxResults](#API_ListJobs_RequestSyntax) **   <a name="sagemaker-ListJobs-request-MaxResults"></a>
The maximum number of jobs to return in the response. The default value is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListJobs_RequestSyntax) **   <a name="sagemaker-ListJobs-request-NameContains"></a>
A string in the job name to filter results. Only jobs whose name contains the specified string are returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListJobs_RequestSyntax) **   <a name="sagemaker-ListJobs-request-NextToken"></a>
If the previous response was truncated, this token retrieves the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListJobs_RequestSyntax) **   <a name="sagemaker-ListJobs-request-SortBy"></a>
The field to sort results by.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListJobs_RequestSyntax) **   <a name="sagemaker-ListJobs-request-SortOrder"></a>
The sort order for results. Valid values are `Ascending` and `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListJobs_RequestSyntax) **   <a name="sagemaker-ListJobs-request-StatusEquals"></a>
A filter that returns only jobs with the specified status.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting | DeleteFailed`
Required: No

## Response Syntax
<a name="API_ListJobs_ResponseSyntax"></a>

```
{
   "JobSummaries": [
      {
         "JobArn": "string",
         "JobCategory": "string",
         "JobName": "string",
         "JobSecondaryStatus": "string",
         "JobStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobSummaries](#API_ListJobs_ResponseSyntax) **   <a name="sagemaker-ListJobs-response-JobSummaries"></a>
An array of `JobSummary` objects that provide summary information about the jobs.
Type: Array of [JobSummary](API_JobSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_ListJobs_ResponseSyntax) **   <a name="sagemaker-ListJobs-response-NextToken"></a>
If the response is truncated, this token retrieves the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListJobs)
