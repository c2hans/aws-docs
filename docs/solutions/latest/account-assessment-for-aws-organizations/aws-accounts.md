---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/aws-accounts.html
---

# AWS Account Structure
<a name="aws-accounts"></a>

Follow these guidelines when setting up accounts for each stack:

## Hub Account
<a name="hub-account"></a>

The Hub stack contains all compute and storage resources of the solution to facilitate scans. Select a member account within your AWS Organization to deploy the Hub stack. Since this account will have read access to resource names and policies in all spoke accounts, including bucket names and secret names, choose an account that you protect as carefully as the most sensitive target account you intend to scan.

Important: Avoid using the Organizations management account as your Hub account, as it’s best practice to keep the management account free from operational workloads.

## Spoke Accounts
<a name="spoke-accounts"></a>

Deploy the Spoke stack to any member account within your AWS Organization that requires assessment, including the Hub account itself. This stack consists of a single IAM role that grants read access to the policies of all supported services.

For efficient deployment across multiple AWS accounts, consider using CloudFormation StackSets.

## Organizations Management Account
<a name="organizations-management-account"></a>

The Org-Management stack must be deployed in your Organizations management account. This stack consists of a single IAM role that will be assumed by the Hub stack’s Lambda function and grants minimal required permissions to access data of the Organization. This role enables: - Reading account information (listing accounts and their parent relationships) - Reading Delegated Administrator configurations and their services - Viewing AWS service access settings for the Organization - Reading and listing Organization policies

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account Assessment for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
