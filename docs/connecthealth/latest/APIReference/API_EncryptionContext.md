---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_EncryptionContext.html
---

# EncryptionContext
<a name="API_EncryptionContext"></a>

Encryption context for a Domain.

## Contents
<a name="API_EncryptionContext_Contents"></a>

 ** encryptionType **   <a name="connecthealth-Type-EncryptionContext-encryptionType"></a>
The type of encryption key used.
Type: String
Valid Values: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KEY`
Required: Yes

 ** kmsKeyArn **   <a name="connecthealth-Type-EncryptionContext-kmsKeyArn"></a>
The ARN of the KMS key. Only present when encryptionType is CUSTOMER\_MANAGED\_KEY.
Type: String
Pattern: `arn:aws:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9-]+`
Required: No

## See Also
<a name="API_EncryptionContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/EncryptionContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/EncryptionContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/EncryptionContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
