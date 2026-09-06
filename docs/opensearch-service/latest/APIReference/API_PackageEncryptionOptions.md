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
