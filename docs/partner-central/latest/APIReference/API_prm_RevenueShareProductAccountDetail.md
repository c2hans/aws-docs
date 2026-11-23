---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_RevenueShareProductAccountDetail.html
---

# RevenueShareProductAccountDetail

A typed list of AWS accounts for an AWS Marketplace product, as returned by GetMarketplaceRevenueShare, with its count and full list of AWS account IDs.

## Contents
<a name="API_prm_RevenueShareProductAccountDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountIds **   <a name="AWSPartnerCentral-Type-prm_RevenueShareProductAccountDetail-AccountIds"></a>
The full list of AWS account IDs of this type.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** AccountType **   <a name="AWSPartnerCentral-Type-prm_RevenueShareProductAccountDetail-AccountType"></a>
The type of AWS account list.
Type: String
Valid Values: `DEPLOYMENT | ORGANIZATION`
Required: Yes

 ** Count **   <a name="AWSPartnerCentral-Type-prm_RevenueShareProductAccountDetail-Count"></a>
The number of AWS accounts of this type.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_prm_RevenueShareProductAccountDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/RevenueShareProductAccountDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/RevenueShareProductAccountDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/RevenueShareProductAccountDetail)
