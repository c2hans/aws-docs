---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIRecommendationJobSummary.html
---

# AIRecommendationJobSummary
<a name="API_AIRecommendationJobSummary"></a>

Summary information about an AI recommendation job.

## Contents
<a name="API_AIRecommendationJobSummary_Contents"></a>

 ** AIRecommendationJobArn **   <a name="sagemaker-Type-AIRecommendationJobSummary-AIRecommendationJobArn"></a>
The Amazon Resource Name (ARN) of the recommendation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-recommendation-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** AIRecommendationJobName **   <a name="sagemaker-Type-AIRecommendationJobSummary-AIRecommendationJobName"></a>
The name of the recommendation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** AIRecommendationJobStatus **   <a name="sagemaker-Type-AIRecommendationJobSummary-AIRecommendationJobStatus"></a>
The status of the recommendation job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: Yes

## See Also
<a name="API_AIRecommendationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIRecommendationJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIRecommendationJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIRecommendationJobSummary)
