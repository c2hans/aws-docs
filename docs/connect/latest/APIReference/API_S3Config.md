---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_S3Config.html
---

# S3Config
<a name="API_S3Config"></a>

Information about the Amazon Simple Storage Service (Amazon S3) storage type.

## Contents
<a name="API_S3Config_Contents"></a>

 ** BucketName **   <a name="connect-Type-S3Config-BucketName"></a>
The S3 bucket name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** BucketPrefix **   <a name="connect-Type-S3Config-BucketPrefix"></a>
The S3 bucket prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** EncryptionConfig **   <a name="connect-Type-S3Config-EncryptionConfig"></a>
The Amazon S3 encryption configuration.
Type: [EncryptionConfig](API_EncryptionConfig.md) object
Required: No

## See Also
<a name="API_S3Config_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/S3Config)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/S3Config)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/S3Config)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
