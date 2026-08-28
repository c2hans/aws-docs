---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_OkvEncryptionKeyConfiguration.html
---

# OkvEncryptionKeyConfiguration
<a name="API_OkvEncryptionKeyConfiguration"></a>

The configuration of the Oracle Key Vault (OKV) encryption key used for an Autonomous Database.

## Contents
<a name="API_OkvEncryptionKeyConfiguration_Contents"></a>

 ** certificateDirectoryName **   <a name="odb-Type-OkvEncryptionKeyConfiguration-certificateDirectoryName"></a>
The name of the directory that contains the Oracle Key Vault (OKV) certificate.
Type: String
Required: Yes

 ** directoryName **   <a name="odb-Type-OkvEncryptionKeyConfiguration-directoryName"></a>
The name of the directory where the Oracle Key Vault (OKV) configuration is stored.
Type: String
Required: Yes

 ** okvKmsKey **   <a name="odb-Type-OkvEncryptionKeyConfiguration-okvKmsKey"></a>
The identifier of the Oracle Key Vault (OKV) key to use for encryption.
Type: String
Required: Yes

 ** okvUri **   <a name="odb-Type-OkvEncryptionKeyConfiguration-okvUri"></a>
The URI of the Oracle Key Vault (OKV) server.
Type: String
Required: Yes

 ** certificateId **   <a name="odb-Type-OkvEncryptionKeyConfiguration-certificateId"></a>
The identifier of the Oracle Key Vault (OKV) certificate.
Type: String
Required: No

## See Also
<a name="API_OkvEncryptionKeyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/OkvEncryptionKeyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/OkvEncryptionKeyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/OkvEncryptionKeyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
