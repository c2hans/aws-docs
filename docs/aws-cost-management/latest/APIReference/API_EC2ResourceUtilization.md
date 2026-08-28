---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_EC2ResourceUtilization.html
---

# EC2ResourceUtilization
<a name="API_EC2ResourceUtilization"></a>

Utilization metrics for the instance.

## Contents
<a name="API_EC2ResourceUtilization_Contents"></a>

 ** DiskResourceUtilization **   <a name="awscostmanagement-Type-EC2ResourceUtilization-DiskResourceUtilization"></a>
The field that contains a list of disk (local storage) metrics that are associated with the current instance.
Type: [DiskResourceUtilization](API_DiskResourceUtilization.md) object
Required: No

 ** EBSResourceUtilization **   <a name="awscostmanagement-Type-EC2ResourceUtilization-EBSResourceUtilization"></a>
The EBS field that contains a list of EBS metrics that are associated with the current instance.
Type: [EBSResourceUtilization](API_EBSResourceUtilization.md) object
Required: No

 ** MaxCpuUtilizationPercentage **   <a name="awscostmanagement-Type-EC2ResourceUtilization-MaxCpuUtilizationPercentage"></a>
The maximum observed or expected CPU utilization of the instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MaxMemoryUtilizationPercentage **   <a name="awscostmanagement-Type-EC2ResourceUtilization-MaxMemoryUtilizationPercentage"></a>
The maximum observed or expected memory utilization of the instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MaxStorageUtilizationPercentage **   <a name="awscostmanagement-Type-EC2ResourceUtilization-MaxStorageUtilizationPercentage"></a>
The maximum observed or expected storage utilization of the instance. This doesn't include EBS storage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** NetworkResourceUtilization **   <a name="awscostmanagement-Type-EC2ResourceUtilization-NetworkResourceUtilization"></a>
The network field that contains a list of network metrics that are associated with the current instance.
Type: [NetworkResourceUtilization](API_NetworkResourceUtilization.md) object
Required: No

## See Also
<a name="API_EC2ResourceUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/EC2ResourceUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/EC2ResourceUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/EC2ResourceUtilization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
