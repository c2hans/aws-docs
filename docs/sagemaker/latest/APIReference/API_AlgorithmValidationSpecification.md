---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmValidationSpecification.html
---

# AlgorithmValidationSpecification
<a name="API_AlgorithmValidationSpecification"></a>

Specifies configurations for one or more training jobs that SageMaker runs to test the algorithm.

## Contents
<a name="API_AlgorithmValidationSpecification_Contents"></a>

 ** ValidationProfiles **   <a name="sagemaker-Type-AlgorithmValidationSpecification-ValidationProfiles"></a>
An array of `AlgorithmValidationProfile` objects, each of which specifies a training job and batch transform job that SageMaker runs to validate your algorithm.
Type: Array of [AlgorithmValidationProfile](API_AlgorithmValidationProfile.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** ValidationRole **   <a name="sagemaker-Type-AlgorithmValidationSpecification-ValidationRole"></a>
The IAM roles that SageMaker uses to run the training jobs.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

## See Also
<a name="API_AlgorithmValidationSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AlgorithmValidationSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AlgorithmValidationSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AlgorithmValidationSpecification)
