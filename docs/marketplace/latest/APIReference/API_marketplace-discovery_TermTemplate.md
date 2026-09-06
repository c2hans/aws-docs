---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_TermTemplate.html
---

# TermTemplate
<a name="API_marketplace-discovery_TermTemplate"></a>

A structural template defining how a specific term type is reshaped on each renewal cycle. Exactly one variant is present.

## Contents
<a name="API_marketplace-discovery_TermTemplate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** paymentScheduleTermTemplate **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TermTemplate-paymentScheduleTermTemplate"></a>
The installment schedule used to structure payments on the renewal offer.
Type: [PaymentScheduleTermTemplate](API_marketplace-discovery_PaymentScheduleTermTemplate.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_TermTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/TermTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/TermTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/TermTemplate)
