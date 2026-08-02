---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-site-to-site-vpn.html
---

# AWS Site-to-Site VPN
<a name="aws-site-to-site-vpn"></a>

 Amazon VPC provides the option of creating an IPsec VPN connection between your remote networks and Amazon VPC over the internet, as shown in the following figure.

![Diagram showing how to create an IPsec VPN connection between your remote networks and Amazon VPC over the internet.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-managed-vpn.png)

 Consider taking this approach when you want to take advantage of an AWS-managed VPN endpoint that includes automated redundancy and failover built into the AWS side of the VPN connection.

 The virtual private gateway also supports and encourages multiple user gateway connections so that you can implement redundancy and failover on your side of the VPN connection, as shown in the following figure.

![Diagram showing multiple user gateway connections.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/redundant-aws-site-to-site-vpn-connections.png)

 Both dynamic and static routing options are provided to give you flexibility in your routing configuration. Dynamic routing uses BGP peering to exchange routing information between AWS and these remote endpoints. With dynamic routing, you can also specify routing priorities, policies, and weights (metrics) in your BGP advertisements and influence the network path between your networks and AWS. It’s important to note that when you use BGP, both the IPsec and the BGP sessions must be terminated on the same user gateway device, so it must be capable of terminating both IPsec and BGP sessions.

## Additional resources
<a name="additional-resources"></a>
+  [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+  [Requirements for customer gateway devices](https://docs.aws.amazon.com/vpc/latest/adminguide/Introduction.html#CGRequirements)
+  [Customer gateway devices tested with Amazon VPC](https://docs.aws.amazon.com/vpc/latest/adminguide/Introduction.html#DevicesTested)
