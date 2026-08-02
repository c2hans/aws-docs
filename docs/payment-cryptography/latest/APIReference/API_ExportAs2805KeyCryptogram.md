---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportAs2805KeyCryptogram.html
---

# ExportAs2805KeyCryptogram
<a name="API_ExportAs2805KeyCryptogram"></a>

Parameter information for key material export using AS2805 key cryptogram format.

## Contents
<a name="API_ExportAs2805KeyCryptogram_Contents"></a>

 ** As2805KeyVariant **   <a name="paymentcryptography-Type-ExportAs2805KeyCryptogram-As2805KeyVariant"></a>
The cryptographic usage of the key under export.
Type: String
Valid Values: `TERMINAL_MAJOR_KEY_VARIANT_00 | PIN_ENCRYPTION_KEY_VARIANT_28 | MESSAGE_AUTHENTICATION_KEY_VARIANT_24 | DATA_ENCRYPTION_KEY_VARIANT_22`
Required: Yes

 ** WrappingKeyIdentifier **   <a name="paymentcryptography-Type-ExportAs2805KeyCryptogram-WrappingKeyIdentifier"></a>
A key identifier that can be either a key ARN or an alias name. This allows flexible key identification in operations.
When using a key ARN, it must be a fully qualified ARN in the format: `arn:aws:payment-cryptography:region:account:key/key-id`.
When using an alias, it must begin with `alias/` followed by the alias name.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

## See Also
<a name="API_ExportAs2805KeyCryptogram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ExportAs2805KeyCryptogram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ExportAs2805KeyCryptogram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ExportAs2805KeyCryptogram)
