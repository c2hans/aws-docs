---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

You can uninstall the QnABot on AWS solution from the AWS Management Console or by using the AWS Command Line Interface.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. Select this solution’s installation stack.

1. Choose **Delete**.

**Note**
Some IAM Roles are retained after stack deletion. You can find and delete them by searching `AdminRole`, `OpenSearchDashboardsRole`, `UnauthenticatedRole`, and `UserRole`. You can also find all the roles by taking the first portion of your deleted **Stack ID** found in CloudFormation.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. Optionally, you can use the [AWS CloudShell](https://aws.amazon.com/cloudshell/) service to run AWS CLI commands. After confirming that the AWS CLI is available, run the following command:

```
$ aws cloudformation delete-stack --stack-name <installation-stack-name>
```
