---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AutoTransferBillingGroupCreationPreference.html
---

# AutoTransferBillingGroupCreationPreference
<a name="API_AutoTransferBillingGroupCreationPreference"></a>

 The auto billing group creation preference for a billing transfer. When the preference is enabled, AWS Billing Conductor automatically creates an indirect billing transfer billing group, with the specified pricing plan, for each account that transfers its bill to the bill source account of the billing transfer.

## Contents
<a name="API_AutoTransferBillingGroupCreationPreference_Contents"></a>

 ** Enabled **   <a name="billingconductor-Type-AutoTransferBillingGroupCreationPreference-Enabled"></a>
 Specifies whether AWS Billing Conductor automatically creates billing groups for the billing transfer. The preference is disabled by default.
Type: Boolean
Required: Yes

 ** PricingPlanArn **   <a name="billingconductor-Type-AutoTransferBillingGroupCreationPreference-PricingPlanArn"></a>
 The Amazon Resource Name (ARN) of the pricing plan to apply to the automatically created billing groups. This value is required when `Enabled` is `true`, and must be omitted when `Enabled` is `false`.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::(aws|[0-9]{12}):pricingplan/)?(BasicPricingPlan|Passthrough|[a-zA-Z0-9]{10})`
Required: No

## See Also
<a name="API_AutoTransferBillingGroupCreationPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/AutoTransferBillingGroupCreationPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/AutoTransferBillingGroupCreationPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/AutoTransferBillingGroupCreationPreference)
