---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AlarmConfiguration.html
---

# AlarmConfiguration
<a name="API_AlarmConfiguration"></a>

The details for the CloudWatch alarm you want to apply to an automation or command.

## Contents
<a name="API_AlarmConfiguration_Contents"></a>

 ** Alarms **   <a name="systemsmanager-Type-AlarmConfiguration-Alarms"></a>
The name of the CloudWatch alarm specified in the configuration.
Type: Array of [Alarm](API_Alarm.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** IgnorePollAlarmFailure **   <a name="systemsmanager-Type-AlarmConfiguration-IgnorePollAlarmFailure"></a>
When this value is *true*, your automation or command continues to run in cases where we can’t retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT\_DATA, the automation or command continues to run, regardless of this value. Default is *false*.
Type: Boolean
Required: No

## See Also
<a name="API_AlarmConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AlarmConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AlarmConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AlarmConfiguration)
