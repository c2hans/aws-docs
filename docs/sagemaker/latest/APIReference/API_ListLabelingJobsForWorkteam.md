---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListLabelingJobsForWorkteam.html
---

# ListLabelingJobsForWorkteam
<a name="API_ListLabelingJobsForWorkteam"></a>

Gets a list of labeling jobs assigned to a specified work team.

## Request Syntax
<a name="API_ListLabelingJobsForWorkteam_RequestSyntax"></a>

```
{
   "JobReferenceCodeContains": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "WorkteamArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLabelingJobsForWorkteam_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobReferenceCodeContains](#API_ListLabelingJobsForWorkteam_RequestSyntax) **   <a name="sagemaker-ListLabelingJobsForWorkteam-request-JobReferenceCodeContains"></a>
A filter the limits jobs to only the ones whose job reference code contains the specified string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: No

 ** [MaxResults](#API_ListLabelingJobsForWorkteam_RequestSyntax) **   <a name="sagemaker-ListLabelingJobsForWorkteam-request-MaxResults"></a>
The maximum number of labeling jobs to return in each page of the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListLabelingJobsForWorkteam_RequestSyntax) **   <a name="sagemaker-ListLabelingJobsForWorkteam-request-NextToken"></a>
If the result of the previous `ListLabelingJobsForWorkteam` request was truncated, the response includes a `NextToken`. To retrieve the next set of labeling jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListLabelingJobsForWorkteam_RequestSyntax) **   <a name="sagemaker-ListLabelingJobsForWorkteam-request-SortBy"></a>
The field to sort results by. The default is `CreationTime`.
Type: String
Valid Values: `CreationTime`
Required: No

 ** [SortOrder](#API_ListLabelingJobsForWorkteam_RequestSyntax) **   <a name="sagemaker-ListLabelingJobsForWorkteam-request-SortOrder"></a>
The sort order for results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [WorkteamArn](#API_ListLabelingJobsForWorkteam_RequestSyntax) **   <a name="sagemaker-ListLabelingJobsForWorkteam-request-WorkteamArn"></a>
The Amazon Resource Name (ARN) of the work team for which you want to see labeling jobs for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workteam/.*`
Required: Yes

## Response Syntax
<a name="API_ListLabelingJobsForWorkteam_ResponseSyntax"></a>

```
{
   "LabelingJobSummaryList": [
      {
         "JobReferenceCode": "string",
         "LabelCounters": {
            "HumanLabeled": number,
            "PendingHuman": number,
            "Total": number
         },
         "LabelingJobName": "string",
         "NumberOfHumanWorkersPerDataObject": number,
         "WorkRequesterAccountId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLabelingJobsForWorkteam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LabelingJobSummaryList](#API_ListLabelingJobsForWorkteam_ResponseSyntax) **   <a name="sagemaker-ListLabelingJobsForWorkteam-response-LabelingJobSummaryList"></a>
An array of `LabelingJobSummary` objects, each describing a labeling job.
Type: Array of [LabelingJobForWorkteamSummary](API_LabelingJobForWorkteamSummary.md) objects

 ** [NextToken](#API_ListLabelingJobsForWorkteam_ResponseSyntax) **   <a name="sagemaker-ListLabelingJobsForWorkteam-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of labeling jobs, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListLabelingJobsForWorkteam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListLabelingJobsForWorkteam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListLabelingJobsForWorkteam)
