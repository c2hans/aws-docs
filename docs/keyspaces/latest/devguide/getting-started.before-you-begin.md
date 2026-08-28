---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.before-you-begin.html
---

# Tutorial prerequisites and considerations
<a name="getting-started.before-you-begin"></a>

Before you can get started with Amazon Keyspaces, follow the AWS setup instructions in [Accessing Amazon Keyspaces (for Apache Cassandra)](accessing.md). These steps include signing up for AWS and creating an AWS Identity and Access Management (IAM) user with access to Amazon Keyspaces.

To complete all the steps of the tutorial, you need to install `cqlsh`. You can follow the setup instructions at [Using `cqlsh` to connect to Amazon Keyspaces](programmatic.cqlsh.md).

To access Amazon Keyspaces using `cqlsh` or the AWS CLI, we recommend using AWS CloudShell. CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. You can run AWS Command Line Interface (AWS CLI) commands against Amazon Keyspaces using your preferred shell (Bash, PowerShell or Z shell). To use `cqlsh`, you must install the `cqlsh-expansion`. For `cqlsh-expansion` installation instructions, see [Using the `cqlsh-expansion` to connect to Amazon Keyspaces](programmatic.cqlsh.md#using_cqlsh). For more information about CloudShell see [Using AWS CloudShell to access Amazon Keyspaces](using-aws-with-cloudshell.md).

To use the AWS CLI to create, view, and delete resources in Amazon Keyspaces, follow the setup instructions at [Downloading and Configuring the AWS CLI](access.cli.md#access.cli.installcli).

After completing the prerequisite steps, proceed to [Create a keyspace in Amazon Keyspaces](getting-started.keyspaces.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
