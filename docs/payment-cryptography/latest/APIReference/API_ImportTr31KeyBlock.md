---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportTr31KeyBlock.html
---

# ImportTr31KeyBlock
<a name="API_ImportTr31KeyBlock"></a>

Parameter information for key material import using symmetric TR-31 key exchange method.

## Contents
<a name="API_ImportTr31KeyBlock_Contents"></a>

 ** WrappedKeyBlock **   <a name="paymentcryptography-Type-ImportTr31KeyBlock-WrappedKeyBlock"></a>
The TR-31 wrapped key block to import.
Type: String
Length Constraints: Minimum length of 56. Maximum length of 9984.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

 ** WrappingKeyIdentifier **   <a name="paymentcryptography-Type-ImportTr31KeyBlock-WrappingKeyIdentifier"></a>
The `KeyARN` of the key that will decrypt or unwrap a TR-31 key block during import.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

## See Also
<a name="API_ImportTr31KeyBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ImportTr31KeyBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ImportTr31KeyBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ImportTr31KeyBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
