---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_SoftwareRevenue.html
---

# SoftwareRevenue
<a name="API_SoftwareRevenue"></a>

Specifies a customer's procurement terms details. Required only for partners in eligible programs.

## Contents
<a name="API_SoftwareRevenue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DeliveryModel **   <a name="AWSPartnerCentral-Type-SoftwareRevenue-DeliveryModel"></a>
Specifies the customer's intended payment type agreement or procurement method to acquire the solution or service outlined in the `Opportunity`.
Type: String
Valid Values: `Contract | Pay-as-you-go | Subscription`
Required: No

 ** EffectiveDate **   <a name="AWSPartnerCentral-Type-SoftwareRevenue-EffectiveDate"></a>
Specifies the `Opportunity`'s customer engagement start date for the contract's effectiveness.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: No

 ** ExpirationDate **   <a name="AWSPartnerCentral-Type-SoftwareRevenue-ExpirationDate"></a>
Specifies the expiration date for the contract between the customer and AWS partner. It signifies the termination date of the agreed-upon engagement period between both parties.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: No

 ** Value **   <a name="AWSPartnerCentral-Type-SoftwareRevenue-Value"></a>
Specifies the payment value (amount and currency).
Type: [MonetaryValue](API_MonetaryValue.md) object
Required: No

## See Also
<a name="API_SoftwareRevenue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/SoftwareRevenue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/SoftwareRevenue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/SoftwareRevenue)
