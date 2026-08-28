---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/device-connections.html
---

# Connections in AWS Global Networks for Transit Gateways
<a name="device-connections"></a>

Create a connection between two devices in your global network using AWS Network Manager. The connection can be between a physical or virtual appliance and a third-party appliance in a VPC, or between physical appliances in an on-premises network. To create a connection the device must first be added to your global network. For the steps to add a device, see [Add a device using AWS Network Manager](nm-devices-add.md). You can also use an optional link to create the connection. For the steps to create a link, see [Add a link using AWS Network Manager](nm-site-link-add.md).

A connection is created for a specific global network and cannot be shared with other global networks.

**Topics**
+ [Create a connection](creating-a-connection.md)
+ [Update a connection](updating-a-connection.md)
+ [Delete a connection](deleting-a-connection.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
