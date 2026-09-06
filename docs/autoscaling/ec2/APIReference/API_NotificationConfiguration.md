---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_NotificationConfiguration.html
---

# NotificationConfiguration
<a name="API_NotificationConfiguration"></a>

Describes a notification.

## Contents
<a name="API_NotificationConfiguration_Contents"></a>

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** NotificationType **
One of the following event notification types:
+  `autoscaling:EC2_INSTANCE_LAUNCH`
+  `autoscaling:EC2_INSTANCE_LAUNCH_ERROR`
+  `autoscaling:EC2_INSTANCE_TERMINATE`
+  `autoscaling:EC2_INSTANCE_TERMINATE_ERROR`
+  `autoscaling:TEST_NOTIFICATION`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** TopicARN **
The Amazon Resource Name (ARN) of the Amazon SNS topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_NotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/NotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/NotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/NotificationConfiguration)
