---
source_url: https://docs.aws.amazon.com/elemental-statmux/latest/configguide/config-wrkr-cf-cg-firewall.html
---

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Open Ports on the Firewall for AWS Elemental Statmux Nodes
<a name="config-wrkr-cf-cg-firewall"></a>

You can enable or disable the firewall. We recommend that your nodes always be installed behind a customer firewall on a private network, regardless of if the individual firewall is enabled on each node. The node firewall is enabled by default.

When the node firewall is enabled, the installer configures the ports that must be open for incoming and outgoing traffic for each node. Use the following procedure to open more ports if you need them.

**To open ports on the node firewall**

1. On the AWS Elemental Statmux web interface, go to the **Settings** page and choose **Firewall**.

   You must turn on the node firewall before you can make any changes to the ports.

1. In the **Firewall Settings**, choose **Firewall On**.

1. (Optional) To enable a port, choose **Accept** for that port.

1. (Optional) To add a new port, complete the fields in the **Add Incoming Port** section.

1. When you're done, choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Statmux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-statmux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
