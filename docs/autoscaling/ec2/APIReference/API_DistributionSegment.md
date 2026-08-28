---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DistributionSegment.html
---

# DistributionSegment
<a name="API_DistributionSegment"></a>

Use this structure to specify the capacity types that Amazon EC2 Auto Scaling prioritizes when it launches instances.

## Contents
<a name="API_DistributionSegment_Contents"></a>

 ** TargetCapacityTypes.member.N **
The capacity types to prioritize, in order. Amazon EC2 Auto Scaling attempts to launch instances in the priority order of the capacity types, and within each capacity type, in the order of instance types listed in your launch template `Overrides`.
The following lists the valid values:
on-demand-capacity-reservation
On-Demand Capacity Reservations.
capacity-block
Capacity Blocks.
interruptible-capacity-reservation
Interruptible Capacity Reservations.
on-demand
On-Demand capacity. Include this value to allow the group to fall back to On-Demand capacity when the preceding capacity types are unavailable.
Type: Array of strings
Valid Values: `on-demand-capacity-reservation | capacity-block | interruptible-capacity-reservation | on-demand`
Required: No

## See Also
<a name="API_DistributionSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DistributionSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DistributionSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DistributionSegment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
