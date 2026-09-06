---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_network_protection_layered.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC05-BP02 Control traffic at all layers
<a name="sec_network_protection_layered"></a>

  When architecting your network topology, you should examine the connectivity requirements of each component. For example, if a component requires internet accessibility (inbound and outbound), connectivity to VPCs, edge services, and external data centers.

 A VPC allows you to define your network topology that spans an AWS Region with a private IPv4 address range that you set, or an IPv6 address range AWS selects. You should apply multiple controls with a defense in depth approach for both inbound and outbound traffic, including the use of security groups (stateful inspection firewall), Network ACLs, subnets, and route tables. Within a VPC, you can create subnets in an Availability Zone. Each subnet can have an associated route table that defines routing rules for managing the paths that traffic takes within the subnet. You can define an internet routable subnet by having a route that goes to an internet or NAT gateway attached to the VPC, or through another VPC.

 When an instance, Amazon Relational Database Service(Amazon RDS) database, or other service is launched within a VPC, it has its own security group per network interface. This firewall is outside the operating system layer and can be used to define rules for allowed inbound and outbound traffic. You can also define relationships between security groups. For example, instances within a database tier security group only accept traffic from instances within the application tier, by reference to the security groups applied to the instances involved. Unless you are using non-TCP protocols, it shouldn’t be necessary to have an Amazon Elastic Compute Cloud(Amazon EC2) instance directly accessible by the internet (even with ports restricted by security groups) without a load balancer, or [CloudFront](https://aws.amazon.com/cloudfront). This helps protect it from unintended access through an operating system or application issue. A subnet can also have a network ACL attached to it, which acts as a stateless firewall. You should configure the network ACL to narrow the scope of traffic allowed between layers, note that you need to define both inbound and outbound rules.

 Some AWS services require components to access the internet for making API calls, where [AWS API endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) are located. Other AWS services use [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) within your Amazon VPCs. Many AWS services, including Amazon S3 and Amazon DynamoDB, support VPC endpoints, and this technology has been generalized in [AWS PrivateLink](https://aws.amazon.com/privatelink/). We recommend you use this approach to access AWS services, third-party services, and your own services hosted in other VPCs securely. All network traffic on AWS PrivateLink stays on the global AWS backbone and never traverses the internet. Connectivity can only be initiated by the consumer of the service, and not by the provider of the service. Using AWS PrivateLink for external service access allows you to create air-gapped VPCs with no internet access and helps protect your VPCs from external threat vectors. Third-party services can use AWS PrivateLink to allow their customers to connect to the services from their VPCs over private IP addresses. For VPC assets that need to make outbound connections to the internet, these can be made outbound only (one-way) through an AWS managed NAT gateway, outbound only internet gateway, or web proxies that you create and manage.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Control network traffic in a VPC: Implement VPC best practices to control traffic.
  +  [Amazon VPC security](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html)
  +  [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)
  +  [Amazon VPC security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
  +  [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
+  Control traffic at the edge: Implement edge services, such as Amazon CloudFront, to provide an additional layer of protection and other features.
  +  [Amazon CloudFront use cases](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html)
  +  [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
  +  [AWS Web Application Firewall (AWS WAF)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-section.html)
  +  [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
  +  [Amazon VPC Ingress Routing](https://aws.amazon.com/about-aws/whats-new/2019/12/amazon-vpc-ingress-routing-insert-virtual-appliances-forwarding-path-vpc-traffic/)
+  Control private network traffic: Implement services that protect your private traffic for your workload.
  +  [Amazon VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
  +  [Amazon VPC Endpoint Services (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html)
  +  [Amazon VPC Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
  +  [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
  +  [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
  +  [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/user-getting-started.html)
  +  [Amazon S3 Access Points](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-section.html)
+  [Amazon Inspector](https://aws.amazon.com/inspector)
+  [Getting started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)

 **Related videos:**
+  [AWS Transit Gateway reference architectures for many VPCs](https://youtu.be/9Nikqn_02Oc)
+  [Application Acceleration and Protection with Amazon CloudFront, AWS WAF, and AWS Shield](https://youtu.be/0xlwLEccRe0)

 **Related examples:**
+  [Lab: Automated Deployment of VPC](https://www.wellarchitectedlabs.com/Security/200_Automated_Deployment_of_VPC/README.html)
