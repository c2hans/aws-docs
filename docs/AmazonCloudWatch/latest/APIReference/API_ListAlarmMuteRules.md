---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListAlarmMuteRules.html
---

# ListAlarmMuteRules
<a name="API_ListAlarmMuteRules"></a>

Lists alarm mute rules in your AWS account and region.

You can filter the results by alarm name to find all mute rules targeting a specific alarm, or by status to find rules that are scheduled, active, or expired.

This operation supports pagination for accounts with many mute rules. Use the `MaxRecords` and `NextToken` parameters to retrieve results in multiple calls.

 **Permissions**

To list mute rules, you need the `cloudwatch:ListAlarmMuteRules` permission.

## Request Syntax
<a name="API_ListAlarmMuteRules_RequestSyntax"></a>

```
{
   "AlarmName": "{{string}}",
   "MaxRecords": {{number}},
   "NextToken": "{{string}}",
   "Statuses": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListAlarmMuteRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlarmName](#API_ListAlarmMuteRules_RequestSyntax) **   <a name="ACW-ListAlarmMuteRules-request-AlarmName"></a>
Filter results to show only mute rules that target the specified alarm name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [MaxRecords](#API_ListAlarmMuteRules_RequestSyntax) **   <a name="ACW-ListAlarmMuteRules-request-MaxRecords"></a>
The maximum number of mute rules to return in one call. The default is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAlarmMuteRules_RequestSyntax) **   <a name="ACW-ListAlarmMuteRules-request-NextToken"></a>
The token returned from a previous call to indicate where to continue retrieving results.
Type: String
Required: No

 ** [Statuses](#API_ListAlarmMuteRules_RequestSyntax) **   <a name="ACW-ListAlarmMuteRules-request-Statuses"></a>
Filter results to show only mute rules with the specified statuses. Valid values are `SCHEDULED`, `ACTIVE`, or `EXPIRED`.
Type: Array of strings
Valid Values: `SCHEDULED | ACTIVE | EXPIRED`
Required: No

## Response Syntax
<a name="API_ListAlarmMuteRules_ResponseSyntax"></a>

```
{
   "AlarmMuteRuleSummaries": [
      {
         "AlarmMuteRuleArn": "string",
         "ExpireDate": number,
         "LastUpdatedTimestamp": number,
         "MuteType": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAlarmMuteRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlarmMuteRuleSummaries](#API_ListAlarmMuteRules_ResponseSyntax) **   <a name="ACW-ListAlarmMuteRules-response-AlarmMuteRuleSummaries"></a>
A list of alarm mute rule summaries.
Type: Array of [AlarmMuteRuleSummary](API_AlarmMuteRuleSummary.md) objects

 ** [NextToken](#API_ListAlarmMuteRules_ResponseSyntax) **   <a name="ACW-ListAlarmMuteRules-response-NextToken"></a>
The token to use when requesting the next set of results. If this field is absent, there are no more results to retrieve.
Type: String

## Errors
<a name="API_ListAlarmMuteRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The next token specified is invalid.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## Examples
<a name="API_ListAlarmMuteRules_Examples"></a>

### List all mute rules
<a name="API_ListAlarmMuteRules_Example_1"></a>

List all alarm mute rules in your account.

#### Sample Request
<a name="API_ListAlarmMuteRules_Example_1_Request"></a>

```
aws cloudwatch list-alarm-mute-rules
```

#### Sample Response
<a name="API_ListAlarmMuteRules_Example_1_Response"></a>

```
{
    "AlarmMuteRuleSummaries": [
        {
            "Name": "DailyMaintenanceWindow",
            "AlarmMuteRuleArn": "arn:aws:cloudwatch:us-east-1:123456789012:alarm-mute-rule:DailyMaintenanceWindow",
            "Status": "SCHEDULED",
            "MuteType": "RECURRING",
            "LastUpdatedTimestamp": "2026-01-15T10:30:00Z"
        },
        {
            "Name": "ProductionDeployment-2026-01-20",
            "AlarmMuteRuleArn": "arn:aws:cloudwatch:us-east-1:123456789012:alarm-mute-rule:ProductionDeployment-2026-01-20",
            "Status": "ACTIVE",
            "MuteType": "ONE_TIME",
            "LastUpdatedTimestamp": "2026-01-20T13:00:00Z"
        },
        {
            "Name": "WeeklyBackupWindow",
            "AlarmMuteRuleArn": "arn:aws:cloudwatch:us-west-2:123456789012:alarm-mute-rule:WeeklyBackupWindow",
            "Status": "SCHEDULED",
            "MuteType": "RECURRING",
            "ExpireDate": "2026-12-31T23:59:59Z",
            "LastUpdatedTimestamp": "2026-01-05T12:00:00Z"
        }
    ]
}
```

### List mute rules targeting a specific alarm
<a name="API_ListAlarmMuteRules_Example_2"></a>

List all mute rules that target a specific alarm.

#### Sample Request
<a name="API_ListAlarmMuteRules_Example_2_Request"></a>

```
aws cloudwatch list-alarm-mute-rules \
	--alarm-name "WebServerCPUAlarm"
```

#### Sample Response
<a name="API_ListAlarmMuteRules_Example_2_Response"></a>

```
{
    "AlarmMuteRuleSummaries": [
        {
            "Name": "DailyMaintenanceWindow",
            "AlarmMuteRuleArn": "arn:aws:cloudwatch:us-east-1:123456789012:alarm-mute-rule:DailyMaintenanceWindow",
            "Status": "SCHEDULED",
            "MuteType": "RECURRING",
            "LastUpdatedTimestamp": "2026-01-15T10:30:00Z"
        },
        {
            "Name": "EmergencyMuteRule",
            "AlarmMuteRuleArn": "arn:aws:cloudwatch:us-east-1:123456789012:alarm-mute-rule:EmergencyMuteRule",
            "Status": "ACTIVE",
            "MuteType": "ONE_TIME",
            "LastUpdatedTimestamp": "2026-01-21T14:00:00Z"
        }
    ]
}
```

## See Also
<a name="API_ListAlarmMuteRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListAlarmMuteRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListAlarmMuteRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListAlarmMuteRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListAlarmMuteRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListAlarmMuteRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListAlarmMuteRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListAlarmMuteRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListAlarmMuteRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListAlarmMuteRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListAlarmMuteRules)
