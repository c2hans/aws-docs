---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/agentless-mgn.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Installing the AWS Transform MGN vCenter Client for Agentless Replication on vCenter source environments
<a name="agentless-mgn"></a>

AWS Transform MGN allows you to perform agentless snapshot replication from your vCenter source environment into AWS. This is achieved by installing the MGN vCenter Client in your vCenter environment. MGN recommends using agent-based replication when possible, as it supports CDP (Continuous Data Protection) and provides the shortest cutover window. Agentless replication should be used when your company’s policies prevent you from installing the AWS Replication Agent on each individual server.

**Topics**
+ [Agentless replication overview](installing-vcenter-overview-mgn.md)
+ [VMware limitations](installing-vcenter-reques-mgn.md)
+ [Generating vCenter Client IAM credentials](vcenter-credentials-mgn.md)
+ [Installing the MGN vCenter Client](installing-vcenter-appliance-mgn.md)
+ [Replicating servers from vCenter to AWS](replicating-vcenter-aws-mgn.md)
+ [Updating the vCenter or AWS Credentials](updating-vcenter-or-aws-credentials.md)
+ [Differentiating agentless and agent-based servers](differences-vcenter-aws.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
