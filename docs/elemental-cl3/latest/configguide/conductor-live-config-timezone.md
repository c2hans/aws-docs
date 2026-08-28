---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-timezone.html
---

# Setting the web interface time zone
<a name="conductor-live-config-timezone"></a>

This information applies to AWS Elemental Conductor Live, AWS Elemental Live and AWS Elemental Statmux. Follow this procedure if you didn't set the time zone when you installed the software on each node, or if you want to change the time zone on any node.

The time zone set on the node is used as follows:
+ The web interface shows all activity with a timestamp for the time zone that you specify.
+ Activity using the Linux CLI or the REST API doesn't use this time zone.

**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.

| Node | Work on this node? |
| --- | --- |
| Primary Conductor Live node | Yes |
| Secondary Conductor Live node | No. Instead, the primary Conductor Live pushes its configuration to the secondary Conductor Live |
| Each worker node | Yes |

**To set the time zone on the Conductor Live**

Perform this procedure on the primary Conductor Live.

1. On the web interface for the primary Conductor Live, go to the **Settings** page and choose **General**.

1. In **Timezone**, choose the time zone, then choose **Update**.

**To set the time zone on the worker nodes**

Perform this procedure on each worker node.

1. On the worker web interface, choose **Settings** from the main menu. Choose the **Network** tab, then choose **General**.

1. Choose the time zone, then choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
