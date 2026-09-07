---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/evaluating.html
---

# Evaluating network access options for SaaS offerings
<a name="evaluating"></a>

The metrics that are important to your organization will depend on who your customers are, your business strategy, and your organizational objectives. This guide presents metrics that you can use to choose a networking access approach, but you should prioritize those that meet the unique requirements of your use case.

## Evaluation metrics
<a name="evaluating-metrics"></a>

Some metrics are consistent across organizations and use cases, and these are the metrics that we can help you rate. The following are these metrics:
+ **Ease of integration** – How quickly and easily can you onboard new customers?
+ **Total cost of ownership (TCO)** – What is the cost structure? Beyond fixed and variable infrastructure costs, there are major additional cost considerations associated with operational overhead, dependency on experts, cost of implementing changes, and compliance. For more information, see the [Total cost of ownership](#evaluating-metrics-tco) section.
+ **Scalability** – Is your network access approach able to scale in order to support your company's growth? Scaling your customer base has important architectural and organizational considerations. Consider how you might scale to accommodate 5—100 times as many customers as you support today.
+ **Adaptability** – Can you implement changes easily? Changes might include a new application, a new capability, a different platform, or a different network.
+ **Network isolation** – How much of the network infrastructure are you exposing to your customers? Are you providing just the right degree of access, or are you exposing whole networks? If you isolate network resources early, it will be easier to provide security, privacy, and compliance assurances later.
+ **Observability** – What's your ability to detect service failure or degradation? How easy and fast is it to identify the problem? How quickly (and with what overhead) can you help your customers understand their points of failure and help them resolve it?
+ **Time to repair** – What's the lead time between the detection of a service failure or degradation and resuming operations? What are the factors that affect this ability?

Other metrics are unique to your organization or offering because they relate to your business operations, strategy, or goals. Only you can rate these metrics. The following are these metrics:
+ **Business model alignment** – What is your business model, and how well do individual access approaches align with it?
+ **Total addressable market (TAM)** – What is your current and future market, and how well is it covered by the network access approach?
+ **Return on investment (ROI)** – What improvements do you expect in profitability and margins? Are the expected financial benefits sufficient to meet your needs for adaptable and flexible service access?
+ **Regulatory compliance** – What kind of regulatory requirements apply, and in which market?
+ **Service-level agreements (SLAs)** – Do customers need your SaaS offering to be highly available? What sort of commitments are you contractually obliged to uphold?

## Total cost of ownership
<a name="evaluating-metrics-tco"></a>

This section explores total cost of ownership (TCO), which is one of the evaluation metrics used to compare the network access approaches. TCO is a composite metric consisting of fixed and variable infrastructure costs, operational overhead, specialist dependency, cost of change, and compliance costs.

The TCO rating for each network access approach might vary for your use case. For example, the *cost of change* for a SaaS provider with a simple web-service and five tenants differs from a SaaS provider with a complex, interconnected product portfolio and hundreds or thousands of tenants. Additionally, not all components have the same weight. For example, hiring a networking specialist is often more expensive than the infrastructure costs that support an individual deployment of your service. Use the values in the following table for initial orientation and as a reference point for further discussion.

|
|
| **Access approach** | **Fixed infrastructure costs** | **Variable infrastructure costs** | **Operational overhead** | **Specialist dependency** | **Cost of change** | **Compliance costs** |
| --- |--- |--- |--- |--- |--- |--- |
| **VPC peering** | None | None | High | Low | High | Medium |
| **AWS PrivateLink** | Low | Low | Low | None | Low | Low |
| **Amazon VPC Lattice** | Medium | Medium | Low | Low | Low | Low |
| **AWS Transit Gateway** | Medium | Medium | Low | Low | Low | Medium |
| **AWS Site-to-Site VPN** | Medium | High | High | Medium | Medium | Low |
| **AWS Direct Connect** | High | Medium | Medium | High | High | Low |
| **Public internet access** | Low | High | Medium | Low | Low | High |

### VPC peering costs
<a name="vpc-peering-costs.3d798a86-907f-5b1b-a8d7-7d0c9a635d79"></a>

There is no direct infrastructure cost associated with a VPC peering connection. When traffic stays within the same Availability Zone, there is no data transfer charge. However, operational overhead can be significant because management and complexity grow exponentially with each additional peering connection. Some basic understanding of networking is enough to set up a peering connection, but changes on the network are difficult to implement with more than a handful of peering connections. Compliance costs are slightly higher because both parties are exposing an entire VPC to each other, rather than individual services.

### AWS PrivateLink costs
<a name="9999999999999999privatelink--costs.8a1c4265-c0b5-5604-aa0a-ccc8c99fbe56"></a>

AWS PrivateLink is often a cost-effective solution with small operational overhead. This is because the SaaS provider must manage only a Network Load Balancer, and the consumer must manage only VPC endpoints. You can make changes on both sides transparently, which reduces expensive and resource-intensive cross-organizational collaboration. Compliance costs tend to be low because the SaaS provider is exposing only the services that they want and not the entire network.

### Amazon VPC Lattice costs
<a name="9999999999999999vpclatlong--costs.46257bb4-b0d8-5088-bc62-8855776124a9"></a>

Amazon VPC Lattice offers a balanced cost structure with moderate fixed and variable infrastructure costs. As a fully managed service network, it significantly reduces operational overhead by automating service discovery, traffic management, and access controls across multiple VPCs. This simplifies both initial deployment and ongoing management compared to manual networking configurations. You can implement changes through policy-based controls without complex routing updates, which reduces the dependency on networking specialists. Compliance costs tend to be lower than traditional networking approaches because VPC Lattice provides fine-grained access controls and comprehensive visibility through built-in monitoring and logging capabilities. This can make it easier to demonstrate regulatory compliance.

### AWS Transit Gateway costs
<a name="9999999999999999awstglong--costs.e254cf59-fb26-589d-8969-441da4af42da"></a>

AWS Transit Gateway has larger hourly and data processing charges than AWS PrivateLink, but it has similar operational overhead. You must have deeper knowledge of the AWS Transit Gateway service and routing on AWS in order to correctly set up all the route tables. Infrastructure changes might require routing or DNS updates. Compliance costs are similar to VPC peering because both parties are potentially exposing subnetworks or entire VPCs to each other. AWS Transit Gateway route tables also need to be handled with care because they're shared by multiple consumers, and you must not allow any traffic between them.

### AWS Site-to-Site VPN costs
<a name="9999999999999999s2slong--costs.66e93fdf-0c39-58cb-aacd-3787d677c55f"></a>

Because Site-to-Site VPN essentially sends traffic to the internet, the variable cost is highest in comparison due to data transfer charges. Although it's a managed virtual private network (VPN) service, it comes with significant operational overhead, especially on the customer gateway. Provisioning and operations require advanced knowledge of networking, and changes often require action from both parties. Compliance costs are usually low because security teams often preapprove IPsec tunnels without additional review.

### AWS Direct Connect costs
<a name="9999999999999999aws-dc-long--costs.a9591497-9603-5ae3-bd5c-d479476ba0db"></a>

AWS Direct Connect comes with the largest fixed infrastructure cost because it is a private physical connection directly into the AWS Cloud. Specialist knowledge is required to set up and operate a Border Gateway Protocol (BGP) session (if required), to operate a VPN connection, and to perform traffic engineering. This service reduces the effort for security teams because it blends private connectivity with the option of additionally having Media Access Control Security (MACsec) and IPsec encryption.

### Public internet access costs
<a name="public-internet-access-costs.de178090-09a8-5c5a-92d9-333de082bbd5"></a>

*Public internet access* refers to the AWS resources that you can use to make an application publicly accessible, such as an Application Load Balancer. For this approach, there are variable costs linked to providing access to your services, including charges for [data transfer out to the internet](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html#data-transfer-out-internet). Operational overhead and compliance costs can be significant because you're exposing the service to the Internet and will require additional security and authentication mechanisms. However, there is no complex routing involved, and neither party has to know details about each other's infrastructure.

## Networking value map
<a name="evaluating-map"></a>

To help you see the big picture and make informed decisions, this guide includes a networking value map for each scenario. Because the ratings differ from scenario to scenario, the same service might score differently for two scenarios. The value maps are radar charts, where a hypothetical perfect score would be a five in all categories.

For example, the following image shows a sample radar chart. It includes only the metrics that we can help evaluate. We recommend that you create your own value map that includes the additional metrics that only you can evaluate.

![A sample radar chart.](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/c49804da-ae07-41ff-be73-20c0ec3498ce.png)
