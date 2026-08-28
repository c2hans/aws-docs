---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseAnalysisConfiguration.html
---

# SavingsPlansPurchaseAnalysisConfiguration
<a name="API_SavingsPlansPurchaseAnalysisConfiguration"></a>

The configuration for the Savings Plans purchase analysis.

## Contents
<a name="API_SavingsPlansPurchaseAnalysisConfiguration_Contents"></a>

 ** AnalysisType **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisConfiguration-AnalysisType"></a>
The type of analysis.
Type: String
Valid Values: `MAX_SAVINGS | CUSTOM_COMMITMENT | TARGET_AVERAGE_COVERAGE`
Required: Yes

 ** LookBackTimePeriod **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisConfiguration-LookBackTimePeriod"></a>
The time period associated with the analysis.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

 ** SavingsPlansToAdd **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisConfiguration-SavingsPlansToAdd"></a>
Savings Plans to include in the analysis.
Type: Array of [SavingsPlans](API_SavingsPlans.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** AccountId **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisConfiguration-AccountId"></a>
The account that the analysis is for.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** AccountScope **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisConfiguration-AccountScope"></a>
The account scope that you want your analysis for.
Type: String
Valid Values: `PAYER | LINKED`
Required: No

 ** SavingsPlansTargetCoverage **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisConfiguration-SavingsPlansTargetCoverage"></a>
Specifies the target Savings Plans coverage as a percentage from `10` to `100`. This field is required when `AnalysisType` is `TARGET_AVERAGE_COVERAGE`. It defines the target average hourly coverage that the recommended Savings Plans commitment should achieve over the lookback period.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** SavingsPlansToExclude **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisConfiguration-SavingsPlansToExclude"></a>
Savings Plans to exclude from the analysis.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
Required: No

## See Also
<a name="API_SavingsPlansPurchaseAnalysisConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansPurchaseAnalysisConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansPurchaseAnalysisConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansPurchaseAnalysisConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
