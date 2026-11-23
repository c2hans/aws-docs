---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsSoftwareRevenue.html
---

# AwsSoftwareRevenue

Seller-provided PARC deal terms for the opportunity, including commitment value, discount percentage, and contract dates.

## Contents
<a name="API_AwsSoftwareRevenue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Discount **   <a name="AWSPartnerCentral-Type-AwsSoftwareRevenue-Discount"></a>
Discount percentage offered on the software revenue. Percent convention: 15.00 means 15%.
Type: String
Required: No

 ** EffectiveDate **   <a name="AWSPartnerCentral-Type-AwsSoftwareRevenue-EffectiveDate"></a>
Contract effective (start) date in YYYY-MM-DD format.
Type: String
Required: No

 ** ExpirationDate **   <a name="AWSPartnerCentral-Type-AwsSoftwareRevenue-ExpirationDate"></a>
Contract expiration (end) date in YYYY-MM-DD format.
Type: String
Required: No

 ** Value **   <a name="AWSPartnerCentral-Type-AwsSoftwareRevenue-Value"></a>
The committed value and currency for the procurement terms.
Type: [MonetaryValue](API_MonetaryValue.md) object
Required: No

## See Also
<a name="API_AwsSoftwareRevenue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsSoftwareRevenue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsSoftwareRevenue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsSoftwareRevenue)
