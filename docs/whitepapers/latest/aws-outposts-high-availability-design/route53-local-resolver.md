---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/route53-local-resolver.html
---

# Route 53 Local Resolver on Outposts
<a name="route53-local-resolver"></a>

When the AWS Outposts service link gets impacted by a temporary disconnect, the local DNS resolution fails, making it difficult for applications and services to discover other services, even when they are running on the same Outposts rack. However, with Route 53 Resolver on AWS Outposts, applications and services will continue to benefit from local DNS resolution to discover other services – even in the case of connectivity loss to the parent AWS Region. At the same time, for DNS resolution for on-premises host names, the Route 53 Resolver on Outposts helps to reduce latency as query results are cached and served locally, while being fully integrated with Route 53 Resolver endpoints.

Route 53 resolver Inbound endpoints forward DNS queries they receive from outside the VPC to the Resolver running in Outposts. In contrast, Route 53 Resolver Outbound enable Route 53 Resolvers to forward DNS queries to DNS resolvers that you manage on your on-premises network as is illustrated in the following diagram.

![Diagram showing Route 53 resolver on Outposts](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-51-route53-resolver-outposts.png)

## Route 53 Resolver on Outposts considerations
<a name="route53-considerations"></a>

Consider the following:
+ You must enable the Route 53 Resolver on Outposts, and it applies to the whole Outposts deployment, even if that involves multiple compute racks under a single Outposts ID.
+ In order to enable this feature, your Outposts must have enough compute capacity to deploy the local resolver in the form of at least 4 EC2 instances of any c5.xlarge, m5.large or m5.xlarge.
+ If you are using private DNS, you must share the Private Hosted Zone with the required Outposts VPCs’ in order to cache the records locally in the Route 53 Resolver on Outposts.
+ In order to enable integration with on-premises DNS with Inbound and Outbound endpoints, your Outposts must have enough compute capacity to deploy two EC2 instances per Route53 endpoint.
