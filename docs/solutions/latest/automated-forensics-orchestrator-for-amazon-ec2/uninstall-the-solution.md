---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/uninstall-the-solution.html
---

# Uninstall the Guidance
<a name="uninstall-the-solution"></a>

## Using the AWS Command Line Interface (CLI)
<a name="using-the-aws-command-line-interface-cli"></a>
+ Run `cdk destroy --all` from the `sources` folder, or
+ Delete the stack from the CloudFormation console in Forensic, Application, and Security Hub AWS Account.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. On the **Stacks** page, select this Guidance’s installation stack.

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Forensics Orchestrator for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
