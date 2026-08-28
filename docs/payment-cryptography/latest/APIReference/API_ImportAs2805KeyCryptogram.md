---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportAs2805KeyCryptogram.html
---

# ImportAs2805KeyCryptogram
<a name="API_ImportAs2805KeyCryptogram"></a>

Parameter information for key material import using AS2805 key cryptogram format.

## Contents
<a name="API_ImportAs2805KeyCryptogram_Contents"></a>

 ** As2805KeyVariant **   <a name="paymentcryptography-Type-ImportAs2805KeyCryptogram-As2805KeyVariant"></a>
The cryptographic usage of the key under import.
Type: String
Valid Values: `TERMINAL_MAJOR_KEY_VARIANT_00 | PIN_ENCRYPTION_KEY_VARIANT_28 | MESSAGE_AUTHENTICATION_KEY_VARIANT_24 | DATA_ENCRYPTION_KEY_VARIANT_22`
Required: Yes

 ** Exportable **   <a name="paymentcryptography-Type-ImportAs2805KeyCryptogram-Exportable"></a>
Specified whether the key is exportable. This data is immutable after the key is imported.
Type: Boolean
Required: Yes

 ** KeyAlgorithm **   <a name="paymentcryptography-Type-ImportAs2805KeyCryptogram-KeyAlgorithm"></a>
The key algorithm of the key under import.
Type: String
Valid Values: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256 | HMAC_SHA256 | HMAC_SHA384 | HMAC_SHA512 | HMAC_SHA224 | RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521`
Required: Yes

 ** KeyModesOfUse **   <a name="paymentcryptography-Type-ImportAs2805KeyCryptogram-KeyModesOfUse"></a>
The list of cryptographic operations that you can perform using the key. The modes of use are deﬁned in section A.5.3 of the TR-31 spec.
Type: [KeyModesOfUse](API_KeyModesOfUse.md) object
Required: Yes

 ** WrappedKeyCryptogram **   <a name="paymentcryptography-Type-ImportAs2805KeyCryptogram-WrappedKeyCryptogram"></a>
The wrapped key cryptogram under import.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 4096.
Pattern: `[0-9A-F]+`
Required: Yes

 ** WrappingKeyIdentifier **   <a name="paymentcryptography-Type-ImportAs2805KeyCryptogram-WrappingKeyIdentifier"></a>
A key identifier that can be either a key ARN or an alias name. This allows flexible key identification in operations.
When using a key ARN, it must be a fully qualified ARN in the format: `arn:aws:payment-cryptography:region:account:key/key-id`.
When using an alias, it must begin with `alias/` followed by the alias name.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

## See Also
<a name="API_ImportAs2805KeyCryptogram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ImportAs2805KeyCryptogram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ImportAs2805KeyCryptogram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ImportAs2805KeyCryptogram)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
