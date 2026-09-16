---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAlarmMuteRule.html
---

# DeleteAlarmMuteRule
<a name="API_DeleteAlarmMuteRule"></a>

Deletes a specific alarm mute rule.

When you delete a mute rule, any alarms that are currently being muted by that rule are immediately unmuted. If those alarms are in an ALARM state, their configured actions will trigger.

This operation is idempotent. If you delete a mute rule that does not exist, the operation succeeds without returning an error.

 **Permissions**

To delete a mute rule, you need the `cloudwatch:DeleteAlarmMuteRule` permission on the alarm mute rule resource.

## Request Parameters
<a name="API_DeleteAlarmMuteRule_RequestParameters"></a>

 ** AlarmMuteRuleName **
The name of the alarm mute rule to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Errors
<a name="API_DeleteAlarmMuteRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteAlarmMuteRule_Examples"></a>

### Delete a mute rule
<a name="API_DeleteAlarmMuteRule_Example_1"></a>

Delete a specific alarm mute rule. This operation does not return any output on success.

#### Sample Request
<a name="API_DeleteAlarmMuteRule_Example_1_Request"></a>

```
aws cloudwatch delete-alarm-mute-rule \
	--alarm-mute-rule-name "DailyMaintenanceWindow"
```

## See Also
<a name="API_DeleteAlarmMuteRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DeleteAlarmMuteRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarmMuteRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteAlarmMuteRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DeleteAlarmMuteRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarmMuteRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DeleteAlarmMuteRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DeleteAlarmMuteRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DeleteAlarmMuteRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAlarmMuteRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarmMuteRule)
