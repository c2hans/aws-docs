---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html
---

# Expression
<a name="API_billing_Expression"></a>

 See [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html). Billing view only supports `LINKED_ACCOUNT`, `Tags`, and `CostCategories`.

## Contents
<a name="API_billing_Expression_Contents"></a>

 ** costCategories **   <a name="awscostmanagement-Type-billing_Expression-costCategories"></a>
 The filter that's based on `CostCategory` values.
Type: [CostCategoryValues](API_billing_CostCategoryValues.md) object
Required: No

 ** dimensions **   <a name="awscostmanagement-Type-billing_Expression-dimensions"></a>
 The specific `Dimension` to use for `Expression`.
Type: [DimensionValues](API_billing_DimensionValues.md) object
Required: No

 ** tags **   <a name="awscostmanagement-Type-billing_Expression-tags"></a>
 The specific `Tag` to use for `Expression`.
Type: [TagValues](API_billing_TagValues.md) object
Required: No

 ** timeRange **   <a name="awscostmanagement-Type-billing_Expression-timeRange"></a>
 Specifies a time range filter for the billing view data.
Type: [TimeRange](API_billing_TimeRange.md) object
Required: No

## See Also
<a name="API_billing_Expression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/Expression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/Expression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/Expression)
