---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobAlgorithmsConfig.html
---

# LabelingJobAlgorithmsConfig
<a name="API_LabelingJobAlgorithmsConfig"></a>

Provides configuration information for auto-labeling of your data objects. A `LabelingJobAlgorithmsConfig` object must be supplied in order to use auto-labeling.

## Contents
<a name="API_LabelingJobAlgorithmsConfig_Contents"></a>

 ** LabelingJobAlgorithmSpecificationArn **   <a name="sagemaker-Type-LabelingJobAlgorithmsConfig-LabelingJobAlgorithmSpecificationArn"></a>
Specifies the Amazon Resource Name (ARN) of the algorithm used for auto-labeling. You must select one of the following ARNs:
+  *Image classification*

   `arn:aws:sagemaker:region:027400017018:labeling-job-algorithm-specification/image-classification`
+  *Text classification*

   `arn:aws:sagemaker:region:027400017018:labeling-job-algorithm-specification/text-classification`
+  *Object detection*

   `arn:aws:sagemaker:region:027400017018:labeling-job-algorithm-specification/object-detection`
+  *Semantic Segmentation*

   `arn:aws:sagemaker:region:027400017018:labeling-job-algorithm-specification/semantic-segmentation`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** InitialActiveLearningModelArn **   <a name="sagemaker-Type-LabelingJobAlgorithmsConfig-InitialActiveLearningModelArn"></a>
At the end of an auto-label job Ground Truth sends the Amazon Resource Name (ARN) of the final model used for auto-labeling. You can use this model as the starting point for subsequent similar jobs by providing the ARN of the model here.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model/.*`
Required: No

 ** LabelingJobResourceConfig **   <a name="sagemaker-Type-LabelingJobAlgorithmsConfig-LabelingJobResourceConfig"></a>
Provides configuration information for a labeling job.
Type: [LabelingJobResourceConfig](API_LabelingJobResourceConfig.md) object
Required: No

## See Also
<a name="API_LabelingJobAlgorithmsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobAlgorithmsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobAlgorithmsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobAlgorithmsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
