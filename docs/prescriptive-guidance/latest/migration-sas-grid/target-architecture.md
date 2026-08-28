---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/target-architecture.html
---

# Target architecture
<a name="target-architecture"></a>

Although you can choose the appropriate instance types for your specific workload needs, for SAS Grid Manager on SAS 9.4, SAS recommends [Amazon EC2 I3en instances](https://aws.amazon.com/ec2/instance-types/i3en/). We also recommend using [Amazon VPC](https://aws.amazon.com/vpc/), which provides increased isolation control, customization, and security.

The following diagram shows SAS Grid on AWS with data, metadata, middle tier, and server tiers. This high-availability architecture is deployed on two Availability Zones for an active-active disaster recovery failover strategy.

![SAS Grid architecture on AWS with high availability and warm standby](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/images/guide-img/305d2670-30eb-46db-a41c-bed418267f47/images/601bad9c-3ffd-45f3-b167-b6571ebb41de.png)

This architecture includes the following components:
+ [Virtual private cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) – A virtual network dedicated to your AWS account. This is logically isolated from other virtual networks in the AWS Cloud. You can also create a hardware virtual private network (VPN) connection between your corporate data center and your VPC, and use the AWS Cloud as an extension of your corporate data center. The VPC is configured with two Availability Zones, public subnets, and private subnets to provide the network infrastructure for SAS Grid on AWS.
+ [Internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) – This gateway is attached to your VPC. By default, it comes with a security group that allows **no inbound** traffic and **all outbound** traffic to the internet.
+ [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) – The network address translation (NAT) gateways enable instances in private subnets to connect to the internet.
+ VPC endpoints – Gateway endpoints for Amazon S3 and DynamoDB eliminate NAT Gateway data transfer costs for these services. Interface endpoints for AWS Systems Manager, CloudWatch, and the Amazon EC2 API help keep management traffic on the AWS network, improving security and reducing costs.
+ Linux bastion host – Provides secure access to Linux instances located in the private and public subnets of your VPC.
**Note**
While bastion hosts are included for traditional access patterns, consider [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) to eliminate bastion hosts entirely. This reduces your attack surface, eliminates the need to manage SSH keys, and provides centralized audit logging of all access sessions.
+ Remote Desktop gateway – Provides remote administration. This gateway uses remote desktop protocol (RDP) over HTTPS to establish a secure, encrypted connection between remote users on the internet and Windows-based EC2 instances.
+ [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) – Ensures that the number of bastion hosts and Remote Desktop gateway instances always matches the capacity you specify during launch.
+ [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) – Integrates with Amazon S3 and makes it easy to process cloud datasets using the Lustre high-performance file system.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html) – Enables you to store and retrieve any amount of data at any time, from anywhere on the web.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
