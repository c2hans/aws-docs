---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansUtilization.html
---

# SavingsPlansUtilization
<a name="API_SavingsPlansUtilization"></a>

The measurement of how well you're using your existing Savings Plans.

## Contents
<a name="API_SavingsPlansUtilization_Contents"></a>

 ** TotalCommitment **   <a name="awscostmanagement-Type-SavingsPlansUtilization-TotalCommitment"></a>
The total amount of Savings Plans commitment that's been purchased in an account (or set of accounts).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** UnusedCommitment **   <a name="awscostmanagement-Type-SavingsPlansUtilization-UnusedCommitment"></a>
The amount of your Savings Plans commitment that wasn't consumed from Savings Plans eligible usage in a specific period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** UsedCommitment **   <a name="awscostmanagement-Type-SavingsPlansUtilization-UsedCommitment"></a>
The amount of your Savings Plans commitment that was consumed from Savings Plans eligible usage in a specific period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** UtilizationPercentage **   <a name="awscostmanagement-Type-SavingsPlansUtilization-UtilizationPercentage"></a>
The amount of `UsedCommitment` divided by the `TotalCommitment` for your Savings Plans.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_SavingsPlansUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansUtilization)
