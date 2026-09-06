---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ProposalSummary.html
---

# ProposalSummary
<a name="API_marketplace-agreements_ProposalSummary"></a>

A summary of the proposal received from the proposer.

## Contents
<a name="API_marketplace-agreements_ProposalSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** offerId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ProposalSummary-offerId"></a>
The unique identifier of the offer in AWS Marketplace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\S{1,64}`
Required: No

 ** offerSetId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ProposalSummary-offerSetId"></a>
A unique identifier for the offer set containing this offer. All agreements created from offers in this set include this identifier as context.
Type: String
Pattern: `\S{1,50}`
Required: No

 ** resources **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ProposalSummary-resources"></a>
The list of resources involved in the agreement.
Type: Array of [Resource](API_marketplace-agreements_Resource.md) objects
Required: No

## See Also
<a name="API_marketplace-agreements_ProposalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ProposalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ProposalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ProposalSummary)
