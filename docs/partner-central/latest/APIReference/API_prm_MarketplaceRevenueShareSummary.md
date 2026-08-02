---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_MarketplaceRevenueShareSummary.html
---

# MarketplaceRevenueShareSummary
<a name="API_prm_MarketplaceRevenueShareSummary"></a>

Summary information about a marketplace revenue share.

## Contents
<a name="API_prm_MarketplaceRevenueShareSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-Arn"></a>
The Amazon Resource Name (ARN) of the marketplace revenue share.
Type: String
Required: Yes

 ** ProductId **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-ProductId"></a>
The AWS Marketplace product identifier.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`
Required: Yes

 ** Catalog **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-Catalog"></a>
The catalog that the marketplace revenue share belongs to.
Type: String
Valid Values: `AWS | Sandbox`
Required: No

 ** CreatedDate **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-CreatedDate"></a>
The date when the marketplace revenue share was created.
Type: Timestamp
Required: No

 ** LastModifiedDate **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-LastModifiedDate"></a>
The date when the marketplace revenue share was last modified.
Type: Timestamp
Required: No

 ** LatestRevision **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-LatestRevision"></a>
The latest revision number of the marketplace revenue share.
Type: Integer
Required: No

 ** ProductCode **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-ProductCode"></a>
The AWS Marketplace product code.
Type: String
Required: No

 ** ProductName **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-ProductName"></a>
The display name of the AWS Marketplace product.
Type: String
Required: No

 ** TotalActiveMarketplaceRevenueShareAllocationCount **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-TotalActiveMarketplaceRevenueShareAllocationCount"></a>
The number of active allocations under this share.
Type: Integer
Required: No

 ** TotalMarketplaceRevenueShareAllocationCount **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareSummary-TotalMarketplaceRevenueShareAllocationCount"></a>
The total number of allocations under this share.
Type: Integer
Required: No

## See Also
<a name="API_prm_MarketplaceRevenueShareSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareSummary)
