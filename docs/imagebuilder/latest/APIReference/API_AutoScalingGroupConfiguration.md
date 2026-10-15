---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_AutoScalingGroupConfiguration.html
---

# AutoScalingGroupConfiguration
<a name="API_AutoScalingGroupConfiguration"></a>

Identifies the Amazon EC2 Auto Scaling group that Image Builder takes the build instance from, and how long Image Builder waits when the group has no instance available.

## Contents
<a name="API_AutoScalingGroupConfiguration_Contents"></a>

 ** name **   <a name="imagebuilder-Type-AutoScalingGroupConfiguration-name"></a>
The name of the Auto Scaling group, in the same account and AWS Region as the infrastructure configuration. To specify a group, you must have permissions to describe it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** capacityWaitTimeoutSeconds **   <a name="imagebuilder-Type-AutoScalingGroupConfiguration-capacityWaitTimeoutSeconds"></a>
The number of seconds that Image Builder waits for an instance to become available in the group before the build fails. If you set this value to 0 or omit it, the build fails as soon as the group has no instance available.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: No

## See Also
<a name="API_AutoScalingGroupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/AutoScalingGroupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/AutoScalingGroupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/AutoScalingGroupConfiguration)
