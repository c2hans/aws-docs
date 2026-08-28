---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-10.html
---

# WKLD.10 Deploy private resources into private subnets
<a name="wkld-10"></a>

Deploy resources that don't require direct internet access (such as Amazon EC2 instances, databases, queues, caching, or other infrastructure) into a VPC private subnet. Private subnets don't have a route declared in their route table to an attached internet gateway and cannot receive internet traffic. Traffic from a private subnet that is destined for the internet must go through network address translation (NAT). You can use a managed AWS NAT Gateway or an Amazon EC2 instance running NAT processes in a public subnet. For more information about network isolation, see [Infrastructure security in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html) in the Amazon Virtual Private Cloud (Amazon VPC) documentation.

Use the following practices when creating private resources and subnets:
+ When creating a private subnet, disable **Auto-assign public IPv4 address**.
+ When creating private Amazon EC2 instances, disable **Auto-assign Public IP**. This prevents a public IP address from being assigned if the instance is unintentionally deployed into a public subnet due to misconfiguration.
+ When creating [AWS Fargate](https://aws.amazon.com/fargate/) tasks and services, deploy them into private subnets and set **Assign public IP** to **TURNED OFF**. Fargate tasks deployed in a public subnet can be assigned a public IP address, which exposes them directly to the internet. For more information, see [AWS Fargate task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html) in the Amazon Elastic Container Service (Amazon ECS) documentation.

When deploying a resource, specify the private subnet in the resource's network configuration.

**Note**
Private subnets are available at no additional charge. If your private resources require outbound internet access, AWS NAT Gateway incurs an hourly charge and a per-GB data-processing charge. For more information, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
