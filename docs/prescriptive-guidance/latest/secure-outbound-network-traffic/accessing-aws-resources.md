---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-outbound-network-traffic/accessing-aws-resources.html
---

# Accessing AWS resources
<a name="accessing-aws-resources"></a>

A VPC endpoint provides a private connection between a VPC and a supported AWS service without requiring an internet gateway or NAT gateway. For example, you can use VPC endpoints to connect your VPC to Amazon Simple Storage Service (Amazon S3) or Amazon Elastic Container Registry (Amazon ECR).

Amazon VPC provides three types of VPC endpoints:
+ [Interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) connect VPCs to AWS services supported by AWS PrivateLink.
+ [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html) provide reliable connectivity to Amazon S3 and Amazon DynamoDB specifically.
+ [Gateway Load Balancer endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway-load-balancer.html) connect VPCs to custom applications that are hosted behind a Gateway Load Balancer.

For a list of supported services, see [AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html) in the Amazon VPC documentation.

**Note**
Gateway Load Balancer endpoints are helpful when privately sharing an application to users outside of the application's VPC or AWS account. For more information, see the **Establishing private connectivity between internal applications** section of this guide.
