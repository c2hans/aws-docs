---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Offer.html
---

# Offer
<a name="API_Offer"></a>

An offer dictates usage terms for the model.

## Contents
<a name="API_Offer_Contents"></a>

 ** offerToken **   <a name="bedrock-Type-Offer-offerToken"></a>
Offer token.
Type: String
Required: Yes

 ** termDetails **   <a name="bedrock-Type-Offer-termDetails"></a>
Details about the terms of the offer.
Type: [TermDetails](API_TermDetails.md) object
Required: Yes

 ** offerId **   <a name="bedrock-Type-Offer-offerId"></a>
Offer Id for a model offer.
Type: String
Required: No

## See Also
<a name="API_Offer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/Offer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/Offer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/Offer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
