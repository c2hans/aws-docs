---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/appendix-a-high-level-ha-architecture-for-software-vpn-instances.html
---

# Appendix A: High-Level HA architecture for software VPN instances
<a name="appendix-a-high-level-ha-architecture-for-software-vpn-instances"></a>

 Creating a fully resilient VPC connection for software VPN instances requires the setup and configuration of multiple VPN instances and a monitoring instance to monitor the health of the VPN connections.

![VPC with redundant VPN appliances across availability zones connecting to customer network.](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/high-level-software-vpn-ha.png)

* High-Level Software VPN HA *

 We recommend configuring your VPC route tables to leverage all VPN instances simultaneously by directing traffic from all of the subnets in one Availability Zone through its respective VPN instances in the same Availability Zone. Each VPN instance then provides VPN connectivity for instances that share the same Availability Zone.

## VPN monitoring
<a name="vpn-monitoring"></a>

 To monitor Software based VPN appliance you can create a VPN Monitor. The VPN monitor is a custom instance that you will need to run the VPN monitoring scripts. This instance is intended to run and monitor the state of VPN connection and VPN instances. If a VPN instance or connection goes down, the monitor needs to stop, terminate, or restart the VPN instance while also rerouting traffic from the affected subnets to the working VPN instance until both connections are functional again. Since customer requirements vary, AWS does not currently provide prescriptive guidance for setting up this monitoring instance. However, an example script for enabling [HA between NAT instances](https://aws.amazon.com/articles/2781451301784570) could be used as a starting point for creating an HA solution for Software VPN instances. We recommend that you think through the necessary business logic to provide notification or attempt to automatically repair network connectivity in the event of a VPN connection failure.

 Additionally, you can monitor the AWS Managed VPN tunnels using Amazon CloudWatch metrics, which collects data points from the VPN service into readable, near real-time metrics. Each VPN connection collects and publishes a variety of tunnel metrics to Amazon CloudWatch. These metrics allow you to monitor tunnel health, activity, and create automated actions.
