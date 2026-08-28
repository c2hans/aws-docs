---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-network.html
---

# Configuring nodes for connectivity
<a name="config-conductor-live-network"></a>

This section describe how to configure the node so that it can communicate with Conductor Live, and with upstream systems and downstream systems.

**Note**
If your deployment involves several Conductor Live clusters, we strongly recommend that you set up each cluster in its own network.

**Topics**
+ [Configure DNS servers](config-cluster-dns.md)
+ [Configuring NTP and PTP servers](config-cluster-ntp.md)
+ [Configure Ethernet interfaces](config-conductor-live-config-ethernet-add.md)
+ [Configuring a firewall and opening ports](network-firewall.md)
+ [Enabling and disabling HTTPS](ssl-config.md)
+ [Adding SDI input devices](conductor-live-config-sdi-dev.md)
+ [Configuring SDI video routers](conductor-live-config-sdi-rou.md)
+ [Adding mount points to worker nodes](config-wrkr-cf-config-mount.md)
+ [Setting the web interface time zone](conductor-live-config-timezone.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
