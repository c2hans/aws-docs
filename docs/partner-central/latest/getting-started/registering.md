---
source_url: https://docs.aws.amazon.com/partner-central/latest/getting-started/registering.html
---

# Registering in AWS Partner Central
<a name="registering"></a>

Registering as an AWS Partner is the first step for your AWS Partner business. This section guides you through the registration process, including providing required information and completing verification steps.

**Important**
If you are an existing partner with an existing AWS Partner Central account, you should not register a new account in AWS Partner Central. Instead, the existing Alliance Lead should take the action to migrate your current AWS Partner Central account to the new experience on the AWS Console. For more information, see [Migrating to Partner Central on the AWS Console](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=Partner-Central-Migration-Guide).

## Before you register
<a name="before-you-register"></a>

To register for AWS Partner Central, ensure you have:
+ **Legal authority to register on behalf of your company** — The person registering must have legal authority to accept the [AWS Partner Network Terms and Conditions](https://aws.amazon.com/partners/terms-and-conditions/) and **APN Customer Engagements Terms and Conditions** on behalf of your company.
+ **An AWS account on a paid plan and in good standing** — You need an AWS account for registration. This account will be used for APN fee billing, and the billing address will be used as your headquarters address in the discovery portal. Whether you use an existing account from your organization or create a new one, the account must be on a paid plan and in good standing. For guidance on selecting an AWS account for AWS Partner Central, see [account selection guidance](https://docs.aws.amazon.com/partner-central/latest/getting-started/aws-account-selection.html).
+ **Access credentials and permissions for your AWS account** — You need credentials and permissions to log into the AWS account. After registration, you'll also need specific permissions to access AWS Partner Central and Marketplace data. Work with your IAM Administrator to grant you [AWSPartnerCentralFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.html) and [AWSMarketplaceSellerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.html).

## Working with your IAM Administrator
<a name="working-with-iam-admin"></a>

You will need to get the AWS account access and permissions needed to proceed with AWS Partner Central registration. Normally you will need help from your organization's IAM Administrator. IAM Administrators typically work in IT Security, Information Security, or dedicated IAM teams within Governance and Compliance organizations. If you're unsure who your IAM Administrator is, reach out to your IT department or whoever manages your company's AWS accounts or teams who have AWS accounts (for example, the AWS Marketplace team).

Your IAM Administrator will need to:
+ Provision access to the selected AWS account for the person performing the registration (the 'alliance lead').
+ Set up the appropriate permissions using AWS managed policies for AWS Partner Central users.

You will become the primary contact managing the AWS Partner Central account upon successful registration.

After you have access to your AWS account, you can start the [registration process](https://docs.aws.amazon.com/partner-central/latest/getting-started/registration-process.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
