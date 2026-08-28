---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/adminguide/faq.html
---

# Frequently asked questions (FAQs)
<a name="faq"></a>

The following information can help you troubleshoot common issues in enabling IAM Identity Center.

| Question | Answer |
| --- | --- |
| Why is IAM Identity Center integration required? | IAM Identity Center is the feature within IAM that manages the synchronization of identity sources. IAM Identity Center is the identity source for the AWS Supply Chain instance. You need to configure IAM Identity Center to setup the AWS Console and the AWS Supply Chain web application. For more information on IAM Identity Center, see [Enabling AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) in the *[AWS IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/)*. |
| Why use an IAM Identity Center organization instance for AWS Supply Chain? | By creating an organization instance, you can enable IAM Identity Center access across AWS accounts. For example, if your IAM Identity Center is not enabled in the same AWS account as the AWS Supply Chain instance account. For more information on benefits on creating an organization IAM Identity Center instance, see [Organization instances of IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/organization-instances-identity-center.html) in the *[AWS IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/)*. |
| Why are delegated administrator privileges required for AWS Supply Chain? | It is not required to have an delegated administrator to use AWS Supply Chain but it's a best practice for an AWS Organization setup to restrict access to the *management account* for the organization and manage IAM Identity Center. For more information, see [Delegated adminsitrotor for AWS Organizations.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html).<br />While creating an organization instance, make sure the account that will be used to create an AWS Supply Chain instance is part of the same organization as the IAM Identity Center account. Make sure the required permissions are enabled to create an instance and you can create an AWS Supply Chain instance in the same region as the IAM Identity Center account. For information on required permissions to create a AWS Supply Chain instance, see [Getting started with AWS Supply Chain](getting-started.md). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
