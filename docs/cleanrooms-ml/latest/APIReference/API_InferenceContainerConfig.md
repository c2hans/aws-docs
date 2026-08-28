---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_InferenceContainerConfig.html
---

# InferenceContainerConfig
<a name="API_InferenceContainerConfig"></a>

Provides configuration information for the inference container.

## Contents
<a name="API_InferenceContainerConfig_Contents"></a>

 ** imageUri **   <a name="API-Type-InferenceContainerConfig-imageUri"></a>
The registry path of the docker image that contains the inference algorithm. Clean Rooms ML currently only supports the `registry/repository[:tag]` image path format. For more information about using images in Clean Rooms ML, see the [Sagemaker API reference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html#sagemaker-Type-AlgorithmSpecification-TrainingImage).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_InferenceContainerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/InferenceContainerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/InferenceContainerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/InferenceContainerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
