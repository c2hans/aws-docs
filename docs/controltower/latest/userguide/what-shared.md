---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/what-shared.html
---

# What are the shared accounts?
<a name="what-shared"></a>

In AWS Control Tower, the shared accounts in your landing zone are provisioned during setup: the management account, the log archive account, and the audit account.

## What is the management account?
<a name="what-is-mgmt"></a>

This is the account that you created specifically for your landing zone. This account is used for billing for everything in your landing zone. It's also used for Account Factory provisioning of accounts, as well as to manage OUs and controls.

**Note**
It is not recommended to run any type of production workloads from an AWS Control Tower management account. Create a separate AWS Control Tower account to run your workloads.

For more information, see [Management account](special-accounts.md#mgmt-account).

## What is the log archive account?
<a name="what-is-log-archive"></a>

This account works as a repository for logs of API activities and resource configurations from all accounts in the landing zone.

For more information, see [Log archive account](special-accounts.md#log-archive-account).

## What is the audit account?
<a name="what-is-audit"></a>

The audit account is a restricted account that's designed to give your security and compliance teams read and write access to all accounts in your landing zone. From the audit account, you have programmatic access to review accounts, by means of a role that is granted to Lambda functions only. The audit account does not allow you to log in to other accounts manually. For more information about Lambda functions and roles, see [Configure a Lambda function to assume a role from another AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-assume-iam-role).

For more information, see [Audit account](special-accounts.md#audit-account).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
