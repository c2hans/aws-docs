---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-11.html
---

# WKLD.11 Restrict network access by using security groups
<a name="wkld-11"></a>

Use security groups to control traffic to Amazon EC2 instances, containers, Amazon RDS databases, and other supported resources. *Security groups* act as a virtual firewall that can be applied to a group of related resources to consistently define rules for allowing inbound and outbound traffic. In addition to rules based on IP addresses and ports, security groups support rules to allow traffic from resources associated with other security groups. For example, a database security group can have rules to allow only traffic from an application server security group.

Security groups apply to AWS Fargate tasks in the same way they apply to Amazon EC2 instances. When you create an Amazon ECS service or run a Fargate task, you assign one or more security groups to the task's Elastic Network Interface. For more information, see [AWS Fargate task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html) in the Amazon Elastic Container Service documentation.

By default, security groups allow all outbound traffic but don't allow inbound traffic. You can remove the outbound traffic rule, or configure additional rules to restrict outbound traffic and allow inbound traffic. If the security group has no outbound rules, outbound traffic from your instance is blocked. For more information, see [Control traffic to resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the Amazon VPC documentation.

The following example shows three security groups that control traffic from an Application Load Balancer to containers (Amazon EC2 instances or Fargate tasks) that connect to an Amazon RDS for PostgreSQL database.

|
|
| Security group | Inbound rules | Outbound rules |
| --- |--- |--- |
| Application Load Balancer security group | **Description:** Allow HTTPS traffic from anywhere<br />**Type:** HTTPS<br />**Source:** Anywhere-IPv4 (0.0.0.0/0) | **Description:** Allow all traffic to anywhere<br />**Type:** All traffic<br />**Destination:** Anywhere-IPv4 (0.0.0.0/0) |
| Container security group (Amazon EC2 or Fargate task) | **Description:** Allow HTTP traffic from the Application Load Balancer<br />**Type:** HTTP<br />**Source:** Application Load Balancer security group | **Description:** Allow all traffic to anywhere<br />**Type:** All traffic<br />**Destination:** Anywhere-IPv4 (0.0.0.0/0) |
| Amazon RDS database security group | **Description:** Allow PostgreSQL traffic from container<br />**Type:** PostgreSQL<br />**Source:** Container security group | None |

**Note**
Security groups are available at no additional charge.
