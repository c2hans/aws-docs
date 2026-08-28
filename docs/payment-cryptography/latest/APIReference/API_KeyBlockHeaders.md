---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_KeyBlockHeaders.html
---

# KeyBlockHeaders
<a name="API_KeyBlockHeaders"></a>

Optional metadata for export associated with the key material. This data is signed but transmitted in clear text.

## Contents
<a name="API_KeyBlockHeaders_Contents"></a>

 ** KeyExportability **   <a name="paymentcryptography-Type-KeyBlockHeaders-KeyExportability"></a>
Specifies subsequent exportability of the key within the key block after it is received by the receiving party. It can be used to further restrict exportability of the key after export from AWS Payment Cryptography.
When set to `EXPORTABLE`, the key can be subsequently exported by the receiver under a KEK using TR-31 or TR-34 key block export only. When set to `NON_EXPORTABLE`, the key cannot be subsequently exported by the receiver. When set to `SENSITIVE`, the key can be exported by the receiver under a KEK using TR-31, TR-34, RSA wrap and unwrap cryptogram or using a symmetric cryptogram key export method. For further information refer to [ANSI X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022).
Type: String
Valid Values: `EXPORTABLE | NON_EXPORTABLE | SENSITIVE`
Required: No

 ** KeyModesOfUse **   <a name="paymentcryptography-Type-KeyBlockHeaders-KeyModesOfUse"></a>
The list of cryptographic operations that you can perform using the key. The modes of use are deﬁned in section A.5.3 of the TR-31 spec.
Type: [KeyModesOfUse](API_KeyModesOfUse.md) object
Required: No

 ** KeyVersion **   <a name="paymentcryptography-Type-KeyBlockHeaders-KeyVersion"></a>
Parameter used to indicate the version of the key carried in the key block or indicate the value carried in the key block is a component of a key.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9A-Z]{2}+`
Required: No

 ** OptionalBlocks **   <a name="paymentcryptography-Type-KeyBlockHeaders-OptionalBlocks"></a>
Parameter used to indicate the type of optional data in key block headers. Refer to [ANSI X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022) for information on allowed data type for optional blocks.
Optional block character limit is 112 characters. For each optional block, 2 characters are reserved for optional block ID and 2 characters reserved for optional block length. More than one optional blocks can be included as long as the combined length does not increase 112 characters.
Type: String to string map
Key Length Constraints: Fixed length of 2.
Key Pattern: `[0-9A-Z]{2}+`
Value Length Constraints: Minimum length of 1. Maximum length of 108.
Value Pattern: `[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_KeyBlockHeaders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/KeyBlockHeaders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/KeyBlockHeaders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/KeyBlockHeaders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
