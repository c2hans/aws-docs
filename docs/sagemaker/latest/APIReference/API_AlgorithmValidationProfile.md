---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmValidationProfile.html
---

# AlgorithmValidationProfile
<a name="API_AlgorithmValidationProfile"></a>

Defines a training job and a batch transform job that SageMaker runs to validate your algorithm.

The data provided in the validation profile is made available to your buyers on AWS Marketplace.

## Contents
<a name="API_AlgorithmValidationProfile_Contents"></a>

 ** ProfileName **   <a name="sagemaker-Type-AlgorithmValidationProfile-ProfileName"></a>
The name of the profile for the algorithm. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** TrainingJobDefinition **   <a name="sagemaker-Type-AlgorithmValidationProfile-TrainingJobDefinition"></a>
The `TrainingJobDefinition` object that describes the training job that SageMaker runs to validate your algorithm.
Type: [TrainingJobDefinition](API_TrainingJobDefinition.md) object
Required: Yes

 ** TransformJobDefinition **   <a name="sagemaker-Type-AlgorithmValidationProfile-TransformJobDefinition"></a>
The `TransformJobDefinition` object that describes the transform job that SageMaker runs to validate your algorithm.
Type: [TransformJobDefinition](API_TransformJobDefinition.md) object
Required: No

## See Also
<a name="API_AlgorithmValidationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AlgorithmValidationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AlgorithmValidationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AlgorithmValidationProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
