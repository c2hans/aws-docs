---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_S3FileSystemConfig.html
---

# S3FileSystemConfig
<a name="API_S3FileSystemConfig"></a>

Configuration for the custom Amazon S3 file system.

## Contents
<a name="API_S3FileSystemConfig_Contents"></a>

 ** S3Uri **   <a name="sagemaker-Type-S3FileSystemConfig-S3Uri"></a>
The Amazon S3 URI of the S3 file system configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(s3)://([^/]+)/?(.*)`
Required: Yes

 ** MountPath **   <a name="sagemaker-Type-S3FileSystemConfig-MountPath"></a>
The file system path where the Amazon S3 storage location will be mounted within the Amazon SageMaker Studio environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3FileSystemConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/S3FileSystemConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/S3FileSystemConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/S3FileSystemConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
