---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PendingCloudwatchLogsExports.html
---

# PendingCloudwatchLogsExports
<a name="API_PendingCloudwatchLogsExports"></a>

A list of the log types whose configuration is still pending. In other words, these log types are in the process of being activated or deactivated.

## Contents
<a name="API_PendingCloudwatchLogsExports_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LogTypesToDisable.member.N **
Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.
Type: Array of strings
Required: No

 ** LogTypesToEnable.member.N **
Log types that are in the process of being deactivated. After they are deactivated, these log types aren't exported to CloudWatch Logs.
Type: Array of strings
Required: No

## See Also
<a name="API_PendingCloudwatchLogsExports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/PendingCloudwatchLogsExports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/PendingCloudwatchLogsExports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/PendingCloudwatchLogsExports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
