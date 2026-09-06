---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgePresetDeploymentOutput.html
---

# EdgePresetDeploymentOutput
<a name="API_EdgePresetDeploymentOutput"></a>

The output of a SageMaker Edge Manager deployable resource.

## Contents
<a name="API_EdgePresetDeploymentOutput_Contents"></a>

 ** Type **   <a name="sagemaker-Type-EdgePresetDeploymentOutput-Type"></a>
The deployment type created by SageMaker Edge Manager. Currently only supports AWS IoT Greengrass Version 2 components.
Type: String
Valid Values: `GreengrassV2Component`
Required: Yes

 ** Artifact **   <a name="sagemaker-Type-EdgePresetDeploymentOutput-Artifact"></a>
The Amazon Resource Name (ARN) of the generated deployable resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** Status **   <a name="sagemaker-Type-EdgePresetDeploymentOutput-Status"></a>
The status of the deployable resource.
Type: String
Valid Values: `COMPLETED | FAILED`
Required: No

 ** StatusMessage **   <a name="sagemaker-Type-EdgePresetDeploymentOutput-StatusMessage"></a>
Returns a message describing the status of the deployed resource.
Type: String
Required: No

## See Also
<a name="API_EdgePresetDeploymentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgePresetDeploymentOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgePresetDeploymentOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgePresetDeploymentOutput)
