---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/options-aws.html
---

# SaaS consumers operating on AWS
<a name="options-aws"></a>

This section discusses connectivity options if both you and your consumers are operating in the AWS Cloud. This scenario offers the largest flexibility because many AWS services natively integrate and because both parties have access to the entire AWS service portfolio.

**This section discusses the following network access approaches:**
+ [Integrating with AWS PrivateLink](#options-aws-privatelink)
+ [Sharing an Amazon VPC Lattice service](#options-amazon-vpc-lattice)
+ [Creating VPC peering connections](#options-aws-vpc-peering)
+ [Connecting VPCs with AWS Transit Gateway](#options-aws-transit-gateway)

The following networking value map summarizes how each of these options scores for each evaluation metric. For more information about the evaluation metrics, see [Evaluation metrics](evaluating.md#evaluating-metrics) in this guide. In the map, a five represents the best score, such as the lowest TCO, best network isolation, or lowest time to repair. For more information about how to read this radar chart, see [Networking value map](evaluating.md#evaluating-map) in this guide.

![Radar chart that shows scores for each evaluation metric.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/11679979-a0c4-41e0-b6e0-62fe80eefcda.png)

The radar chart shows the following values.

|
|
| **Evaluation metric** | **AWS PrivateLink** | **Amazon VPC Lattice** | **VPC peering** | **AWS Transit Gateway** |
| --- |--- |--- |--- |--- |
| **Ease of integration** | 5 | 5 | 4 | 3 |
| **TCO** | 5 | 5 | 3 | 4 |
| **Scalability** | 5 | 4 | 1 | 4 |
| **Adaptability** | 4 | 5 | 2 | 3 |
| **Network isolation** | 5 | 5 | 2 | 3 |
| **Observability** | 4 | 5 | 4 | 4 |
| **Time to repair** | 5 | 5 | 5 | 4 |

## Integrating with AWS PrivateLink
<a name="options-aws-privatelink"></a>

[AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) is the most cloud-native way to integrate a SaaS offering. SaaS providers can host their application either behind a [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html). The Network Load Balancer directly integrates with an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), and [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html). It is also possible to route traffic from the Network Load Balancer to interface VPC endpoints in the SaaS provider account. This helps you use an API to reach applications, such as through [Amazon API Gateway](https://repost.aws/knowledge-center/invoke-private-api-gateway) or [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html). If your application requires access to resources in the customer environment that aren't load balanced, such as a database, you can use [resource VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/use-resource-endpoint.html).

AWS PrivateLink supports a bandwidth of up to 100 Gbps per Availability Zone. The following diagram shows a basic configuration with some possible integrations. It connects two consumer accounts to the SaaS provider account through AWS PrivateLink. There are service endpoints in the consumer accounts and a Network Load Balancer in the SaaS provider account.

![Basic configuration for AWS PrivateLink with optional integrations.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/e923e1eb-a6d5-4282-ae9a-e651eb4b506d.png)

The following are the benefits of this approach:
+ Ease of integration: No route table changes required
+ Ease of integration: You can [offer endpoint services through AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/privatelink.html)
+ Ease of integration: VPC endpoints support [friendly DNS names](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-dns-names.html)
+ Scalability: It can scale to thousands of SaaS consumers
+ Adaptability: Support for overlapping CIDR ranges
+ Adaptability: Support for IPv6
+ Adaptability: Cross-Region support
+ TCO: AWS PrivateLink is a fully managed service, so it requires less operational effort
+ Network isolation: Security benefit for the SaaS consumer because traffic can't be initiated from the SaaS provider
+ Network isolation: Security benefit for the SaaS provider because they are not exposing an entire subnet or VPC

The following are the drawbacks of this approach:
+ Adaptability: SaaS provider must use the same Availability Zones as the consumer
+ Adaptability: Support only for client-initiated connections, and resource VPC endpoints are required for service-initiated communication
+ Adaptability: Network Load Balancer is the only direct integration for AWS PrivateLink

## Sharing an Amazon VPC Lattice service
<a name="options-amazon-vpc-lattice"></a>

To use [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) as a connectivity option for your SaaS application, you first create one or more VPC Lattice services that represent your SaaS application components. You configure listeners and routing rules to direct traffic to your backend targets, such as Amazon EC2 instances, containers, or AWS Lambda functions. For more information, see [Connecting Saas services within a VPC Lattice service network](https://aws.amazon.com/blogs/networking-and-content-delivery/connecting-saas-services-within-a-vpc-lattice-service-network/) (AWS blog post). Concept-wise, this is almost the same as configuring an Application Load Balancer. Then, you share your SaaS service securely with customer AWS accounts or organizations by using [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html), specifying what permissions they have. After customers accept the resource share, they can associate your SaaS service with their existing or newly created VPC Lattice service networks to enable service-to-service communication.

Each VPC Lattice service can support up to 10 Gbps and 10,000 requests per second per Availability Zone. By implementing auth policies, your customers can have fine-grained control over which services and resources can access the SaaS application. You can use [resource gateways](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateway.html) to access resources that require a TCP connection. For example, this might be an Amazon EKS cluster that you manage, or it might be a customer-managed resource that your application needs to access. For more information about using resource gateways for SaaS offerings, see [Extend SaaS capabilities across AWS accounts using AWS PrivateLink support for VPC resources](https://aws.amazon.com/blogs/networking-and-content-delivery/extend-saas-capabilities-across-aws-accounts-using-aws-privatelink-support-for-vpc-resources/) (AWS blog post).

The following diagram shows a high-level VPC Lattice configuration with some example integrations. It uses customer-managed service networks to access the SaaS application.

![Basic configuration for Amazon VPC Lattice with optional integrations.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/257c41f0-adec-453d-afb6-1efa49be95a5.png)

The following are the benefits of this approach:
+ Ease of integration: No route table changes required
+ Ease of integration: Service discovery out of the box
+ Scalability: It can scale to thousands of SaaS consumers
+ Adaptability: Support for overlapping CIDR ranges
+ Adaptability: Support for IPv6
+ Adaptability: Integrates with any AWS compute service as a VPC Lattice service
+ TCO: VPC Lattice is a fully managed service, so it requires less operational effort
+ TCO: Built-in load balancing with advanced traffic routing
+ Network isolation: Fine-grained authorization with auth policies
+ Network isolation: Security benefit for the SaaS consumer because traffic cannot be initiated from the SaaS provider
+ Network isolation: Security benefit for the SaaS provider because you are not exposing an entire subnet or VPC

The following are the drawbacks of this approach:
+ Adaptability: Support only for client-initiated connections, and resource gateways are required for service-initiated communication
+ Adaptability: No cross-Region support

## Creating VPC peering connections
<a name="options-aws-vpc-peering"></a>

When you use [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) to connect the SaaS provider's VPC with the consumer's VPC, both parties are able to initiate connections. This requires proper configuration of security groups, firewalls, and network-access control lists (NACLs) in both accounts. Otherwise, unwanted traffic might enter the network through the peering connection. You can use security groups to reference security groups from peered VPCs. This can help you control access to your application because allow-listing security groups provides more explicit and granular access control compared to allow-listing IP addresses.

With VPC peering, the SaaS offering can be reached through a service or resource deployed in the VPC. Most SaaS applications sit behind an Application Load Balancer or Network Load Balancer. [AWS AppSync private APIs](https://docs.aws.amazon.com/appsync/latest/devguide/using-private-apis.html) or [Amazon API Gateway private APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html) are other common entry points to SaaS applications because they can be a target over a peering connection through interface VPC endpoints.

After you establish a peering connection, you must update the route tables for the VPCs in both accounts to define the peering connection as the next hop for the respective CIDR range. This solution is recommended only for SaaS providers who have a few consumers because managing multiple peering connections quickly becomes too complex.

The following diagram shows a basic configuration with some possible integrations. VPCs in two consumer accounts have a peering connection with a VPC in the SaaS provider account.

![Basic configuration of VPC peering connections between multiple accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/4c52b4d6-a31c-4777-a218-471439e07354.png)

The following are the benefits of this approach:
+ Time to repair: No single point of failure for communication
+ Scalability: No bandwidth limitations over VPC peering
+ TCO: No cost for peering connection or traffic over the peering connection within the same Availability Zone
+ TCO: No infrastructure to manage
+ Adaptability: Support for IPv6
+ Adaptability: Inter-Region peering supported

The following are the drawbacks of this approach:
+ Adaptability: No support for transitive routing
+ Adaptability: No support for overlapping CIDR ranges
+ Scalability: Limited scalability (maximum 125 peering connections per VPC)
+ TCO: Complexity grows exponentially with each additional peering connection
+ TCO: Overhead from managing route tables, peering connections themselves, security group rules, and traffic inspection
+ Network isolation: Tight security controls required because entire VPCs of both parties are exposed

## Connecting VPCs with AWS Transit Gateway
<a name="options-aws-transit-gateway"></a>

When you connect VPCs through [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), it creates VPC attachments and deploys network interfaces in the subnets of each Availability Zone that should route traffic to and from the VPC. It is recommended to have a dedicated `/28` subnet in every Availability Zone for the VPC attachment. For more information, see [Amazon VPC Transit Gateways design best practices](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-best-design-practices.html). The VPCs need an updated route table to send traffic through the deployed network interface, and the Transit Gateway route tables need to be updated accordingly. In a multi-tenant configuration, you want the SaaS provider's VPC to have a route to all of the consumers' VPCs. The consumer's VPCs should have a route only to the SaaS provider's VPC.

Transit Gateway is highly available by design. It supports monitoring with [VPC Flow Logs](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-vpc-flow-logs-for-aws-transit-gateway/), and the maximum bandwidth for a Transit Gateway attachment is 100 Gbps per Availability Zone. Like VPC peering, this approach enables cross-VPC security group referencing, which simplifies access control between the environments.

There are two main options to connect consumers to your SaaS offering with Transit Gateway.

**Option 1: Using RAM**

In the first option, the service provider [shares the Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-share.html) with the consumers by using [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html). This allows the consumers to deploy the VPC attachments in their own accounts. The following diagram shows this option at a high level.

![Consumers deploy transit gateway attachments to their VPCs.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/c82f3900-53a8-4568-a94e-653cfb26c581.png)

**Option 2: Peered transit gateways**

The second option is to peer your transit gateway with a transit gateway in the consumers' accounts. This provides consumers with more flexibility because they can now fully control the route tables within their transit gateway. For example, they could set up centralized inspection between the service and their workloads. A drawback of this option is only static routing between transit gateways is supported. The following diagram shows this option at a high level.

![Consumers and the SaaS provider create peered transit gateways.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/581208dc-0f8d-4915-bfb0-9c42bb742b4d.png)

The following are the benefits of this approach:
+ Scalability: Support for up to 5,000 attachments
+ Scalability: One place to manage and monitor all connected VPCs
+ Adaptability: AWS Transit Gateway can also attach to VPNs, Direct Connect gateways, and third-party SD-WAN appliances
+ Adaptability: Flexible architecture, such as [adding an inspection VPC](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/)
+ Adaptability: Support for transitive routing
+ Adaptability: Can peer intra-Region and inter-Region transit gateways
+ Adaptability: Support for IPv6
+ TCO: AWS Transit Gateway is a fully managed service, so it requires less operational effort
+ TCO: TCO grows linearly with each additional transit gateway attachment

The following are the drawbacks of this approach:
+ Ease of integration: Routing configuration requires advanced networking knowledge
+ Adaptability: No support for overlapping CIDR ranges
+ TCO: Overhead from managing route tables entries, security group rules, and traffic inspection
+ Security: Tight security controls required because entire VPCs of both parties are exposed

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
