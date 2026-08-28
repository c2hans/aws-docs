---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansSavings.html
---

# SavingsPlansSavings
<a name="API_SavingsPlansSavings"></a>

The amount of savings that you're accumulating, against the public On-Demand rate of the usage accrued in an account.

## Contents
<a name="API_SavingsPlansSavings_Contents"></a>

 ** NetSavings **   <a name="awscostmanagement-Type-SavingsPlansSavings-NetSavings"></a>
The savings amount that you're accumulating for the usage that's covered by a Savings Plans, when compared to the On-Demand equivalent of the same usage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** OnDemandCostEquivalent **   <a name="awscostmanagement-Type-SavingsPlansSavings-OnDemandCostEquivalent"></a>
How much the amount that the usage would have cost if it was accrued at the On-Demand rate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_SavingsPlansSavings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansSavings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansSavings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansSavings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
