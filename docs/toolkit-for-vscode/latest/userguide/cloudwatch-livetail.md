---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/cloudwatch-livetail.html
---

# Amazon CloudWatch Logs Live Tail
<a name="cloudwatch-livetail"></a>

Live stream your CloudWatch log events as they are ingested into a particular Log Group with Amazon CloudWatch Logs Live Tail.

For detailed information about the Live Tail feature, see the [Troubleshoot with CloudWatch Logs Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) topic in the *Amazon CloudWatch Logs* User Guide.

Live Tail sessions incur costs by session usage time, per minute. For information about pricing, view the *Logs* tab in the **Paid Tier** section of the [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) guide.

## Starting a Live Tail session from the VS Code Command Palette
<a name="cloudwatch-livetail-commandpalette"></a>

To start a Live Tail session from the VS Code Command Palette, complete the following steps.

For detailed information about Amazon CloudWatch Logs filters and patterns, see the [Filter and pattern syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) section in the *Amazon CloudWatch* User Guide.

**Starting a tailing session from the Command Palette**

1. From VS Code, open the **Command Palette** by pressing **cmd\+shift\+p** (Windows: **ctrl\+shift\+p**).

1. From the **Command Palette**, enter the command `AWS: Tail Log Group`, then select it to open the **Tail log group** dialog in VS Code and follow the prompts to continue.
**Note**
At the first prompt you have the option to switch your AWS Region before proceeding to the next steps.

1. From the **Tail Log Group (1/3)** prompt, choose the log group you want to tail.

1. From the **Include log events from... (2/3)** prompt, choose the log stream filter to apply to your tailing session.

1. From the **Provide log event filter pattern... (3/3)** prompt, enter your filter pattern in the provided field, then press the **Enter** key to continue or the **ESC** key to cancel the search.

1. Upon completion, your results stream into the VS Code editor
**Note**
If a Live Tail session running in the VS Code window matches the configuration of a newly submitted Tail Log Group command, a new session doesn't start. Instead, your existing session becomes the active text editor.

## Starting a Live Tail session from the AWS Explorer
<a name="cloudwatch-livetail-explorer"></a>

To start a Live Tail session from the AWS Toolkit Explorer, complete the following steps.

**Starting a tailing session from the AWS Explorer**

1. From the AWS Toolkit Explorer, expand **CloudWatch**.

1. Open the context menu for (right-click) the Log Group you want to tail, then choose **Tail Log Group** to open the tailing prompt.

1. Follow the prompts to continue.

1. Your results will stream into the VS Code editor.

## Stopping a Live Tail session
<a name="cloudwatch-livetail-explorer"></a>

There are 2 ways to stop a running Tailing session.

**Stopping a tailing session**

1. Click the **Stop tailing** CodeLens at the bottom of the tailing-session text document.

1. Close all editors containing the tailing-session text document.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
