---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_EstimatedMonthlySavings.html
---

# EstimatedMonthlySavings
<a name="API_automation_EstimatedMonthlySavings"></a>

 Contains information about estimated monthly cost savings.

## Contents
<a name="API_automation_EstimatedMonthlySavings_Contents"></a>

 ** afterDiscountSavings **   <a name="computeoptimizer-Type-automation_EstimatedMonthlySavings-afterDiscountSavings"></a>
 The estimated monthly savings after applying any discounts.
Type: Double
Required: Yes

 ** beforeDiscountSavings **   <a name="computeoptimizer-Type-automation_EstimatedMonthlySavings-beforeDiscountSavings"></a>
 The estimated monthly savings before applying any discounts.
Type: Double
Required: Yes

 ** currency **   <a name="computeoptimizer-Type-automation_EstimatedMonthlySavings-currency"></a>
 The currency of the estimated savings.
Type: String
Required: Yes

 ** savingsEstimationMode **   <a name="computeoptimizer-Type-automation_EstimatedMonthlySavings-savingsEstimationMode"></a>
The mode used to calculate savings, either BeforeDiscount or AfterDiscount.
Type: String
Valid Values: `BeforeDiscount | AfterDiscount`
Required: Yes

## See Also
<a name="API_automation_EstimatedMonthlySavings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/EstimatedMonthlySavings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/EstimatedMonthlySavings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/EstimatedMonthlySavings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
