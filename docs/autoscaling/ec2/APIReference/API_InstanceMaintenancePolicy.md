---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceMaintenancePolicy.html
---

# InstanceMaintenancePolicy
<a name="API_InstanceMaintenancePolicy"></a>

Describes an instance maintenance policy.

For more information, see [Set instance maintenance policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Contents
<a name="API_InstanceMaintenancePolicy_Contents"></a>

 ** MaxHealthyPercentage **
Specifies the upper threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the maximum percentage of the group that can be in service and healthy, or pending, to support your workload when replacing instances. Value range is 100 to 200. To clear a previously set value, specify a value of `-1`.
Both `MinHealthyPercentage` and `MaxHealthyPercentage` must be specified, and the difference between them cannot be greater than 100. A large range increases the number of instances that can be replaced at the same time.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 200.
Required: No

 ** MinHealthyPercentage **
Specifies the lower threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the minimum percentage of the group to keep in service, healthy, and ready to use to support your workload when replacing instances. Value range is 0 to 100. To clear a previously set value, specify a value of `-1`.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 100.
Required: No

## See Also
<a name="API_InstanceMaintenancePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/InstanceMaintenancePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/InstanceMaintenancePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/InstanceMaintenancePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
