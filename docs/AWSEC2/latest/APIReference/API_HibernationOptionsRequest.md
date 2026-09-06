---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html
---

# HibernationOptionsRequest
<a name="API_HibernationOptionsRequest"></a>

Indicates whether your instance is configured for hibernation. This parameter is valid only if the instance meets the [hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html). For more information, see [Hibernate your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_HibernationOptionsRequest_Contents"></a>

 ** Configured **
Set to `true` to enable your instance for hibernation.
For Spot Instances, if you set `Configured` to `true`, either omit the `InstanceInterruptionBehavior` parameter (for [`SpotMarketOptions`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMarketOptions.html)), or set it to `hibernate`. When `Configured` is true:
+ If you omit `InstanceInterruptionBehavior`, it defaults to `hibernate`.
+ If you set `InstanceInterruptionBehavior` to a value other than `hibernate`, you'll get an error.
Default: `false`
Type: Boolean
Required: No

## See Also
<a name="API_HibernationOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/HibernationOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/HibernationOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/HibernationOptionsRequest)
