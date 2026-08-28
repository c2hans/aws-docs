---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

Follow the step-by-step instructions in this section to uninstall the solution into your account. You can use the AWS Management Console, AWS CLI, or [AWS CloudFormation](using-aws-cloudformation.md).

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

Complete the following steps to delete the `scene-intelligence-with-rosbag-on-aws-create` and `scene-intelligence-with-rosbag-on-aws-delete` stacks.

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select this solution’s stack.

1. Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name scene-intelligence-with-rosbag-on-aws-create

$ aws cloudformation wait stack-delete-complete --stack-name scene-intelligence-with-rosbag-on-aws-create

$ aws cloudformation delete-stack --stack-name scene-intelligence-with-rosbag-on-aws-delete

$ aws cloudformation wait stack-delete-complete --stack-name scene-intelligence-with-rosbag-on-aws-delete
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
