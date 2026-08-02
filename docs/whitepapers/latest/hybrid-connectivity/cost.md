---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/cost.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost
<a name="cost"></a>

## Definition
<a name="definition-cost"></a>

 In the cloud, the cost of hybrid connectivity includes the cost of provisioned resources and usage. Cost of provisioned resources is measured in units of time, usually hourly. Usage is for data transfer and processing usually measured to in gigabytes (GB). Other costs include the cost of connectivity to the AWS network point of presence. If your network is within the same colocation facility, it might be as little as the cost of a cross connect. If your network is in a different location, there will be a service provider or APN Direct Connect partner costs involved.

## Key questions
<a name="key-questions-cost"></a>
+  How much data do you anticipate sending into AWS per month from your facility and from the internet?
+  How much data do you anticipate sending from AWS per month to your facility and to the internet?
+  How often will these amounts change?
+  What changes in a failure scenario?

## Capabilities to consider
<a name="capabilities-to-consider-cost"></a>

 If you have bandwidth-heavy workloads that you wish to run on AWS, AWS Direct Connect can reduce your network costs into and out of AWS in two ways. First, by transferring data to and from AWS directly, you can reduce your bandwidth costs paid to your internet service provider. Second, all data transferred over your dedicated connection is charged at the reduced AWS Direct Connect data transfer rate, rather than internet data transfer rates – see the [Direct Connect pricing page](https://aws.amazon.com/directconnect/pricing/) for details.

 AWS Direct Connect allows the use of AWS Direct Connect SiteLink to interconnect your sites using the AWS backbone – see [the SiteLink launch blog](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-direct-connect-sitelink/) for more information. Leveraging this capability incurs normal Direct Connect data transfer costs, along with a charge per hour SiteLink is enabled. You can enable and disable SiteLink on-demand, and it may be a good option for failure scenarios involving the internet or private network connectivity.

 If you are using a network service provider for connectivity between on-premises and a Direct Connect location, your ability and the time needed to change your bandwidth commitments is based on your contract with the service provider.

 The AWS backbone can deliver your traffic to any AWS Region except China from any AWS network point of presence. This capability has many technical benefits over using the internet to access remote AWS Regions, but has a cost – see the [EC2 Data Transfer pricing page](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer) for details. If there is an [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/pricing/) in the traffic path, it adds data processing cost per GB, however if using inter-region peering between two Transit Gateways, you are only billed once for the Transit Gateway data processing.

 Optimal application design keeps data processing within AWS and minimizes unnecessary data egress charges. Data ingress to AWS is free.

**Note**
As part of the overall connectivity solution, in addition to the AWS connection cost, you should also consider cost of the end-to-end connectivity including service provider cost, cross connects, racks, and equipment within DX location (if required).

 If you are not sure if you should use the internet or a private connection, calculate a breakeven point where AWS Direct Connect becomes less expensive than using the internet. If the volume of data means that AWS Direct Connect is less expensive, and you require permanent connectivity, AWS Direct Connect is the optimal connectivity choice.

 If the connectivity is temporary and the internet meets other requirements, it can be cheaper to use AWS S2S VPN over the internet due to the elasticity of the internet. Note this requires that you have sufficient internet connectivity from your on-premises network.

 If you are within a facility which has AWS Direct Connect (the list is [available on the Direct Connect website](https://aws.amazon.com/directconnect/locations/)), you can establish a cross-connect to AWS. This means using dedicated connections at 1,10, or 100Gbps. AWS Direct Connect partners offer more bandwidth options and smaller capacities, which may optimize your connectivity cost. For example, you can start at a 50 Mbps Hosted Connection versus a 1 Gbps Dedicated Connection.

 With AWS Transit Gateway, you can share your VPN and Direct Connect connections with many VPCs. While you are charged for the number of connections that you make to the AWS Transit Gateway per hour and the amount of traffic that flows through AWS Transit Gateway, it simplifies management and reduces the number of VPN connections and VIFs required. The benefits and cost savings of lower operational overhead can easily outweigh the additional cost of data processing. Optionally, you can consider a design where AWS Transit Gateway is in the traffic path to most VPCs, but not all. This approach avoids the AWS Transit Gateway data processing fees for use cases where you need to transfer large amounts of data into AWS. Refer to the Connectivity Models section for further details on this design. Another approach is to combine AWS Direct Connect as a primary path with AWS S2S VPN over the internet as backup/failover path. While technically feasible and very cost effective, this solution has technical downsides (discussed in the Reliability section of this whitepaper) and can be more difficult to manage. AWS [doesn’t recommend this for highly critical or critical workloads](https://aws.amazon.com/directconnect/resiliency-recommendation/).

 The final approach is a customer-managed VPN or SD-WAN deployed in Amazon EC2 instance(s). This can be cheaper at scale if there are tens to hundreds of site when compared to AWS S2S VPN. However, there is management overhead, licensing costs, and EC2 resource cost for each virtual appliance to consider.

## Decision matrix
<a name="decision-matrix"></a>

*Table 3 – Example Corp. Automotive connectivity design inputs*

|  Category  |  Customer-managed VPN or SD-WAN  |  AWS S2S VPN  |  AWS Accelerated S2S VPN  |  AWS Direct Connect Hosted Connection  |  AWS Direct Connect Dedicated Connection  |
| --- | --- | --- | --- | --- | --- |
|  Requires internet connection  |  Yes  |  Yes  |  Yes  |  No  |  No  |
|  Provisioned resources cost  |  EC2 instance and software licensing  |  [AWS S2S VPN](https://aws.amazon.com/vpn/pricing/)  |  [AWS S2S VPN](https://aws.amazon.com/vpn/pricing/) and [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/pricing/)  |  [Applicable capacity slice of port cost](https://aws.amazon.com/directconnect/pricing/)  |  [Dedicated port cost](https://aws.amazon.com/directconnect/pricing/)  |
|  Data transfer cost  |  Internet rate  |  Internet rate or Direct Connect rate  |  Internet with data transfer premium  |  Direct Connect rate  |  Direct Connect rate  |
|  Transit Gateway  |  Optional  |  Optional  |  Required  |  Optional  |  Optional  |
|  AWS Data processing cost  |  N/A  |  Only with AWS Transit Gateway  |  Yes  |  Only with AWS Transit Gateway  |  Only with AWS Transit Gateway  |
|  Can be used over AWS Direct Connect?  |  Yes  |  Yes  |  No  |  N/A  |  N/A  |
