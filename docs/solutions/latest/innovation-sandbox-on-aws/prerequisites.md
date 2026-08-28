---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

Before launching the stacks, you must meet the following prerequisites:

1.  **Identify the AWS account where you want to deploy the solution**: Use the [AWS Management Console](https://console.aws.amazon.com/console/home) to identify and name this as the **Hub** account. We recommend you dedicate this account for running the solution with no other workloads running in the account.

1.  **Verify your home Region**: You must deploy all the stacks in the same AWS Region, and enable IAM Identity Center (IDC) in the same home Region. If you have already enabled IDC, use that Region as your home Region.

1.  **Ensure you have set up an [AWS Organizations](https://docs.aws.amazon.com/organizations/) organization to deploy the solution into**: AWS Organizations helps you centrally manage and govern your environment as you grow and scale your AWS resources. For more information on how to get started, refer to the [Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) tutorial.

1.  **Ensure you have enabled Service Control Policies with Organizations**: For more information, refer to [Managing organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html).

1.  **Ensure you have enabled and set up AWS IAM Identity Center**: [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) is used to centrally manage access to your AWS accounts and applications. Enable IAM Identity Center at the organizational level, either using the Organization Management account or a delegated administration account.
   + To enable IAM Identity Center, open the IAM Identity Center console, choose your home Region, and on the main page, for Enable IAM Identity Center, choose **Enable**.

1.  **Configure Amazon SES for the application to send email notifications**: Set up Amazon SES for the solution and request production access using the Hub account. For more information, see [Setting up Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/setting-up.html) and [Requesting production access](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html). You later configure the notification sender address on the **Settings** page of the web UI. The solution rejects the save unless that address (or its parent domain) is a verified identity in Amazon SES in the Hub account.

1.  **Enable resource sharing using AWS Resource Access Manager (RAM)**: For more information on how to set this up, refer to [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs).

1.  **Activate trusted access for AWS CloudFormation StackSets**: AWS CloudFormation StackSets extends the capability of stacks by allowing you to create, update, or delete stacks across multiple accounts and AWS Regions with a single operation. For more information on how to activate trusted access, refer to [Activate trusted access for stacksets with AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html).

1.  **Enable AWS Cost Explorer on the Org Management account**: Ensure that you have enabled AWS Cost Explorer for tracking costs. For more information, refer to [Enable Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html). Note that AWS Cost Explorer requires approximately 24 hours to be enabled for your account.

1.  **Dedicated AWS Lambda concurrent executions limit**: Use [AWS Service Quotas](https://console.aws.amazon.com/servicequotas/home/services/lambda/quotas/L-B99A9384) in your AWS console to verify your AWS Lambda concurrent executions.
   + The Applied quota value in your account should be greater than or equal to the AWS default quota value (which is 1000). If the Applied quota value is less than 1000, choose the **Request quota increase** button to request an increase to this value to at least 1000 before deploying the solution. For more information, refer to the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).

1.  **Ensure that all accounts used are members of the AWS Organization**: The deployment will fail if this is not the case.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
