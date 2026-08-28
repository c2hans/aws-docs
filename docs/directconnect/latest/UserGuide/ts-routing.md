---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/ts-routing.html
---

# Troubleshoot routing issues
<a name="ts-routing"></a>

Consider a situation where your virtual interface is up and you've established a BGP peering session. If you cannot route traffic over the virtual interface, use the following steps to troubleshoot the issue:

1. Ensure that you are advertising a route for your on-premises network prefix over the BGP session. For a private virtual interface, this can be a private or public network prefix. For a public virtual interface, this must be your publicly routable network prefix.

1. For a private virtual interface, ensure that your VPC security groups and network ACLs allow inbound and outbound traffic for your on-premises network prefix. For more information, see [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) and [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html) in the *Amazon VPC User Guide*.

1. For a private virtual interface, ensure that your VPC route tables have prefixes pointing to the virtual private gateway to which your private virtual interface is connected. For example, if you prefer to have all your traffic routed towards your on-premises network by default, you can add the default route (0.0.0.0/0 or ::/0) with the virtual private gateway as the target in your VPC route tables.
   + Alternatively, enable route propagation to automatically update routes in your route tables based on your dynamic BGP route advertisement. You can have up to 100 propagated routes per route table. This limit cannot be increased. For more information, see [Enabling and Disabling Route Propagation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#EnableDisableRouteProp) in the *Amazon VPC User Guide*.

1. If the above steps do not resolve your routing issues, [contact AWS Support](https://aws.amazon.com/support/createCase).

The following flow chart contains the steps to diagnose routing issues.

![Troubleshoot Direct Connect](http://docs.aws.amazon.com/directconnect/latest/UserGuide/images/troubleshooting-chart-routing.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
