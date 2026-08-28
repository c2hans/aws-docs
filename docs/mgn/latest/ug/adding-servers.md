---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/adding-servers.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Adding source servers
<a name="adding-servers"></a>

Add source servers to AWS Transform MGN by installing the AWS Replication Agent (also referred to as "the Agent") on them. The Agent can be installed on both Linux and Windows servers. You can add source servers from vCenter without installing an agent through the agentless replication feature.

Quick links:

+ [Linux installation instructions](linux-agent.md)
+ [Windows installation instructions](windows-agent.md)
+ [Agentless replication instructions](agentless-mgn.md)

**Note**
While the use of AWS Transform MGN is free for 90 days, you will incur charges for any AWS infrastructure that is provisioned during migration and after cutover, such as compute (Amazon EC2) and storage (Amazon EBS or FSx for ONTAP) resources. These are billed to your account separately, at your regular rates.

**Topics**
+ [Installation requirements](installation-requirements.md)
+ [Operating systems supported by MGN](Supported-Operating-Systems.md)
+ [Installing the AWS Replication Agent](agent-installation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
