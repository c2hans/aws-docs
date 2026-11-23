---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchRelatedEntityIdentifiers.html
---

# OpportunitySearchRelatedEntityIdentifiers

Contains the related-entity identifiers (AWS Marketplace offers, offer sets, and solutions) returned for an opportunity in search results.

## Contents
<a name="API_OpportunitySearchRelatedEntityIdentifiers_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsMarketplaceOffers **   <a name="AWSPartnerCentral-Type-OpportunitySearchRelatedEntityIdentifiers-AwsMarketplaceOffers"></a>
The AWS Marketplace offers associated with this opportunity.
Type: Array of strings
Pattern: `arn:aws:aws-marketplace:[a-z]{1,2}-[a-z]*-\d+:\d{12}:AWSMarketplace/Offer/.*`
Required: No

 ** AwsMarketplaceOfferSets **   <a name="AWSPartnerCentral-Type-OpportunitySearchRelatedEntityIdentifiers-AwsMarketplaceOfferSets"></a>
The AWS Marketplace offer sets associated with this opportunity.
Type: Array of strings
Pattern: `arn:aws:aws-marketplace:[a-z]{1,2}-[a-z]*-\d+:\d{12}:AWSMarketplace/OfferSet/offerset-.*`
Required: No

 ** AwsMarketplaceSolutions **   <a name="AWSPartnerCentral-Type-OpportunitySearchRelatedEntityIdentifiers-AwsMarketplaceSolutions"></a>
The AWS Marketplace solutions associated with this opportunity.
Type: Array of strings
Length Constraints: Minimum length of 4. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** Solutions **   <a name="AWSPartnerCentral-Type-OpportunitySearchRelatedEntityIdentifiers-Solutions"></a>
The proposed solutions to address the customer's business problem.
Type: Array of strings
Pattern: `S-[0-9]{1,19}`
Required: No

## See Also
<a name="API_OpportunitySearchRelatedEntityIdentifiers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchRelatedEntityIdentifiers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchRelatedEntityIdentifiers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchRelatedEntityIdentifiers)
