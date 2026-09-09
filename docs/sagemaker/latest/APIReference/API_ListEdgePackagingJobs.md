---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEdgePackagingJobs.html
---

# ListEdgePackagingJobs
<a name="API_ListEdgePackagingJobs"></a>

Returns a list of edge packaging jobs.

## Request Syntax
<a name="API_ListEdgePackagingJobs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "ModelNameContains": "{{string}}",
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEdgePackagingJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListEdgePackagingJobs_RequestSyntax) **   <a name="sagemaker-ListEdgePackagingJobs-request-MaxResults"></a>
Maximum number of results to select.
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [ModelNameContains](#API_ListEdgePackagingJobs_RequestSyntax) **   <a name="sagemaker-ListEdgePackagingJobs-request-ModelNameContains"></a>
Filter for jobs where the model name contains this string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NameContains](#API_ListEdgePackagingJobs_RequestSyntax) **   <a name="sagemaker-ListEdgePackagingJobs-request-NameContains"></a>
Filter for jobs containing this name in their packaging job name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListEdgePackagingJobs_RequestSyntax) **   <a name="sagemaker-ListEdgePackagingJobs-request-NextToken"></a>
The response from the last list when returning a list large enough to need tokening.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListEdgePackagingJobs_RequestSyntax) **   <a name="sagemaker-ListEdgePackagingJobs-request-SortBy"></a>
Use to specify what column to sort by.
Type: String
Valid Values: `NAME | MODEL_NAME | CREATION_TIME | LAST_MODIFIED_TIME | STATUS`
Required: No

 ** [SortOrder](#API_ListEdgePackagingJobs_RequestSyntax) **   <a name="sagemaker-ListEdgePackagingJobs-request-SortOrder"></a>
What direction to sort by.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListEdgePackagingJobs_RequestSyntax) **   <a name="sagemaker-ListEdgePackagingJobs-request-StatusEquals"></a>
The job status to filter for.
Type: String
Valid Values: `STARTING | INPROGRESS | COMPLETED | FAILED | STOPPING | STOPPED`
Required: No

## Response Syntax
<a name="API_ListEdgePackagingJobs_ResponseSyntax"></a>

```
{
   "EdgePackagingJobSummaries": [
      {
         "CompilationJobName": "string",
         "EdgePackagingJobArn": "string",
         "EdgePackagingJobName": "string",
         "EdgePackagingJobStatus": "string",
         "ModelName": "string",
         "ModelVersion": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEdgePackagingJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EdgePackagingJobSummaries](#API_ListEdgePackagingJobs_ResponseSyntax) **   <a name="sagemaker-ListEdgePackagingJobs-response-EdgePackagingJobSummaries"></a>
Summaries of edge packaging jobs.
Type: Array of [EdgePackagingJobSummary](API_EdgePackagingJobSummary.md) objects

 ** [NextToken](#API_ListEdgePackagingJobs_ResponseSyntax) **   <a name="sagemaker-ListEdgePackagingJobs-response-NextToken"></a>
Token to use when calling the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListEdgePackagingJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListEdgePackagingJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListEdgePackagingJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListEdgePackagingJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListEdgePackagingJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListEdgePackagingJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListEdgePackagingJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListEdgePackagingJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListEdgePackagingJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListEdgePackagingJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListEdgePackagingJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListEdgePackagingJobs)
