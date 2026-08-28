---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-account.html
---

# Step 1: Create an AWS Account
<a name="getting-started-create-account"></a>

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

If you want to use an existing AWS account, ensure that it uses an AWS region that is supported for Amazon IVS:

1. Navigate to the [Amazon IVS Console](https://console.aws.amazon.com/ivs). If you see the usual IVS console page (showing "Global Solution, regional content"), you’re fine; skip to [Step 2: Set Up IAM Permissions](getting-started-iam-permissions.md). If you are redirected to an AWS "unsupported region" page, you need to select a new region.

1. Select the appropriate tab (**Live streaming**, for IVS; **Stream chat**, for IVS Chat), then select one of the listed regions. *Note which region you choose; you will need it later*.

At any time, you can view your AWS account activity and manage your account by going to [https://aws.amazon.com/](https://aws.amazon.com/) and choosing **My Account**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
