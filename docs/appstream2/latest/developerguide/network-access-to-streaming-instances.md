---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/network-access-to-streaming-instances.html
---

# Network Access to Your Streaming Instance
<a name="network-access-to-streaming-instances"></a>

A security group acts as a stateful firewall that controls what traffic is allowed to reach your streaming instances. When you launch an WorkSpaces Applications streaming instance, assign it to one or more security groups. Then, add rules to each security group that control traffic for the instance. You can modify the rules for a security group at any time. The new rules are automatically applied to all instances to which the security group is assigned.

For more information, see [Security Groups in Amazon WorkSpaces Applications](managing-network-security-groups.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
