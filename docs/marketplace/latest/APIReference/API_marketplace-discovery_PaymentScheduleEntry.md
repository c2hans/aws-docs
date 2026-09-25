---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PaymentScheduleEntry.html
---

# PaymentScheduleEntry
<a name="API_marketplace-discovery_PaymentScheduleEntry"></a>

A single installment entry in the renewal payment schedule.

## Contents
<a name="API_marketplace-discovery_PaymentScheduleEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** chargeDateOffset **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PaymentScheduleEntry-chargeDateOffset"></a>
The relative offset from the renewal agreement start date when this installment is due, represented in ISO 8601 duration format (for example, P1M or P30D).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** chargePercentage **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PaymentScheduleEntry-chargePercentage"></a>
The percentage of the increased Total Contract Value (TCV) to charge in this installment. All entries in a schedule sum to 100.00.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** dayOfMonth **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PaymentScheduleEntry-dayOfMonth"></a>
The optional calendar day of month on which the charge occurs. When absent, the charge day is derived from `chargeDateOffset`. For months with fewer days than the specified day, the charge occurs on the last day of the month. For example, if `dayOfMonth` is 31, the charge in April occurs on April 30.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 31.
Required: No

## See Also
<a name="API_marketplace-discovery_PaymentScheduleEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PaymentScheduleEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PaymentScheduleEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PaymentScheduleEntry)
