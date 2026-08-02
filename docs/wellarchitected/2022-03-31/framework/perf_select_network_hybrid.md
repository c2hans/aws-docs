---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_select_network_hybrid.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP03 Choose appropriately sized dedicated connectivity or VPN for hybrid workloads
<a name="perf_select_network_hybrid"></a>

 When a common network is required to connect on-premises and cloud resources in AWS, ensure that you have adequate bandwidth to meet your performance requirements. Estimate the bandwidth and latency requirements for your hybrid workload. These numbers will drive the sizing requirements for AWS Direct Connect or your VPN endpoints.

 **Desired outcome:** When deploying a workload that will need hybrid network connectivity, you have multiple configuration options for connectivity, such as managed and non-managed VPNs or Direct Connect. Select the appropriate connection type for each workload while ensuring you have adequate bandwidth and encryption requirements between your location and the cloud.

 **Common anti-patterns:**
+  You only evaluate VPN solutions for your network encryption requirements.
+  You don’t evaluate backup or parallel connectivity options.
+  You use default configurations for routers, tunnels, and BGP sessions.
+  You fail to understand or identify all workload requirements (encryption, protocol, bandwidth and traffic needs).

 **Benefits of establishing this best practice:** Selecting and configuring appropriately sized hybrid network solutions will increase the reliability of your workload and maximize performance opportunities. By identifying workload requirements, planning ahead, and evaluating hybrid solutions you will minimize expensive physical network changes and operational overhead while increasing your time to market.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Develop a hybrid networking architecture based on your bandwidth requirements: Estimate the bandwidth and latency requirements of your hybrid applications. Based on your bandwidth requirements, a single VPN or Direct Connect connection might not be enough, and you must architect a hybrid setup to enable traffic load balancing across multiple connections. Direct connect may be required which offers more predictable and consistent performance due to its private network connectivity. It is great for production workloads that require consistent latency and almost zero jitter.

 AWS Direct Connect provides dedicated connectivity to the AWS environment, from 50 Mbps up to 10 Gbps. This gives you managed and controlled latency and provisioned bandwidth so your workload can connect easily and in a performant way to other environments. Using one of the AWS Direct Connect partners, you can have end-to-end connectivity from multiple environments, thus providing an extended network with consistent performance.

 The AWS Site-to-Site VPN is a managed VPN service for VPCs. When a VPN connection is created, AWS provides tunnels to two different VPN endpoints. With AWS Transit Gateway, you can simplify the connectivity between multiple VPCs and also connect to any VPC attached to AWS Transit Gateway with a single VPN connection. AWS Transit Gateway also enables you to scale beyond the 1.25Gbps IPsec VPN throughput limit by enabling equal cost multi-path (ECMP) routing support over multiple VPN tunnels.

 **Level of effort for the implementation plan: **There is a *high* level of effort to evaluate workload needs for hybrid networks and to implement hybrid networking solutions.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [Network Load Balancer ](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
+ [Networking Products with AWS](https://aws.amazon.com/products/networking/)
+ [Transit Gateway ](https://docs.aws.amazon.com/vpc/latest/tgw)
+ [Transitioning to latency-based Routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html)
+ [VPC Endpoints ](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)
+ [VPC Flow Logs ](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  [Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+  [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html)
+  [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
+  [Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

 **Related videos:**
+ [Connectivity to AWS and hybrid AWS network architectures (NET317-R1) ](https://www.youtube.com/watch?v=eqW6CPb58gs)
+ [Optimizing Network Performance for Amazon EC2 Instances (CMP308-R1) ](https://www.youtube.com/watch?v=DWiwuYtIgu0)
+  [AWS Global Accelerator](https://www.youtube.com/watch?v=lAOhr-5Urfk)
+  [Direct Connect* *](https://www.youtube.com/watch?v=DXFooR95BYc&t=6s)
+  [Transit Gateway Connect](https://www.youtube.com/watch?v=_MPY_LHSKtM&t=491s)
+  [VPN Solutions](https://www.youtube.com/watch?v=qmKkbuS9gRs)
+  [Security with VPN Solutions](https://www.youtube.com/watch?v=FrhVV9nG4UM)

 **Related examples:**
+  [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
+  [AWS Networking Workshops](https://networking.workshop.aws/)
