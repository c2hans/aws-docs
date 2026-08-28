---
source_url: https://docs.aws.amazon.com/vsts/latest/userguide/setting-up.html
---

# Setting up the AWS Toolkit for Azure DevOps
<a name="setting-up"></a>

To use the AWS Toolkit for Azure DevOps to access AWS, you need an AWS account and AWS credentials. When build agents run the tasks contained in the tools, the tasks must be configured with, or have access to, those AWS credentials to enable them to call AWS service APIs. To increase the security of your AWS account, we recommend that you do not use your root account credentials. You should create an *IAM user* to provide access credentials to the tasks running in the build agent processes.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Microsoft Azure DevOps. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vsts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
