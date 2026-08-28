---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/cloud-watch-search.html
---

# Searching CloudWatch log groups
<a name="cloud-watch-search"></a>

You can use Search Log Group to search all log streams in a log group.

For detailed information about the Amazon CloudWatch Logs service, see the [Working with Log Groups and Log Streams ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Working-with-log-groups-and-streams.html) topic in the *Amazon CloudWatch User Guide*.

## Searching log groups from the VS Code Command Palette
<a name="cloud-watch-search-command"></a>

To search log groups from the VS Code Command Palette, complete the following steps.

For detailed information about Amazon CloudWatch Logs filters and patterns, see the [Filter and pattern syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) section in the *Amazon CloudWatch User Guide*.

1. From VS Code, open the **Command Palette** by pressing **cmd\+shift\+p** (windows: **ctrl\+shift\+p**).

1. From the Command Palette, enter the command **AWS: Search Log Group**, then select it to open the search log group dialog in VS Code and follow the prompts to continue.
**Note**
From the first prompt, you have the option to switch your AWS region before proceeding to the next steps.

1. From the **Select Log Group (1/3)** prompt, choose the log group you want to search.

1. From the **Select Time Filter (2/3)** prompt, choose the time filter to apply to your search.

1. From the **Search Log Group... (3/3)** prompt, enter your search pattern in the provided field, then press the **Enter** key to continue or the **ESC** key to cancel the search.

1. Your search results open in the VS Code editor, when the search is complete.

## Searching log groups from the AWS Explorer
<a name="cloud-watch-search-explorer"></a>

To search log groups from the AWS Toolkit for Visual Studio Code Explorer, complete the following steps.

1. From the AWS Toolkit for Visual Studio Code Explorer expand **CloudWatch**.

1. Open the context menu for (right-click) the Search Log Group you want to search, then choose **Search Log Group** to open the search prompt.

1. Follow the prompts by selecting a time frame to continue.

1. When prompted, enter your search pattern in the provided field, then press the **Enter** key to continue or the **ESC** key to cancel the search.

1. Your search results open in the VS Code editor when the search is complete.

## Working with search log results
<a name="cloud-watch-search-results"></a>

After completing a successful CloudWatch log group search, your search results open in the VS Code editor. The following procedures describe how to work with search log results.

**Note**
When viewing a single log stream, the following features are limited to the results in your currently-active log stream.

**Saving your search log group results**

To save your search log group results locally, complete the following steps.

1. From your search log group results, choose the **Save Log to File** icon button, located in the upper right-hand corner of the VS Code editor.

1. From the **Save As** prompt, specify the name and location you would like to save the file to.

1. Choosing **OK** saves the file to your local machine.

**Changing the time range the time-range**

To change the time range that is active in your search log group results, complete the following steps.

1. From your search log group results, choose the **Search by date...** icon button, located in the upper right-hand corner of the VS Code editor.

1. From the **Select Time Filter** prompt, choose a new time range for your search log results.

1. Your results are updated when the **Select Time Filter** prompt is closed.

**Changing the search pattern**

To change the search pattern that is active in your search log group results, complete the following steps.

1. From your search log group results, choose the **Search by Pattern...** icon button, located in the upper right-hand corner of VS Code editor.

1. From the **Search Log Group** prompt, enter the new search pattern in the provided field.

1. Press the **Enter** key to close the prompt and update your results with the new search pattern.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
