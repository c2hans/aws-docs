---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_EncryptionConfig.html
---

# EncryptionConfig
<a name="API_connect-outbound-campaigns-v2_EncryptionConfig"></a>

Contains the encryption configuration for an Connect Customer instance.

## Contents
<a name="API_connect-outbound-campaigns-v2_EncryptionConfig_Contents"></a>

 ** enabled **   <a name="connect-Type-connect-outbound-campaigns-v2_EncryptionConfig-enabled"></a>
The status of whether encryption is done using a customer managed key or an AWS owned key.
Type: Boolean
Required: Yes

 ** encryptionType **   <a name="connect-Type-connect-outbound-campaigns-v2_EncryptionConfig-encryptionType"></a>
The type of encryption.
Type: String
Valid Values: `KMS`
Required: No

 ** keyArn **   <a name="connect-Type-connect-outbound-campaigns-v2_EncryptionConfig-keyArn"></a>
The Amazon Resource Name (ARN) of the customer managed key or an AWS owned key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_EncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/EncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/EncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/EncryptionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
