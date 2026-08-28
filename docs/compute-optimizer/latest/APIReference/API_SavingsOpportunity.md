---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_SavingsOpportunity.html
---

# SavingsOpportunity
<a name="API_SavingsOpportunity"></a>

Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.

Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.

**Important**
Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide*.

## Contents
<a name="API_SavingsOpportunity_Contents"></a>

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-SavingsOpportunity-estimatedMonthlySavings"></a>
An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing..
Type: [EstimatedMonthlySavings](API_EstimatedMonthlySavings.md) object
Required: No

 ** savingsOpportunityPercentage **   <a name="computeoptimizer-Type-SavingsOpportunity-savingsOpportunityPercentage"></a>
The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a given resource.
Type: Double
Required: No

## See Also
<a name="API_SavingsOpportunity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/SavingsOpportunity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/SavingsOpportunity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/SavingsOpportunity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
