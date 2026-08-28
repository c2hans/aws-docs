---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/setting-up.html
---

# Set up to use Amazon EC2 Auto Scaling
<a name="setting-up"></a>

Before you start using Amazon EC2 Auto Scaling, complete the following tasks.

**Topics**
+ [Prepare to use the AWS CLI](#set-up-cli)

## Prepare to use the AWS CLI
<a name="set-up-cli"></a>

You can use the AWS command line tools to issue commands at your system's command line to perform Amazon EC2 Auto Scaling and other AWS tasks.

To use the AWS Command Line Interface (AWS CLI), download, install, and configure version 1 or 2 of the AWS CLI. The same Amazon EC2 Auto Scaling functionality is available in version 1 and 2. To install the AWS CLI version 1, see [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html) in the *AWS CLI Version 1 User Guide*. To install the AWS CLI version 2, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS CLI Version 2 User Guide*.

AWS CloudShell lets you skip installing the AWS CLI in your development environment, and use it in the AWS Management Console instead. In addition to avoiding installation, you also don't need to configure credentials, and you don't need to specify a region. Your AWS Management Console session provides this context to the AWS CLI. You can use AWS CloudShell in supported AWS Regions. For more information, see [Create Auto Scaling groups from the command line using AWS CloudShell](create-auto-scaling-groups-with-cloudshell.md).

For more information, see [autoscaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/) in the *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
