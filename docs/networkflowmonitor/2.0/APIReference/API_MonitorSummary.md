---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_MonitorSummary.html
---

# MonitorSummary
<a name="API_MonitorSummary"></a>

A summary of information about a monitor, including the ARN, the name, and the status.

## Contents
<a name="API_MonitorSummary_Contents"></a>

 ** monitorArn **   <a name="networkflowmonitor-Type-MonitorSummary-monitorArn"></a>
The Amazon Resource Name (ARN) of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`
Required: Yes

 ** monitorName **   <a name="networkflowmonitor-Type-MonitorSummary-monitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** monitorStatus **   <a name="networkflowmonitor-Type-MonitorSummary-monitorStatus"></a>
The status of a monitor. The status can be one of the following
+  `PENDING`: The monitor is in the process of being created.
+  `ACTIVE`: The monitor is active.
+  `INACTIVE`: The monitor is inactive.
+  `ERROR`: Monitor creation failed due to an error.
+  `DELETING`: The monitor is in the process of being deleted.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING`
Required: Yes

## See Also
<a name="API_MonitorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/MonitorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/MonitorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/MonitorSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Flow Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkflowmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
