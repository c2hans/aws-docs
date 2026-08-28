---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SymmetricEncryptionAttributes.html
---

# SymmetricEncryptionAttributes
<a name="API_SymmetricEncryptionAttributes"></a>

Parameters requried to encrypt plaintext data using symmetric keys.

## Contents
<a name="API_SymmetricEncryptionAttributes_Contents"></a>

 ** Mode **   <a name="paymentcryptographydata-Type-SymmetricEncryptionAttributes-Mode"></a>
The block cipher method to use for encryption.
Type: String
Valid Values: `ECB | CBC | CFB | CFB1 | CFB8 | CFB64 | CFB128 | OFB`
Required: Yes

 ** InitializationVector **   <a name="paymentcryptographydata-Type-SymmetricEncryptionAttributes-InitializationVector"></a>
An input used to provide the intial state. If no value is provided, AWS Payment Cryptography defaults it to zero.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `(?:[0-9a-fA-F]{16}|[0-9a-fA-F]{32})`
Required: No

 ** PaddingType **   <a name="paymentcryptographydata-Type-SymmetricEncryptionAttributes-PaddingType"></a>
The padding to be included with the data.
Type: String
Valid Values: `PKCS1 | OAEP_SHA1 | OAEP_SHA256 | OAEP_SHA512`
Required: No

## See Also
<a name="API_SymmetricEncryptionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/SymmetricEncryptionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/SymmetricEncryptionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/SymmetricEncryptionAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
