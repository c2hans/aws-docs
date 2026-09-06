---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ScheduleItem.html
---

# ScheduleItem
<a name="API_marketplace-discovery_ScheduleItem"></a>

A payment installment within a payment schedule term.

## Contents
<a name="API_marketplace-discovery_ScheduleItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** chargeAmount **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ScheduleItem-chargeAmount"></a>
The amount to be charged on the charge date.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** chargeDate **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ScheduleItem-chargeDate"></a>
The date when the payment is due.
Type: Timestamp
Required: Yes

## See Also
<a name="API_marketplace-discovery_ScheduleItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ScheduleItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ScheduleItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ScheduleItem)
