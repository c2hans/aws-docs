---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAutoMLJobs.html
---

# ListAutoMLJobs
<a name="API_ListAutoMLJobs"></a>

Request a list of jobs.

## Request Syntax
<a name="API_ListAutoMLJobs_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "LastModifiedTimeAfter": {{number}},
   "LastModifiedTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAutoMLJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-CreationTimeAfter"></a>
Request a list of jobs, using a filter for time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-CreationTimeBefore"></a>
Request a list of jobs, using a filter for time.
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-LastModifiedTimeAfter"></a>
Request a list of jobs, using a filter for time.
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-LastModifiedTimeBefore"></a>
Request a list of jobs, using a filter for time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-MaxResults"></a>
Request a list of jobs up to a specified limit.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-NameContains"></a>
Request a list of jobs, using a search filter for name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-SortBy"></a>
The parameter by which to sort the results. The default is `Name`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-SortOrder"></a>
The sort order for the results. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListAutoMLJobs_RequestSyntax) **   <a name="sagemaker-ListAutoMLJobs-request-StatusEquals"></a>
Request a list of jobs, using a filter for status.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping`
Required: No

## Response Syntax
<a name="API_ListAutoMLJobs_ResponseSyntax"></a>

```
{
   "AutoMLJobSummaries": [
      {
         "AutoMLJobArn": "string",
         "AutoMLJobName": "string",
         "AutoMLJobSecondaryStatus": "string",
         "AutoMLJobStatus": "string",
         "CreationTime": number,
         "EndTime": number,
         "FailureReason": "string",
         "LastModifiedTime": number,
         "PartialFailureReasons": [
            {
               "PartialFailureMessage": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAutoMLJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoMLJobSummaries](#API_ListAutoMLJobs_ResponseSyntax) **   <a name="sagemaker-ListAutoMLJobs-response-AutoMLJobSummaries"></a>
Returns a summary list of jobs.
Type: Array of [AutoMLJobSummary](API_AutoMLJobSummary.md) objects

 ** [NextToken](#API_ListAutoMLJobs_ResponseSyntax) **   <a name="sagemaker-ListAutoMLJobs-response-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListAutoMLJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListAutoMLJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListAutoMLJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListAutoMLJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListAutoMLJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListAutoMLJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListAutoMLJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListAutoMLJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListAutoMLJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListAutoMLJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListAutoMLJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListAutoMLJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
