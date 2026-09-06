---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_PricingPlanListElement.html
---

# PricingPlanListElement
<a name="API_PricingPlanListElement"></a>

A representation of a pricing plan.

## Contents
<a name="API_PricingPlanListElement_Contents"></a>

 ** Arn **   <a name="billingconductor-Type-PricingPlanListElement-Arn"></a>
The pricing plan Amazon Resource Names (ARN). This can be used to uniquely identify a pricing plan.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::(aws|[0-9]{12}):pricingplan/)?(BasicPricingPlan|Passthrough|[a-zA-Z0-9]{10})`
Required: No

 ** CreationTime **   <a name="billingconductor-Type-PricingPlanListElement-CreationTime"></a>
The time when the pricing plan was created.
Type: Long
Required: No

 ** Description **   <a name="billingconductor-Type-PricingPlanListElement-Description"></a>
The pricing plan description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="billingconductor-Type-PricingPlanListElement-LastModifiedTime"></a>
The most recent time when the pricing plan was modified.
Type: Long
Required: No

 ** Name **   <a name="billingconductor-Type-PricingPlanListElement-Name"></a>
The name of a pricing plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: No

 ** Size **   <a name="billingconductor-Type-PricingPlanListElement-Size"></a>
The pricing rules count that's currently associated with this pricing plan list element.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_PricingPlanListElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/PricingPlanListElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/PricingPlanListElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/PricingPlanListElement)
