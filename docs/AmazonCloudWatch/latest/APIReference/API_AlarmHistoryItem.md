---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AlarmHistoryItem.html
---

# AlarmHistoryItem
<a name="API_AlarmHistoryItem"></a>

Represents the history of a specific alarm.

## Contents
<a name="API_AlarmHistoryItem_Contents"></a>

 ** AlarmContributorAttributes **   <a name="ACW-Type-AlarmHistoryItem-AlarmContributorAttributes"></a>
A map of attributes that describe the alarm contributor associated with this history item, providing context about the contributor's characteristics at the time of the event.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 150 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** AlarmContributorId **   <a name="ACW-Type-AlarmHistoryItem-AlarmContributorId"></a>
The unique identifier of the alarm contributor associated with this history item, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

 ** AlarmName **   <a name="ACW-Type-AlarmHistoryItem-AlarmName"></a>
The descriptive name for the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** AlarmType **   <a name="ACW-Type-AlarmHistoryItem-AlarmType"></a>
The type of alarm, either metric alarm or composite alarm.
Type: String
Valid Values: `CompositeAlarm | MetricAlarm | LogAlarm`
Required: No

 ** HistoryData **   <a name="ACW-Type-AlarmHistoryItem-HistoryData"></a>
Data about the alarm, in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Required: No

 ** HistoryItemType **   <a name="ACW-Type-AlarmHistoryItem-HistoryItemType"></a>
The type of alarm history item.
Type: String
Valid Values: `ConfigurationUpdate | StateUpdate | Action | AlarmContributorStateUpdate | AlarmContributorAction`
Required: No

 ** HistorySummary **   <a name="ACW-Type-AlarmHistoryItem-HistorySummary"></a>
A summary of the alarm history, in text format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Timestamp **   <a name="ACW-Type-AlarmHistoryItem-Timestamp"></a>
The time stamp for the alarm history item.
Type: Timestamp
Required: No

## See Also
<a name="API_AlarmHistoryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AlarmHistoryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AlarmHistoryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AlarmHistoryItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
