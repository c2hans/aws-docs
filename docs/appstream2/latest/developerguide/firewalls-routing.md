---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/firewalls-routing.html
---

# Firewalls and Routing
<a name="firewalls-routing"></a>

 When creating an WorkSpaces Applications fleet, subnets and a Security Group must be assigned. Subnets have existing assignments of Network Access Control Lists (NACLs) and route table(s). You can associate [up to five security groups](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-security-groups.html) while launching a new image builder or while creating a new fleet Security Groups can have up to [five assignments from the existing Security Groups](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-security-groups.html). For each security group, you add rules that control the outbound and inbound network traffic from and to your instances

A NACL is an optional layer of security for your VPC that acts as a stateless firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC. For more information about the differences between security groups and network ACLs, see [the compare security groups and NACLs page](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html#VPC_Security_Comparison).

When designing and applying Security Group and NACL rules, consider the AWS Well-Architected best practices for least privilege. *Least privilege* is a principle of granting only the permissions required to complete a task.

For customers who have a high-speed private network connecting their on premise environment to AWS (via an AWS Direct Connect), you may consider using the VPC Endpoints for AppStream, which will mean the streaming traffic will be routed via your private network connectivity rather than going across the public internet. For more information on this topic, see the WorkSpaces Applications streaming interface VPC endpoint section of this document.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
