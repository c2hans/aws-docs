---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_CreditDetails.html
---

# CreditDetails
<a name="API_benefits_CreditDetails"></a>

Contains information about credit-based benefit fulfillment, including AWS promotional credits.

## Contents
<a name="API_benefits_CreditDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllocatedAmount **   <a name="AWSPartnerCentral-Type-benefits_CreditDetails-AllocatedAmount"></a>
The total amount of credits that have been allocated for this benefit.
Type: [MonetaryValue](API_benefits_MonetaryValue.md) object
Required: Yes

 ** Codes **   <a name="AWSPartnerCentral-Type-benefits_CreditDetails-Codes"></a>
A list of credit codes that have been generated for this benefit allocation.
Type: Array of [CreditCode](API_benefits_CreditCode.md) objects
Required: Yes

 ** IssuedAmount **   <a name="AWSPartnerCentral-Type-benefits_CreditDetails-IssuedAmount"></a>
The amount of credits that have actually been issued and are available for use.
Type: [MonetaryValue](API_benefits_MonetaryValue.md) object
Required: Yes

## See Also
<a name="API_benefits_CreditDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/CreditDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/CreditDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/CreditDetails)
