---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_MarketplaceRevenueShareProductDetail.html
---

# MarketplaceRevenueShareProductDetail

An AWS Marketplace product in a marketplace revenue share, as returned by GetMarketplaceRevenueShare, with its full typed AWS account lists.

## Contents
<a name="API_prm_MarketplaceRevenueShareProductDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ProductId **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareProductDetail-ProductId"></a>
The AWS Marketplace product identifier.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-zA-Z0-9][.a-zA-Z0-9/-]{1,254}[a-zA-Z0-9]`
Required: Yes

 ** Accounts **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareProductDetail-Accounts"></a>
The typed AWS account lists for the AWS Marketplace product, each with its count and full list of AWS account IDs.
Type: Array of [RevenueShareProductAccountDetail](API_prm_RevenueShareProductAccountDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

 ** ProductCode **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareProductDetail-ProductCode"></a>
The AWS Marketplace product code, resolved by the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9]+`
Required: No

 ** ProductName **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareProductDetail-ProductName"></a>
The display name of the AWS Marketplace product, resolved by the service.
Type: String
Required: No

## See Also
<a name="API_prm_MarketplaceRevenueShareProductDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareProductDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareProductDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareProductDetail)
