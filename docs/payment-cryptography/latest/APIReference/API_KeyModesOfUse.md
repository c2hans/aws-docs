---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_KeyModesOfUse.html
---

# KeyModesOfUse
<a name="API_KeyModesOfUse"></a>

The list of cryptographic operations that you can perform using the key. The modes of use are deﬁned in section A.5.3 of the TR-31 spec.

## Contents
<a name="API_KeyModesOfUse_Contents"></a>

 ** Decrypt **   <a name="paymentcryptography-Type-KeyModesOfUse-Decrypt"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to decrypt data.
Type: Boolean
Required: No

 ** DeriveKey **   <a name="paymentcryptography-Type-KeyModesOfUse-DeriveKey"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to derive new keys.
Type: Boolean
Required: No

 ** Encrypt **   <a name="paymentcryptography-Type-KeyModesOfUse-Encrypt"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to encrypt data.
Type: Boolean
Required: No

 ** Generate **   <a name="paymentcryptography-Type-KeyModesOfUse-Generate"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to generate and verify other card and PIN verification keys.
Type: Boolean
Required: No

 ** NoRestrictions **   <a name="paymentcryptography-Type-KeyModesOfUse-NoRestrictions"></a>
Speciﬁes whether an AWS Payment Cryptography key has no special restrictions other than the restrictions implied by `KeyUsage`.
Type: Boolean
Required: No

 ** Sign **   <a name="paymentcryptography-Type-KeyModesOfUse-Sign"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used for signing.
Type: Boolean
Required: No

 ** Unwrap **   <a name="paymentcryptography-Type-KeyModesOfUse-Unwrap"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to unwrap other keys.
Type: Boolean
Required: No

 ** Verify **   <a name="paymentcryptography-Type-KeyModesOfUse-Verify"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to verify signatures.
Type: Boolean
Required: No

 ** Wrap **   <a name="paymentcryptography-Type-KeyModesOfUse-Wrap"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to wrap other keys.
Type: Boolean
Required: No

## See Also
<a name="API_KeyModesOfUse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/KeyModesOfUse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/KeyModesOfUse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/KeyModesOfUse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
