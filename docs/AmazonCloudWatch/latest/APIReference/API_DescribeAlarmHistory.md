---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html
---

# DescribeAlarmHistory
<a name="API_DescribeAlarmHistory"></a>

Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for either all metric alarms or all composite alarms are returned.

CloudWatch retains the history of an alarm even if you delete the alarm.

To use this operation and return information about a composite alarm, you must be signed on with the `cloudwatch:DescribeAlarmHistory` permission that is scoped to `*`. You can't return information about composite alarms if your `cloudwatch:DescribeAlarmHistory` permission has a narrower scope.

## Request Syntax
<a name="API_DescribeAlarmHistory_RequestSyntax"></a>

```
{
   "AlarmContributorId": "{{string}}",
   "AlarmName": "{{string}}",
   "AlarmTypes": [ "{{string}}" ],
   "EndDate": {{number}},
   "HistoryItemType": "{{string}}",
   "MaxRecords": {{number}},
   "NextToken": "{{string}}",
   "ScanBy": "{{string}}",
   "StartDate": {{number}}
}
```

## Request Parameters
<a name="API_DescribeAlarmHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlarmContributorId](#API_DescribeAlarmHistory_RequestSyntax) **   <a name="ACW-DescribeAlarmHistory-request-AlarmContributorId"></a>
The unique identifier of a specific alarm contributor to filter the alarm history results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

 ** [AlarmName](#API_DescribeAlarmHistory_RequestSyntax) **   <a name="ACW-DescribeAlarmHistory-request-AlarmName"></a>
The name of the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [AlarmTypes](#API_DescribeAlarmHistory_RequestSyntax) **   <a name="ACW-DescribeAlarmHistory-request-AlarmTypes"></a>
Use this parameter to specify whether you want the operation to return metric alarms, composite alarms, or log alarms. If you omit this parameter, only metric alarms are returned.
Type: Array of strings
Valid Values: `CompositeAlarm | MetricAlarm | LogAlarm`
Required: No

 ** [EndDate](#API_DescribeAlarmHistory_RequestSyntax) **   <a name="ACW-DescribeAlarmHistory-request-EndDate"></a>
The ending date to retrieve alarm history.
Type: Timestamp
Required: No

 ** [HistoryItemType](#API_DescribeAlarmHistory_RequestSyntax) **   <a name="ACW-DescribeAlarmHistory-request-HistoryItemType"></a>
The type of alarm histories to retrieve.
Type: String
Valid Values: `ConfigurationUpdate | StateUpdate | Action | AlarmContributorStateUpdate | AlarmContributorAction`
Required: No

 ** [MaxRecords](#API_DescribeAlarmHistory_RequestSyntax) **   <a name="ACW-DescribeAlarmHistory-request-MaxRecords"></a>
The maximum number of alarm history records to retrieve.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeAlarmHistory_RequestSyntax) **   <a name="ACW-DescribeAlarmHistory-request-NextToken"></a>
The token returned by a previous call to indicate that there is more data available.
Type: String
Required: No

 ** [ScanBy](#API_DescribeAlarmHistory_RequestSyntax) **   <a name="ACW-DescribeAlarmHistory-request-ScanBy"></a>
Specified whether to return the newest or oldest alarm history first. Specify `TimestampDescending` to have the newest event history returned first, and specify `TimestampAscending` to have the oldest history returned first.
Type: String
Valid Values: `TimestampDescending | TimestampAscending`
Required: No

 ** [StartDate](#API_DescribeAlarmHistory_RequestSyntax) **   <a name="ACW-DescribeAlarmHistory-request-StartDate"></a>
The starting date to retrieve alarm history.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_DescribeAlarmHistory_ResponseSyntax"></a>

```
{
   "AlarmHistoryItems": [
      {
         "AlarmContributorAttributes": {
            "string" : "string"
         },
         "AlarmContributorId": "string",
         "AlarmName": "string",
         "AlarmType": "string",
         "HistoryData": "string",
         "HistoryItemType": "string",
         "HistorySummary": "string",
         "Timestamp": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAlarmHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlarmHistoryItems](#API_DescribeAlarmHistory_ResponseSyntax) **   <a name="ACW-DescribeAlarmHistory-response-AlarmHistoryItems"></a>
The alarm histories, in JSON format.
Type: Array of [AlarmHistoryItem](API_AlarmHistoryItem.md) objects

 ** [NextToken](#API_DescribeAlarmHistory_ResponseSyntax) **   <a name="ACW-DescribeAlarmHistory-response-NextToken"></a>
The token that marks the start of the next batch of returned results.
Type: String

## Errors
<a name="API_DescribeAlarmHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The next token specified is invalid.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribeAlarmHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarmHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarmHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarmHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarmHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarmHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmHistory)
