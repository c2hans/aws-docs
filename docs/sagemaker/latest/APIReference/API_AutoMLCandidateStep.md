---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateStep.html
---

# AutoMLCandidateStep
<a name="API_AutoMLCandidateStep"></a>

Information about the steps for a candidate and what step it is working on.

## Contents
<a name="API_AutoMLCandidateStep_Contents"></a>

 ** CandidateStepArn **   <a name="sagemaker-Type-AutoMLCandidateStep-CandidateStepArn"></a>
The ARN for the candidate's step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:.*/.*`
Required: Yes

 ** CandidateStepName **   <a name="sagemaker-Type-AutoMLCandidateStep-CandidateStepName"></a>
The name for the candidate's step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** CandidateStepType **   <a name="sagemaker-Type-AutoMLCandidateStep-CandidateStepType"></a>
Whether the candidate is at the transform, training, or processing step.
Type: String
Valid Values: `AWS::SageMaker::TrainingJob | AWS::SageMaker::TransformJob | AWS::SageMaker::ProcessingJob`
Required: Yes

## See Also
<a name="API_AutoMLCandidateStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLCandidateStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLCandidateStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLCandidateStep)
