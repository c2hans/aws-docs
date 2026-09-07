---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/http-api.html
---

# HTTP API
<a name="http-api"></a>

 HTTP API is a type of API Gateway that delivers enhanced features, improved performance, and an easier developer experience compared to REST APIs for certain use cases. In addition, HTTP APIs come with reduced request pricing.

 For private integrations, HTTP APIs offer additional integration endpoints for a VPC link, such as ALBs, NLBs, and [AWS Cloud Map](https://aws.amazon.com/cloud-map/). For any existing applications or micro services that have ALBs or AWS Cloud Map to route traffic, you can use the same setup. HTTP APIs can route traffic to those endpoints through a VPC link.

## Private integration
<a name="private-integration-2"></a>

 Because HTTP APIs offer three different private integration targets, you should consider which integration target best suits your use case. Depending on the backend service, one or more targets can be used by creating multiple VPC links to connect to Application Load Balancers, Network Load Balancers, or AWS Cloud Map services.

 *Table 2 – HTTP API private integration*

|  Integration target  |  Listener  |  Use cases  |
| --- | --- | --- |
|  NLB  |  TCP or TLS listener  |  TLS passthrough is possible <br /> High throughput  |
|  ALB  |  HTTP or HTTPS listener  |  Layer 7 routing <br /> Content-based routing  |
|  AWS Cloud Map  |  Namespace/service <br /> AWS Cloud Map parameters (optional)  |  Service discovery  |

## Sample architecture patterns
<a name="sample-architecture-patterns-1"></a>

### ALB architecture (ECS)
<a name="alb-architecture-ecs"></a>

 HTTP API private integration allows NLB and ALB for integration targets for load balancers. If you have any backend service fronted with ALBs, you can use the existing setup without re-architecting. Because ALBs allow different routing options, such as path-based routing, this option provides flexibility on the ALB routing level. To create listener rules to achieve path-based routing, see [Listener rules for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html).

 The figure shows private integration with ALB in HTTP API. The ALB uses path-based routing rules to route traffic to two different ECS services.

![A diagram that shows HTTP API private integration with ALB.](https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/images/http-api.png)

### Cloud Map architecture (microservices)
<a name="cloud-map-architecture-microservices"></a>

 With the AWS Cloud Map target option, you can use AWS Cloud Map to discover services like ECS and EC2-based services. Using AWS Cloud Map as a front-end service for microservices, you can leverage a private integration with an AWS Cloud Map target in HTTP APIs to route requests to different endpoints.

![A diagram that shows HTTP API private integration with Cloud Map.](https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/images/http-api-cloud-map.png)

### Private integration cross-account
<a name="private-integration-cross-account-1"></a>

 For cross-account access of private resources with HTTP APIs the architecture is very similar to that of REST APIs. For HTTP API private integrations, all resources must be owned by the same AWS account, including the load balancer or AWS Cloud Map service, VPC link, and HTTP API. Cross-account access to backend resources requires intermediate networking (for example, AWS PrivateLink, VPC Peering, or Transit Gateway) with the load balancer or AWS Cloud Map service residing in the same account as the API Gateway. The difference is you now have the choice of ALB, NLB or AWS Cloud Map for the VPC Link, rather than just an NLB.

 In the following sample architecture, AWS PrivateLink is used to access resources in another AWS account. The VPC link must exist in the same account as the API Gateway. The Application Load Balancer used in this VPC link is pointing to the VPC endpoint private IP addresses of the PrivateLink connection.

![A diagram that shows HTTP private cross-account integration using AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/images/private-cross-account.png)

 For more information and to deploy a code example, see the [Building private cross-account APIs using Amazon API Gateway and AWS PrivateLink blog](https://aws.amazon.com/blogs/compute/building-private-cross-account-apis-using-amazon-api-gateway-and-aws-privatelink/).

 With HTTP APIs, you can also use AWS Cloud Map to create a VPC link connection. In the following sample architecture, AWS Cloud Map is used to resolve private resources in another AWS account. The central API Gateway account and the resource account VPCs are connected using AWS Transit Gateway VPC attachments to provide private routing. Transit Gateway is an alternative to using VPC peering by providing a hub and spoke network design.

![A document that shows HTTP private cross-account integration using AWS Cloud Map and AWS Transit Gateway.](https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/images/private-cross-account2.png)

**Note**
AWS Cloud Map integration using [Amazon ECS service discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html) does not support cross-account patterns. To implement the architecture shown in the previous diagram, you must [register cross-account ECS resources manually in the AWS Cloud Map namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/registering-instances.html).
