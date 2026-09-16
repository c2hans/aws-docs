---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAIBenchmarkJobs.html
---

# ListAIBenchmarkJobs
<a name="API_ListAIBenchmarkJobs"></a>

Returns a list of AI benchmark jobs in your account. You can filter the results by name, status, and creation time, and sort the results. The response is paginated.

## Request Syntax
<a name="API_ListAIBenchmarkJobs_RequestSyntax"></a>

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
<a name="API_ListAIBenchmarkJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListAIBenchmarkJobs_RequestSyntax) **   <a name="sagemaker-ListAIBenchmarkJobs-request-MaxResults"></a>
The maximum number of benchmark jobs to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListAIBenchmarkJobs_RequestSyntax) **   <a name="sagemaker-ListAIBenchmarkJobs-request-NameContains"></a>
A string in the job name. This filter returns only jobs whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListAIBenchmarkJobs_RequestSyntax) **   <a name="sagemaker-ListAIBenchmarkJobs-request-NextToken"></a>
If the previous call to `ListAIBenchmarkJobs` didn't return the full set of jobs, the call returns a token for getting the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListAIBenchmarkJobs_RequestSyntax) **   <a name="sagemaker-ListAIBenchmarkJobs-request-SortBy"></a>
The field to sort results by. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListAIBenchmarkJobs_RequestSyntax) **   <a name="sagemaker-ListAIBenchmarkJobs-request-SortOrder"></a>
The sort order for results. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListAIBenchmarkJobs_RequestSyntax) **   <a name="sagemaker-ListAIBenchmarkJobs-request-StatusEquals"></a>
A filter that returns only benchmark jobs with the specified status.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: No

## Response Syntax
<a name="API_ListAIBenchmarkJobs_ResponseSyntax"></a>

```
{
   "AIBenchmarkJobs": [
      {
         "AIBenchmarkJobArn": "string",
         "AIBenchmarkJobName": "string",
         "AIBenchmarkJobStatus": "string",
         "AIWorkloadConfigName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAIBenchmarkJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AIBenchmarkJobs](#API_ListAIBenchmarkJobs_ResponseSyntax) **   <a name="sagemaker-ListAIBenchmarkJobs-response-AIBenchmarkJobs"></a>
An array of `AIBenchmarkJobSummary` objects, one for each benchmark job that matches the specified filters.
Type: Array of [AIBenchmarkJobSummary](API_AIBenchmarkJobSummary.md) objects

 ** [NextToken](#API_ListAIBenchmarkJobs_ResponseSyntax) **   <a name="sagemaker-ListAIBenchmarkJobs-response-NextToken"></a>
If the response is truncated, Amazon SageMaker AI returns this token. To retrieve the next set of jobs, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListAIBenchmarkJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListAIBenchmarkJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListAIBenchmarkJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListAIBenchmarkJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListAIBenchmarkJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListAIBenchmarkJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListAIBenchmarkJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListAIBenchmarkJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListAIBenchmarkJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListAIBenchmarkJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListAIBenchmarkJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListAIBenchmarkJobs)
