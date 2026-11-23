---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_MarketplaceRevenueShareSummary.html
---

# MarketplaceRevenueShareSummary

Summary information about a marketplace revenue share.

## Contents
<a name="API_prm_MarketplaceRevenueShareSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-Arn"></a>
The Amazon Resource Name (ARN) of the marketplace revenue share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/marketplace-revenue-share/mrs-[a-z0-9]{13}`
Required: Yes

 ** Catalog **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-Catalog"></a>
The catalog that the marketplace revenue share belongs to.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** CreatedDate **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-CreatedDate"></a>
The date when the marketplace revenue share was created.
Type: Timestamp
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-Id"></a>
The unique identifier of the marketplace revenue share, in short ID form (for example, mrs-0a1b2c3d4e5f6).
Type: String
Length Constraints: Fixed length of 17.
Pattern: `mrs-[a-z0-9]{13}`
Required: Yes

 ** LastModifiedDate **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-LastModifiedDate"></a>
The date when the marketplace revenue share was last modified.
Type: Timestamp
Required: Yes

 ** LatestRevision **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-LatestRevision"></a>
The latest revision of the marketplace revenue share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: Yes

 ** Products **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-Products"></a>
The AWS Marketplace products in the marketplace revenue share, each with per-type AWS account counts. Empty when the marketplace revenue share is closed.
Type: Array of [MarketplaceRevenueShareProductSummary](API_prm_MarketplaceRevenueShareProductSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: Yes

 ** TotalActiveMarketplaceRevenueShareAllocationCount **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-TotalActiveMarketplaceRevenueShareAllocationCount"></a>
The number of active allocations under this share.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** TotalMarketplaceRevenueShareAllocationCount **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-TotalMarketplaceRevenueShareAllocationCount"></a>
The total number of allocations under this share.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** EffectiveFrom **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-EffectiveFrom"></a>
The date from which the marketplace revenue share is effective, derived from the earliest start date among its ACTIVE marketplace revenue share allocations (YYYY-MM-DD). Not returned when the marketplace revenue share has no ACTIVE marketplace revenue share allocations.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** EffectiveUntil **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-EffectiveUntil"></a>
The date until which the marketplace revenue share is effective, derived from the latest end date among its ACTIVE marketplace revenue share allocations (YYYY-MM-DD). Not returned when the marketplace revenue share has no ACTIVE marketplace revenue share allocations.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

## See Also
<a name="API_prm_MarketplaceRevenueShareSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareSummary)
