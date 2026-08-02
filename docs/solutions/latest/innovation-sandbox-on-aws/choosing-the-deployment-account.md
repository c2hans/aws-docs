---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/choosing-the-deployment-account.html
---

# Choosing the deployment accounts
<a name="choosing-the-deployment-account"></a>

## Accounts
<a name="accounts"></a>

To deploy this solution, you will need access to these accounts.

 **Organizations Management account**

The **AccountPool** stack, deployed into the AWS Organizations management account, is used to manage the lifecycle on sandbox accounts controlled by the solution.

This stack consists of a single IAM role that will be assumed by the Hub stack’s Lambda function and grants minimal required permissions to access data of the Organization. The permissions on this role are least privileged to only allow read actions from Cost Explorer, read actions on the account pool OUs, and move account actions on the account pool OUs. The trust policy on the role only allows for a single Intermediate IAM role from the Compute stack to assume into it.

 **IAM IDC account**

The **IAM Identity Center (IDC)** stack deployed into the AWS Account containing the organizations AWS IAM Identity Center instance, is used to manage the solution web UI and sandbox account access.

This stack initializes user groups and corresponding permission sets in the instance that administrators can manually add users to. The IDC stack also contains an IAM Role. The permissions on this role are least privileged to only allow the actions required by the solution. The trust policy on the role only allows for a single Intermediate IAM role from the Compute stack to assume into it.

 **Hub account**

The **Data** and **Compute** stacks contain all data, compute, and storage resources for the solution to serve the frontend application, handle API requests, facilitate scans, and manage the account lifecycle.

Select a member account within your AWS Organization to deploy these stacks. This account will have administrative access to the spoke accounts to enable the Account Cleaner component for account recycling operations. Due to these elevated permissions, treat the Hub account as a highly sensitive asset. We strongly recommend using a dedicated account with stringent access controls and limiting the number of users who can access it. Implement robust security measures to protect this account, similar to accounts you would use for your most critical AWS environments.

**Important**
We do not recommend using the Organizations Management account to keep the management account free from operational workloads.

 **Sandbox account**

The **SandboxAccount** stack is automatically configured as a service-managed StackSet resource in the AccountPool stack, using the **AccountPool OU** as the deployment target. This stack contains a single **Spoke** role, which is crucial for the account clean-up process. The Spoke role is automatically created by the service-managed StackSet after onboarding the sandbox accounts. It is assumed by compute resources in the Compute stack to run the account clean-up job.

**Important**
These sandbox accounts are strictly intended for non-production usage and should never run production workloads.

## Home Region
<a name="home-region"></a>

Identifying the home Region is crucial for the successful deployment of the ISB solution. For the solution to work as expected:
+ Deploy all four stacks in the same Region.
+ Enable IDC in the same home Region. Identify the Region where IDC is enabled in your AWS Organization, as this will be the home Region for for the ISB solution.

**Note**
The home Region is only for deployment resources. The sandbox accounts can use any Regions that are defined in the managed Regions list (CFN Param).
