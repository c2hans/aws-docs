---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_EncryptionKey.html
---

# EncryptionKey
<a name="API_EncryptionKey"></a>

The encryption key used to encrypt this object.

## Contents
<a name="API_EncryptionKey_Contents"></a>

 ** Id **   <a name="translate-Type-EncryptionKey-Id"></a>
The Amazon Resource Name (ARN) of the encryption key being used to encrypt this object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Pattern: `(arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:kms:)?([a-z]{2}-[a-z]+(-[a-z]+)?-\d:)?(\d{12}:)?(((key/)?[a-zA-Z0-9-_]+)|(alias/[a-zA-Z0-9:/_-]+))`
Required: Yes

 ** Type **   <a name="translate-Type-EncryptionKey-Type"></a>
The type of encryption key used by Amazon Translate to encrypt this object.
Type: String
Valid Values: `KMS`
Required: Yes

## See Also
<a name="API_EncryptionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/EncryptionKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/EncryptionKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/EncryptionKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
