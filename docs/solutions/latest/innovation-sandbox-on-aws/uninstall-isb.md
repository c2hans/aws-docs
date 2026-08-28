---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/uninstall-isb.html
---

# Uninstall solution stacks
<a name="uninstall-isb"></a>

You can uninstall the stacks, use the AWS Management Console or the AWS Command Line Interface (AWS CLI).

Make sure you uninstall the stacks in this order:

1. Compute stack

1. Data stack

1. IDC stack

1. AccountPool stack

**Note**
If you upgraded to v1.3.0 or later from an earlier version, your account contains legacy AWS AppConfig configuration profiles whose names include **GlobalConfigHostedConfiguration** and **ReportingConfigHostedConfiguration**. These profiles are not managed by any of the solution’s stacks and have no effect on the solution. They are safe to delete manually from the AWS AppConfig console after you finish uninstalling.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. Choose the stack you want to delete.

1. Choose **Delete stack**.

**Note**
Make sure you uninstall the stacks in this order: Compute, Data, IDC, and AccountPool.

### Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Verify that AWS CLI is available in your environment. For installation instructions, refer to [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*.

Once you have access to AWS CLI, run the following command:

```
$ aws cloudformation delete-stack --stack-name <STACK_NAME>
```

**Note**
Make sure you uninstall the stacks in this order: Compute, Data, IDC, and AccountPool.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
