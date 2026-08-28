---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-validationerror.html
---

# Problem: "ValidationError: Stack <stack-name> cannot be deleted while TerminationProtection is enabled" error
<a name="problem-validationerror"></a>

Depending on your deployment, you might choose to remove an existing solution-provisioned CloudFormation stack. Solution-provisioned stacks have termination protection activated by default. If you attempt to delete a stack with termination protection activated, the deletion fails. The stack and its status remain unchanged. You might receive a [Core pipeline error](problem-core-pipeline-failure.md) message like the following, with `AWSAccelerator-<STACK_NAME>- <ACCOUNT_ID>-<REGION> ` representing the stack name:

 `AWSAccelerator-<STACK_NAME>- <ACCOUNT_ID>-<REGION> failed: Error [ValidationError]: Stack <STACK_NAME>- <ACCOUNT_ID>-<REGION>] cannot be deleted while TerminationProtection is enabled`

## Resolution
<a name="resolution-6"></a>

## Option 1: Use the AWS Management Console
<a name="option-1-use-the-aws-management-console"></a>

1. Deactivate termination protection on the stack. For more information, see [Protecting a stack from being Deleted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html) in the *AWS CloudFormation User Guide*.

1. Attempt deletion again.

## Option 2: Use the AWS Command Line Interface
<a name="option-2-use-the-aws-command-line-interface"></a>

1. Deactivate termination protection on the stack by running the [update-termination-protection](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-termination-protection.html) command with the CLI:

   ```
   $ aws cloudformation update-termination-protection --stack-name <stack-name> --no-enable-termination-protection
   ```

1. Attempt deletion again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
