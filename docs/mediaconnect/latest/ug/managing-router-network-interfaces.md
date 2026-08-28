---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/managing-router-network-interfaces.html
---

# Managing router network interfaces in MediaConnect
<a name="managing-router-network-interfaces"></a>

Router network interfaces control how the router communicates with the outside world. Router I/Os that connect to a public or VPC endpoints need a network interface, which determines how the router I/O connects to other resources and what security measures protect the connection. Note that router connections to MediaLive channels and MediaConnect flows are automatically managed and do not require a network interface.

You can work with two types of router network interface:
+ **Public network interfaces **- These allow communication over the public internet. They're ideal for connecting to external sources or destinations like cameras, encoders, and content delivery platforms. When using public interfaces, you must specify allowed IP addresses (CIDRs) for security purposes.
+ **VPC network interfaces** - These connect to resources within your Amazon Virtual Private Cloud (VPC), and provide private networking within AWS. VPC interfaces are best suited for connecting your router to other AWS services or resources within your VPC.

You can use the same router network interface for multiple inputs and outputs on your router. This allows you to simplify your network configuration and reduce the number of interfaces you need to maintain.

This chapter shows you everything you need to know about working with router network interfaces.

**Topics**
+ [Creating a router network interface in MediaConnect](creating-router-network-interfaces.md)
+ [Viewing router network interfaces in MediaConnect](viewing-router-network-interfaces.md)
+ [Updating a router network interface in MediaConnect](editing-router-network-interface.md)
+ [Deleting a router network interface in MediaConnect](deleting-router-network-interface.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
