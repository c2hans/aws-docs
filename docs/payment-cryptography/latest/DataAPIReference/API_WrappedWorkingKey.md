---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_WrappedWorkingKey.html
---

# WrappedWorkingKey
<a name="API_WrappedWorkingKey"></a>

The parameter information of the outgoing wrapped key block.

## Contents
<a name="API_WrappedWorkingKey_Contents"></a>

 ** KeyCheckValue **   <a name="paymentcryptographydata-Type-WrappedWorkingKey-KeyCheckValue"></a>
The key check value (KCV) of the key contained within the outgoing TR31WrappedKeyBlock.
 The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed. For more information on KCV, see [KCV](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/terminology.html#terms.kcv) in the * AWS Payment Cryptography User Guide*.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** WrappedKeyMaterial **   <a name="paymentcryptographydata-Type-WrappedWorkingKey-WrappedKeyMaterial"></a>
The wrapped key block of the outgoing transaction key.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 16384.
Required: Yes

 ** WrappedKeyMaterialFormat **   <a name="paymentcryptographydata-Type-WrappedWorkingKey-WrappedKeyMaterialFormat"></a>
The key block format of the wrapped key.
Type: String
Valid Values: `KEY_CRYPTOGRAM | TR31_KEY_BLOCK | TR34_KEY_BLOCK`
Required: Yes

## See Also
<a name="API_WrappedWorkingKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/WrappedWorkingKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/WrappedWorkingKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/WrappedWorkingKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
