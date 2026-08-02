---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost_data_transfer_implement_services.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST08-BP03 Implement services to reduce data transfer costs
<a name="cost_data_transfer_implement_services"></a>

 Implement services to reduce data transfer. For example, using a content delivery network (CDN) such as Amazon CloudFront to deliver content to end users, caching layers using Amazon ElastiCache, or using AWS Direct Connect instead of VPN for connectivity to AWS.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

[Amazon CloudFront](https://aws.amazon.com/cloudfront/) is a global content delivery network that delivers data with low latency and high transfer speeds. It caches data at edge locations across the world, which reduces the load on your resources. By using CloudFront, you can reduce the administrative effort in delivering content to large numbers of users globally, with minimum latency.

[Direct Connect](https://aws.amazon.com/directconnect/) allows you to establish a dedicated network connection to AWS. This can reduce network costs, increase bandwidth, and provide a more consistent network experience than internet-based connections.

[Site-to-Site VPN](https://aws.amazon.com/vpn/) allows you to establish a secure and private connection between your private network and the AWS global network. It is ideal for small offices or business partners because it provides quick and easy connectivity, and it is a fully managed and elastic service.

[VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html) allow connectivity between AWS services over private networking and can be used to reduce public data transfer and [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) costs. [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html) have no hourly charges, and support Amazon Simple Storage Service(Amazon S3) and Amazon DynamoDB. [Interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) are provided by [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html) and have an hourly fee and per GB usage cost.

**Implementation steps**
+ ** Implement services: **Using the data transfer modeling, look at where the largest costs and highest volume flows are. Review the AWS services and assess whether there is a service that reduces or removes the transfer, specifically networking and content delivery. Also look for caching services where there is repeated access to data, or large amounts of data.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/)
+  [AWS Explore Our Products](https://aws.amazon.com/)
+  [AWS caching solutions](https://aws.amazon.com/caching/aws-caching/)
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+  [Deliver content faster with Amazon CloudFront](https://aws.amazon.com/getting-started/tutorials/deliver-content-faster/)
