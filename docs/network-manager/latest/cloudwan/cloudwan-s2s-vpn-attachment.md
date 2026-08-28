---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-s2s-vpn-attachment.html
---

# Site-to-Site VPN attachments in AWS Cloud WAN
<a name="cloudwan-s2s-vpn-attachment"></a>

Attaching a Site-to-Site VPN connection to your core network edge, first requires that you create a Site-to-Site VPN connection with **Target Gateway Type** set to **Not Associated**. See [Create an AWS Cloud WAN Site-to-Site VPN attachment](https://docs.aws.amazon.com/vpn/latest/s2svpn/create-cwan-vpn-attachment.html) in the *AWS Site-to-Site VPN User Guide*.

**Note**
 Your Site-to-Site VPN must be attached to a core network before you can start configuring a customer gateway. AWS doesn't provision these endpoints until the Site-to-Site VPN is attached to the core network.
A Site-to-Site VPN attachment must be created in the same AWS account that owns the core network.

**Topics**
+ [Create a Site-to-Site VPN attachment](cloudwan-vpn-attachment-add.md)
+ [View or edit a Site-to-Site VPN attachment](cloudwan-attachments-viewing-editing-vpn.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
