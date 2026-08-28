---
source_url: https://docs.aws.amazon.com/vpc/latest/userguide/view-flow-log-records-cwl.html
---

# View flow log records with CloudWatch Logs
<a name="view-flow-log-records-cwl"></a>

You can view your flow log records using the CloudWatch Logs console. After you create your flow log, it might take a few minutes for it to be visible in the console.

**To view flow log records published to CloudWatch Logs using the console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, **Log groups**.

1. Select the name of the log group that contains your flow logs to open its details page.

1. Select the name of the log stream that contains the flow log records. For more information, see [Flow log records](flow-log-records.md).

**To view flow log records published to CloudWatch Logs using the command line**
+ [get-log-events](https://docs.aws.amazon.com/cli/latest/reference/logs/get-log-events.html) (AWS CLI)
+ [Get-CWLLogEvent](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-CWLLogEvent.html) (AWS Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
