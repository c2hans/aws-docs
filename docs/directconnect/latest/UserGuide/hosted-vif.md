---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted-vif.html
---

# Hosted Direct Connect virtual interfaces
<a name="hosted-vif"></a>

To use your Direct Connect connection with another account, you can create a hosted virtual interface for that account. The owner of the other account must accept the hosted virtual interface to begin using it. A hosted virtual interface works the same as a standard virtual interface and can connect to public resources or a VPC.

You can use transit virtual interfaces with Direct Connect dedicated or hosted connections of any speed. Hosted connections support only one virtual interface.

To create a virtual interface, you need the following information:

| Resource | Required information |
| --- | --- |
| Connection | The Direct Connect connection or link aggregation group (LAG) for which you are creating the virtual interface. |
| Virtual interface name | A name for the virtual interface. |
| Virtual interface owner | If you're creating the virtual interface for another account, you need the AWS account ID of the other account. |
| (Private virtual interface only) Connection | For connecting to a VPC in the same AWS Region, you need the virtual private gateway for your VPC. The ASN for the Amazon side of the BGP session is inherited from the virtual private gateway. When you create a virtual private gateway, you can specify your own private ASN. Otherwise, Amazon provides a default ASN. For more information, see [Create a Virtual Private Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html#vpn-create-vpg) in the Amazon VPC User Guide. For connecting to a VPC through a Direct Connect gateway, you need the Direct Connect gateway. For more information, see [Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html). |
| VLAN | A unique virtual local area network (VLAN) tag that's not already in use on your connection. The value must be between 1 and 4094 and must comply with the Ethernet 802.1Q standard. This tag is required for any traffic traversing the Direct Connect connection. If you have a hosted connection, your AWS Direct Connect Partner provides this value. You can’t modify the value after you have created the virtual interface. |
| Peer IP addresses |  A virtual interface can support a BGP peering session for IPv4, IPv6, or one of each (dual-stack). Do not use Elastic IPs (EIPs) or Bring your own IP addresses (BYOIP) from the Amazon Pool to create a public virtual interface. You cannot create multiple BGP sessions for the same IP addressing family on the same virtual interface. The IP address ranges are assigned to each end of the virtual interface for the BGP peering session. [See the AWS documentation website for more details](http://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted-vif.html)  |
| Address family | Whether the BGP peering session will be over IPv4 or IPv6. |
| BGP information | [See the AWS documentation website for more details](http://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted-vif.html) |
| (Public virtual interface only) Prefixes you want to advertise |  Public IPv4 routes or IPv6 routes to advertise over BGP. You must advertise at least one prefix using BGP, up to a maximum of 1,000 prefixes.[See the AWS documentation website for more details](http://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted-vif.html) |
| (Private and transit virtual interfaces only) Jumbo frames | The maximum transmission unit (MTU) of packets over Direct Connect. The default is 1500. Setting the MTU of a virtual interface to 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. Jumbo frames apply only to propagated routes from Direct Connect. If you add static routes to a route table that point to your virtual private gateway, then traffic routed through the static routes is sent using 1500 MTU. To check whether a connection or virtual interface supports jumbo frames, select it in the Direct Connect console and find Jumbo frame capable on the virtual interface General configuration page. |
