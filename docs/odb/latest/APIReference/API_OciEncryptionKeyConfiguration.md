---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_OciEncryptionKeyConfiguration.html
---

# OciEncryptionKeyConfiguration
<a name="API_OciEncryptionKeyConfiguration"></a>

The configuration of the Oracle Cloud Infrastructure (OCI) Vault encryption key used for an Autonomous Database.

## Contents
<a name="API_OciEncryptionKeyConfiguration_Contents"></a>

 ** kmsKeyId **   <a name="odb-Type-OciEncryptionKeyConfiguration-kmsKeyId"></a>
The Oracle Cloud Identifier (OCID) of the OCI Vault key to use for encryption.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** vaultId **   <a name="odb-Type-OciEncryptionKeyConfiguration-vaultId"></a>
The Oracle Cloud Identifier (OCID) of the OCI Vault that contains the encryption key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_OciEncryptionKeyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/OciEncryptionKeyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/OciEncryptionKeyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/OciEncryptionKeyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
