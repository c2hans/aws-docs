---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHyperParameterTuningJobs.html
---

# ListHyperParameterTuningJobs
<a name="API_ListHyperParameterTuningJobs"></a>

Gets a list of [HyperParameterTuningJobSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSummary.html) objects that describe the hyperparameter tuning jobs launched in your account.

## Request Syntax
<a name="API_ListHyperParameterTuningJobs_RequestSyntax"></a>

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
<a name="API_ListHyperParameterTuningJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListHyperParameterTuningJobs_RequestSyntax) **   <a name="sagemaker-ListHyperParameterTuningJobs-request-MaxResults"></a>
The maximum number of tuning jobs to return. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListHyperParameterTuningJobs_RequestSyntax) **   <a name="sagemaker-ListHyperParameterTuningJobs-request-NameContains"></a>
A string in the tuning job name. This filter returns only tuning jobs whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListHyperParameterTuningJobs_RequestSyntax) **   <a name="sagemaker-ListHyperParameterTuningJobs-request-NextToken"></a>
If the result of the previous `ListHyperParameterTuningJobs` request was truncated, the response includes a `NextToken`. To retrieve the next set of tuning jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListHyperParameterTuningJobs_RequestSyntax) **   <a name="sagemaker-ListHyperParameterTuningJobs-request-SortBy"></a>
The field to sort results by. The default is `Name`.
Type: String
Valid Values: `Name | Status | CreationTime`
Required: No

 ** [SortOrder](#API_ListHyperParameterTuningJobs_RequestSyntax) **   <a name="sagemaker-ListHyperParameterTuningJobs-request-SortOrder"></a>
The sort order for results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListHyperParameterTuningJobs_RequestSyntax) **   <a name="sagemaker-ListHyperParameterTuningJobs-request-StatusEquals"></a>
A filter that returns only tuning jobs with the specified status.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping | Deleting | DeleteFailed`
Required: No

## Response Syntax
<a name="API_ListHyperParameterTuningJobs_ResponseSyntax"></a>

```
{
   "HyperParameterTuningJobSummaries": [
      {
         "HyperParameterTuningJobArn": "string",
         "HyperParameterTuningJobName": "string",
         "HyperParameterTuningJobStatus": "string",
         "ObjectiveStatusCounters": {
            "Failed": number,
            "Pending": number,
            "Succeeded": number
         },
         "ResourceLimits": {
            "MaxNumberOfTrainingJobs": number,
            "MaxParallelTrainingJobs": number,
            "MaxRuntimeInSeconds": number
         },
         "Strategy": "string",
         "TrainingJobStatusCounters": {
            "Completed": number,
            "InProgress": number,
            "NonRetryableError": number,
            "RetryableError": number,
            "Stopped": number
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHyperParameterTuningJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HyperParameterTuningJobSummaries](#API_ListHyperParameterTuningJobs_ResponseSyntax) **   <a name="sagemaker-ListHyperParameterTuningJobs-response-HyperParameterTuningJobSummaries"></a>
A list of [HyperParameterTuningJobSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSummary.html) objects that describe the tuning jobs that the `ListHyperParameterTuningJobs` request returned.
Type: Array of [HyperParameterTuningJobSummary](API_HyperParameterTuningJobSummary.md) objects

 ** [NextToken](#API_ListHyperParameterTuningJobs_ResponseSyntax) **   <a name="sagemaker-ListHyperParameterTuningJobs-response-NextToken"></a>
If the result of this `ListHyperParameterTuningJobs` request was truncated, the response includes a `NextToken`. To retrieve the next set of tuning jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListHyperParameterTuningJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListHyperParameterTuningJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListHyperParameterTuningJobs)
