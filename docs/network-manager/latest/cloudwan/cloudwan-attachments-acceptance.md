---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-acceptance.html
---

# Accept or reject an AWS Cloud WAN core network attachment
<a name="cloudwan-attachments-acceptance"></a>

When you create an attachment and associate it to a segment that requires an acceptance from the core network owner, the newly created attachment goes into a **Pending attachment acceptance** state. The core network owner has to review the attachment and choose to accept or reject the request.

**To accept or reject an attachment using the console**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Select the check box for the specific attachment that is in the **Pending attachment acceptance** state. Details about the attachment are displayed in the lower part of the page.

1. Choose **Accept** or **Reject**.

1. If you chose **Accept**, the attachment goes into a **Creating (Accept)** state. If you chose **Reject**, the attachment goes into a **Rejected (Reject)** state.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
