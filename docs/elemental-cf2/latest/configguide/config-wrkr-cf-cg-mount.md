---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-wrkr-cf-cg-mount.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Add Mount Points to AWS Elemental Server Nodes
<a name="config-wrkr-cf-cg-mount"></a>

If you have mounted remote shares on the Conductor node or nodes, we strongly recommend that you mount the same shares on all worker nodes.

**To add mount points**

1. On the Conductor web interface, hover over **Configuration** (cog icon) on the main menu and choose **Mount Point** from the dropdown menu.

   The** Conductor Configuration** screen appears showing the **Cluster Mount Point Settings** tab.
**Important**
This screen has the same fields as the Mount Points screen (where you mounted remote shares for the Conductor nodes). But it is not the same screen\!

1. Complete the screen with the same information as you entered on the Mount Points screen.

The folder on the remote server will now be mounted on the worker nodes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
