---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_MonitorSummary.html
---

# MonitorSummary
<a name="API_MonitorSummary"></a>

Displays summary information about a monitor.

## Contents
<a name="API_MonitorSummary_Contents"></a>

 ** monitorArn **   <a name="networksyntheticmonitor-Type-MonitorSummary-monitorArn"></a>
The ARN of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`
Required: Yes

 ** monitorName **   <a name="networksyntheticmonitor-Type-MonitorSummary-monitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** state **   <a name="networksyntheticmonitor-Type-MonitorSummary-state"></a>
The state of the monitor.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING`
Required: Yes

 ** aggregationPeriod **   <a name="networksyntheticmonitor-Type-MonitorSummary-aggregationPeriod"></a>
The time, in seconds, that metrics are collected and sent to Network Synthetic Monitor. Valid values are either `30` or `60`.
Type: Long
Valid Range: Minimum value of 30.
Required: No

 ** tags **   <a name="networksyntheticmonitor-Type-MonitorSummary-tags"></a>
The list of key-value pairs assigned to the monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_MonitorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/MonitorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/MonitorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/MonitorSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Synthetic Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
