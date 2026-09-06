---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponentSourceDetail.html
---

# TrialComponentSourceDetail
<a name="API_TrialComponentSourceDetail"></a>

Detailed information about the source of a trial component. Either `ProcessingJob` or `TrainingJob` is returned.

## Contents
<a name="API_TrialComponentSourceDetail_Contents"></a>

 ** ProcessingJob **   <a name="sagemaker-Type-TrialComponentSourceDetail-ProcessingJob"></a>
Information about a processing job that's the source of a trial component.
Type: [ProcessingJob](API_ProcessingJob.md) object
Required: No

 ** SourceArn **   <a name="sagemaker-Type-TrialComponentSourceDetail-SourceArn"></a>
The Amazon Resource Name (ARN) of the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:.*`
Required: No

 ** TrainingJob **   <a name="sagemaker-Type-TrialComponentSourceDetail-TrainingJob"></a>
Information about a training job that's the source of a trial component.
Type: [TrainingJob](API_TrainingJob.md) object
Required: No

 ** TransformJob **   <a name="sagemaker-Type-TrialComponentSourceDetail-TransformJob"></a>
Information about a transform job that's the source of a trial component.
Type: [TransformJob](API_TransformJob.md) object
Required: No

## See Also
<a name="API_TrialComponentSourceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrialComponentSourceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrialComponentSourceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrialComponentSourceDetail)
