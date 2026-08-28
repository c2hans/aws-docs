---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_AutoScalingGroupProviderUpdate.html
---

# AutoScalingGroupProviderUpdate
<a name="API_AutoScalingGroupProviderUpdate"></a>

The details of the Auto Scaling group capacity provider to update.

## Contents
<a name="API_AutoScalingGroupProviderUpdate_Contents"></a>

 ** managedDraining **   <a name="ECS-Type-AutoScalingGroupProviderUpdate-managedDraining"></a>
The managed draining option for the Auto Scaling group capacity provider. When you enable this, Amazon ECS manages and gracefully drains the EC2 container instances that are in the Auto Scaling group capacity provider.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** managedScaling **   <a name="ECS-Type-AutoScalingGroupProviderUpdate-managedScaling"></a>
The managed scaling settings for the Auto Scaling group capacity provider.
Type: [ManagedScaling](API_ManagedScaling.md) object
Required: No

 ** managedTerminationProtection **   <a name="ECS-Type-AutoScalingGroupProviderUpdate-managedTerminationProtection"></a>
The managed termination protection setting to use for the Auto Scaling group capacity provider. This determines whether the Auto Scaling group has managed termination protection.
When using managed termination protection, managed scaling must also be used otherwise managed termination protection doesn't work.
When managed termination protection is on, Amazon ECS prevents the Amazon EC2 instances in an Auto Scaling group that contain tasks from being terminated during a scale-in action. The Auto Scaling group and each instance in the Auto Scaling group must have instance protection from scale-in actions on. For more information, see [Instance Protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html#instance-protection) in the * AWS Auto Scaling User Guide*.
When managed termination protection is off, your Amazon EC2 instances aren't protected from termination when the Auto Scaling group scales in.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_AutoScalingGroupProviderUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/AutoScalingGroupProviderUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/AutoScalingGroupProviderUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/AutoScalingGroupProviderUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
