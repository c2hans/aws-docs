---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-ethernet-create.html
---

# Creating an Ethernet interface
<a name="config-conductor-live-ethernet-create"></a>

You use the CLI to create Ethernet interfaces using the web interface.
+ If the node is a Conductor Live node and if HA is currently enabled, disable it now. Conductor Live redundancy (HA, or *high availability*) must be disabled before you configure Ethernet interfaces. For instructions, see [Disabling Conductor Live HA (high availability)](conductor-live-config-ha-chg.md).
+ To create the Ethernet interface, see the [Red Hat *Networking Guide*](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_ip_networking_with_ifcg_files).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
