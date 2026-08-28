---
source_url: https://docs.aws.amazon.com/fis/latest/userguide/stop-experiment.html
---

# Stop an experiment
<a name="stop-experiment"></a>

You can stop a running experiment at any time. When you stop an experiment, any post actions that have not been completed for an action are completed before the experiment stops. You cannot resume a stopped experiment.

**To stop an experiment using the console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiments**.

1. Select the experiment, and choose **Stop experiment**.

1. In the confirmation dialog box, choose **Stop experiment**.

**To stop an experiment using the CLI**
Use the [stop-experiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/stop-experiment.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
