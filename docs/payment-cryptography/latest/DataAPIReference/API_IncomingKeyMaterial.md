---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_IncomingKeyMaterial.html
---

# IncomingKeyMaterial
<a name="API_IncomingKeyMaterial"></a>

Parameter information of the incoming WrappedKeyBlock containing the transaction key.

## Contents
<a name="API_IncomingKeyMaterial_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DiffieHellmanTr31KeyBlock **   <a name="paymentcryptographydata-Type-IncomingKeyMaterial-DiffieHellmanTr31KeyBlock"></a>
Parameter information of the TR31WrappedKeyBlock containing the transaction key wrapped using an ECDH dervied key.
Type: [IncomingDiffieHellmanTr31KeyBlock](API_IncomingDiffieHellmanTr31KeyBlock.md) object
Required: No

## See Also
<a name="API_IncomingKeyMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/IncomingKeyMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/IncomingKeyMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/IncomingKeyMaterial)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
