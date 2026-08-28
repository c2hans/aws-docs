---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-the-access-portal.html
---

# Configure the AWS access portal
<a name="configure-the-access-portal"></a>

As an administrator, you can customize the AWS access portal to meet your organization's needs and ensure users can easily access their authorized resources.

## What you can configure
<a name="what-you-can-configure"></a>

**AWS access portal activation**: Set up initial user access to the AWS access portal, including user credential activation and first-time sign-in processes.

**Custom AWS access portal URL (optional)**: Personalize your organization's AWS access portal URL from the default format (`d-xxxxxxxxxx.awsapps.com/start`) to a more recognizable subdomain (`your-company.awsapps.com/start`).

**Before you begin**
Ensure you have administrative access to IAM Identity Center, verify that IAM Identity Center is set up as either an [organization instance](organization-instances-identity-center.md) or [account instance](account-instances-identity-center.md), and plan your custom subdomain name (this is a one-time configuration that cannot be changed later).

Once configured, users can access the AWS access portal using the custom URL and follow the activation process you've established for your organization.

**Topics**
+ [What you can configure](#what-you-can-configure)
+ [Activating the AWS access portal for first-time IAM Identity Center users](howtoactivateaccount.md)
+ [Customizing the AWS access portal URL](howtochangeURL.md)
+ [Confirm users can sign in to the AWS access portal](howtosigninprocedure.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
