---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/transit-gateway.html
---

# Transit gateway configuration
<a name="transit-gateway"></a>

In the AWS Region where the most AWS resources will be provisioned or applications deployed, create a transit gateway in the network account. When you create the transit gateway, clear the default route table propagation and association. Instead, you will attach and propagate routes in specific transit gateway route tables based on the type of VPC.

For this transit gateway, create three different transit gateway route tables:
+ Inbound VPC transit gateway route table:
  + Association – All VPC attachments whose traffic must be inspected, except for the outbound and firewall VPCs.
  + Propagation – Static route with destination `0.0.0.0/0` pointing out to the firewall VPC attachment.
+ Firewall inspection transit gateway route table:
  + Association – Firewall VPC gateway attachment.
  + Propagation – In the firewall VPC transit gateway route table, configure propagation to route traffic from the firewall VPC to respective VPC attachments. To route traffic to internet after inspection, add a static route with destination `0.0.0.0/0` pointing to the outbound VPC.
+ Outbound transit gateway route table:
  + Association – Associate outbound VPC attachment in this route table.
  + Propagation – Create a static route with destination `0.0.0.0/0` pointing out to the firewall VPC gateway attachment.

|
|
| Note: The network account is dedicated to configuring network-related services and components. Don't deploy any additional applications or services in the network account. |
| --- |

The following diagram shows how the traffic from child account VPCs will be routed to and from the centralized network account and the internet or other VPCs.

![Centralized transit gateway connects to spoke accounts through transit gateway attachments.](https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/images/guide-img/734c65f3-3001-4321-a428-6ffbda3b44b0/images/6ec9fa0a-33f5-490b-9b2b-f8431f73a8bc.png)
