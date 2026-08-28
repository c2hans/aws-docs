---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_JobOutputDataConfig.html
---

# JobOutputDataConfig
<a name="API_JobOutputDataConfig"></a>

Specifies the path to the S3 location where you want to store hybrid job artifacts and the encryption key used to store them.

## Contents
<a name="API_JobOutputDataConfig_Contents"></a>

 ** s3Path **   <a name="braket-Type-JobOutputDataConfig-s3Path"></a>
Identifies the S3 path where you want Amazon Braket to store the hybrid job training artifacts. For example, `s3://bucket-name/key-name-prefix`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** kmsKeyId **   <a name="braket-Type-JobOutputDataConfig-kmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that Amazon Braket uses to encrypt the hybrid job training artifacts at rest using Amazon S3 server-side encryption.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_JobOutputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/JobOutputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/JobOutputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/JobOutputDataConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
