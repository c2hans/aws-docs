---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackageConfig.html
---

# ModelPackageConfig
<a name="API_ModelPackageConfig"></a>

 The configuration for the Model package.

## Contents
<a name="API_ModelPackageConfig_Contents"></a>

 ** ModelPackageGroupArn **   <a name="sagemaker-Type-ModelPackageConfig-ModelPackageGroupArn"></a>
 The Amazon Resource Name (ARN) of the model package group of output model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package-group/[\S]{1,2048}`
Required: Yes

 ** SourceModelPackageArn **   <a name="sagemaker-Type-ModelPackageConfig-SourceModelPackageArn"></a>
 The Amazon Resource Name (ARN) of the source model package used for continued fine-tuning and custom model evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: No

## See Also
<a name="API_ModelPackageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackageConfig)
