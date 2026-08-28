---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-config-ethernet-add.html
---

# Configure Ethernet interfaces
<a name="config-conductor-live-config-ethernet-add"></a>

When you installed the software on the individual nodes in an AWS Elemental Conductor Live cluster, you configured eth0. If you need to set up more Ethernet interfaces (network devices), read this section. You can optionally bond Ethernet interfaces to suit your networking requirements.

**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.

| Node | Work on this node? |
| --- | --- |
| Primary Conductor Live node | Yes |
| Secondary Conductor Live node | Yes |
| Each worker node | Yes |

**Topics**
+ [Creating an Ethernet interface](config-conductor-live-ethernet-create.md)
+ [Modifying an Ethernet interface](config-conductor-live-ethernet-modify.md)
+ [Creating or modifying a bond](config-conductor-live-config-bond-add.md)
+ [Dedicating interfaces to MPTS](config-cluster-mpts.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
