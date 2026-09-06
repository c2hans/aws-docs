---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AutoScalingInstanceDetails.html
---

# AutoScalingInstanceDetails
<a name="API_AutoScalingInstanceDetails"></a>

Describes an EC2 instance associated with an Auto Scaling group.

## Contents
<a name="API_AutoScalingInstanceDetails_Contents"></a>

 ** AutoScalingGroupName **
The name of the Auto Scaling group for the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** AvailabilityZone **
The Availability Zone for the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** HealthStatus **
The last reported health status of this instance. `Healthy` means that the instance is healthy and should remain in service. `Unhealthy` means that the instance is unhealthy and Amazon EC2 Auto Scaling should terminate and replace it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** InstanceId **
The ID of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** LifecycleState **
The lifecycle state for the instance. The `Quarantined` state is not used. For more information, see [Amazon EC2 Auto Scaling instance lifecycle](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html) in the *Amazon EC2 Auto Scaling User Guide*.
Valid values: `Pending` \| `Pending:Wait` \| `Pending:Proceed` \| `Quarantined` \| `InService` \| `Terminating` \| `Terminating:Wait` \| `Terminating:Proceed` \| `Terminating:Retained` \| `Terminated` \| `Detaching` \| `Detached` \| `EnteringStandby` \| `Standby` \| `ReplacingRootVolume` \| `ReplacingRootVolume:Wait` \| `ReplacingRootVolume:Proceed` \| `RootVolumeReplaced` \| `Warmed:Pending` \| `Warmed:Pending:Wait` \| `Warmed:Pending:Proceed` \| `Warmed:Pending:Retained` \| `Warmed:Terminating` \| `Warmed:Terminating:Wait` \| `Warmed:Terminating:Proceed` \| `Warmed:Terminating:Retained` \| `Warmed:Terminated` \| `Warmed:Stopped` \| `Warmed:Running` \| `Warmed:Hibernated`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ProtectedFromScaleIn **
Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.
Type: Boolean
Required: Yes

 ** AvailabilityZoneId **
 The Availability Zone ID where the instance is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ImageId **
 The ID of the Amazon Machine Image (AMI) associated with the instance. This field shows the current AMI ID of the instance's root volume. It may differ from the original AMI used when the instance was first launched.
 This field appears for:
+ Instances with root volume replacements through Instance Refresh
+ Instances launched with AMI overrides
This field won't appear for:
+ Existing instances launched from Launch Templates without overrides
+ Existing instances that didn’t have their root volume replaced through Instance Refresh
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** InstanceType **
The instance type of the EC2 instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LaunchConfigurationName **
The launch configuration used to launch the instance. This value is not available if you attached the instance to the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LaunchTemplate **
The launch template for the instance.
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object
Required: No

 ** WeightedCapacity **
The number of capacity units contributed by the instance based on its instance type.
Valid Range: Minimum value of 1. Maximum value of 999.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.
Pattern: `^[\u0031-\u0039][\u0030-\u0039]{0,2}$`
Required: No

## See Also
<a name="API_AutoScalingInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/AutoScalingInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/AutoScalingInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/AutoScalingInstanceDetails)
