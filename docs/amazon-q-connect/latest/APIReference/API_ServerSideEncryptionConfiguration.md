---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ServerSideEncryptionConfiguration.html
---

# ServerSideEncryptionConfiguration
<a name="API_amazon-q-connect_ServerSideEncryptionConfiguration"></a>

The configuration information for the customer managed key used for encryption.

## Contents
<a name="API_amazon-q-connect_ServerSideEncryptionConfiguration_Contents"></a>

 ** kmsKeyId **   <a name="connect-Type-amazon-q-connect_ServerSideEncryptionConfiguration-kmsKeyId"></a>
The customer managed key used for encryption. For more information about setting up a customer managed key for Amazon Q in Connect, see [Enable Amazon Q in Connect for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html). For information about valid ID values, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_ServerSideEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ServerSideEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ServerSideEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ServerSideEncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
