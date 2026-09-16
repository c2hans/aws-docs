---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrainingJobs.html
---

# ListTrainingJobs
<a name="API_ListTrainingJobs"></a>

Lists training jobs.

**Note**
When `StatusEquals` and `MaxResults` are set at the same time, the `MaxResults` number of training jobs are first retrieved ignoring the `StatusEquals` parameter and then they are filtered by the `StatusEquals` parameter, which is returned as a response.
For example, if `ListTrainingJobs` is invoked with the following parameters:
 `{ ... MaxResults: 100, StatusEquals: InProgress ... }`
First, 100 trainings jobs with any status, including those other than `InProgress`, are selected (sorted according to the creation time, from the most current to the oldest). Next, those with a status of `InProgress` are returned.
You can quickly test the API using the following AWS CLI code.
 `aws sagemaker list-training-jobs --max-results 100 --status-equals InProgress`

## Request Syntax
<a name="API_ListTrainingJobs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}",
   "TrainingPlanArnEquals": "{{string}}",
   "WarmPoolStatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTrainingJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListTrainingJobs_RequestSyntax) **   <a name="sagemaker-ListTrainingJobs-request-MaxResults"></a>
The maximum number of training jobs to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListTrainingJobs_RequestSyntax) **   <a name="sagemaker-ListTrainingJobs-request-NameContains"></a>
A string in the training job name. This filter returns only training jobs whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListTrainingJobs_RequestSyntax) **   <a name="sagemaker-ListTrainingJobs-request-NextToken"></a>
If the result of the previous `ListTrainingJobs` request was truncated, the response includes a `NextToken`. To retrieve the next set of training jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListTrainingJobs_RequestSyntax) **   <a name="sagemaker-ListTrainingJobs-request-SortBy"></a>
The field to sort results by. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListTrainingJobs_RequestSyntax) **   <a name="sagemaker-ListTrainingJobs-request-SortOrder"></a>
The sort order for results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListTrainingJobs_RequestSyntax) **   <a name="sagemaker-ListTrainingJobs-request-StatusEquals"></a>
A filter that retrieves only training jobs with a specific status.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting`
Required: No

 ** [TrainingPlanArnEquals](#API_ListTrainingJobs_RequestSyntax) **   <a name="sagemaker-ListTrainingJobs-request-TrainingPlanArnEquals"></a>
The Amazon Resource Name (ARN); of the training plan to filter training jobs by. For more information about reserving GPU capacity for your SageMaker training jobs using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

 ** [WarmPoolStatusEquals](#API_ListTrainingJobs_RequestSyntax) **   <a name="sagemaker-ListTrainingJobs-request-WarmPoolStatusEquals"></a>
A filter that retrieves only training jobs with a specific warm pool status.
Type: String
Valid Values: `Available | Terminated | Reused | InUse`
Required: No

## Response Syntax
<a name="API_ListTrainingJobs_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TrainingJobSummaries": [
      {
         "SecondaryStatus": "string",
         "TrainingJobArn": "string",
         "TrainingJobName": "string",
         "TrainingJobStatus": "string",
         "TrainingPlanArn": "string",
         "WarmPoolStatus": {
            "ResourceRetainedBillableTimeInSeconds": number,
            "ReusedByJob": "string",
            "Status": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListTrainingJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTrainingJobs_ResponseSyntax) **   <a name="sagemaker-ListTrainingJobs-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [TrainingJobSummaries](#API_ListTrainingJobs_ResponseSyntax) **   <a name="sagemaker-ListTrainingJobs-response-TrainingJobSummaries"></a>
An array of `TrainingJobSummary` objects, each listing a training job.
Type: Array of [TrainingJobSummary](API_TrainingJobSummary.md) objects

## Errors
<a name="API_ListTrainingJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListTrainingJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListTrainingJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListTrainingJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListTrainingJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListTrainingJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListTrainingJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListTrainingJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListTrainingJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListTrainingJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListTrainingJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListTrainingJobs)
