---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/set-up-of-robust-network-configuration.html
---

# Robust network configuration
<a name="set-up-of-robust-network-configuration"></a>

The following diagram shows how an ideal network should be built to protect the network by filtering malicious traffic that comes into an organization and blocking traffic that is not supposed to reach the internet or specific sites on the internet. The network can also control traffic within the organization based on your organization's security requirements.

![Multi-AZ, multi-VPC architecture description follows the diagram.](https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/images/guide-img/734c65f3-3001-4321-a428-6ffbda3b44b0/images/42388669-8341-434e-adaa-9be1bbcbb798.png)

All inbound traffic that comes to services hosted by the organization is filtered by AWS WAF and AWS Network Firewall before the traffic reaches the Amazon Elastic Compute Cloud (Amazon EC2) instances. All outbound traffic from the organization is filtered by Network Firewall first before it reaches the destination. Amazon Route 53 manages all the DNS resolutions and provides a source to query DNS logs. AWS Transit Gateway elastic network interfaces help provide centralized networking.
