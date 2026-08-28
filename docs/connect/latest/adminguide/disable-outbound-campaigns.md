---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/disable-outbound-campaigns.html
---

# Disable outbound campaigns in Connect Customer
<a name="disable-outbound-campaigns"></a>

**Important**
You must delete all existing campaigns before you can disable outbound campaigns.

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance alias. The instance alias is also your **instance name**, which appears in your Connect Customer URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box around the instance alias.
![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. In the navigation pane, choose **Telephony under Channels and communications**.

1. To disable outbound campaigns, clear the **Enable outbound campaigns** checkbox.

1. Choose **Save**.

   You can no longer create outbound campaigns.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
