---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_KernelGatewayImageConfig.html
---

# KernelGatewayImageConfig
<a name="API_KernelGatewayImageConfig"></a>

The configuration for the file system and kernels in a SageMaker AI image running as a KernelGateway app.

## Contents
<a name="API_KernelGatewayImageConfig_Contents"></a>

 ** KernelSpecs **   <a name="sagemaker-Type-KernelGatewayImageConfig-KernelSpecs"></a>
The specification of the Jupyter kernels in the image.
Type: Array of [KernelSpec](API_KernelSpec.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** FileSystemConfig **   <a name="sagemaker-Type-KernelGatewayImageConfig-FileSystemConfig"></a>
The Amazon Elastic File System storage configuration for a SageMaker AI image.
Type: [FileSystemConfig](API_FileSystemConfig.md) object
Required: No

## See Also
<a name="API_KernelGatewayImageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/KernelGatewayImageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/KernelGatewayImageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/KernelGatewayImageConfig)
