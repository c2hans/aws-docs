---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/credentials.html
---

# Authentication and access
<a name="credentials"></a>

You don't need to authenticate with AWS to start working with the AWS Toolkit for Visual Studio with Amazon Q. However, most AWS resources are managed through an AWS account. To access all of the AWS Toolkit for Visual Studio with Amazon Q services and features, you'll need at least 2 types of account authentication:

1. Either **AWS Identity and Access Management (IAM)** or **AWS IAM Identity Center** authentication for your AWS accounts. Most AWS services and resources are manged through IAM and IAM Identity Center.

1. An **AWS Builder ID** is either optional for certain other AWS services.

The following topics contain additional details and set up instructions for each credential type and authentication method.

**Topics**
+ [AWS IAM Identity Center credentials in AWS Toolkit for Visual Studio](sso-credentials.md)
+ [AWS IAM credentials](keys-profiles-credentials.md)
+ [AWS Builder ID](builder-id.md)
+ [Multi-factor authentication (MFA) in Toolkit for Visual Studio](mfa-credentials.md)
+ [Setting up external credentials](external-credentials.md)
+ [Updating firewalls and gateways to allow access](endpoints.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
