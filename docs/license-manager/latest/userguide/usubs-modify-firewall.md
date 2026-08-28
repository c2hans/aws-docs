---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-modify-firewall.html
---

# Modify firewall settings for your Microsoft Office subscription
<a name="usubs-modify-firewall"></a>

A firewall protects your network resources from unauthorized inbound or outbound traffic. The rules that you define for your security group act as the firewall for the VPC resources that work together to provide user-based subscriptions Microsoft Office on EC2 Windows instances.

You can use the following steps to edit the subnets and security group. License Manager uses your settings to provision endpoints for Microsoft Office with AWS PrivateLink. For more information about VPC endpoints, see [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) in the *Amazon Virtual Private Cloud* documentation.

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Navigate to the **User-based subscriptions** page, under **Settings** in the left navigation pane.

1. To edit firewall settings, select the Microsoft Office subscription product tab, and then choose **Edit** from the top of the **Firewall** section. This opens the **Edit Firewall** dialog.

1. After you change your settings, choose **Save** to update, or **Cancel** to keep your current settings.

It might take a few minutes for License Manager to complete changes for these settings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
