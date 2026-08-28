---
source_url: https://docs.aws.amazon.com/dcv/latest/access-console/using-browser-network-log-files.html
---

# Using browser and network log files
<a name="using-browser-network-log-files"></a>

The web browser communicates with the Handler component to view and modify resources. If there are issues with communication between the web browser and the Handler, you can troubleshoot using the browser and network log files.

## Accessing Chrome console logs
<a name="accessing-chrome-con-logs"></a>

From a Chrome browser, access the console log window.

1. Do one of the following:
   + Use the shortcut key. For Windows and Linux, use `Ctrl+Shift+J`. For macOS, use, `Cmd+Opt+J`.
   + Select the Chrome menu button on the upper right hand side, select **More Tools** then choose **Developer Tools**.

1. Select the **Console** tab in the **Developer Tools** pane.

In the **Console** tab, errors are highlight in red and warnings are highlight in yellow.

## Accessing Chrome network logs
<a name="accessing-chrome-network-logs"></a>

From a Chrome browser, the network tab contains network calls for uploaded and downloaded resources.

1. Do one of the following:
   + Use the shortcut key. For Windows and Linux, use `Ctrl+Shift+J`. For macOS, use, `Cmd+Opt+J`.
   + Select the Chrome menu button on the upper right hand side, select **More Tools** then choose **Developer Tools**.

1. Select the **Network** tab in the **Developer Tools** pane.

1. Refresh the page.

Errors are highlighted in red. Select an error to see more information about it.

The **Status Code** in both the **Headers** and the **Response** tabs can be used to diagnose issues.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
