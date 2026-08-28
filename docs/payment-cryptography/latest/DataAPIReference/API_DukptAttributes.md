---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DukptAttributes.html
---

# DukptAttributes
<a name="API_DukptAttributes"></a>

Parameters that are used for Derived Unique Key Per Transaction (DUKPT) derivation algorithm.

## Contents
<a name="API_DukptAttributes_Contents"></a>

 ** DukptDerivationType **   <a name="paymentcryptographydata-Type-DukptAttributes-DukptDerivationType"></a>
The key type derived using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you can't use `AES_128` as a derivation type for a BDK of `AES_128` or `TDES_2KEY`.
Type: String
Valid Values: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256`
Required: Yes

 ** KeySerialNumber **   <a name="paymentcryptographydata-Type-DukptAttributes-KeySerialNumber"></a>
The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 24.
Pattern: `(?:[0-9a-fA-F]{16}|[0-9a-fA-F]{20}|[0-9a-fA-F]{24})`
Required: Yes

## See Also
<a name="API_DukptAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/DukptAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/DukptAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/DukptAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
