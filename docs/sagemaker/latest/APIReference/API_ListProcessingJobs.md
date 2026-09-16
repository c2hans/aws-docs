---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListProcessingJobs.html
---

# ListProcessingJobs
<a name="API_ListProcessingJobs"></a>

Lists processing jobs that satisfy various filters.

## Request Syntax
<a name="API_ListProcessingJobs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListProcessingJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListProcessingJobs_RequestSyntax) **   <a name="sagemaker-ListProcessingJobs-request-MaxResults"></a>
The maximum number of processing jobs to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListProcessingJobs_RequestSyntax) **   <a name="sagemaker-ListProcessingJobs-request-NameContains"></a>
A string in the processing job name. This filter returns only processing jobs whose name contains the specified string.
Type: String
Required: No

 ** [NextToken](#API_ListProcessingJobs_RequestSyntax) **   <a name="sagemaker-ListProcessingJobs-request-NextToken"></a>
If the result of the previous `ListProcessingJobs` request was truncated, the response includes a `NextToken`. To retrieve the next set of processing jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListProcessingJobs_RequestSyntax) **   <a name="sagemaker-ListProcessingJobs-request-SortBy"></a>
The field to sort results by. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListProcessingJobs_RequestSyntax) **   <a name="sagemaker-ListProcessingJobs-request-SortOrder"></a>
The sort order for results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListProcessingJobs_RequestSyntax) **   <a name="sagemaker-ListProcessingJobs-request-StatusEquals"></a>
A filter that retrieves only processing jobs with a specific status.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: No

## Response Syntax
<a name="API_ListProcessingJobs_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ProcessingJobSummaries": [
      {
         "ExitMessage": "string",
         "FailureReason": "string",
         "ProcessingJobArn": "string",
         "ProcessingJobName": "string",
         "ProcessingJobStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProcessingJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListProcessingJobs_ResponseSyntax) **   <a name="sagemaker-ListProcessingJobs-response-NextToken"></a>
If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of processing jobs, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [ProcessingJobSummaries](#API_ListProcessingJobs_ResponseSyntax) **   <a name="sagemaker-ListProcessingJobs-response-ProcessingJobSummaries"></a>
An array of `ProcessingJobSummary` objects, each listing a processing job.
Type: Array of [ProcessingJobSummary](API_ProcessingJobSummary.md) objects

## Errors
<a name="API_ListProcessingJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListProcessingJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListProcessingJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListProcessingJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListProcessingJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListProcessingJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListProcessingJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListProcessingJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListProcessingJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListProcessingJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListProcessingJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListProcessingJobs)
