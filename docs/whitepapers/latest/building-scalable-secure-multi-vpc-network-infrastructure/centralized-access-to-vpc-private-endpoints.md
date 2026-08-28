---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-access-to-vpc-private-endpoints.html
---

# Centralized access to VPC private endpoints
<a name="centralized-access-to-vpc-private-endpoints"></a>

A VPC endpoint allows you to privately connect your VPC to supported AWS services without requiring an internet gateway or a NAT device, VPN connection, or Direct Connect connection. Therefore, your VPC is not exposed to the public internet. Instances in your VPC do not require public IP addresses to communicate with AWS service endpoints with this interface endpoint. Traffic between your VPC and other services does not leave the AWS network backbone. VPC endpoints are virtual devices. They are horizontally scaled, redundant, and highly available VPC components. Two types of endpoints can currently be provisioned: interface endpoints (powered by [AWS PrivateLink](https://aws.amazon.com/privatelink)) and gateway endpoints. [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway.html) can be utilized to access Amazon S3 and Amazon DynamoDB services privately. There is no additional charge for using gateway endpoints. Standard charges for data transfer and resource usage apply.

## Interface VPC endpoints
<a name="interface-vpc-endpoints"></a>

An [interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) consists of one or more elastic network interfaces with a private IP address that serves as an entry point for traffic destined to a supported AWS service. When you provision an interface endpoint, a cost is incurred for every hour the endpoint is running along with data processing charges. By default, you create an interface endpoint in every VPC from which you want to access the AWS service. This can be cost prohibitive and challenging to manage in the Landing Zone setup where a customer wants to interact with a speciﬁc AWS service across multiple VPCs. To avoid this, you can host the interface endpoints in a centralized VPC. All the spoke VPCs will use these centralized endpoints via Transit Gateway.

When you create a VPC endpoint to an AWS service, you can enable private DNS. When enabled, the setting creates an AWS managed Route 53 private hosted zone (PHZ), which enables the resolution of public AWS service endpoint to the private IP of the interface endpoint. The managed PHZ only works within the VPC with the interface endpoint. In our setup, when we want spoke VPCs to be able to resolve VPC endpoint DNS hosted in a centralized VPC, the managed PHZ won’t work. To overcome this, disable the option that automatically creates the private DNS when an interface endpoint is created. Next, manually [create a Route 53 private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) matching the [service endpoint name](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) and add an Alias record with the full AWS service endpoint name pointing to the interface endpoint.

1.  Log in to AWS Management Console and navigate to Route 53.

1.  Select the private hosted zone and navigate to **Create Record**.

1.  Populate the **Record Name** field, select Record Type as **A**, and enable **Alias**.

   Note that some services, such as the [Docker and OCI client endpoints](https://docs.aws.amazon.com/general/latest/gr/ecr.html#ecr-docker-endpoints) (`dkr.ecr`), require a wildcard alias (`*`) be used for the **Record Name**.

1.  Under **Route Traffic to section**, select the service to which the traffic should be sent and select the region from the dropdown list.

1.  Select the appropriate routing policy and enable the option to **Evaluate target health**.

 You [associate](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs.html) this private hosted zone with other VPCs within the Landing Zone. This configuration allows the spoke VPCs to resolve the full-service endpoint names to interface endpoints in the centralized VPC.

**Note**
To access the shared private hosted zone, the hosts in the spoke VPCs should use the Route 53 Resolver IP of their VPC. Interface endpoints are also accessible from on-premises networks over VPN and Direct Connect. Use conditional forwarding rules to send all DNS traffic for the full-service endpoint names to Route 53 Resolver inbound endpoints, which will resolve DNS requests according to the private hosted zone.

 In the following figure, Transit Gateway enables traffic flow from the spoke VPCs to the centralized interface endpoints. Create VPC Endpoints and the private hosted zone for it in Network Services Account and share it with spoke VPCs in the spoke accounts. For more details on sharing endpoint information with other VPCs, refer to the [Integrating AWS Transit Gateway with AWS PrivateLink and Amazon Route 53 Resolver](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-aws-transit-gateway-with-aws-privatelink-and-amazon-route-53-resolver/) blog post.

**Note**
A distributed VPC endpoint approach that is, an endpoint per VPC allows you to apply least privilege policies on VPC endpoints. In a centralized approach, you will apply and manage policies for all spoke VPC access on a single endpoint. With growing number of VPCs, the complexity of maintaining least privilege with a single policy document might grow. Single policy document also results in larger blast radius. You are also restricted on the [size of the policy document](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length) (20,480 characters).

![A diagram depicting centralizing interface VPC endpoints](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/centralizing-interface-vpc-endpoints.png)

## Cross Region endpoint access
<a name="cross-region-endpoint-access"></a>

 When you want multiple VPCs set up in different Regions that share a common VPC endpoint, use a PHZ, as outlined earlier. Both VPCs in each Region will be associated with the PHZ with the alias to the endpoint. In order to route traffic between VPCs in a multi-Region architecture, the Transit Gateways in each Region need to be peered together. For more information, refer to this blog: [Using Route 53 Private Hosted Zones for Cross-account Multi-Region Architectures](https://aws.amazon.com/blogs/architecture/using-route-53-private-hosted-zones-for-cross-account-multi-region-architectures/).

 VPCs from different regions can be routed to one another using either Transit Gateways or VPC Peering. Use the following documentation for peering Transit Gateways: [Transit gateway peering attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html).

In this example, the Amazon EC2 instance in the VPC `us-west-1` Region will use the PHZ to get the private IP address of the endpoint in the `us-west-2` Region and route the traffic to the `us-west-2` Region VPC over the Transit Gateway peering or VPC peering. Using this architecture, the traffic remains within the AWS network, securely allowing the EC2 instance in `us-west-1` to access the VPC service in `us-west-2` without going over the internet.

![A diagram depicting multi-Region VPC endpoints](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/multi-region-vpc-endpoints.png)

**Note**
Inter-Region data transfer charges do apply when accessing endpoints across Regions.

 Referring to the previous figure, an endpoint service is created in a VPC in the `us-west-2` Region. This endpoint service provides access to an AWS service in that Region. In order for your instances in another Region (such as `us-east-1`) to access the endpoint in the `us-west-2` Region, you need to create an address record in the PHZ with an alias to the desired VPC endpoint.

 First, make sure that the VPCs in each Region are associated with the PHZ that you created.

 When deploying an endpoint in multiple Availability Zone, the IP address of the endpoint returned from DNS will be from any of the subnets in the Availability Zone that is allocated.

 When invoking the endpoint, use the fully qualified domain name (FQDN) that is in the PHZ.

## AWS Verified Access
<a name="aws-verified-access"></a>

 AWS Verified Access delivers secure access to applications in private network without a VPN. It evaluates requests in real time like identity, device, and location. This service grants access based on policy for applications and connecting the users by improving security of the organization. Verified Access provide access to private applications by acting as an identity aware reverse proxy. User identity and device health, if applicable, are performed before routing traffic to application.

 The following diagram provides a high-level overview of Verified Access. Users send requests to access an application. Verified Access evaluates the request against the access policy for the group and any application-specific endpoint policies. If access is allowed, the request is sent to the application through the endpoint.

![A diagram depicting an overview of Verified Access](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/verified-access-diagram.png)

 The main components in an AWS Verified Access architecture are:
+  **Verified Access instances** – An instance evaluates application requests and grants access only when your security requirements are met.
+  **Verified Access endpoints** – Each endpoint represents an application. An endpoint can be NLB, ALB or network interface.
+  **Verified Access group** – A collection of Verified Access endpoints. We recommend that you group the endpoints for applications with similar security requirements to simplify policy administration.
+  **Access policies** – A set of user-defined rules that determine whether to allow or deny access to an application.
+  **Trust providers** – Verified Access is a service that facilitates the management of user identities and device security states. It is compatible with both AWS and third-party trust providers, requiring that at least one trust provider be attached to each Verified Access instance. Each of these instances can include a single identity trust provider as well as multiple device trust providers.
+  **Trust data** – The security data that your trust provider sends to Verified Access, such as a user's email address or the group they belong to, is evaluated against your access policies each time an application request is received.

 More details can be found in [Verified Access blog posts](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/aws-verified-access/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
