---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-firewall.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Open Ports on the Firewall for AWS Elemental Conductor File Nodes
<a name="config-cond-cf-cg-firewall"></a>

You can enable or disable the firewall. By default, the firewall is enabled.

The installer configures the ports on your firewall that must be open for incoming and outgoing traffic to and from each node. You can open more ports if required for any reason.

**To open ports on the firewall**

1. On the AWS Elemental Conductor File node, click **Nodes** in the main menu.

1. On the **Nodes** screen, choose **Edit** (wrench icon) beside the primary Conductor node.

1. On the **Node Configuration** screen, choose **Firewall**.

1. Choose **Firewall On**. A list of ports appears.

1. In the list of ports, add or delete ports as desired.

1. If you have a secondary Conductor node, switch to the web interface for that node and repeat these steps.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
