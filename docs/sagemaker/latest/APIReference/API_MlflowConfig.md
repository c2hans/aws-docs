---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MlflowConfig.html
---

# MlflowConfig
<a name="API_MlflowConfig"></a>

 The MLflow configuration using SageMaker managed MLflow.

## Contents
<a name="API_MlflowConfig_Contents"></a>

 ** MlflowResourceArn **   <a name="sagemaker-Type-MlflowConfig-MlflowResourceArn"></a>
 The Amazon Resource Name (ARN) of the MLflow resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-[a-zA-Z-]*/.*`
Required: Yes

 ** MlflowExperimentName **   <a name="sagemaker-Type-MlflowConfig-MlflowExperimentName"></a>
 The MLflow experiment name used for this job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** MlflowRunName **   <a name="sagemaker-Type-MlflowConfig-MlflowRunName"></a>
 The MLflow run name used for this job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_MlflowConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MlflowConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MlflowConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MlflowConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
