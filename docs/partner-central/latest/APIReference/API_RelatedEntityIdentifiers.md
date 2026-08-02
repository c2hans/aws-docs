---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_RelatedEntityIdentifiers.html
---

# RelatedEntityIdentifiers
<a name="API_RelatedEntityIdentifiers"></a>

This field provides the associations' information for other entities with the opportunity. These entities include identifiers for `AWSProducts`, `Partner Solutions`, and `AWSMarketplaceOffers`.

## Contents
<a name="API_RelatedEntityIdentifiers_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsMarketplaceOffers **   <a name="AWSPartnerCentral-Type-RelatedEntityIdentifiers-AwsMarketplaceOffers"></a>
Takes one value per opportunity. Each value is an Amazon Resource Name (ARN), in this format: `"offers": ["arn:aws:aws-marketplace:us-east-1:999999999999:AWSMarketplace/Offer/offer-sampleOffer32"]`.
Use the [ListEntities](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html) action in the Marketplace Catalog APIs for a list of offers in the associated Marketplace seller account.
Type: Array of strings
Pattern: `arn:aws:aws-marketplace:[a-z]{1,2}-[a-z]*-\d+:\d{12}:AWSMarketplace/Offer/.*`
Required: No

 ** AwsMarketplaceOfferSets **   <a name="AWSPartnerCentral-Type-RelatedEntityIdentifiers-AwsMarketplaceOfferSets"></a>
Enables the association of AWS Marketplace offer sets with the `Opportunity`. Offer sets allow grouping multiple related marketplace offers together for comprehensive solution packaging. Each value is an Amazon Resource Name (ARN) in this format: `arn:aws:aws-marketplace:us-east-1:999999999999:AWSMarketplace/OfferSet/offerset-sampleOfferSet32`.
Type: Array of strings
Pattern: `arn:aws:aws-marketplace:[a-z]{1,2}-[a-z]*-\d+:\d{12}:AWSMarketplace/OfferSet/offerset-.*`
Required: No

 ** AwsProducts **   <a name="AWSPartnerCentral-Type-RelatedEntityIdentifiers-AwsProducts"></a>
Enables the association of specific AWS products with the `Opportunity`. Partners can indicate the relevant AWS products for the `Opportunity`'s solution and align with the customer's needs. Returns multiple values separated by commas. For example, `"AWSProducts" : ["AmazonRedshift", "AWSAppFabric", "AWSCleanRooms"]`.
Use the file with the list of AWS products hosted on GitHub: [AWS products](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json).
Type: Array of strings
Required: No

 ** Solutions **   <a name="AWSPartnerCentral-Type-RelatedEntityIdentifiers-Solutions"></a>
Enables partner solutions or offerings' association with an opportunity. To associate a solution, provide the solution's unique identifier, which you can obtain with the `ListSolutions` operation.
If the specific solution identifier is not available, you can use the value `Other` and provide details about the solution in the `otherSolutionOffered` field. But when the opportunity reaches the `Committed` stage or beyond, the `Other` value cannot be used, and a valid solution identifier must be provided.
By associating the relevant solutions with the opportunity, you can communicate the offerings that are being considered or implemented to address the customer's business problem.
Type: Array of strings
Pattern: `S-[0-9]{1,19}`
Required: No

## See Also
<a name="API_RelatedEntityIdentifiers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/RelatedEntityIdentifiers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/RelatedEntityIdentifiers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/RelatedEntityIdentifiers)
