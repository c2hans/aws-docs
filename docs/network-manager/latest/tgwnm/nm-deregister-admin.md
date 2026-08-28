---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-deregister-admin.html
---

# Deregister an administrator from multi-account in an AWS global network
<a name="nm-deregister-admin"></a>

Deregistering delegated administrators removes that account's permission to manage global networks for your organization. All registered transit gateways from other member accounts are deregistered from the specific delegated administrator's global networks. For more information about how deregistering delegated administrators works, see [Deregister delegated administrators](nm-multi-account.md#nm-how-it-works-deregister).

**To deregister a delegated administrator**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home) with the management account.

1. Under **Connectivity**, choose **Global Networks**.

1. In the navigation pane, choose **Settings**.

1. In the **Delegated Administrators** section, choose one or more accounts that you want to deregister.

   Depending on your organization size and the number of delegated administrators you're deregistering, this could take several minutes. During this time you won't be able to register any new delegated administrators.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
