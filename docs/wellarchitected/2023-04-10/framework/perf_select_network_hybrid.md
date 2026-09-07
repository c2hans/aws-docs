---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_network_hybrid.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP03 Choose appropriately sized dedicated connectivity or VPN for hybrid workloads
<a name="perf_select_network_hybrid"></a>

 When a common network is required to connect on-premises and cloud resources in AWS, verify that you have adequate bandwidth to meet your performance requirements. Estimate the bandwidth and latency requirements for your hybrid workload. These numbers will drive the sizing requirements for your connectivity options.

 **Desired outcome:** When deploying a workload that will need hybrid networking, you have multiple configuration options for connectivity, such as a dedicated connection or virtual private network (VPN). Select the appropriate connection type for each workload while verifying that you have adequate bandwidth and encryption requirements between your location and the cloud.

 **Common anti-patterns:**
+ You fail to understand or identify all workload requirements (bandwidth, latency, jitter, encryption and traffic needs).
+  You don’t evaluate backup or parallel connectivity options.

 **Benefits of establishing this best practice:** Selecting and configuring appropriately sized hybrid network solutions will increase the reliability of your workload and maximize performance opportunities. By identifying workload requirements, planning ahead, and evaluating hybrid solutions you will minimize expensive physical network changes and operational overhead while increasing your time to market.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Develop a hybrid networking architecture based on your bandwidth requirements. Estimate the bandwidth and latency requirements of your hybrid applications. Consider appropriate connectivity option between using a dedicated network connection or internet-based VPN.

Dedicated connection establishes network connection over private lines. It is suitable when you need high-bandwidth, low-latency while achieving consistent performance. VPN connection establishes secure connection over the internet. It is suitable when you need encrypted connection using an existing internet connection.

Based on your bandwidth requirements, a single VPN or dedicated connection might not be enough, and you must architect a hybrid setup to permit traffic load balancing across multiple connections.

 **Implementation steps**

1.  Estimate the bandwidth and latency requirements of your hybrid applications.

   1.  For existing apps that are moving to AWS, leverage the data from your internal network monitoring systems.

   1.  For new apps or existing apps for which you don’t have monitoring data, consult with the product owners to derive adequate performance metrics and provide a good user experience.

1.  Select dedicated connection or VPN as your connectivity option. Based on all workload requirements (encryption, bandwidth and traffic needs), you can either choose AWS Direct Connect or AWS Site-to-Site VPN (or both). The following diagram will help you choose the appropriate connection type.

   1.  If you consider dedicated connection, AWS Direct Connect may be required, which offers more predictable and consistent performance due to its private network connectivity. AWS Direct Connect provides dedicated connectivity to the AWS environment, from 50 Mbps up to 100 Gbps, using either dedicated connection or hosted connection. This gives you managed and controlled latency and provisioned bandwidth so your workload can connect efficiently to other environments. Using an AWS Direct Connect partners, you can have end-to-end connectivity from multiple environments, providing an extended network with consistent performance. AWS offers scaling direct connect connection bandwidth using either native 100 Gbps, Link Aggregation Group (LAG), or BGP Equal-cost multipath (ECMP).

   1.  If you consider VPN connection, an AWS managed VPN is the recommended option. The AWS Site-to-Site VPN provides a managed VPN service supporting Internet Protocol security (IPsec) protocol. When a VPN connection is created, each VPN connection includes two tunnels for high availability. With AWS Transit Gateway, you can simplify the connectivity between multiple VPCs and also connect to any VPC attached to AWS Transit Gateway with a single VPN connection. AWS Transit Gateway also allows you to scale beyond the 1.25Gbps IPsec VPN throughput limit by allowing equal cost multi-path (ECMP) routing support over multiple VPN tunnels.

![A flowchart that describes the options you should consider when determining if you need deterministic performance in your networking or not.](https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/images/deterministic-performance-flowchart.png)

 **Level of effort for the implementation plan:** High. There is significant effort in evaluating workload needs for hybrid networks and implementing hybrid networking solutions.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [Network Load Balancer ](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
+ [Networking Products with AWS](https://aws.amazon.com/products/networking/)
+ [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw)
+ [Transitioning to latency-based Routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html)
+ [VPC Endpoints ](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)
+ [VPC Flow Logs ](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+  [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html)
+  [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
+  [Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

 **Related videos:**
+ [Connectivity to AWS and hybrid AWS network architectures (NET317-R1) ](https://www.youtube.com/watch?v=eqW6CPb58gs)
+ [Optimizing Network Performance for Amazon EC2 Instances (CMP308-R1) ](https://www.youtube.com/watch?v=DWiwuYtIgu0)
+  [AWS Global Accelerator](https://www.youtube.com/watch?v=lAOhr-5Urfk)
+  [AWS Direct Connect](https://www.youtube.com/watch?v=DXFooR95BYc&t=6s)
+  [Transit Gateway Connect](https://www.youtube.com/watch?v=_MPY_LHSKtM&t=491s)
+  [VPN Solutions](https://www.youtube.com/watch?v=qmKkbuS9gRs)
+  [Security with VPN Solutions](https://www.youtube.com/watch?v=FrhVV9nG4UM)

 **Related examples:**
+  [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
+  [AWS Networking Workshops](https://networking.workshop.aws/)
