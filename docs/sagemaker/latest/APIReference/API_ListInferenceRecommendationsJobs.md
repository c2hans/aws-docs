---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceRecommendationsJobs.html
---

# ListInferenceRecommendationsJobs
<a name="API_ListInferenceRecommendationsJobs"></a>

Lists recommendation jobs that satisfy various filters.

## Request Syntax
<a name="API_ListInferenceRecommendationsJobs_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "LastModifiedTimeAfter": {{number}},
   "LastModifiedTimeBefore": {{number}},
   "MaxResults": {{number}},
   "ModelNameEquals": "{{string}}",
   "ModelPackageVersionArnEquals": "{{string}}",
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInferenceRecommendationsJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-CreationTimeAfter"></a>
A filter that returns only jobs created after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-CreationTimeBefore"></a>
A filter that returns only jobs created before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-LastModifiedTimeAfter"></a>
A filter that returns only jobs that were last modified after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-LastModifiedTimeBefore"></a>
A filter that returns only jobs that were last modified before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-MaxResults"></a>
The maximum number of recommendations to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [ModelNameEquals](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-ModelNameEquals"></a>
A filter that returns only jobs that were created for this model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: No

 ** [ModelPackageVersionArnEquals](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-ModelPackageVersionArnEquals"></a>
A filter that returns only jobs that were created for this versioned model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: No

 ** [NameContains](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-NameContains"></a>
A string in the job name. This filter returns only recommendations whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-NextToken"></a>
If the response to a previous `ListInferenceRecommendationsJobsRequest` request was truncated, the response includes a `NextToken`. To retrieve the next set of recommendations, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-SortBy"></a>
The parameter by which to sort the results.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-SortOrder"></a>
The sort order for the results.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListInferenceRecommendationsJobs_RequestSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-request-StatusEquals"></a>
A filter that retrieves only inference recommendations jobs with a specific status.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | STOPPING | STOPPED | DELETING | DELETED`
Required: No

## Response Syntax
<a name="API_ListInferenceRecommendationsJobs_ResponseSyntax"></a>

```
{
   "InferenceRecommendationsJobs": [
      {
         "CompletionTime": number,
         "CreationTime": number,
         "FailureReason": "string",
         "JobArn": "string",
         "JobDescription": "string",
         "JobName": "string",
         "JobType": "string",
         "LastModifiedTime": number,
         "ModelName": "string",
         "ModelPackageVersionArn": "string",
         "RoleArn": "string",
         "SamplePayloadUrl": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInferenceRecommendationsJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceRecommendationsJobs](#API_ListInferenceRecommendationsJobs_ResponseSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-response-InferenceRecommendationsJobs"></a>
The recommendations created from the Amazon SageMaker Inference Recommender job.
Type: Array of [InferenceRecommendationsJob](API_InferenceRecommendationsJob.md) objects

 ** [NextToken](#API_ListInferenceRecommendationsJobs_ResponseSyntax) **   <a name="sagemaker-ListInferenceRecommendationsJobs-response-NextToken"></a>
A token for getting the next set of recommendations, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListInferenceRecommendationsJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListInferenceRecommendationsJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListInferenceRecommendationsJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
