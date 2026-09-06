---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Rule.html
---

# Rule
<a name="API_Rule"></a>

Defines the schedule configuration for an alarm mute rule.

The rule contains a schedule that specifies when and how long alarms should be muted. The schedule can be a recurring pattern using cron expressions or a one-time mute window using at expressions.

## Contents
<a name="API_Rule_Contents"></a>

 ** Schedule **   <a name="ACW-Type-Rule-Schedule"></a>
The schedule configuration that defines when the mute rule activates and how long it remains active.
Type: [Schedule](API_Schedule.md) object
Required: Yes

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/Rule)
