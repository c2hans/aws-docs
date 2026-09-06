---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/network-infrastructure.html
---

# Network infrastructure
<a name="network-infrastructure"></a>

By default, the guidance provisions a new Virtual Private Cloud (VPC) consisting of three types of subnets: public, private, and isolated. The subnet type is determined by how you configure routing for your subnets. To read more, refer to the [Subnet types for Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-types) section.

Within this configuration, the Druid EC2 instances operate within the private subnets. Security groups are employed to enhance the security of these instances by permitting traffic exclusively from the ALB or from other instances within the Druid cluster, thus restricting access to a select set of trusted sources.

The Druid query instances are accessible via an Application Load Balancer (ALB) that exposes only HTTP and HTTPS protocols. An additional bastion host can be deployed to facilitate access to the instances located within the private subnet or the database in the isolated subnet. Additionally, you can deploy the guidance within an existing VPC if needed.
