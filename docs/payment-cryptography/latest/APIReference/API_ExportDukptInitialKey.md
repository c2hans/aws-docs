---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportDukptInitialKey.html
---

# ExportDukptInitialKey
<a name="API_ExportDukptInitialKey"></a>

Parameter information for IPEK generation during export.

## Contents
<a name="API_ExportDukptInitialKey_Contents"></a>

 ** KeySerialNumber **   <a name="paymentcryptography-Type-ExportDukptInitialKey-KeySerialNumber"></a>
The KSN for IPEK generation using DUKPT.
KSN must be padded before sending to AWS Payment Cryptography. KSN hex length should be 20 for a TDES\_2KEY key or 24 for an AES key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 24.
Pattern: `[0-9A-F]{20}$|^[0-9A-F]{24}`
Required: Yes

## See Also
<a name="API_ExportDukptInitialKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ExportDukptInitialKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ExportDukptInitialKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ExportDukptInitialKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
