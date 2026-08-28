---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-add-discover.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Discover Nodes
<a name="config-wrkr-cf-cg-add-discover"></a>

If a node did not appear in the list of all nodes, you can force its discovery.

**Note**
If this is your first time discovering or add node to a Conductor File cluster, you must [add the nodes via the CLI](config-wrkr-cf-cg-add.md#config-wrkr-cf-cg-add.title) prior to using the web interface for any operations.

**To force discovery**

1. On the primary Conductor web interface, hover over **Nodes** and select Discover Node****.

1. On the **Discover Node** screen, type the hostname or IP address of the node and choose **Discover Node**.

The node appears in the **All Nodes** tab on the **Nodes** screen.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
