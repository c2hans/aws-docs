---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

Describes the encryption for a destination in Amazon S3.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** KMSEncryptionConfig **   <a name="Firehose-Type-EncryptionConfiguration-KMSEncryptionConfig"></a>
The encryption key.
Type: [KMSEncryptionConfig](API_KMSEncryptionConfig.md) object
Required: No

 ** NoEncryptionConfig **   <a name="Firehose-Type-EncryptionConfiguration-NoEncryptionConfig"></a>
Specifically override existing encryption information to ensure that no encryption is used.
Type: String
Valid Values: `NoEncryption`
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/EncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
