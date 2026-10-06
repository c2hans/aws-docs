---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutAlarmMuteRule.html
---

# PutAlarmMuteRule
<a name="API_PutAlarmMuteRule"></a>

Creates or updates an alarm mute rule.

Alarm mute rules automatically mute alarm actions during predefined time windows. When a mute rule is active, targeted alarms continue to evaluate metrics and transition between states, but their configured actions (such as Amazon SNS notifications or Auto Scaling actions) are muted.

You can create mute rules with recurring schedules using `cron` expressions or one-time mute windows using `at` expressions. Each mute rule can target up to 100 specific alarms by name.

If you specify a rule name that already exists, this operation updates the existing rule with the new configuration.

 **Permissions**

To create or update a mute rule, you must have the `cloudwatch:PutAlarmMuteRule` permission on two types of resources: the alarm mute rule resource itself, and each alarm that the rule targets.

For example, If you want to allow a user to create mute rules that target only specific alarms named "WebServerCPUAlarm" and "DatabaseConnectionAlarm", you would create an IAM policy with one statement granting `cloudwatch:PutAlarmMuteRule` on the alarm mute rule resource (`arn:aws:cloudwatch:[REGION]:123456789012:alarm-mute-rule:*`), and another statement granting `cloudwatch:PutAlarmMuteRule` on the targeted alarm resources (`arn:aws:cloudwatch:[REGION]:123456789012:alarm:WebServerCPUAlarm` and `arn:aws:cloudwatch:[REGION]:123456789012:alarm:DatabaseConnectionAlarm`).

You can also use IAM policy conditions to allow targeting alarms based on resource tags. For example, you can restrict users to create/update mute rules to only target alarms that have a specific tag key-value pair, such as `Team=TeamA`.

## Request Syntax
<a name="API_PutAlarmMuteRule_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "ExpireDate": {{number}},
   "MuteTargets": {
      "AlarmNames": [ "{{string}}" ]
   },
   "Name": "{{string}}",
   "Rule": {
      "Schedule": {
         "Duration": "{{string}}",
         "Expression": "{{string}}",
         "Timezone": "{{string}}"
      }
   },
   "StartDate": {{number}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutAlarmMuteRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_PutAlarmMuteRule_RequestSyntax) **   <a name="ACW-PutAlarmMuteRule-request-Description"></a>
A description of the alarm mute rule that helps you identify its purpose.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [ExpireDate](#API_PutAlarmMuteRule_RequestSyntax) **   <a name="ACW-PutAlarmMuteRule-request-ExpireDate"></a>
The date and time when the mute rule expires and is no longer evaluated, specified as a timestamp in ISO 8601 format (for example, `2026-12-31T23:59:59Z`). After this time, the rule status becomes EXPIRED and will no longer mute the targeted alarms.
Type: Timestamp
Required: No

 ** [MuteTargets](#API_PutAlarmMuteRule_RequestSyntax) **   <a name="ACW-PutAlarmMuteRule-request-MuteTargets"></a>
Specifies which alarms this rule applies to.
Type: [MuteTargets](API_MuteTargets.md) object
Required: No

 ** [Name](#API_PutAlarmMuteRule_RequestSyntax) **   <a name="ACW-PutAlarmMuteRule-request-Name"></a>
The name of the alarm mute rule. This name must be unique within your AWS account and region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Rule](#API_PutAlarmMuteRule_RequestSyntax) **   <a name="ACW-PutAlarmMuteRule-request-Rule"></a>
The configuration that defines when and how long alarms should be muted.
Type: [Rule](API_Rule.md) object
Required: Yes

 ** [StartDate](#API_PutAlarmMuteRule_RequestSyntax) **   <a name="ACW-PutAlarmMuteRule-request-StartDate"></a>
The date and time after which the mute rule takes effect, specified as a timestamp in ISO 8601 format (for example, `2026-04-15T08:00:00Z`). If not specified, the mute rule takes effect immediately upon creation and the mutes are applied as per the schedule expression.
Type: Timestamp
Required: No

 ** [Tags](#API_PutAlarmMuteRule_RequestSyntax) **   <a name="ACW-PutAlarmMuteRule-request-Tags"></a>
A list of key-value pairs to associate with the alarm mute rule. You can use tags to categorize and manage your mute rules.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_PutAlarmMuteRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAlarmMuteRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceeded **
The quota for alarms for this customer has already been reached.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_PutAlarmMuteRule_Examples"></a>

### Create a recurring daily mute rule
<a name="API_PutAlarmMuteRule_Example_1"></a>

Create a mute rule that mutes specific alarms every day from 2:00 AM to 4:00 AM UTC.

#### Sample Request
<a name="API_PutAlarmMuteRule_Example_1_Request"></a>

```
aws cloudwatch put-alarm-mute-rule \
    --name "DailyMaintenanceWindow" \
    --description "Mute alarms during daily maintenance" \
    --rule '{
    "Schedule": {
        "Expression": "cron(0 2 * * ?)",
        "Duration": "PT2H",
        "Timezone": "UTC"
        }
    }' \
    --mute-targets '{
        "AlarmNames": ["WebServerCPUAlarm", "DatabaseConnectionAlarm"]
    }'
```

### Create a one-time mute rule
<a name="API_PutAlarmMuteRule_Example_2"></a>

Create a mute rule for a one-time deployment window.

#### Sample Request
<a name="API_PutAlarmMuteRule_Example_2_Request"></a>

```
aws cloudwatch put-alarm-mute-rule \
    --name "ProductionDeployment-2026-01-20" \
    --description "Mute alarms during production deployment" \
    --rule '{
    "Schedule": {
    "Expression": "at(2026-01-20T14:00)",
    "Duration": "PT1H",
    "Timezone": "America/New_York"
        }
    }' \
    --mute-targets '{
        "AlarmNames": ["APILatencyAlarm", "ErrorRateAlarm"]
    }'
```

### Create a weekly mute rule with tags
<a name="API_PutAlarmMuteRule_Example_3"></a>

Create a mute rule that mutes specific alarms every Saturday for 4 hours.

#### Sample Request
<a name="API_PutAlarmMuteRule_Example_3_Request"></a>

```
aws cloudwatch put-alarm-mute-rule \
    --name "WeeklyBackupWindow" \
    --description "Mute alarms during weekly backup" \
    --rule '{
        "Schedule": {
            "Expression": "cron(0 0 ? * SAT)",
            "Duration": "PT4H",
            "Timezone": "America/Los_Angeles"
        }
    }' \
    --mute-targets '{
        "AlarmNames": ["BackupAlarm", "StorageAlarm"]
    }' \
    --tags '[
        {"Key": "Environment", "Value": "Production"},
        {"Key": "Team", "Value": "Operations"}
    ]'
```

## See Also
<a name="API_PutAlarmMuteRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutAlarmMuteRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAlarmMuteRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutAlarmMuteRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutAlarmMuteRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAlarmMuteRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutAlarmMuteRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutAlarmMuteRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutAlarmMuteRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutAlarmMuteRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutAlarmMuteRule)
