---
source_url: https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-ethernet.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Configure Ethernet Devices on AWS Elemental Server Nodes
<a name="config-wrkr-cf-cg-ethernet"></a>

When you installed each AWS Elemental product in the cluster, you configured eth0. You can now set up eth1 and any additional Ethernet devices. Optionally, you can also bond two devices that you have set up.

**Ethernet devices and the management interface**
When you installed AWS Elemental Server, you configured eth0 as the management interface. Note that setting up a device as the management interface does *not* dedicate this device to management traffic. The device can still handle other traffic.

**Topics**
+ [Add Ethernet Devices](config-wrkr-cf-cg-ethernet-add.md)
+ [Bond Ethernet Devices](config-wrkr-cf-cg-ethernet-bond.md)

**Important**
If you use the Linux CLI to configure network interfaces, DO NOT use the web interface to manage network settings. This will overwrite networking configurations that were made using the CLI.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
