---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergEncryptedKey.html
---

# IcebergEncryptedKey
<a name="API_IcebergEncryptedKey"></a>

Encryption key structure used for Iceberg table encryption. Contains the key ID, encrypted key metadata, optional reference to the encrypting key, and additional properties for the table's encryption scheme.

## Contents
<a name="API_IcebergEncryptedKey_Contents"></a>

 ** EncryptedKeyMetadata **   <a name="Glue-Type-IcebergEncryptedKey-EncryptedKeyMetadata"></a>
Encrypted key and metadata, base64 encoded. The format of encrypted key metadata is determined by the table's encryption scheme and can be a wrapped format specific to the table's KMS provider.
Type: String
Length Constraints: Maximum length of 2056.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** KeyId **   <a name="Glue-Type-IcebergEncryptedKey-KeyId"></a>
Unique identifier of the encryption key used for Iceberg table encryption. This ID is used to reference the key in table metadata and track which key was used to encrypt specific data.
Type: String
Length Constraints: Maximum length of 2056.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** EncryptedById **   <a name="Glue-Type-IcebergEncryptedKey-EncryptedById"></a>
Optional ID of the key used to encrypt or wrap the key metadata in Iceberg table encryption. This field references another encryption key that was used to encrypt the current key's metadata.
Type: String
Length Constraints: Maximum length of 2056.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Properties **   <a name="Glue-Type-IcebergEncryptedKey-Properties"></a>
A string to string map of additional metadata used by the table's encryption scheme. These properties provide additional context and configuration for the encryption key implementation.
Type: String to string map
Required: No

## See Also
<a name="API_IcebergEncryptedKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergEncryptedKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergEncryptedKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergEncryptedKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
