---
source_url: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock_getting_started.html
---

# Getting started with Amazon Bedrock policies
<a name="orgs_manage_policies_bedrock_getting_started"></a>

Before you configure Amazon Bedrock policies, ensure you understand the prerequisites and implementation requirements. This topic guides you through the process of setting up and managing these policies in your organization.

## Before you begin
<a name="bedrock_getting_started-before-begin"></a>

Review the following requirements before implementing Amazon Bedrock policies:
+ Your account must be part of an AWS organization
+ You must be signed in as either:
  + The management account for the organization
  + A delegated administrator account with permissions to manage Amazon Bedrock policies
+ You must enable the Amazon Bedrock policy type in the root of your organization

## Implementation steps
<a name="bedrock_getting_started-implementation"></a>

To implement Amazon Bedrock policies effectively, follow these steps in sequence. Each step ensures proper configuration and helps prevent common issues during setup. The management account or delegated administrator can perform these steps through the AWS Organizations console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

1. [Enable Amazon Bedrock policies for your organization](enable-policy-type.md).

1. [Create an Amazon Bedrock policy](orgs_manage_policies_bedrock_syntax.md).

1. [Attach the Amazon Bedrock policy to your organization's root, OU, or account](orgs_policies_attach.md).

1. [View the combined effective Amazon Bedrock policy that applies to an account](orgs_manage_policies_effective.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
