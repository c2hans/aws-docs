---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_RevenueShareProductAccountEntry.html
---

# RevenueShareProductAccountEntry

A typed list of AWS accounts for an AWS Marketplace product, as specified in a CreateMarketplaceRevenueShare or UpdateMarketplaceRevenueShare request.

## Contents
<a name="API_prm_RevenueShareProductAccountEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountIds **   <a name="AWSPartnerCentral-Type-prm_RevenueShareProductAccountEntry-AccountIds"></a>
The AWS account IDs of this type. Each ID must be a 12-digit AWS account ID. AWS account ownership is verified after the request is accepted.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** AccountType **   <a name="AWSPartnerCentral-Type-prm_RevenueShareProductAccountEntry-AccountType"></a>
The type of AWS account list.
Type: String
Valid Values: `DEPLOYMENT | ORGANIZATION`
Required: Yes

## See Also
<a name="API_prm_RevenueShareProductAccountEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/RevenueShareProductAccountEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/RevenueShareProductAccountEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/RevenueShareProductAccountEntry)
