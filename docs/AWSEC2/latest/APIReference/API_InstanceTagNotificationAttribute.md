---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceTagNotificationAttribute.html
---

# InstanceTagNotificationAttribute
<a name="API_InstanceTagNotificationAttribute"></a>

Describes the registered tag keys for the current Region.

## Contents
<a name="API_InstanceTagNotificationAttribute_Contents"></a>

 ** includeAllTagsOfInstance **
Indicates wheter all tag keys in the current Region are registered to appear in scheduled event notifications. `true` indicates that all tag keys in the current Region are registered.
Type: Boolean
Required: No

 ** InstanceTagKeySet.N **
The registered tag keys.
Type: Array of strings
Required: No

## See Also
<a name="API_InstanceTagNotificationAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceTagNotificationAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceTagNotificationAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceTagNotificationAttribute)
