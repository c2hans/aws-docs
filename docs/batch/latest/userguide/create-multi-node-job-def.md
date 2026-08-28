---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/create-multi-node-job-def.html
---

# Create a multi-node parallel job definition
<a name="create-multi-node-job-def"></a>

Before you can run jobs in AWS Batch, you must create a job definition. This process varies slightly between single-node and multi-node parallel jobs. This topic covers specifically how to create a job definition for an AWS Batch multi-node parallel job (also known as *gang scheduling*). For more information, see [Multi-node parallel jobs](multi-node-parallel-jobs.md).

**Note**
AWS Fargate doesn't support multi-node parallel jobs.

**Topics**
+ [Tutorial: Create a multi-node parallel job definition on Amazon EC2 resources](multi-node-job-def-ec2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
