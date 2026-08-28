---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_EncryptionSummary.html
---

# EncryptionSummary
<a name="API_EncryptionSummary"></a>

The encryption configuration for an Autonomous Database.

## Contents
<a name="API_EncryptionSummary_Contents"></a>

 ** encryptionKeyConfiguration **   <a name="odb-Type-EncryptionSummary-encryptionKeyConfiguration"></a>
The configuration of the encryption key used for the Autonomous Database.
Type: [EncryptionKeyConfiguration](API_EncryptionKeyConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** encryptionKeyProvider **   <a name="odb-Type-EncryptionSummary-encryptionKeyProvider"></a>
The provider of the encryption key used for the Autonomous Database.
Type: String
Valid Values: `ORACLE_MANAGED | AWS_KMS | OKV | OCI`
Required: No

## See Also
<a name="API_EncryptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/EncryptionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/EncryptionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/EncryptionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
