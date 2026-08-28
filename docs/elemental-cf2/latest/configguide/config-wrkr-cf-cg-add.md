---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-add.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Add AWS Elemental Server Nodes to the Cluster
<a name="config-wrkr-cf-cg-add"></a>

Add all of the worker nodes to the cluster so that they can be controlled by the Conductor node.

**Important**
If this is your first time adding worker nodes to a cluster you must add worker nodes to the Conductor File cluster via the CLI. Using the Conductor File web interface to discover the worker node and add to the cluster causes the worker node to go into a failed state.

**To add worker nodes to the cluster via the CLI**

1. On the worker node, enter the following command to change the directory:

   `cd /opt/elemental_se`

1. Enter the following command to start the configurations script on the worker node:

   `sudo ./configure`

1. After being prompted to add the worker node to the Conductor File cluster, you are asked to trust the public key from the conductor node(s). You must accept this for the Conductor File node to control the worker node.

1. After trusting the public key, continue through the configuration prompts as normal.

**Note**
After you run the configuration script on the worker node, you can add or remove any future nodes using the Conductor File web interface. EXCEPTION: If you kickstart the worker node after you added it to the Conductor File cluster, you must add it back into the cluster via the CLI again.

**To add worker nodes to the cluster**

1. On the primary Conductor web interface, choose **Nodes**.

1. On the **Nodes** screen, scroll down to the list of nodes.

1. Choose **All Nodes** to display a list of all the Conductor and worker nodes in the network. If a given node does not appear in the list, you must force discovery, as described in the next section.

1. Select the nodes to add to the cluster or use the checkbox to select all nodes, and choose **Add to Cluster** (\+ icon).

1. Wait a few minutes and then select the **Cluster** tab to view all of the nodes in the cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
