---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-delete-appmonitor.html
---

# Stopping using CloudWatch RUM or deleting an app monitor
<a name="CloudWatch-RUM-delete-appmonitor"></a>

To stop using CloudWatch RUM with an application, remove the code snippet that RUM generated from your application's code.

To delete a RUM app monitor, follow these steps.

**To delete an app monitor**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Application Signals**, **RUM**.

1. Choose the button next to the name of the application, and then choose **Actions**, **Delete**.

1. In the confirmation box, enter **Delete** and then choose **Delete**.

1. If you haven't done so already, delete the CloudWatch RUM code snippet from your application's code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
