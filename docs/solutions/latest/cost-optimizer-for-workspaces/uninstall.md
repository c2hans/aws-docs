---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/uninstall.html
---

# Uninstall the solution
<a name="uninstall"></a>

You can uninstall Cost Optimizer for Amazon WorkSpaces from the AWS Management Console or by using the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI). Delete all the spoke account stacks and then delete the hub account stack.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?) for spoke accounts.

1. Select this solution’s spoke account main stack.

1. Choose **Delete**.

1. Sign in to the CloudFormation console for the hub account.

1. Select this solution’s hub account stack.

1. Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-the-aws-command-line-interface"></a>

Determine whether the (AWS CLI) is available in your environment. For installation instructions, refer to [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name <installation-stack-name>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cost Optimizer for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
