---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListLabelingJobs.html
---

# ListLabelingJobs
<a name="API_ListLabelingJobs"></a>

Gets a list of labeling jobs.

## Request Syntax
<a name="API_ListLabelingJobs_RequestSyntax"></a>

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
<a name="API_ListLabelingJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-CreationTimeAfter"></a>
A filter that returns only labeling jobs created after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-CreationTimeBefore"></a>
A filter that returns only labeling jobs created before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-LastModifiedTimeAfter"></a>
A filter that returns only labeling jobs modified after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-LastModifiedTimeBefore"></a>
A filter that returns only labeling jobs modified before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-MaxResults"></a>
The maximum number of labeling jobs to return in each page of the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-NameContains"></a>
A string in the labeling job name. This filter returns only labeling jobs whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-NextToken"></a>
If the result of the previous `ListLabelingJobs` request was truncated, the response includes a `NextToken`. To retrieve the next set of labeling jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-SortBy"></a>
The field to sort results by. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-SortOrder"></a>
The sort order for results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListLabelingJobs_RequestSyntax) **   <a name="sagemaker-ListLabelingJobs-request-StatusEquals"></a>
A filter that retrieves only labeling jobs with a specific status.
Type: String
Valid Values: `Initializing | InProgress | Completed | Failed | Stopping | Stopped`
Required: No

## Response Syntax
<a name="API_ListLabelingJobs_ResponseSyntax"></a>

```
{
   "LabelingJobSummaryList": [
      {
         "AnnotationConsolidationLambdaArn": "string",
         "CreationTime": number,
         "FailureReason": "string",
         "InputConfig": {
            "DataAttributes": {
               "ContentClassifiers": [ "string" ]
            },
            "DataSource": {
               "S3DataSource": {
                  "ManifestS3Uri": "string"
               },
               "SnsDataSource": {
                  "SnsTopicArn": "string"
               }
            }
         },
         "LabelCounters": {
            "FailedNonRetryableError": number,
            "HumanLabeled": number,
            "MachineLabeled": number,
            "TotalLabeled": number,
            "Unlabeled": number
         },
         "LabelingJobArn": "string",
         "LabelingJobName": "string",
         "LabelingJobOutput": {
            "FinalActiveLearningModelArn": "string",
            "OutputDatasetS3Uri": "string"
         },
         "LabelingJobStatus": "string",
         "LastModifiedTime": number,
         "PreHumanTaskLambdaArn": "string",
         "WorkteamArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLabelingJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LabelingJobSummaryList](#API_ListLabelingJobs_ResponseSyntax) **   <a name="sagemaker-ListLabelingJobs-response-LabelingJobSummaryList"></a>
An array of `LabelingJobSummary` objects, each describing a labeling job.
Type: Array of [LabelingJobSummary](API_LabelingJobSummary.md) objects

 ** [NextToken](#API_ListLabelingJobs_ResponseSyntax) **   <a name="sagemaker-ListLabelingJobs-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of labeling jobs, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListLabelingJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListLabelingJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListLabelingJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListLabelingJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListLabelingJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListLabelingJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListLabelingJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListLabelingJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListLabelingJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListLabelingJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListLabelingJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListLabelingJobs)
