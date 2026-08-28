---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillEstimatesFilter.html
---

# ListBillEstimatesFilter
<a name="API_AWSBCMPricingCalculator_ListBillEstimatesFilter"></a>

 Represents a filter for listing bill estimates.

## Contents
<a name="API_AWSBCMPricingCalculator_ListBillEstimatesFilter_Contents"></a>

 ** name **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_ListBillEstimatesFilter-name"></a>
 The name of the filter attribute.
Type: String
Valid Values: `STATUS | NAME`
Required: Yes

 ** values **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_ListBillEstimatesFilter-values"></a>
 The values to filter by.
Type: Array of strings
Required: Yes

 ** matchOption **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_ListBillEstimatesFilter-matchOption"></a>
 The match option for the filter (e.g., equals, contains).
Type: String
Valid Values: `EQUALS | STARTS_WITH | CONTAINS`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_ListBillEstimatesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/ListBillEstimatesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/ListBillEstimatesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/ListBillEstimatesFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
