---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgeOutputConfig.html
---

# EdgeOutputConfig
<a name="API_EdgeOutputConfig"></a>

The output configuration.

## Contents
<a name="API_EdgeOutputConfig_Contents"></a>

 ** S3OutputLocation **   <a name="sagemaker-Type-EdgeOutputConfig-S3OutputLocation"></a>
The Amazon Simple Storage (S3) bucker URI.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-EdgeOutputConfig-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume after compilation job. If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** PresetDeploymentConfig **   <a name="sagemaker-Type-EdgeOutputConfig-PresetDeploymentConfig"></a>
The configuration used to create deployment artifacts. Specify configuration options with a JSON string. The available configuration options for each type are:
+  `ComponentName` (optional) - Name of the GreenGrass V2 component. If not specified, the default name generated consists of "SagemakerEdgeManager" and the name of your SageMaker Edge Manager packaging job.
+  `ComponentDescription` (optional) - Description of the component.
+  `ComponentVersion` (optional) - The version of the component.
**Note**
 AWS IoT Greengrass uses semantic versions for components. Semantic versions follow a* major.minor.patch* number system. For example, version 1.0.0 represents the first major release for a component. For more information, see the [semantic version specification](https://semver.org/).
+  `PlatformOS` (optional) - The name of the operating system for the platform. Supported platforms include Windows and Linux.
+  `PlatformArchitecture` (optional) - The processor architecture for the platform.

  Supported architectures Windows include: Windows32\_x86, Windows64\_x64.

  Supported architectures for Linux include: Linux x86\_64, Linux ARMV8.
Type: String
Required: No

 ** PresetDeploymentType **   <a name="sagemaker-Type-EdgeOutputConfig-PresetDeploymentType"></a>
The deployment type SageMaker Edge Manager will create. Currently only supports AWS IoT Greengrass Version 2 components.
Type: String
Valid Values: `GreengrassV2Component`
Required: No

## See Also
<a name="API_EdgeOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgeOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgeOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgeOutputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
