---
source_url: https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/network-configuration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Network configuration
<a name="network-configuration"></a>

 With Amazon Virtual Private Cloud (Amazon VPC), you can provision a logically isolated section of the AWS Cloud that is dedicated to your account. You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, security settings, and configuration of route tables and network gateways.

 A *subnet* is a range of IP addresses in your Amazon VPC. You can launch AWS resources into a subnet that you select. Use a public subnet for resources that must be connected to the internet, and a private subnet for resources that won't be connected to the internet.

 To protect the AWS resources in each subnet, you can use multiple layers of security, including security groups and network access control lists (ACLs).

 The following table describes the basic differences between security groups and network ACLs.

|  **Security group**  |  **Network ACL**  |
| --- | --- |
|  Operates at the instance level (first layer of defense)  |  Operates at the subnet level (second layer of defense)  |
|  Supports allow rules only  |  Supports allow rules and deny rules  |
|  Stateful: Return traffic is automatically allowed, regardless of any rules  |  Stateless: Return traffic must be explicitly allowed by rules  |
|  Evaluates all rules before deciding whether to allow traffic  |  Processes rules in numerical order when deciding whether to allow traffic  |
|  Applies to an instance only if someone specifies the security group when launching the instance, or associates the security group with the instance later on  |  Automatically applies to all instances in the subnets it's associated with (backup layer of defense, so you don't have to rely on someone specifying the security group)  |

 Amazon VPC provides isolation, additional security, and the ability to separate Amazon EC2 instances into subnets, and allows the use of private IP addresses. All of these are important in database implementation.

Deploy the Oracle Database instance in a private subnet and allow only application servers within the Amazon VPC, or a bastion host within the Amazon VPC, to access the database instance.

Create appropriate security groups that allow access only to specific IP addresses through the designated ports. These recommendations apply to Oracle Database regardless of whether you’re using Amazon RDS or Amazon EC2.

![Oracle Database in private subnet of an Amazon VPC](http://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/images/oracle-db-private-subnet.png)

 Oracle Database in private subnet of an Amazon VPC

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
