---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/tunnel-endpoint-lifecycle.html
---

# AWS Site-to-Site VPN tunnel endpoint lifecycle control
<a name="tunnel-endpoint-lifecycle"></a>

Tunnel endpoint lifecycle control provides control over the schedule of endpoint replacements, and can help minimize connectivity disruptions during AWS managed tunnel endpoint replacements. With this feature, you can choose to accept AWS managed updates to tunnel endpoints at a time that works best for your business. Use this feature if you have short-term business needs or can only support a single tunnel per VPN connection.

**Note**
In rare circumstances, AWS might apply critical updates to tunnel endpoints immediately, even if the tunnel endpoint lifecycle control feature is enabled.

**Topics**
+ [How tunnel endpoint lifecycle control works](#how-elc-works)
+ [Enable tunnel endpoint lifecycle control](enable-elc.md)
+ [Verify if tunnel endpoint lifecycle control is enabled](view-elc-status.md)
+ [Check for available updates](view-elc-updates.md)
+ [Accept a maintenance update](accept-update.md)
+ [Turn tunnel endpoint lifecycle control off](turn-elc-off.md)

## How tunnel endpoint lifecycle control works
<a name="how-elc-works"></a>

Turn on the tunnel endpoint lifecycle control feature for individual tunnels within a VPN connection. It can be enabled at the time of VPN creation or by modifying tunnel options for an existing VPN connection.

After tunnel endpoint lifecycle control is enabled, you will gain additional visibility into upcoming tunnel maintenance events in two ways:
+ You will receive AWS Health notifications for upcoming tunnel endpoint replacements.
+ The status of pending maintenance, along with the **Maintenance auto applied after** and **Last maintenance applied** timestamps, can be seen in the AWS Management Console or by using the [get-vpn-tunnel-replacement-status](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-vpn-tunnel-replacement-status.html) AWS CLI command.

When a tunnel endpoint maintenance is available, you will have the opportunity to accept the update at a time that is convenient for you, before the given **Maintenance auto applied after** timestamp.

If you do not apply updates before the **Maintenance auto applied after** date, AWS will automatically perform the tunnel endpoint replacement soon after, as part of the regular maintenance update cycle.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
