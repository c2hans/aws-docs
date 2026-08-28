---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-servers.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Configure DNS and NTP Servers for the Cluster
<a name="config-cond-cf-cg-servers"></a>

You can configure servers in the following ways:
+ Create a list of DNS servers for each node to use.
+ Create a list of NTP servers for each node to use.

**To configure servers**

1. On the AWS Elemental Conductor File node, choose **Nodes** in the main menu.

1. On the **Nodes** screen, choose **Edit** (wrench icon) beside the primary Conductor node.

1. On the The **Hostname, DNS & NTP** tab, choose **Network > Hostname, DNS & NTP**.
**Important**
This screen has a warning in red. It does not apply the first time you set up DNS and NTP servers.

1. Add servers as desired and choose **Save**.

1. If you have a secondary Conductor node, switch to the web interface for that node and repeat these steps.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
