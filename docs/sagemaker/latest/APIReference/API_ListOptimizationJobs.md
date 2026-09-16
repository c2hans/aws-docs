---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListOptimizationJobs.html
---

# ListOptimizationJobs
<a name="API_ListOptimizationJobs"></a>

Lists the optimization jobs in your account and their properties.

## Request Syntax
<a name="API_ListOptimizationJobs_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "LastModifiedTimeAfter": {{number}},
   "LastModifiedTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "OptimizationContains": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListOptimizationJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-CreationTimeAfter"></a>
Filters the results to only those optimization jobs that were created after the specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-CreationTimeBefore"></a>
Filters the results to only those optimization jobs that were created before the specified time.
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-LastModifiedTimeAfter"></a>
Filters the results to only those optimization jobs that were updated after the specified time.
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-LastModifiedTimeBefore"></a>
Filters the results to only those optimization jobs that were updated before the specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-MaxResults"></a>
The maximum number of optimization jobs to return in the response. The default is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-NameContains"></a>
Filters the results to only those optimization jobs with a name that contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-NextToken"></a>
A token that you use to get the next set of results following a truncated response. If the response to the previous request was truncated, that response provides the value for this token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [OptimizationContains](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-OptimizationContains"></a>
Filters the results to only those optimization jobs that apply the specified optimization techniques. You can specify either `Quantization` or `Compilation`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [SortBy](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-SortBy"></a>
The field by which to sort the optimization jobs in the response. The default is `CreationTime`
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-SortOrder"></a>
The sort order for results. The default is `Ascending`
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListOptimizationJobs_RequestSyntax) **   <a name="sagemaker-ListOptimizationJobs-request-StatusEquals"></a>
Filters the results to only those optimization jobs with the specified status.
Type: String
Valid Values: `INPROGRESS | COMPLETED | FAILED | STARTING | STOPPING | STOPPED`
Required: No

## Response Syntax
<a name="API_ListOptimizationJobs_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OptimizationJobSummaries": [
      {
         "CreationTime": number,
         "DeploymentInstanceType": "string",
         "LastModifiedTime": number,
         "MaxInstanceCount": number,
         "OptimizationJobArn": "string",
         "OptimizationJobName": "string",
         "OptimizationJobStatus": "string",
         "OptimizationTypes": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_ListOptimizationJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOptimizationJobs_ResponseSyntax) **   <a name="sagemaker-ListOptimizationJobs-response-NextToken"></a>
The token to use in a subsequent request to get the next set of results following a truncated response.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [OptimizationJobSummaries](#API_ListOptimizationJobs_ResponseSyntax) **   <a name="sagemaker-ListOptimizationJobs-response-OptimizationJobSummaries"></a>
A list of optimization jobs and their properties that matches any of the filters you specified in the request.
Type: Array of [OptimizationJobSummary](API_OptimizationJobSummary.md) objects

## Errors
<a name="API_ListOptimizationJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListOptimizationJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListOptimizationJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListOptimizationJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListOptimizationJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListOptimizationJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListOptimizationJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListOptimizationJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListOptimizationJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListOptimizationJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListOptimizationJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListOptimizationJobs)
