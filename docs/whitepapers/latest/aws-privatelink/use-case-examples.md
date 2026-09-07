---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/use-case-examples.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Use-case examples
<a name="use-case-examples"></a>

 This section showcases some of the most common use cases for consuming and providing AWS PrivateLink endpoint services.

## Private access to SaaS applications
<a name="private-access-to-saas-applications"></a>

 AWS PrivateLink enables Software-as-a-Service (SaaS) providers to build highly scalable and secure services on AWS. Service providers can privately expose their service to thousands of customers on AWS with ease.

 A SaaS (or service) provider can use a Network Load Balancer to target instances in their Amazon VPC which will represent their endpoint service. Customers in AWS can then be granted access to the endpoint service and create an interface VPC endpoint in their own Amazon VPC that is associated with the endpoint service. This allows customers to access the SaaS provider’s service privately from within their own Amazon VPC.

 Follow the best practice of creating an AWS PrivateLink endpoint in each Availability Zone within the region that the service is deployed into. This provides a highly available and low-latency experience for service consumers.

 Service consumers who are not already on AWS and want to access a SaaS service hosted on AWS can utilize AWS Direct Connect for private connectivity to the service provider. Customers can use an AWS Direct Connect connection to access service provider services hosted in AWS.

 For example, a customer is interested in understanding their log data and selects a logging analytics SaaS offering hosted on AWS to ingest their logs in order to create visual dashboards. One way of transferring the logs into the SaaS provider’s service is to send them to the public-facing AWS endpoints of the SaaS service for ingestion.

 With AWS PrivateLink, the service provider can create an endpoint service by placing their service instances behind a Network Load Balancer enabling customers to create an interface VPC endpoint in their Amazon VPC that is associated with their endpoint service. As a result, customers can privately and securely transfer log data to an interface VPC endpoint in their Amazon VPC and not over public facing AWS endpoints. Refer to the following figure for an illustration.

![A diagram depciting private connectivity to cloud-based SaaS services .](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/private-connectivity.png)

## Shared services
<a name="shared-services"></a>

 As customers deploy their workloads on AWS, common service dependencies will often begin to emerge among the workloads. These shared services include security services, logging, monitoring, Dev Ops tools, and authentication to name a few. These common services can be abstracted into their own Amazon VPC and shared among the workloads that exist in their own separate Amazon VPCs. The Amazon VPC that contains and shares the common services is often referred to as a Shared Services VPC.

 Traditionally, workloads inside Amazon VPCs use VPC peering to access the common services in the Shared Services VPC. Customers can implement VPC peering effectively, however, there are caveats. VPC peering allows instances from one Amazon VPC to talk to any instance in the peered VPC. Customers are responsible for implementing fine grained network access controls to ensure that only the specific resources intended to be consumed from within the Shared Services VPC are accessible from the peered VPCs. In some cases, a customer running at scale can have hundreds of Amazon VPCs, and VPC peering has a limit of 125 peering connections to a single Amazon VPC.

 AWS PrivateLink provides a secure and scalable mechanism that allows common services in the Shared Services VPC to be exposed as an endpoint service, and consumed by workloads in separate Amazon VPCs. The actor exposing an endpoint service is called a service provider. AWS PrivateLink endpoint services are scalable and can be consumed by thousands of Amazon VPCs.

 The service provider creates an AWS PrivateLink endpoint service using a Network Load Balancer that then only targets specific ports on specific instances in the Shared Services VPC. For high availability and low latency, we recommend using a Network Load Balancer with targets in at least two Availability Zones within a Region.

 A service consumer is the actor consuming the AWS PrivateLink endpoint service from the service provider. When a service consumer has been granted permission to consume the endpoint service, they create an interface endpoint in their VPC that connects to the endpoint service from the Shared Services VPC. As an architectural best practice to achieve low latency and high availability, we recommend creating an Interface VPC endpoint in each available Availability Zones supported by the endpoint service. Service consumer VPC instances can use a VPC’s available endpoints to access the endpoint service via one of the following ways:
+ The private endpoint- specific DNS hostnames that are generated for the interface VPC endpoints, or
+ The Interface VPC endpoint’s IP addresses.

 On-premises resources can also access AWS PrivateLink endpoint services over AWS Direct Connect. Create an Amazon VPC with up to 20 interface VPC endpoints and associate with the endpoint services from the Shared Services VPC. End the AWS Direct Connect connection’s private virtual interface to a virtual private gateway. Next, attach the virtual private gateway to the newly created Amazon VPC. Resources on-premises are then able to access and consume AWS PrivateLink endpoint services over the AWS Direct connection. The following figure illustrates a shared services Amazon VPC using AWS PrivateLink.

![A diagram depicting shared services VPC using AWS PrivateLink .](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/shared-services-vpc.png)

## Hybrid services
<a name="hybrid-services"></a>

 As customers start their migration to the cloud, a common architecture pattern used is a hybrid cloud environment. This means that customers will begin to migrate their workloads into AWS over time, but they will also start to use native AWS services to serve their clients.

 In a Shared Services VPC, the instances behind the endpoint service exist on the AWS Cloud. AWS PrivateLink allows you to extend resource targets for the AWS PrivateLink endpoint service to resources in an on-premises data center.

 The Network Load Balancer for the AWS PrivateLink endpoint service can use resources in an on-premises data center as well as instances in AWS. Service consumers on AWS still access the AWS PrivateLink endpoint service by creating an interface VPC endpoint that is associated with the endpoint service in their VPC, but the requests they make over the interface VPC endpoint will be forwarded to resources in the on-premises data center.

 The Network Load Balancer enables the extension of a service architecture to load balance workloads across resources in AWS and on-premises resources, and makes it easy to migrate-to-cloud, burst-to-cloud, or failover-to-cloud. As customers complete the migration to the cloud, on-premises targets would be replaced by target instances in AWS and the hybrid scenario would convert to a Shared Services VPC solution. Refer to the following figure for a diagram on hybrid connectivity to services over AWS Direct Connect.

![A diagram showing hybrid connectivity to services over AWS Direct Connect .](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/hybrid-services.png)

## Presenting microservices
<a name="presenting-microservices"></a>

 Customers are continuing to adopt modern, scalable architecture patterns for their workloads. A microservice is a variant of the service-oriented architecture (SOA) that structures an application as a collection of loosely-coupled services that do one specialized job and do it well.

 AWS PrivateLink is well suited for a microservices environment. Customers can give teams who own a particular service an Amazon VPC to develop and deploy their service in. Once they are ready to deploy the service for consumption by other services, they can create an endpoint service. For example, endpoint service may consist of a Network Load Balancer that can target Amazon Elastic Compute Cloud (Amazon EC2) instances or containers on Amazon Elastic Container Service (Amazon ECS). Service teams can then deploy their microservices on either one of these platforms and the Network Load Balancer would provide access to the service.

 A service consumer would then request access to the endpoint service and create an interface VPC endpoint associated with an endpoint service in their Amazon VPC. The service consumer can then begin to consume the microservice over the interface VPC endpoint.

 The architecture in the following figure shows microservices which are segmented into different Amazon VPCs, and potentially different service providers. Each of the consumers who have been granted access to the endpoint services would simply create interface VPC endpoints associated with the given endpoint service in their Amazon VPC for each of the microservices it wishes to consume. The service consumers will communicate with the AWS PrivateLink endpoints via endpoint-specific DNS hostnames that are generated when the endpoints are created in the Amazon VPCs of the service consumer.

 The nature of a microservice is to have a call stack of various microservices throughout the lifecycle of a request. What is illustrated as a service consumer in the following figure can also become a service provider. The service consumer can aggregate what it needs from the services it consumed and present itself as a higher-level microservice.

![A diagram presenting microservices via AWS PrivateLink.](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/presenting-microservices.png)

## Inter-Region endpoint services
<a name="inter-region-endpoint-services"></a>

 Customers and SaaS providers who host their service in a single region can extend their service to additional Regions through inter-Region VPC Peering. Service providers can leverage a Network Load Balancer in a remote Region and create an IP target group that uses the IPs of their instance fleet in the remote Region hosting the service.

 Inter-Region VPC Peering traffic leverages Amazon’s private fiber network to ensure that services communicate privately with the AWS PrivateLink endpoint service in the remote region. This allows the service consumer to use local interface VPC endpoints to connect to an endpoint service in an Amazon VPC in a remote Region.

The following figure shows inter-Region endpoint services. A service provider is hosting an AWS PrivateLink endpoint service in the US-EAST-1 Region. Service consumers of the endpoint service require the service provider to provide a local interface VPC endpoint that is associated with the endpoint service in the EU-WEST-2 Region.

 Service providers can use inter-Region VPC peering to provide local endpoint service access to their customers in remote Regions. This approach can help the service providers gain the agility to provide the access their customers want while not having to immediately deploy their service resources in the remote Regions, but instead deploying them when they are ready. If the service provider has chosen to expand their service resources into remote Regions that are currently using inter-Region VPC peering, the service provider will have to remove the targets from the Network Load Balancer in the remote Region and point them to the targets in the local Region.

Because the remote endpoint service is communicating with resources in a remote Region, additional latency will be incurred when the service consumer communicates with the endpoint service. The service provider will also have to cover the costs for the inter-Region VPC peering data transfer. Depending on the workload, this could be a long- term approach for some service providers so long as they evaluate the pros and cons of the service consumer experience and their own operating model.

![A diagram depicting inter-Region endpoint services .](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/inter-region-endpoint.png)

## Inter-Region access to endpoint services
<a name="inter-region-access-to-endpoint-services"></a>

 As customers expand their global footprint by deploying workloads in multiple AWS Regions across the globe, they will need to ensure that the services that depend on AWS PrivateLink endpoint services have connectivity from the Region they are hosted in. Customers can use inter-Region VPC peering to enable services in another Region to communicate with the interface VPC endpoint, stopping the endpoint service which directs traffic to the AWS PrivateLink endpoint service hosted in the remote Region.

 Inter-Region VPC peering traffic is transported over Amazon’s network and ensures that your services communicate privately to the AWS PrivateLink endpoint service in the remote Region.

The following figure visualizes the inter-Region access to endpoint services. A customer has deployed a workload in the EU-WEST-1 Region that needs to access an AWS PrivateLink endpoint service hosted in the US-EAST-1 Region. The service consumer will first need to create an Amazon VPC in the Region where the AWS PrivateLink endpoint service is currently being hosted in. They will then need to create an inter-Region VPC Peering connection from the Amazon VPC in their Region to the Amazon VPC in the remote Region. The service consumer will then need to create an interface VPC endpoint in the Amazon VPC in the remote Region that is associated with the endpoint service. The workload in the service consumers Amazon VPC can now communicate with the endpoint service in the remote Region by using inter-Region VPC Peering. The service consumer will have to consider the additional latency when communicating with endpoint service hosted in the remote Region, as well as the inter-Region data transfer costs between the two Regions.

![A diagram depicting inter-Region access to endpoint services.](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/inter-region.jpeg)
