---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_PricingRuleListElement.html
---

# PricingRuleListElement
<a name="API_PricingRuleListElement"></a>

A representation of a pricing rule.

## Contents
<a name="API_PricingRuleListElement_Contents"></a>

 ** Arn **   <a name="billingconductor-Type-PricingRuleListElement-Arn"></a>
The Amazon Resource Name (ARN) used to uniquely identify a pricing rule.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`
Required: No

 ** AssociatedPricingPlanCount **   <a name="billingconductor-Type-PricingRuleListElement-AssociatedPricingPlanCount"></a>
The pricing plans count that this pricing rule is associated with.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** BillingEntity **   <a name="billingconductor-Type-PricingRuleListElement-BillingEntity"></a>
 The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplace.
Type: String
Pattern: `[a-zA-Z0-9() ]+`
Required: No

 ** CreationTime **   <a name="billingconductor-Type-PricingRuleListElement-CreationTime"></a>
The time when the pricing rule was created.
Type: Long
Required: No

 ** Description **   <a name="billingconductor-Type-PricingRuleListElement-Description"></a>
The pricing rule description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="billingconductor-Type-PricingRuleListElement-LastModifiedTime"></a>
 The most recent time when the pricing rule was modified.
Type: Long
Required: No

 ** ModifierPercentage **   <a name="billingconductor-Type-PricingRuleListElement-ModifierPercentage"></a>
A percentage modifier applied on the public pricing rates.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** Name **   <a name="billingconductor-Type-PricingRuleListElement-Name"></a>
The name of a pricing rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: No

 ** Operation **   <a name="billingconductor-Type-PricingRuleListElement-Operation"></a>
 Operation is the specific AWS action covered by this line item. This describes the specific usage of the line item.
 If the `Scope` attribute is set to `SKU`, this attribute indicates which operation the `PricingRule` is modifying. For example, a value of `RunInstances:0202` indicates the operation of running an Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

 ** Scope **   <a name="billingconductor-Type-PricingRuleListElement-Scope"></a>
The scope of pricing rule that indicates if it is globally applicable, or if it is service-specific.
Type: String
Valid Values: `GLOBAL | SERVICE | BILLING_ENTITY | SKU`
Required: No

 ** Service **   <a name="billingconductor-Type-PricingRuleListElement-Service"></a>
If the `Scope` attribute is `SERVICE`, this attribute indicates which service the `PricingRule` is applicable for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** Tiering **   <a name="billingconductor-Type-PricingRuleListElement-Tiering"></a>
 The set of tiering configurations for the pricing rule.
Type: [Tiering](API_Tiering.md) object
Required: No

 ** Type **   <a name="billingconductor-Type-PricingRuleListElement-Type"></a>
The type of pricing rule.
Type: String
Valid Values: `MARKUP | DISCOUNT | TIERING`
Required: No

 ** UsageType **   <a name="billingconductor-Type-PricingRuleListElement-UsageType"></a>
 Usage type is the unit that each service uses to measure the usage of a specific type of resource.
If the `Scope` attribute is set to `SKU`, this attribute indicates which usage type the `PricingRule` is modifying. For example, `USW2-BoxUsage:m2.2xlarge` describes an` M2 High Memory Double Extra Large` instance in the US West (Oregon) Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

## See Also
<a name="API_PricingRuleListElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/PricingRuleListElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/PricingRuleListElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/PricingRuleListElement)
