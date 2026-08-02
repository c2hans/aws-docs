---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CodeEditorAppImageConfig.html
---

# CodeEditorAppImageConfig
<a name="API_CodeEditorAppImageConfig"></a>

The configuration for the file system and kernels in a SageMaker image running as a Code Editor app. The `FileSystemConfig` object is not supported.

## Contents
<a name="API_CodeEditorAppImageConfig_Contents"></a>

 ** ContainerConfig **   <a name="sagemaker-Type-CodeEditorAppImageConfig-ContainerConfig"></a>
The configuration used to run the application image container.
Type: [ContainerConfig](API_ContainerConfig.md) object
Required: No

 ** FileSystemConfig **   <a name="sagemaker-Type-CodeEditorAppImageConfig-FileSystemConfig"></a>
The Amazon Elastic File System storage configuration for a SageMaker AI image.
Type: [FileSystemConfig](API_FileSystemConfig.md) object
Required: No

## See Also
<a name="API_CodeEditorAppImageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CodeEditorAppImageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CodeEditorAppImageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CodeEditorAppImageConfig)
