---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_MarketplaceRevenueShareAllocationSummary.html
---

# MarketplaceRevenueShareAllocationSummary

Summary information about a marketplace revenue share allocation.

## Contents
<a name="API_prm_MarketplaceRevenueShareAllocationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedDate **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-CreatedDate"></a>
The date when the allocation was created.
Type: Timestamp
Required: Yes

 ** EffectiveFrom **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-EffectiveFrom"></a>
The effective start date of the allocation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** EffectiveUntil **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-EffectiveUntil"></a>
The effective end date of the marketplace revenue share allocation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** LastModifiedDate **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-LastModifiedDate"></a>
The date when the allocation was last modified.
Type: Timestamp
Required: Yes

 ** MarketplaceRevenueShareAllocationId **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-MarketplaceRevenueShareAllocationId"></a>
The unique identifier of the allocation.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `mrsa-[a-z0-9]{13}`
Required: Yes

 ** MarketplaceRevenueShareIdentifier **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-MarketplaceRevenueShareIdentifier"></a>
The identifier of the parent marketplace revenue share, in short ID form (for example, mrs-0a1b2c3d4e5f6).
Type: String
Length Constraints: Fixed length of 17.
Pattern: `mrs-[a-z0-9]{13}`
Required: Yes

 ** RevenueSharePercent **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-RevenueSharePercent"></a>
The revenue share percentage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `\d{1,3}(\.\d{1,2})?`
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-Status"></a>
The status of the allocation.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

## See Also
<a name="API_prm_MarketplaceRevenueShareAllocationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareAllocationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareAllocationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareAllocationSummary)
