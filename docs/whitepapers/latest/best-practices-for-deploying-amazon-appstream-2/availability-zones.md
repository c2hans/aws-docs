---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/availability-zones.html
---

# Availability Zones
<a name="availability-zones"></a>

 An [https://aws.amazon.com/about-aws/global-infrastructure/regions_az/](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) (AZ) is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

 Amazon WorkSpaces Applications requires only one subnet for a fleet to launch in. The best practice is to configure a minimum of two Availability Zones, one subnet per unique Availability Zone. To optimize fleet auto scaling, use more than two Availability Zones. Scaling horizontally has the added benefit of adding IP space in subnets for growth, which is covered in the following Subnet sizing section of this document. The [https://aws.amazon.com/console/](https://aws.amazon.com/console/) provides for only two subnets to be specified during the creation of a fleet. Use the [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-fleet.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-fleet.html) (AWS CLI) or AWS CloudFormation to allow for more than two [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html).

## Subnet sizing
<a name="subnet-sizing"></a>

 Dedicate subnets to WorkSpaces Applications fleets to allow for flexibility in routing policies, and Network Access Control List. Stacks will likely have separate resource requirements. For example, WorkSpaces Applications Stacks can have isolation requirements giving way to separate rule sets. When several Amazon WorkSpaces Applications fleets use the same subnets, ensure the sum of all fleets’ **Maximum Capacity** doesn’t exceed the total number of IP addresses available.

 If the maximum capacity for all fleets in the same subnet could, or has, exceeded the total number of IP addresses available, migrate fleets to dedicated subnets. This prevents automatic scaling events from exhausting allocated IP space. If the total capacity for a fleet exceeds the allocated IP space of the subnets assigned, use the API, or AWS CLI “*[update fleet](https://docs.aws.amazon.com/cli/latest/reference/appstream/update-fleet.html)”* to assign more subnets. For more information, refer to [https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html).

 It is a best practice to scale out the number of subnets, sizing subnets accordingly while reserving capacity to grow in your VPC. Additionally, ensure that WorkSpaces Applications fleet maximums do not exceed the total IP space allocated by subnets. For every subnet in AWS, [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#vpc-sizing-ipv4](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#vpc-sizing-ipv4) when calculating the total amount of IP space. Using more than two subnets and scaling horizontally offers several benefits, such as:
+  Greater resilience from an Availability Zone failure
+  Greater throughput when automatic scaling fleet instances
+  More efficient usage of private IP addresses, avoiding IP burn

 When sizing subnets for Amazon WorkSpaces Applications, consider the total number of subnets, and the expected peak concurrency during peak utilization. This can be monitored using (`InUseCapacity`) plus reserved capacity (`AvailableCapacity`) for a fleet. In Amazon WorkSpaces Applications, the sum of consumed and available-to-be-consumed WorkSpaces Applications fleet instances is labeled `ActualCapacity`. To properly size total IP space, forecast the required `ActualCapacity`, and divide by the number of subnets, minus one subnet for resilience, assigned to the fleet.

 For example, if the anticipated maximum number of fleet instances at peak is 1000, and the business requirement is to be resilient in one Availability Zone failure, 3 x/23 subnets satisfy the technical and business requirements.
+  /23 = 512 Hosts — 5 Reserved = 507 fleet instances per subnet
+  3 subnets — 1 subnet = 2 subnets
+  2 subnets x 507 fleet instance per subnet = 1,014 fleet instances at peak

![Diagram showing reduced capacity when utilizing three subnets versus two subnets. The total changes from 1,521 Fleet instances to 1,014 Fleet instances.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/images/subnet-sizing.png)

 *Subnet sizing example*

 While 2 x /22 subnets would also satisfy resiliency, consider the following:
+  Instead of 1,536 IP addresses being reserved, using two AZs results in 2,048 IP addresses being reserved, wasting IP addresses that could go to other functions.
+  If one AZ becomes inaccessible, the ability to scale out fleet instances is limited by the throughput of an AZ. This can extend the duration of `PendingCapacity`.

## Subnet routing
<a name="subnet-routing"></a>

 It is a best practice to create private subnets for WorkSpaces Applications instances, routing to the public internet through a centralized VPC for outbound traffic. Inbound traffic for the WorkSpaces Applications session streaming is handled through Amazon WorkSpaces Applications service via Streaming Gateways: you do not need to configure public subnets for this.

## Intra-Region connectivity
<a name="intra-region-connectivity"></a>

 For WorkSpaces Applications fleet instances joined to an Active Directory Domain, configure Active Directory Domain Controllers in a Shared Services VPC in each AWS Region. Sources for Active Directory can be either [https://docs.aws.amazon.com/cli/latest/reference/appstream/create-fleet.html](https://docs.aws.amazon.com/cli/latest/reference/appstream/create-fleet.html)-based Domain Controllers or [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html). Routing between the shared services and WorkSpaces Applications VPCs can be either through a [https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html) or a [https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html). Although transit gateways solve the complexity of routing at scale, there are a number of reasons why VPC peering is preferable in most settings:
+  VPC peering is a direct connection between the two VPCs (no extra hop).
+  There is no hourly charge, just the standard data transfer rate between Availability Zones.
+  There is no limit on bandwidth.
+  Support for accessing Security Groups between VPCs.

 This is especially true if WorkSpaces Applications instances connect to application infrastructure and/or file servers with large datasets in a shared service VPC. By optimizing the path to these commonly accessed resources, VPC peering connection is preferred, even in designs where all other VPC and internet routing are performed via transit gateway.

## Outbound internet traffic
<a name="outbound-internet-traffic"></a>

 While routing directly to shared services is mostly optimized through a peering connection, outbound traffic for WorkSpaces Applications can be designed by [https://aws.amazon.com/blogs/networking-and-content-delivery/creating-a-single-internet-exit-point-from-multiple-vpcs-using-aws-transit-gateway/](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-a-single-internet-exit-point-from-multiple-vpcs-using-aws-transit-gateway/). In a multi-VPC design, it is a standard practice to have a dedicated VPC that controls all outgoing internet traffic. With this configuration, Transit Gateways have greater flexibility, and control of routing over standard routing tables attached to subnets. This design also supports transitive routing without additional complexity, and removes the need for redundant network address translation (NAT) gateways, or NAT instances in each VPC.

 Once all outbound internet traffic is centralized into a singular VPC, NAT gateways or NAT instances are a common design choice. To determine which is best for your organization, view the administration guide for [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html). [https://aws.amazon.com/network-firewall/](https://aws.amazon.com/network-firewall/) can extend protection beyond security group and network access control levels by protecting at the route level and offering stateless and stateful rules from layers 3 through 7 in the [https://en.wikipedia.org/wiki/OSI_model](https://en.wikipedia.org/wiki/OSI_model). For more information, refer to [https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/). If your organization has chosen a third-party product that performs advanced features such as URL filtering, deploy the service into your outbound internet VPC. This can replace NAT gateways or NAT instances. Follow the guidelines provided by the third-party vendor.

## On-premises
<a name="on-premises"></a>

 When connectivity to on-premises resources is required, especially for WorkSpaces Applications instances joined to Active Directory, establish a highly [https://aws.amazon.com/directconnect/resiliency-recommendation/](https://aws.amazon.com/directconnect/resiliency-recommendation/).
