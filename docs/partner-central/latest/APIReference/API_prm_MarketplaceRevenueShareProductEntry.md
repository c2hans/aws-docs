---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_MarketplaceRevenueShareProductEntry.html
---

# MarketplaceRevenueShareProductEntry

An AWS Marketplace product and, optionally, its typed AWS account lists, as specified in a CreateMarketplaceRevenueShare or UpdateMarketplaceRevenueShare request.

## Contents
<a name="API_prm_MarketplaceRevenueShareProductEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ProductId **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareProductEntry-ProductId"></a>
The AWS Marketplace product ID or product ARN. The marketplace revenue share stores and returns the product ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-:/.]+`
Required: Yes

 ** Accounts **   <a name="AWSPartnerCentral-Type-prm_MarketplaceRevenueShareProductEntry-Accounts"></a>
The typed AWS account lists for the AWS Marketplace product, such as its AWS deployed accounts. Optional. If omitted, the service determines the AWS accounts. Specify at most one entry per AWS account type, and include at least one AWS account in each entry. An empty list is treated the same as omitting the field.
Type: Array of [RevenueShareProductAccountEntry](API_prm_RevenueShareProductAccountEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

## See Also
<a name="API_prm_MarketplaceRevenueShareProductEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareProductEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareProductEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/MarketplaceRevenueShareProductEntry)
