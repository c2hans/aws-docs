---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_TargetInstance.html
---

# TargetInstance
<a name="API_TargetInstance"></a>

Details on recommended instance.

## Contents
<a name="API_TargetInstance_Contents"></a>

 ** CurrencyCode **   <a name="awscostmanagement-Type-TargetInstance-CurrencyCode"></a>
The currency code that AWS used to calculate the costs for this instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** DefaultTargetInstance **   <a name="awscostmanagement-Type-TargetInstance-DefaultTargetInstance"></a>
Determines whether this recommendation is the defaulted AWS recommendation.
Type: Boolean
Required: No

 ** EstimatedMonthlyCost **   <a name="awscostmanagement-Type-TargetInstance-EstimatedMonthlyCost"></a>
The expected cost to operate this instance type on a monthly basis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedMonthlySavings **   <a name="awscostmanagement-Type-TargetInstance-EstimatedMonthlySavings"></a>
The estimated savings that result from modification, on a monthly basis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ExpectedResourceUtilization **   <a name="awscostmanagement-Type-TargetInstance-ExpectedResourceUtilization"></a>
The expected utilization metrics for target instance type.
Type: [ResourceUtilization](API_ResourceUtilization.md) object
Required: No

 ** PlatformDifferences **   <a name="awscostmanagement-Type-TargetInstance-PlatformDifferences"></a>
Explains the actions that you might need to take to successfully migrate your workloads from the current instance type to the recommended instance type.
Type: Array of strings
Valid Values: `HYPERVISOR | NETWORK_INTERFACE | STORAGE_INTERFACE | INSTANCE_STORE_AVAILABILITY | VIRTUALIZATION_TYPE`
Required: No

 ** ResourceDetails **   <a name="awscostmanagement-Type-TargetInstance-ResourceDetails"></a>
Details on the target instance type.
Type: [ResourceDetails](API_ResourceDetails.md) object
Required: No

## See Also
<a name="API_TargetInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/TargetInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/TargetInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/TargetInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
