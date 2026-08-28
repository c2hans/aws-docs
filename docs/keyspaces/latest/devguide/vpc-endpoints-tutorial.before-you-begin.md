---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.before-you-begin.html
---

# Tutorial prerequisites and considerations
<a name="vpc-endpoints-tutorial.before-you-begin"></a>

Before you start this tutorial, follow the AWS setup instructions in [Accessing Amazon Keyspaces (for Apache Cassandra)](accessing.md). These steps include signing up for AWS and creating an AWS Identity and Access Management (IAM) principal with access to Amazon Keyspaces. Take note of the name of the IAM user and the access keys because you'll need them later in this tutorial.

Create a keyspace with the name `myKeyspace`and at least one table to test the connection using the VPC endpoint later in this tutorial. You can find detailed instructions in [Getting started with Amazon Keyspaces (for Apache Cassandra)](getting-started.md).

After completing the prerequisite steps, proceed to [Step 1: Launch an Amazon EC2 instance](vpc-endpoints-tutorial.launch-ec2-instance.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
