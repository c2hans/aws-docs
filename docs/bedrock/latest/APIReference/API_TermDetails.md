---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_TermDetails.html
---

# TermDetails
<a name="API_TermDetails"></a>

Describes the usage terms of an offer.

## Contents
<a name="API_TermDetails_Contents"></a>

 ** legalTerm **   <a name="bedrock-Type-TermDetails-legalTerm"></a>
Describes the legal terms.
Type: [LegalTerm](API_LegalTerm.md) object
Required: Yes

 ** supportTerm **   <a name="bedrock-Type-TermDetails-supportTerm"></a>
Describes the support terms.
Type: [SupportTerm](API_SupportTerm.md) object
Required: Yes

 ** usageBasedPricingTerm **   <a name="bedrock-Type-TermDetails-usageBasedPricingTerm"></a>
 Describes the pricing terms.
Type: [PricingTerm](API_PricingTerm.md) object
Required: Yes

 ** validityTerm **   <a name="bedrock-Type-TermDetails-validityTerm"></a>
 Describes the validity terms.
Type: [ValidityTerm](API_ValidityTerm.md) object
Required: No

## See Also
<a name="API_TermDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/TermDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/TermDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/TermDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
