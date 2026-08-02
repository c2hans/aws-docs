---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MuteTargets.html
---

# MuteTargets
<a name="API_MuteTargets"></a>

Specifies which alarms an alarm mute rule applies to.

You can target up to 100 specific alarms by name. When a mute rule is active, the targeted alarms continue to evaluate metrics and transition between states, but their configured actions are muted.

## Contents
<a name="API_MuteTargets_Contents"></a>

 ** AlarmNames **   <a name="ACW-Type-MuteTargets-AlarmNames"></a>
The list of alarm names that this mute rule targets. You can specify up to 100 alarm names.
Each alarm name must be between 1 and 255 characters in length. The alarm names must match existing alarms in your AWS account and region.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_MuteTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MuteTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MuteTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MuteTargets)
