---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-creating-or-editing-existing-alarm-console.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Configuring a CloudWatch alarm to create OpsItems (console)
<a name="OpsCenter-creating-or-editing-existing-alarm-console"></a>

You can manually create an alarm or update an existing alarm to create OpsItems from Amazon CloudWatch.

**To create a CloudWatch alarm and configure Systems Manager as a target of that alarm**

1. Complete steps 1–9 as specified in [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the *Amazon CloudWatch User Guide*.

1. In the **Systems Manager action ** section, choose **Add Systems Manager OpsCenter action**.

1. Choose **OpsItems**.

1. For **Severity**, choose from 1 to 4.

1. (Optional) For **Category**, choose a category for the OpsItem.

1. Complete steps 11–13 as specified in [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the *Amazon CloudWatch User Guide*.

1. Choose **Next** and complete the wizard.

**To edit an existing alarm and configure Systems Manager as a target of that alarm**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**.

1. Select the alarm, and then choose **Actions**, **Edit**.

1. (Optional) Change settings in the **Metrics** and **Conditions** sections, and then choose **Next**.

1. In the **Systems Manager** section, choose **Add Systems Manager OpsCenter action**.

1. For **Severity**, choose a number.
**Note**
Severity is a user-defined value. You or your organization determine what each severity value means and any service-level agreement associated with each severity.

1. (Optional) For **Category**, choose an option.

1. Choose **Next** and complete the wizard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
