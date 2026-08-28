---
source_url: https://docs.aws.amazon.com/signer/latest/api/API_HashAlgorithmOptions.html
---

# HashAlgorithmOptions
<a name="API_HashAlgorithmOptions"></a>

The hash algorithms that are available to a code-signing job.

## Contents
<a name="API_HashAlgorithmOptions_Contents"></a>

 ** allowedValues **   <a name="signer-Type-HashAlgorithmOptions-allowedValues"></a>
The set of accepted hash algorithms allowed in a code-signing job.
Type: Array of strings
Valid Values: `SHA1 | SHA256`
Required: Yes

 ** defaultValue **   <a name="signer-Type-HashAlgorithmOptions-defaultValue"></a>
The default hash algorithm that is used in a code-signing job.
Type: String
Valid Values: `SHA1 | SHA256`
Required: Yes

## See Also
<a name="API_HashAlgorithmOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/HashAlgorithmOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/HashAlgorithmOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/HashAlgorithmOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
