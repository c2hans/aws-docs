---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_CloudwatchLogsExportConfiguration.html
---

# CloudwatchLogsExportConfiguration
<a name="API_CloudwatchLogsExportConfiguration"></a>

The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB instance or DB cluster.

The `EnableLogTypes` and `DisableLogTypes` arrays determine which logs will be exported (or not exported) to CloudWatch Logs.

Valid log types are: `audit` (to publish audit logs) and `slowquery` (to publish slow-query logs). See [Publishing Neptune logs to Amazon CloudWatch logs](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html).

## Contents
<a name="API_CloudwatchLogsExportConfiguration_Contents"></a>

 ** DisableLogTypes.member.N **
The list of log types to disable.
Type: Array of strings
Required: No

 ** EnableLogTypes.member.N **
The list of log types to enable.
Type: Array of strings
Required: No

## See Also
<a name="API_CloudwatchLogsExportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/CloudwatchLogsExportConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CloudwatchLogsExportConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/CloudwatchLogsExportConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
