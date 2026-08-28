---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PackageEncryptionOptions.html
---

# PackageEncryptionOptions
<a name="API_PackageEncryptionOptions"></a>

Encryption options for a package.

## Contents
<a name="API_PackageEncryptionOptions_Contents"></a>

 ** EncryptionEnabled **   <a name="opensearchservice-Type-PackageEncryptionOptions-EncryptionEnabled"></a>
Whether encryption is enabled for the package.
Type: Boolean
Required: Yes

 ** KmsKeyIdentifier **   <a name="opensearchservice-Type-PackageEncryptionOptions-KmsKeyIdentifier"></a>
KMS key ID for encrypting the package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `.*`
Required: No

## See Also
<a name="API_PackageEncryptionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/PackageEncryptionOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/PackageEncryptionOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/PackageEncryptionOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
