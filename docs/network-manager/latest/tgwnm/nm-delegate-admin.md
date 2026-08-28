---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-delegate-admin.html
---

# Register an administrator for multi-account in an AWS global network
<a name="nm-delegate-admin"></a>

Use the AWS Global Networks for Transit Gateways console to register delegated administrators. You can register up to ten delegated administrators. Delegated administrators can assume the SLR and IAM roles deployed while enabling trusted access for access across multiple accounts. For more information about delegated administrators, see [Delegated administrators](nm-multi-account.md#nm-how-it-works-delegate).

**To register a delegated administrator**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home) with the management account.

1. Under **Connectivity**, choose **Global Networks**.

1. In the navigation pane, choose **Settings**.

1. In the **Delegated Administrators** section, choose **Register delegated administrator**.

1. From the **AWS account ID** dropdown list, choose one or more AWS Organizations accounts that you want to delegate administrator permissions to.

1. Choose **Register delegated administrator**.

1. When the delegated administrator is registered, you can then register transit gateways from any transit gateways from any account within your organization to the global network in the delegated administrator account. For more information about registering transit gateways in the global network of a delegated administrator account, see [Transit gateway registrations in AWS Global Networks for Transit Gateways](tgw-registrations.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
