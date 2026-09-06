---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchTemplate.html
---

# LaunchTemplate
<a name="API_LaunchTemplate"></a>

Use this structure to specify the launch templates and instance types (overrides) for a mixed instances policy.

When you update the launch template or overrides in the [UpdateAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_UpdateAutoScalingGroup.html) API call, existing Amazon EC2 instances continue to run. When scaling out occurs, Amazon EC2 Auto Scaling launches instances to match the new settings. When scaling in occurs, Amazon EC2 Auto Scaling terminates instances according to the group's termination policies.

## Contents
<a name="API_LaunchTemplate_Contents"></a>

 ** LaunchTemplateSpecification **
The launch template.
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object
Required: No

 ** Overrides.member.N **
Any properties that you specify override the same properties in the launch template.
Type: Array of [LaunchTemplateOverrides](API_LaunchTemplateOverrides.md) objects
Required: No

## See Also
<a name="API_LaunchTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/LaunchTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/LaunchTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/LaunchTemplate)
