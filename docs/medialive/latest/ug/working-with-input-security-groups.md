---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/working-with-input-security-groups.html
---

# Working with input security groups
<a name="working-with-input-security-groups"></a>

In MediaLive, an *input security group* contains a list of rules. Each rule is a range of IP addresses (CIDR blocks) that are allowed to push content to MediaLive. When you attach an input security group to an input, you apply a rule to that input—only an upstream system with an IP address from one of the ranges in that input security group is allowed to push content to that input. MediaLive will ignore push requests from IP addresses not covered by that input security group.

You can include up to 10 rules (IP address ranges or CIDR blocks) in one input security group.

You can attach the same input security group to any number of inputs.

**Topics**
+ [Purpose of an input security group](purpose-input-security-groups.md)
+ [Creating an input security group](create-input-security-groups.md)
+ [Editing an input security group](edit-input-security-group.md)
+ [Deleting an input security group](delete-input-security-group.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
