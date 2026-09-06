---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/networking.html
---

# Networking at the edge
<a name="networking"></a>

When you design solutions that use AWS edge infrastructure, such as AWS Outposts or Local Zones, you must carefully consider the network design. The network forms the foundation of connectivity for reaching workloads that are deployed in these edge locations, and is critical for ensuring low latency. This section outlines various aspects of hybrid edge connectivity.

## VPC architecture
<a name="vpc-architecture"></a>

A virtual private cloud (VPC) spans all Availability Zones in its AWS Region. You can seamlessly extend any VPC in the Region to Outposts or Local Zones by using the AWS console or the AWS Command Line Interface (AWS CLI) to add an Outpost or Local Zone subnet. The following examples show how to create subnets in AWS Outposts and Local Zones by using the AWS CLI:
+ **AWS Outposts**: To add an Outpost subnet to a VPC, specify the Amazon Resource Name (ARN) of the Outpost.

  ```
  aws ec2 create-subnet --vpc-id vpc-081ec835f3EXAMPLE \
  --cidr-block 10.0.0.0/24 \
  --outpost-arn arn:aws:outposts:us-west-2:11111111111:outpost/op-0e32example1 \
  --tag-specifications ResourceType=subnet,Tags=[{Key=Name,Value=my-ipv4-only-subnet}]
  ```

  For more information, see the [AWS Outposts documentation](https://docs.aws.amazon.com/outposts/latest/userguide/launch-instance.html#create-subnet).
+ **Local Zones**: To add a Local Zone subnet to a VPC, follow the same procedure that you use with Availability Zones, but specify the Local Zone ID (`<local-zone-name>` in the following example).

  ```
  aws ec2 create-subnet --vpc-id vpc-081ec835f3EXAMPLE \
  --cidr-block 10.0.1.0/24 \
  --availability-zone <local-zone-name> \
  --tag-specifications ResourceType=subnet,Tags=[{Key=Name,Value=my-ipv4-only-subnet}]
  ```

  For more information, see the [Local Zones documentation](https://docs.aws.amazon.com/local-zones/latest/ug/getting-started.html#getting-started-create-local-zone-subnet).

The following diagram shows an AWS architecture that includes Outpost and Local Zone subnets.

![AWS architecture with Outpost and Local Zone subnets.](http://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/images/guide-img/117f803b-a3ee-4c57-ae66-84b53da14c2b/images/01fae28a-fe72-4ab7-be27-e505f5a37b28.png)

## Edge to Region traffic
<a name="edge-to-region-traffic"></a>

When you design a hybrid architecture by using services such as Local Zones and AWS Outposts, consider both control flows and data traffic flows between the edge infrastructures and AWS Regions. Depending on the type of edge infrastructure, your responsibility might vary: Some infrastructures require you to manage the connection to the parent Region, whereas others handle this through the AWS global infrastructure. This section explores the control plane and data plane connectivity implications for Local Zones and AWS Outposts.

### AWS Outposts control plane
<a name="9999999999999999out--control-plane.d3f062f7-174f-51f3-8275-708ee75392e5"></a>

AWS Outposts provides a networking construct called a *service link*. The service link is a required connection between AWS Outposts and the selected AWS Region or parent Region (also referred to as *home Region*). It enables the management of the Outpost and the exchange of traffic between the Outpost and AWS Region. The service link uses an encrypted set of VPN connections to communicate with the home Region. You must provide connectivity between AWS Outposts and the AWS Region either through an internet link or an Direct Connect public virtual interface (public VIF), or through an Direct Connect private virtual interface (private VIF). For an optimal experience and resiliency, AWS recommends that you use redundant connectivity of at least 500 Mbps (1 Gbps is better) for the service link connection to the AWS Region. The minimum 500 Mbps service link connection allows you to launch Amazon EC2 instances, attach Amazon EBS volumes, and access AWS services such as Amazon EKS, Amazon EMR, and Amazon CloudWatch metrics. The network must support a maximum transmission unit (MTU) of 1,500 bytes between the Outpost and the service link endpoints in the parent AWS Region. For more information, see [AWS Outposts connectivity to AWS Regions](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html) in the Outposts documentation[.](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html)

![Service link for Outposts using Direct Connect (private VIF) and private connectivity.](http://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/images/guide-img/117f803b-a3ee-4c57-ae66-84b53da14c2b/images/4cbf732b-2a12-4e5b-afe7-779d6f05bb7b.png)

For information about creating resilient architectures for service links that use Direct Connect and the public internet, see the [Anchor connectivity](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/anchor-connectivity.html) section in the AWS whitepaper *AWS Outposts High Availability Design and Architecture Considerations*.

### AWS Outposts data plane
<a name="9999999999999999out--data-plane.3f51b816-3759-576a-a8a5-c601acc272e4"></a>

The data plane between AWS Outposts and the AWS Region is supported by the same service link architecture that is used by the control plane. The bandwidth of the data plane service link between AWS Outposts and the AWS Region should correlate with the amount of data that must be exchanged: The greater the data dependence, the greater the link bandwidth should be.

The bandwidth requirements vary depending on the following characteristics:
+ The number of AWS Outposts racks and capacity configurations
+ Workload characteristics such as AMI size, application elasticity, and burst speed needs
+ VPC traffic to the Region

The traffic between EC2 instances in AWS Outposts and EC2 instances in the AWS Region has an MTU of 1,300 bytes. We recommend that you discuss these requirements with an AWS hybrid cloud specialist before you propose an architecture that has co-dependencies between the Region and AWS Outposts.

### Local Zones data plane
<a name="9999999999999999lzs--data-plane.a5da91a5-80f6-5af0-b45a-2c9dda672928"></a>

The data plane between Local Zones and the AWS Region is supported through the AWS global infrastructure. The data plane is extended through a VPC from the AWS Region to a Local Zone. Local Zones also provide a high-bandwidth, secure connection to the AWS Region, and enables you to seamlessly connect to the full range of Regional services through the same APIs and tool sets.

The following table shows the connection options and associated MTUs.

|
|
| **From** | **To** | **MTU** |
| --- |--- |--- |
| Amazon EC2 in Region | Amazon EC2 in Local Zones | 1,300 bytes |
| Direct Connect | Local Zones | 1,468 bytes |
| Internet gateway | Local Zones | 1,500 bytes |
| Amazon EC2 in Local Zones | Amazon EC2 in Local Zones | 9,001 bytes |

Local Zones use the AWS global infrastructure to connect with AWS Regions. The infrastructure is fully managed by AWS, so you don't have to set up this connectivity. We recommend that you discuss your Local Zones requirements and considerations with an AWS hybrid cloud specialist before you design any architecture that has co-dependencies between the Region and Local Zones.

## Edge to on-premises traffic
<a name="edge-to-on-premises-traffic"></a>

AWS hybrid cloud services are designed to address use cases that require low latency, local data processing, or data residency compliance. The network architecture for accessing this data is important, and it depends on whether your workload is running in AWS Outposts or Local Zones. Local connectivity also requires a well-defined scope, as discussed in the following sections.

### AWS Outposts local gateway
<a name="9999999999999999out--local-gateway.bcc0c0f1-a989-5f61-9765-71f6a6a45e2d"></a>

The local gateway (LGW) is a core component of the AWS Outposts architecture. The local gateway enables connectivity between your Outpost subnets and your on-premises network. The primary role of an LGW is to provide connectivity from an Outpost to your local on-premises network. It also provides connectivity to the internet through your on-premises network through either [direct VPC routing](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#direct-vpc-routing) or [customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing).
+ **Direct VPC routing** uses the private IP address of the instances in your VPC to facilitate communication with your on-premises network. These addresses are advertised to your on-premises network with Border Gateway Protocol (BGP). Advertisement to BGP is only for the private IP addresses that belong to the subnets on your Outpost rack. This type of routing is the default mode for AWS Outposts. In this mode, the local gateway doesn't perform NAT for instances, and you do not need to assign Elastic IP addresses to your EC2 instances. The following diagram shows an AWS Outposts local gateway that uses direct VPC routing.

![Outposts local gateway with direct VPC mode.](http://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/images/guide-img/117f803b-a3ee-4c57-ae66-84b53da14c2b/images/74ee0008-583c-4bc4-af71-96913c6e54ad.png)

+ With **customer-owned IP** addresses, you can provide an address range, known as a *customer-owned IP (CoIP) address pool*, which supports overlapping CIDR ranges and other network topologies. When you choose a CoIP, you must create an address pool, assign it to the local gateway route table, and advertise these addresses back to your network through BGP. CoIP addresses provide local or external connectivity to resources in your on-premises network. You can assign these IP addresses to resources on your Outpost, such as EC2 instances, by allocating a new Elastic IP address from the CoIP, and then assigning it to your resource. The following diagram shows an AWS Outposts local gateway that uses CoIP mode.

![Outposts local gateway with COIP mode.](http://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/images/guide-img/117f803b-a3ee-4c57-ae66-84b53da14c2b/images/c43a6528-7077-4746-bf3b-781d84293bce.png)

Local connectivity from AWS Outposts to a local network requires some parameter configurations, such as enabling the BGP routing protocol and advertising prefixes between the BGP peers. The MTU that can be supported between your Outpost and local gateway is 1,500 bytes. For more information, contact an AWS hybrid cloud specialist or review the [AWS Outposts documentation](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html).

### Local Zones and the internet
<a name="9999999999999999lzs--and-the-internet.07f44a5c-122a-5294-a205-8c5a7652e1a4"></a>

Industries that require low-latency or local data residency (examples include gaming, live streaming, financial services, and the government) can use Local Zones to deploy and provide their applications to end users over the internet. During the deployment of a Local Zone, you must allocate public IP addresses for use in a Local Zone. When you allocate Elastic IP addresses, you can specify the location from which the IP address is advertised. This location is called a *network border group*. A network border group is a collection of Availability Zones, Local Zones, or AWS Wavelength Zones from which AWS advertises a public IP address. This helps ensure minimum latency or physical distance between the AWS network and the users who access the resources in these Zones.

To expose an Amazon EC2-hosted workload in a Local Zone to the internet, you can enable the **Auto-assign Public IP** option when you launch the EC2 instance. If you use an Application Load Balancer, you can define it as internet-facing so that public IP addresses assigned to the Local Zone can be propagated by the border network that's associated with the Local Zone. In addition, when you use Elastic IP addresses, you can associate one of these resources with an EC2 instance after its launch. When you send traffic through an internet gateway in Local Zones, the same [instance bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) specifications used by the Region are applied. Local Zone network traffic goes directly to the internet or to points of presence (PoPs) without traversing the Local Zone's parent Region, to enable access to low-latency computing.

Local Zones provide the following connectivity options over the internet:
+ Public access: Connects workloads or virtual appliances to the internet by using Elastic IP addresses through an internet gateway.
+ Outbound internet access: Enables resources to reach public endpoints through network address translation (NAT) instances or virtual appliances with associated Elastic IP addresses, without direct internet exposure.
+ VPN connectivity: Establishes private connections by using Internet Protocol Security (IPsec) VPN through virtual appliances with associated Elastic IP addresses.

For more information, see [Connectivity options for Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity.html) in the Local Zones documentation.

### Local Zones and Direct Connect
<a name="9999999999999999lzs--and-9999999999999999aws-dc-.c0afae40-e09d-5a49-8b01-ccbc275f8269"></a>

Local Zones also support Direct Connect, which lets you route your traffic over a private network connection. For more information, see [Direct Connect in Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity-direct-connect.html) in the Local Zones documentation.

### Local Zones and transit gateways
<a name="9999999999999999lzs--and-transit-gateways.c4fc4421-6958-5b7c-8d7b-25c48d93951f"></a>

AWS Transit Gateway doesn't support direct VPC attachments to Local Zone subnets. However, you can connect to Local Zone workloads by creating Transit Gateway attachments in the parent Availability Zone subnets of the same VPC. This configuration enables interconnectivity between multiple VPCs and your Local Zone workloads. For more information, see [Transit gateway connection between Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity-transit-gateway-lzs.html) in the Local Zones documentation.

### Local Zones and VPC peering
<a name="9999999999999999lzs--and-vpc-peering.e66e7850-2451-5480-844e-9f11d6c9f96b"></a>

You can extend any VPC from a parent Region into a Local Zone by creating a new subnet and assigning it to the Local Zone. VPC peering can be established between VPCs that are extended to Local Zones. When the peered VPCs are in the same Local Zone, traffic stays within the Local Zone and does not hairpin through the parent Region.
