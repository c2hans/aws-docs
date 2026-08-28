---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCompilationJobs.html
---

# ListCompilationJobs
<a name="API_ListCompilationJobs"></a>

Lists model compilation jobs that satisfy various filters.

To create a model compilation job, use [CreateCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCompilationJob.html). To get information about a particular model compilation job you have created, use [DescribeCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCompilationJob.html).

## Request Syntax
<a name="API_ListCompilationJobs_RequestSyntax"></a>

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
<a name="API_ListCompilationJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-CreationTimeAfter"></a>
A filter that returns the model compilation jobs that were created after a specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-CreationTimeBefore"></a>
A filter that returns the model compilation jobs that were created before a specified time.
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-LastModifiedTimeAfter"></a>
A filter that returns the model compilation jobs that were modified after a specified time.
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-LastModifiedTimeBefore"></a>
A filter that returns the model compilation jobs that were modified before a specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-MaxResults"></a>
The maximum number of model compilation jobs to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-NameContains"></a>
A filter that returns the model compilation jobs whose name contains a specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-NextToken"></a>
If the result of the previous `ListCompilationJobs` request was truncated, the response includes a `NextToken`. To retrieve the next set of model compilation jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-SortBy"></a>
The field by which to sort results. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-SortOrder"></a>
The sort order for results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListCompilationJobs_RequestSyntax) **   <a name="sagemaker-ListCompilationJobs-request-StatusEquals"></a>
A filter that retrieves model compilation jobs with a specific `CompilationJobStatus` status.
Type: String
Valid Values: `INPROGRESS | COMPLETED | FAILED | STARTING | STOPPING | STOPPED`
Required: No

## Response Syntax
<a name="API_ListCompilationJobs_ResponseSyntax"></a>

```
{
   "CompilationJobSummaries": [
      {
         "CompilationEndTime": number,
         "CompilationJobArn": "string",
         "CompilationJobName": "string",
         "CompilationJobStatus": "string",
         "CompilationStartTime": number,
         "CompilationTargetDevice": "string",
         "CompilationTargetPlatformAccelerator": "string",
         "CompilationTargetPlatformArch": "string",
         "CompilationTargetPlatformOs": "string",
         "CreationTime": number,
         "LastModifiedTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCompilationJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompilationJobSummaries](#API_ListCompilationJobs_ResponseSyntax) **   <a name="sagemaker-ListCompilationJobs-response-CompilationJobSummaries"></a>
An array of [CompilationJobSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CompilationJobSummary.html) objects, each describing a model compilation job.
Type: Array of [CompilationJobSummary](API_CompilationJobSummary.md) objects

 ** [NextToken](#API_ListCompilationJobs_ResponseSyntax) **   <a name="sagemaker-ListCompilationJobs-response-NextToken"></a>
If the response is truncated, Amazon SageMaker AI returns this `NextToken`. To retrieve the next set of model compilation jobs, use this token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListCompilationJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListCompilationJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListCompilationJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListCompilationJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListCompilationJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListCompilationJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListCompilationJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListCompilationJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListCompilationJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListCompilationJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListCompilationJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListCompilationJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
