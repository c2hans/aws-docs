---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCandidatesForAutoMLJob.html
---

# ListCandidatesForAutoMLJob
<a name="API_ListCandidatesForAutoMLJob"></a>

List the candidates created for the job.

## Request Syntax
<a name="API_ListCandidatesForAutoMLJob_RequestSyntax"></a>

```
{
   "AutoMLJobName": "{{string}}",
   "CandidateNameEquals": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCandidatesForAutoMLJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoMLJobName](#API_ListCandidatesForAutoMLJob_RequestSyntax) **   <a name="sagemaker-ListCandidatesForAutoMLJob-request-AutoMLJobName"></a>
List the candidates created for the job by providing the job's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

 ** [CandidateNameEquals](#API_ListCandidatesForAutoMLJob_RequestSyntax) **   <a name="sagemaker-ListCandidatesForAutoMLJob-request-CandidateNameEquals"></a>
List the candidates for the job and filter by candidate name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [MaxResults](#API_ListCandidatesForAutoMLJob_RequestSyntax) **   <a name="sagemaker-ListCandidatesForAutoMLJob-request-MaxResults"></a>
List the job's candidates up to a specified limit.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 300.
Required: No

 ** [NextToken](#API_ListCandidatesForAutoMLJob_RequestSyntax) **   <a name="sagemaker-ListCandidatesForAutoMLJob-request-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListCandidatesForAutoMLJob_RequestSyntax) **   <a name="sagemaker-ListCandidatesForAutoMLJob-request-SortBy"></a>
The parameter by which to sort the results. The default is `Descending`.
Type: String
Valid Values: `CreationTime | Status | FinalObjectiveMetricValue`
Required: No

 ** [SortOrder](#API_ListCandidatesForAutoMLJob_RequestSyntax) **   <a name="sagemaker-ListCandidatesForAutoMLJob-request-SortOrder"></a>
The sort order for the results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListCandidatesForAutoMLJob_RequestSyntax) **   <a name="sagemaker-ListCandidatesForAutoMLJob-request-StatusEquals"></a>
List the candidates for the job and filter by status.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping`
Required: No

## Response Syntax
<a name="API_ListCandidatesForAutoMLJob_ResponseSyntax"></a>

```
{
   "Candidates": [
      {
         "CandidateName": "string",
         "CandidateProperties": {
            "CandidateArtifactLocations": {
               "BacktestResults": "string",
               "Explainability": "string",
               "ModelInsights": "string"
            },
            "CandidateMetrics": [
               {
                  "MetricName": "string",
                  "Set": "string",
                  "StandardMetricName": "string",
                  "Value": number
               }
            ]
         },
         "CandidateStatus": "string",
         "CandidateSteps": [
            {
               "CandidateStepArn": "string",
               "CandidateStepName": "string",
               "CandidateStepType": "string"
            }
         ],
         "FailureReason": "string",
         "FinalAutoMLJobObjectiveMetric": {
            "MetricName": "string",
            "StandardMetricName": "string",
            "Type": "string",
            "Value": number
         },
         "InferenceContainerDefinitions": {
            "string" : [
               {
                  "Environment": {
                     "string" : "string"
                  },
                  "Image": "string",
                  "ModelDataUrl": "string"
               }
            ]
         },
         "InferenceContainers": [
            {
               "Environment": {
                  "string" : "string"
               },
               "Image": "string",
               "ModelDataUrl": "string"
            }
         ],
         "ObjectiveStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCandidatesForAutoMLJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Candidates](#API_ListCandidatesForAutoMLJob_ResponseSyntax) **   <a name="sagemaker-ListCandidatesForAutoMLJob-response-Candidates"></a>
Summaries about the `AutoMLCandidates`.
Type: Array of [AutoMLCandidate](API_AutoMLCandidate.md) objects

 ** [NextToken](#API_ListCandidatesForAutoMLJob_ResponseSyntax) **   <a name="sagemaker-ListCandidatesForAutoMLJob-response-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListCandidatesForAutoMLJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListCandidatesForAutoMLJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListCandidatesForAutoMLJob)
