---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_ServerSideEncryptionConfiguration.html
---

# ServerSideEncryptionConfiguration
<a name="API_ServerSideEncryptionConfiguration"></a>

Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Kendra. Amazon Kendra doesn't support asymmetric keys.

## Contents
<a name="API_ServerSideEncryptionConfiguration_Contents"></a>

 ** KmsKeyId **   <a name="kendra-Type-ServerSideEncryptionConfiguration-KmsKeyId"></a>
The identifier of the AWS KMS key. Amazon Kendra doesn't support asymmetric keys.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ServerSideEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ServerSideEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ServerSideEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ServerSideEncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
