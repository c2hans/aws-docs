---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SAMLPrivateKey.html
---

# SAMLPrivateKey
<a name="API_SAMLPrivateKey"></a>

Contains the private keys for the SAML provider.

This data type is used as a response element in the [GetSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSAMLProvider.html) operation.

## Contents
<a name="API_SAMLPrivateKey_Contents"></a>

 ** KeyId **
The unique identifier for the SAML private key.
Type: String
Length Constraints: Minimum length of 22. Maximum length of 64.
Pattern: `[A-Z0-9]+`
Required: No

 ** Timestamp **
The date and time, in [ISO 8601 date-time ](http://www.iso.org/iso/iso8601) format, when the private key was uploaded.
Type: Timestamp
Required: No

## See Also
<a name="API_SAMLPrivateKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SAMLPrivateKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SAMLPrivateKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SAMLPrivateKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
