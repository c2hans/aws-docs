---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_PaymentScheduleTermTemplate.html
---

# PaymentScheduleTermTemplate
<a name="API_marketplace-agreements_PaymentScheduleTermTemplate"></a>

Defines the payment schedule that is applied to the renewed agreement.

## Contents
<a name="API_marketplace-agreements_PaymentScheduleTermTemplate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** schedule **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentScheduleTermTemplate-schedule"></a>
The installments that make up the payment schedule of the renewed agreement. The `ChargePercentage` values of all installments add up to `100`.
Type: Array of [PaymentScheduleEntry](API_marketplace-agreements_PaymentScheduleEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## See Also
<a name="API_marketplace-agreements_PaymentScheduleTermTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/PaymentScheduleTermTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/PaymentScheduleTermTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/PaymentScheduleTermTemplate)
