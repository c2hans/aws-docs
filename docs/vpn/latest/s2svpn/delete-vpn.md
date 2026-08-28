---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-vpn.html
---

# Delete an AWS Site-to-Site VPN connection and gateway
<a name="delete-vpn"></a>

If you no longer need an AWS Site-to-Site VPN connection, you can delete it. When you delete a Site-to-Site VPN connection, we do not delete the customer gateway or virtual private gateway that was associated with the Site-to-Site VPN connection. If you no longer need the customer gateway and virtual private gateway, you can delete them.

**Warning**
If you delete your Site-to-Site VPN connection and then create a new one, you must download a new configuration file and reconfigure the customer gateway device.

**Topics**
+ [Delete a VPN connection](delete-vpn-connection.md)
+ [Delete a customer gateway](delete-cgw.md)
+ [Detach and delete a virtual private gateway](delete-vgw.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
