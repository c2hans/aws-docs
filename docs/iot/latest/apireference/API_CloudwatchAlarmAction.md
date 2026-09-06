---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CloudwatchAlarmAction.html
---

# CloudwatchAlarmAction
<a name="API_CloudwatchAlarmAction"></a>

Describes an action that updates a CloudWatch alarm.

## Contents
<a name="API_CloudwatchAlarmAction_Contents"></a>

 ** alarmName **   <a name="iot-Type-CloudwatchAlarmAction-alarmName"></a>
The CloudWatch alarm name.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-CloudwatchAlarmAction-roleArn"></a>
The IAM role that allows access to the CloudWatch alarm.
Type: String
Required: Yes

 ** stateReason **   <a name="iot-Type-CloudwatchAlarmAction-stateReason"></a>
The reason for the alarm change.
Type: String
Required: Yes

 ** stateValue **   <a name="iot-Type-CloudwatchAlarmAction-stateValue"></a>
The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT\_DATA.
Type: String
Required: Yes

## See Also
<a name="API_CloudwatchAlarmAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CloudwatchAlarmAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CloudwatchAlarmAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CloudwatchAlarmAction)
