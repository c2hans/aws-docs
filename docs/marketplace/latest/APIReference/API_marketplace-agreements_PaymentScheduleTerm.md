---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_PaymentScheduleTerm.html
---

# PaymentScheduleTerm
<a name="API_marketplace-agreements_PaymentScheduleTerm"></a>

Defines an installment-based pricing model where customers are charged a fixed price on different dates during the agreement validity period. This is used most commonly for flexible payment schedule pricing.

## Contents
<a name="API_marketplace-agreements_PaymentScheduleTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentScheduleTerm-currencyCode"></a>
Defines the currency for the prices mentioned in the term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentScheduleTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** schedule **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentScheduleTerm-schedule"></a>
List of the payment schedule where each element defines one installment of payment. It contains the information necessary for calculating the price.
Type: Array of [ScheduleItem](API_marketplace-agreements_ScheduleItem.md) objects
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentScheduleTerm-type"></a>
Type of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_PaymentScheduleTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/PaymentScheduleTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/PaymentScheduleTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/PaymentScheduleTerm)
