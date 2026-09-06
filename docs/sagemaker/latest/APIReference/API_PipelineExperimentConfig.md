---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineExperimentConfig.html
---

# PipelineExperimentConfig
<a name="API_PipelineExperimentConfig"></a>

Specifies the names of the experiment and trial created by a pipeline.

## Contents
<a name="API_PipelineExperimentConfig_Contents"></a>

 ** ExperimentName **   <a name="sagemaker-Type-PipelineExperimentConfig-ExperimentName"></a>
The name of the experiment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** TrialName **   <a name="sagemaker-Type-PipelineExperimentConfig-TrialName"></a>
The name of the trial.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

## See Also
<a name="API_PipelineExperimentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PipelineExperimentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PipelineExperimentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PipelineExperimentConfig)
