---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansCoverageData.html
---

# SavingsPlansCoverageData
<a name="API_SavingsPlansCoverageData"></a>

Specific coverage percentage, On-Demand costs, and spend covered by Savings Plans, and total Savings Plans costs for an account.

## Contents
<a name="API_SavingsPlansCoverageData_Contents"></a>

 ** CoveragePercentage **   <a name="awscostmanagement-Type-SavingsPlansCoverageData-CoveragePercentage"></a>
The percentage of your existing Savings Plans covered usage, divided by all of your eligible Savings Plans usage in an account (or set of accounts).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** OnDemandCost **   <a name="awscostmanagement-Type-SavingsPlansCoverageData-OnDemandCost"></a>
The cost of your AWS usage at the public On-Demand rate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SpendCoveredBySavingsPlans **   <a name="awscostmanagement-Type-SavingsPlansCoverageData-SpendCoveredBySavingsPlans"></a>
The amount of your AWS usage that's covered by a Savings Plans.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** TotalCost **   <a name="awscostmanagement-Type-SavingsPlansCoverageData-TotalCost"></a>
The total cost of your AWS usage, regardless of your purchase option.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_SavingsPlansCoverageData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansCoverageData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansCoverageData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansCoverageData)
