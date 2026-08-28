---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-edit-application.html
---

# Editing your CloudWatch RUM app monitor settings
<a name="CloudWatch-RUM-edit-application"></a>

To change an app monitor's settings, follow these steps. You can change any settings except the app monitor name.

**To edit how your application uses CloudWatch RUM**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Application Signals**, **RUM**.

1. Choose the button next to the name of the application, and then choose **Actions**, **Edit**.

1. Change any settings except the application name. For more information about the settings, see [Creating a CloudWatch RUM app monitor for a web application](CloudWatch-RUM-get-started-create-app-monitor.md).

1. When finished, choose **Save**.

   Changing the settings changes the code snippet. You must now paste the updated code snippet into your application.

1. After the code snippet is created, choose **Copy to clipboard** or **Download**, and then choose **Done**.

   To start monitoring with the new settings, you insert the code snippet into your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
