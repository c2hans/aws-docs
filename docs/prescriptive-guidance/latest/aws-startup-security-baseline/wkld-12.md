---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-12.html
---

# WKLD.12 Use VPC endpoints to access supported services
<a name="wkld-12"></a>

In VPCs, resources that need to access AWS or other external services require either a route to the internet (`0.0.0.0/0`) or to the public IP address of the target service. Use VPC endpoints to enable a private IP route from your VPC to supported AWS or other services, removing the need for an internet gateway, NAT device, virtual private network (VPN) connection, or AWS Direct Connect connection.

You can attach policies and security groups to VPC endpoints to control access to a service. For example, you can write a VPC endpoint policy for [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) to allow only item-level actions and prevent table-level actions for resources in the VPC, regardless of their own permission policy. You can also write an Amazon S3 bucket policy to allow only requests originating from a specific VPC endpoint, denying other external access. A VPC endpoint can also have a security group rule that, for example, restricts access to Amazon EC2 instances associated with an application-specific security group, such as the business-logic tier of a web application.

VPC endpoints come in two types: *interface* endpoints and *gateway* endpoints. You access most services by using a VPC interface endpoint. DynamoDB is accessed using a gateway endpoint. Amazon S3 supports both interface and gateway endpoints. We recommend gateway endpoints for workloads that are contained within a single AWS account and Region. Gateway endpoints come at no additional charge. We recommend interface endpoints when you need more extensible access, such as to an Amazon S3 bucket from other VPCs, from on-premises networks, or from different AWS Regions.

For more information about using VPC endpoints, see the following resources:
+ For more information about selecting between gateway and interface endpoints for Amazon S3, see [Choosing your VPC endpoint strategy for Amazon S3](https://aws.amazon.com/blogs/architecture/choosing-your-vpc-endpoint-strategy-for-amazon-s3/) on the AWS Architecture Blog.
+ [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint) in the Amazon VPC documentation.
+ [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html) in the Amazon VPC documentation.
+ For example Amazon S3 bucket policies that restrict access to a specific VPC or VPC endpoint, see [Restricting access to a specific VPC](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.html#example-bucket-policies-restrict-access-vpc) in the Amazon S3 documentation.
+ For example DynamoDB endpoint policies that restrict actions, see [Endpoint policies for DynamoDB](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html#vpc-endpoints-policies-ddb) in the Amazon VPC documentation.

**Note**
Gateway endpoints are available at no additional charge. Interface endpoints incur an hourly charge and a per-GB data-processing charge. These charges are lower than the equivalent charges for routing traffic through AWS NAT Gateway. For more information, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
