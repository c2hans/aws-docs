---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-ethernet-modify.html
---

# Modifying an Ethernet interface
<a name="config-conductor-live-ethernet-modify"></a>

You use the CLI to modify Ethernet interfaces using the web interface.
+ If the node is a Conductor Live node and if HA is currently enabled, disable it now. Conductor Live redundancy (HA, or *high availability*) must be disabled before you configure network interfaces. For instructions, see [Disabling Conductor Live HA (high availability)](conductor-live-config-ha-chg.md).
+ To modify an Ethernet interface, see the [Red Hat *Networking Guide*](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_ip_networking_with_ifcg_files).

**Warning**
The **Devices** page on the Conductor Live web interface includes the pencil icon that lets you edit the Ethernet interface. However, you must not use the web interface to modify interfaces because you will break the configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
