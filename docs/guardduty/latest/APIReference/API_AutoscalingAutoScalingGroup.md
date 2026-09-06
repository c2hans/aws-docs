---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AutoscalingAutoScalingGroup.html
---

# AutoscalingAutoScalingGroup
<a name="API_AutoscalingAutoScalingGroup"></a>

Contains information about the Auto Scaling Group involved in a GuardDuty finding, including unique identifiers of the Amazon EC2 instances.

## Contents
<a name="API_AutoscalingAutoScalingGroup_Contents"></a>

 ** ec2InstanceUids **   <a name="guardduty-Type-AutoscalingAutoScalingGroup-ec2InstanceUids"></a>
A list of unique identifiers for the compromised Amazon EC2 instances that are part of the same Auto Scaling Group.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_AutoscalingAutoScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AutoscalingAutoScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AutoscalingAutoScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AutoscalingAutoScalingGroup)
