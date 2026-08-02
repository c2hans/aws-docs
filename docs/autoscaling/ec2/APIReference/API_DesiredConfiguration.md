---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DesiredConfiguration.html
---

# DesiredConfiguration
<a name="API_DesiredConfiguration"></a>

Describes the desired configuration for an instance refresh.

If you specify a desired configuration, you must specify either a `LaunchTemplate` or a `MixedInstancesPolicy`.

## Contents
<a name="API_DesiredConfiguration_Contents"></a>

 ** LaunchTemplate **
Describes the launch template and the version of the launch template that Amazon EC2 Auto Scaling uses to launch Amazon EC2 instances. For more information about launch templates, see [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object
Required: No

 ** MixedInstancesPolicy **
Use this structure to launch multiple instance types and On-Demand Instances and Spot Instances within a single Auto Scaling group.
A mixed instances policy contains information that Amazon EC2 Auto Scaling can use to launch instances and help optimize your costs. For more information, see [Auto Scaling groups with multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: [MixedInstancesPolicy](API_MixedInstancesPolicy.md) object
Required: No

## See Also
<a name="API_DesiredConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DesiredConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DesiredConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DesiredConfiguration)
