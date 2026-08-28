---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_EncryptionKeyConfiguration.html
---

# EncryptionKeyConfiguration
<a name="API_EncryptionKeyConfiguration"></a>

The configuration of the encryption key used for an Autonomous Database. This is a union, so only one of the following members can be specified.

## Contents
<a name="API_EncryptionKeyConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsEncryptionKey **   <a name="odb-Type-EncryptionKeyConfiguration-awsEncryptionKey"></a>
The configuration of the AWS Key Management Service (KMS) encryption key.
Type: [AwsEncryptionKeyConfiguration](API_AwsEncryptionKeyConfiguration.md) object
Required: No

 ** ociEncryptionKey **   <a name="odb-Type-EncryptionKeyConfiguration-ociEncryptionKey"></a>
The configuration of the Oracle Cloud Infrastructure (OCI) Vault encryption key.
Type: [OciEncryptionKeyConfiguration](API_OciEncryptionKeyConfiguration.md) object
Required: No

 ** okvEncryptionKey **   <a name="odb-Type-EncryptionKeyConfiguration-okvEncryptionKey"></a>
The configuration of the Oracle Key Vault (OKV) encryption key.
Type: [OkvEncryptionKeyConfiguration](API_OkvEncryptionKeyConfiguration.md) object
Required: No

## See Also
<a name="API_EncryptionKeyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/EncryptionKeyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/EncryptionKeyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/EncryptionKeyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
