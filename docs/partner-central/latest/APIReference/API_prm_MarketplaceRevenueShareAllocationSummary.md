---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_MarketplaceRevenueShareAllocationSummary.html
---

# MarketplaceRevenueShareAllocationSummary
<a name="API_prm_MarketplaceRevenueShareAllocationSummary"></a>

Summary information about a marketplace revenue share allocation.

## Contents
<a name="API_prm_MarketplaceRevenueShareAllocationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the parent marketplace revenue share.
Type: String
Required: Yes

 ** EffectiveFrom **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-EffectiveFrom"></a>
The effective start date of the allocation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** MarketplaceRevenueShareAllocationId **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-MarketplaceRevenueShareAllocationId"></a>
The unique identifier of the allocation.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `mrsa-[A-Za-z0-9]{13}`
Required: Yes

 ** ProductId **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-ProductId"></a>
The AWS Marketplace product identifier.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`
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

 ** CreatedDate **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-CreatedDate"></a>
The date when the allocation was created.
Type: Timestamp
Required: No

 ** EffectiveUntil **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-EffectiveUntil"></a>
The effective end date of the allocation, or null if open-ended.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** LastModifiedDate **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-LastModifiedDate"></a>
The date when the allocation was last modified.
Type: Timestamp
Required: No

 ** ProductName **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareAllocationSummary-ProductName"></a>
The display name of the AWS Marketplace product.
Type: String
Required: No

## See Also
<a name="API_prm_MarketplaceRevenueShareAllocationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareAllocationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareAllocationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareAllocationSummary)
