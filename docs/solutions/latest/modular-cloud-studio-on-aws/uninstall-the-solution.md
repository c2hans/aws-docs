---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

You can uninstall the MCS solution from the AWS Management Console or by using the AWS Command Line Interface (AWS CLI). You must manually delete the modules and some of the core resources created by this solution. AWS Solutions do not automatically delete dependents of modules and storage backup resources in case you have stored data to retain. As such, see the following information on how to delete S3 buckets, CloudWatch logs, EC2 AMIs (from Leostream Broker module) and SSM parameters (from Leostream Broker module).

**Important**
Before uninstalling the solution, ensure that all modules and all spoke Regions have been disabled, and any Third-Party modules registered to the solution have been de-registered.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home/).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name <installation-stack-name>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
