---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansAmortizedCommitment.html
---

# SavingsPlansAmortizedCommitment
<a name="API_SavingsPlansAmortizedCommitment"></a>

The amortized amount of Savings Plans purchased in a specific account during a specific time interval.

## Contents
<a name="API_SavingsPlansAmortizedCommitment_Contents"></a>

 ** AmortizedRecurringCommitment **   <a name="awscostmanagement-Type-SavingsPlansAmortizedCommitment-AmortizedRecurringCommitment"></a>
The amortized amount of your Savings Plans commitment that was purchased with either a `Partial` or a `NoUpfront`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** AmortizedUpfrontCommitment **   <a name="awscostmanagement-Type-SavingsPlansAmortizedCommitment-AmortizedUpfrontCommitment"></a>
The amortized amount of your Savings Plans commitment that was purchased with an `Upfront` or `PartialUpfront` Savings Plans.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** TotalAmortizedCommitment **   <a name="awscostmanagement-Type-SavingsPlansAmortizedCommitment-TotalAmortizedCommitment"></a>
The total amortized amount of your Savings Plans commitment, regardless of your Savings Plans purchase method.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_SavingsPlansAmortizedCommitment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansAmortizedCommitment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansAmortizedCommitment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansAmortizedCommitment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
