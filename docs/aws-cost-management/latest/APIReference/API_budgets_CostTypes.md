---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CostTypes.html
---

# CostTypes
<a name="API_budgets_CostTypes"></a>

The types of cost that are included in a `COST` budget, such as tax and subscriptions.

 `USAGE`, `RI_UTILIZATION`, `RI_COVERAGE`, `SAVINGS_PLANS_UTILIZATION`, and `SAVINGS_PLANS_COVERAGE` budgets don't have `CostTypes`.

## Contents
<a name="API_budgets_CostTypes_Contents"></a>

 ** IncludeCredit **   <a name="awscostmanagement-Type-budgets_CostTypes-IncludeCredit"></a>
Specifies whether a budget includes credits.
The default value is `true`.
Type: Boolean
Required: No

 ** IncludeDiscount **   <a name="awscostmanagement-Type-budgets_CostTypes-IncludeDiscount"></a>
Specifies whether a budget includes discounts.
The default value is `true`.
Type: Boolean
Required: No

 ** IncludeOtherSubscription **   <a name="awscostmanagement-Type-budgets_CostTypes-IncludeOtherSubscription"></a>
Specifies whether a budget includes non-RI subscription costs.
The default value is `true`.
Type: Boolean
Required: No

 ** IncludeRecurring **   <a name="awscostmanagement-Type-budgets_CostTypes-IncludeRecurring"></a>
Specifies whether a budget includes recurring fees such as monthly RI fees.
The default value is `true`.
Type: Boolean
Required: No

 ** IncludeRefund **   <a name="awscostmanagement-Type-budgets_CostTypes-IncludeRefund"></a>
Specifies whether a budget includes refunds.
The default value is `true`.
Type: Boolean
Required: No

 ** IncludeSubscription **   <a name="awscostmanagement-Type-budgets_CostTypes-IncludeSubscription"></a>
Specifies whether a budget includes subscriptions.
The default value is `true`.
Type: Boolean
Required: No

 ** IncludeSupport **   <a name="awscostmanagement-Type-budgets_CostTypes-IncludeSupport"></a>
Specifies whether a budget includes support subscription fees.
The default value is `true`.
Type: Boolean
Required: No

 ** IncludeTax **   <a name="awscostmanagement-Type-budgets_CostTypes-IncludeTax"></a>
Specifies whether a budget includes taxes.
The default value is `true`.
Type: Boolean
Required: No

 ** IncludeUpfront **   <a name="awscostmanagement-Type-budgets_CostTypes-IncludeUpfront"></a>
Specifies whether a budget includes upfront RI costs.
The default value is `true`.
Type: Boolean
Required: No

 ** UseAmortized **   <a name="awscostmanagement-Type-budgets_CostTypes-UseAmortized"></a>
Specifies whether a budget uses the amortized rate.
The default value is `false`.
Type: Boolean
Required: No

 ** UseBlended **   <a name="awscostmanagement-Type-budgets_CostTypes-UseBlended"></a>
Specifies whether a budget uses a blended rate.
The default value is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_budgets_CostTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/CostTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/CostTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/CostTypes)
