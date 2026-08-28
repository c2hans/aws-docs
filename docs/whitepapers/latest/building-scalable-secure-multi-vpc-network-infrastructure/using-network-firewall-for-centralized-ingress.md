---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/using-network-firewall-for-centralized-ingress.html
---

# Using the AWS Network Firewall for centralized ingress
<a name="using-network-firewall-for-centralized-ingress"></a>

In this architecture, ingress traffic is inspected by AWS Network Firewall before reaching the rest of the VPCs. In this setup, traffic is split among all firewall endpoints deployed in the Edge VPC. You deploy a public subnet between the firewall endpoint and the Transit Gateway subnet. You can use an ALB or NLB, which contain IP targets in your spoke VPCs while handling Auto Scaling for targets behind them.

![A diagram depicting ingress traffic inspection using AWS Network Firewall](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/ingress-inspection-using-aws-nf.png)

 To simplify deployment and management of AWS Network Firewall in this model, AWS Firewall Manager can be used. Firewall Manager allows you to centrally administer your different firewalls by automatically applying protection you create in the centralized location to multiple accounts. Firewall Manager supports both distributed and centralized deployment models for Network Firewall. The blog post [How to deploy AWS Network Firewall by using AWS Firewall Manager](https://aws.amazon.com/blogs/security/how-to-deploy-aws-network-firewall-by-using-aws-firewall-manager/) provides more details on the model.

## Deep Packet Inspection (DPI) with AWS Network Firewall
<a name="deep-packet-inspection-with-network-firewall"></a>

 Network Firewall can perform deep packet inspection (DPI) on ingress traffic. Using a Transport Layer Security (TLS) certificate stored in AWS Certificate Manager (ACM), Network Firewall can decrypt packets, perform DPI, and re-encrypt packets. There are a few considerations for setting up DPI with Network Firewall. First, a trusted TLS certificate must be stored in ACM. Second, Network Firewall rules must be configured to correctly send packets for decryption and re-encryption. Refer to the blog post [TLS inspection configuration for encrypted traffic and AWS Network Firewall](https://aws.amazon.com/blogs/security/tls-inspection-configuration-for-encrypted-traffic-and-aws-network-firewall/) for more details.

## Key considerations for AWS Network Firewall in a centralized ingress architecture
<a name="key-considerations-66"></a>
+ Elastic Load Balancing in Edge VPC can only have IP addresses as target types, not a hostname. In the preceding figure, the targets are the private IPs of the Network Load Balancer in spoke VPCs. Using IP targets behind the ELB in the edge VPC results in the loss of Auto Scaling.
+ Consider using AWS Firewall Manager as a single pane of glass for your firewall endpoints.
+ This deployment model uses traffic inspection right as it enters the edge VPC, so it has the potential to reduce the overall cost of your inspection architecture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
