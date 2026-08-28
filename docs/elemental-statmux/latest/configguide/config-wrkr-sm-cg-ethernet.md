---
source_url: https://docs.aws.amazon.com/elemental-statmux/latest/configguide/config-wrkr-sm-cg-ethernet.html
---

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Configure Ethernet Devices on AWS Elemental Statmux Nodes
<a name="config-wrkr-sm-cg-ethernet"></a>

When you installed each AWS Elemental product in the cluster, you configured eth0. You can now set up eth1 and any additional Ethernet devices. Optionally, you can also bond two devices that you have set up.

**Ethernet devices and the management interface**
When you installed AWS Elemental Statmux, you configured eth0 as the management interface. Note that setting up a device as the management interface does *not* dedicate this device to management traffic. The device can still handle other traffic.

**Topics**
+ [Add Ethernet Devices](config-wrkr-sm-cg-ethernet-add.md)
+ [Bond Ethernet Devices](config-wrkr-sm-cg-ethernet-bond.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Statmux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-statmux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
