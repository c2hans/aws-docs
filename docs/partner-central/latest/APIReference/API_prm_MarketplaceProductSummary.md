---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_MarketplaceProductSummary.html
---

# MarketplaceProductSummary
<a name="API_prm_MarketplaceProductSummary"></a>

Read-time AWS Marketplace product attributes returned in revenue attribution responses, including service-resolved fields.

## Contents
<a name="API_prm_MarketplaceProductSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ProductCode **   <a name="AWSPartnerCentral-Type-prm_MarketplaceProductSummary-ProductCode"></a>
The AWS Marketplace product code resolved using the product identifier.
Type: String
Required: No

 ** ProductId **   <a name="AWSPartnerCentral-Type-prm_MarketplaceProductSummary-ProductId"></a>
The product identifier provided at attribution creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-:/.]+`
Required: No

 ** ProductName **   <a name="AWSPartnerCentral-Type-prm_MarketplaceProductSummary-ProductName"></a>
The display name of the AWS Marketplace product.
Type: String
Required: No

## See Also
<a name="API_prm_MarketplaceProductSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/MarketplaceProductSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/MarketplaceProductSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/MarketplaceProductSummary)
