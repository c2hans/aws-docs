---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_TermTemplate.html
---

# TermTemplate
<a name="API_marketplace-agreements_TermTemplate"></a>

Defines how a specific type of term changes each time the agreement renews. Exactly one of the following fields is set.

## Contents
<a name="API_marketplace-agreements_TermTemplate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** paymentScheduleTermTemplate **   <a name="AWSMarketplaceService-Type-marketplace-agreements_TermTemplate-paymentScheduleTermTemplate"></a>
Defines the payment schedule that is applied to the renewed agreement.
Type: [PaymentScheduleTermTemplate](API_marketplace-agreements_PaymentScheduleTermTemplate.md) object
Required: No

## See Also
<a name="API_marketplace-agreements_TermTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/TermTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/TermTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/TermTemplate)
