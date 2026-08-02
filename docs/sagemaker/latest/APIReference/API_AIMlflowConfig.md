---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIMlflowConfig.html
---

# AIMlflowConfig
<a name="API_AIMlflowConfig"></a>

The MLflow tracking configuration for logging metrics and parameters to a SageMaker managed MLflow tracking server.

## Contents
<a name="API_AIMlflowConfig_Contents"></a>

 ** MlflowResourceArn **   <a name="sagemaker-Type-AIMlflowConfig-MlflowResourceArn"></a>
The Amazon Resource Name (ARN) of the SageMaker managed MLflow resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-(app|tracking-server)/.*`
Required: Yes

 ** MlflowExperimentName **   <a name="sagemaker-Type-AIMlflowConfig-MlflowExperimentName"></a>
The MLflow experiment name used for tracking.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\-_./]+`
Required: No

 ** MlflowRunName **   <a name="sagemaker-Type-AIMlflowConfig-MlflowRunName"></a>
The MLflow run name used for tracking.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\-_./]+`
Required: No

## See Also
<a name="API_AIMlflowConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIMlflowConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIMlflowConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIMlflowConfig)
