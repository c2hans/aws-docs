---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelRegisterSettings.html
---

# ModelRegisterSettings
<a name="API_ModelRegisterSettings"></a>

The model registry settings for the SageMaker Canvas application.

## Contents
<a name="API_ModelRegisterSettings_Contents"></a>

 ** CrossAccountModelRegisterRoleArn **   <a name="sagemaker-Type-ModelRegisterSettings-CrossAccountModelRegisterRoleArn"></a>
The Amazon Resource Name (ARN) of the SageMaker model registry account. Required only to register model versions created by a different SageMaker Canvas AWS account than the AWS account in which SageMaker model registry is set up.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** Status **   <a name="sagemaker-Type-ModelRegisterSettings-Status"></a>
Describes whether the integration to the model registry is enabled or disabled in the Canvas application.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ModelRegisterSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelRegisterSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelRegisterSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelRegisterSettings)
