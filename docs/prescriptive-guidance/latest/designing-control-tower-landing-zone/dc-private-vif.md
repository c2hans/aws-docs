---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/dc-private-vif.html
---

# Direct Connect with private VIF over virtual private gateway
<a name="dc-private-vif"></a>

The following diagram shows how you can connect VPCs and on-premises environments through a virtual private gateway over a private VIF by using Direct Connect.

![Connecting VPCs and on-premises through virtual private gateway over private VIF](https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/images/guide-img/156d118c-ed00-4c5b-9a02-63c2673a3342/images/f7ddc0f0-8e26-4406-b63a-237f0824cab7.png)

Most large enterprise customers deploy resources within a large number of VPCs across multiple AWS Regions and require connectivity from data centers that are spread across geographies. By using an Direct Connect gateway, which is a global construct, you can use existing Direct Connect connections to connect to resources in VPCs across AWS Regions. You can associate up to 10 virtual private gateways (each attached to a VPC) in different AWS Regions, directly to an Direct Connect gateway. Alternatively, you can use Transit Gateway to attach to thousands of VPCs. For more information, see the [next section](dc-transit-vif.md).
