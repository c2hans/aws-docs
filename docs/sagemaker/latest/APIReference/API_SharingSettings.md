---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SharingSettings.html
---

# SharingSettings
<a name="API_SharingSettings"></a>

Specifies options for sharing Amazon SageMaker AI Studio notebooks. These settings are specified as part of `DefaultUserSettings` when the `CreateDomain` API is called, and as part of `UserSettings` when the `CreateUserProfile` API is called. When `SharingSettings` is not specified, notebook sharing isn't allowed.

## Contents
<a name="API_SharingSettings_Contents"></a>

 ** NotebookOutputOption **   <a name="sagemaker-Type-SharingSettings-NotebookOutputOption"></a>
Whether to include the notebook cell output when sharing the notebook. The default is `Disabled`.
Type: String
Valid Values: `Allowed | Disabled`
Required: No

 ** S3KmsKeyId **   <a name="sagemaker-Type-SharingSettings-S3KmsKeyId"></a>
When `NotebookOutputOption` is `Allowed`, the AWS Key Management Service (KMS) encryption key ID used to encrypt the notebook cell output in the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** S3OutputPath **   <a name="sagemaker-Type-SharingSettings-S3OutputPath"></a>
When `NotebookOutputOption` is `Allowed`, the Amazon S3 bucket used to store the shared notebook snapshots.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_SharingSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SharingSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SharingSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SharingSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
