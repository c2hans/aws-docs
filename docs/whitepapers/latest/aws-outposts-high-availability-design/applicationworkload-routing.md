---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/applicationworkload-routing.html
---

# Application/workload routing
<a name="applicationworkload-routing"></a>

There are two paths out of the Outpost for application workloads:
+ The service link path: Consider that application traffic will compete with Outposts control plane traffic, in addition to limiting the [MTU to 1300 bytes](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html#service-links).
+ The local gateway (LGW) path: Consider that the customer's local network allows access to both applications that are on-premises and also in the AWS Region.

You configure the Outpost subnet route tables to control which path to take to reach destination networks. Routes pointed to the LGW will direct traffic out the Local Gateway and to the on-premises network. Routes pointed to the services and resources in the Region, such as Internet Gateway, NAT Gateway, Virtual Private Gateway, and TGW, will use [service link](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html) to reach these targets. If you have a VPC peering connection with multiple VPCs on the same Outpost, the traffic between the VPCs remains on the Outpost and doesn't use the service link back to the Region. For information on VPC peering, see [Connect VPCs using VPC peering](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html) in the *Amazon VPC User Guide*.

![Diagram showing a visualization of the Outpost service link and LGW network paths](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/outpost-service-link-and-lgw-network-paths.png)

 You should take care when planning application routing to consider both normal operation and limited routing and service availability during network failures. The Service Link path is not available when an Outpost is disconnected from the Region.

 You should provision diverse paths and configure dynamic routing between the Outpost LGW and your critical on-premises applications, systems and users. Redundant network paths allow the network to route traffic around failures and ensure that on-premises resources will be able to communicate with workloads running on the Outpost during partial network failures.

 Outpost VPC route configurations are static. You configure subnet routing tables through the AWS Management Console, CLI, APIs, and other Infrastructure as Code (IaC) tools; however, you will not be able modify the subnet routing tables during a disconnect event. You will have to reestablish connectivity between the Outpost and the Region to update the route tables. Use the same routes for normal operations as you plan to use during disconnect events.

 Resources on the Outpost can reach the internet via the service link and an Internet Gateway (IGW) in the Region or via the Local Gateway (LGW) path. Routing internet traffic over the LGW path and the on-premises network allows you to use existing on-premises internet ingress/egress points and may provide lower latency, higher MTUs, and reduced AWS data egress charges when compared to using the service link path to an IGW in the Region.

 If your application must run on-premises and it needs to be accessible from the public internet, you should route the application traffic over your on-premises internet connection(s) to the LGW to reach the resources on the Outpost.

 While you can configure subnets on an Outpost like public subnets in the Region, this may be an undesirable practice for most use cases. Inbound internet traffic will come in through the AWS Region and be routed over the service link to the resources running on the Outpost.

 The response traffic will in turn be routed over the service link and back out through the AWS Region’s internet connections. This traffic pattern may add latency and will incur data egress charges as traffic leaves the Region on its way to the Outpost and as return traffic comes back through the Region and egresses out to the internet. If your application can run in the Region, the Region is the best place to run it.

 Traffic between VPC resources (in the same VPC) will always follow the local VPC CIDR route and be routed between subnets by the implicit VPC routers.

 For example, traffic between an EC2 instance running on the Outpost and a VPC Endpoint in the Region will always be routed over the service link.

![Diagram showing local VPC routing through the implicit routers](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/local-vpc-routing-through-implicit-routers.png)

## Recommended practices for application/workload routing
<a name="recommended-practices-for-applicationworkload-routing"></a>
+  Use the Local Gateway (LGW) path instead of the service link path where possible.
+  Route internet traffic over the LGW path.
+  Configure the Outpost subnet routing tables with a standard set of routes – they will be used for both normal operations and during disconnect events.
+  Provision redundant network paths between the Outpost LGW and critical on-premises application resources. Use dynamic routing to automate traffic redirection around on-premises network failures.
