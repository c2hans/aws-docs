---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansCoverage.html
---

# SavingsPlansCoverage
<a name="API_SavingsPlansCoverage"></a>

The amount of Savings Plans eligible usage that's covered by Savings Plans. All calculations consider the On-Demand equivalent of your Savings Plans usage.

## Contents
<a name="API_SavingsPlansCoverage_Contents"></a>

 ** Attributes **   <a name="awscostmanagement-Type-SavingsPlansCoverage-Attributes"></a>
The attribute that applies to a specific `Dimension`.
Type: String to string map
Required: No

 ** Coverage **   <a name="awscostmanagement-Type-SavingsPlansCoverage-Coverage"></a>
The amount of Savings Plans eligible usage that the Savings Plans covered.
Type: [SavingsPlansCoverageData](API_SavingsPlansCoverageData.md) object
Required: No

 ** TimePeriod **   <a name="awscostmanagement-Type-SavingsPlansCoverage-TimePeriod"></a>
The time period of the request.
Type: [DateInterval](API_DateInterval.md) object
Required: No

## See Also
<a name="API_SavingsPlansCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansCoverage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
