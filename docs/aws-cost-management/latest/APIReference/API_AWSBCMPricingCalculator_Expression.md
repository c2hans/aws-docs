---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_Expression.html
---

# Expression
<a name="API_AWSBCMPricingCalculator_Expression"></a>

 Represents a complex filtering expression for cost and usage data.

## Contents
<a name="API_AWSBCMPricingCalculator_Expression_Contents"></a>

 ** and **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_Expression-and"></a>
 A list of expressions to be combined with AND logic.
Type: Array of [Expression](#API_AWSBCMPricingCalculator_Expression) objects
Required: No

 ** costCategories **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_Expression-costCategories"></a>
 Filters based on cost categories.
Type: [ExpressionFilter](API_AWSBCMPricingCalculator_ExpressionFilter.md) object
Required: No

 ** dimensions **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_Expression-dimensions"></a>
 Filters based on dimensions (e.g., service, operation).
Type: [ExpressionFilter](API_AWSBCMPricingCalculator_ExpressionFilter.md) object
Required: No

 ** not **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_Expression-not"></a>
 An expression to be negated.
Type: [Expression](#API_AWSBCMPricingCalculator_Expression) object
Required: No

 ** or **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_Expression-or"></a>
 A list of expressions to be combined with OR logic.
Type: Array of [Expression](#API_AWSBCMPricingCalculator_Expression) objects
Required: No

 ** tags **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_Expression-tags"></a>
 Filters based on resource tags.
Type: [ExpressionFilter](API_AWSBCMPricingCalculator_ExpressionFilter.md) object
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_Expression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/Expression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/Expression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/Expression)
