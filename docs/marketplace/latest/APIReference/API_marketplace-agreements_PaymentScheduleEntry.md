---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_PaymentScheduleEntry.html
---

# PaymentScheduleEntry
<a name="API_marketplace-agreements_PaymentScheduleEntry"></a>

A single installment in a payment schedule template. Because the start date of the renewed agreement isn't known when the offer is created, the charge date of each installment is expressed as an offset from that start date rather than as an absolute date.

## Contents
<a name="API_marketplace-agreements_PaymentScheduleEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** chargeDateOffset **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentScheduleEntry-chargeDateOffset"></a>
The time between the start date of the renewed agreement and the date this installment is charged. The duration is represented in the ISO 8601 format in either whole months or whole days (for example, `P1M` for 1 month or `P30D` for 30 days). All installments in a schedule use the same unit.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 6.
Pattern: `P(\d{1,4}M|\d{1,4}D)`
Required: No

 ** chargePercentage **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentScheduleEntry-chargePercentage"></a>
The percentage of the total contract value of the renewed agreement that is charged in this installment. Valid values range from `0.01` to `100.00`, with up to two decimal places.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `(100(\.0{1,2})?|[1-9]\d?(\.\d{1,2})?|0\.(0[1-9]|[1-9]\d?))`
Required: No

 ** dayOfMonth **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PaymentScheduleEntry-dayOfMonth"></a>
The day of the month on which this installment is charged, from `1` to `31`. Use this field to anchor the charge to a specific calendar day within the month identified by `ChargeDateOffset`. This field is supported only when `ChargeDateOffset` is expressed in months.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 31.
Required: No

## See Also
<a name="API_marketplace-agreements_PaymentScheduleEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/PaymentScheduleEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/PaymentScheduleEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/PaymentScheduleEntry)
