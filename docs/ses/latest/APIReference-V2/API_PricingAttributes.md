---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PricingAttributes.html
---

# PricingAttributes
<a name="API_PricingAttributes"></a>

The pricing attributes that apply to your Amazon SES account, including the currently active pricing plan and any scheduled change.

## Contents
<a name="API_PricingAttributes_Contents"></a>

 ** CurrentPlan **   <a name="SES-Type-PricingAttributes-CurrentPlan"></a>
The pricing plan that is currently active on your Amazon SES account.
Type: String
Valid Values: `NONE | ESSENTIALS | PRO | ENTERPRISE`
Required: No

 ** NextPlan **   <a name="SES-Type-PricingAttributes-NextPlan"></a>
The pricing plan that will become active at the start of the next monthly cycle, if a scheduled change has been requested. This field is empty when no scheduled change is pending.
Type: String
Valid Values: `NONE | ESSENTIALS | PRO | ENTERPRISE`
Required: No

## See Also
<a name="API_PricingAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PricingAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PricingAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PricingAttributes)
