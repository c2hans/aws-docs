---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_JupyterLabAppImageConfig.html
---

# JupyterLabAppImageConfig
<a name="API_JupyterLabAppImageConfig"></a>

The configuration for the file system and kernels in a SageMaker AI image running as a JupyterLab app. The `FileSystemConfig` object is not supported.

## Contents
<a name="API_JupyterLabAppImageConfig_Contents"></a>

 ** ContainerConfig **   <a name="sagemaker-Type-JupyterLabAppImageConfig-ContainerConfig"></a>
The configuration used to run the application image container.
Type: [ContainerConfig](API_ContainerConfig.md) object
Required: No

 ** FileSystemConfig **   <a name="sagemaker-Type-JupyterLabAppImageConfig-FileSystemConfig"></a>
The Amazon Elastic File System storage configuration for a SageMaker AI image.
Type: [FileSystemConfig](API_FileSystemConfig.md) object
Required: No

## See Also
<a name="API_JupyterLabAppImageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/JupyterLabAppImageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/JupyterLabAppImageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/JupyterLabAppImageConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
