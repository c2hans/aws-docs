---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses [CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation templates specify the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the templates.

Before you launch the automated deployment, review the architecture and other considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the Quota Monitor for AWS into your account.

 **Time to deploy:** Approximately five minutes.

## Prerequisites
<a name="prerequisites"></a>
+ If you are using AWS Organizations, you can deploy `quota-monitor-prerequisite.template` to fulfill needed prerequisites. For detailed instructions, refer to [Step 2a: Launch the prerequisite stack (optional)](step-2a.-launch-the-prerequisite-stack-optional.md).
+ To support quota usage monitoring with Trusted Advisor, each account must have a Business- or Enterprise-level [Support](https://aws.amazon.com/premiumsupport/) plan to gain access to the Trusted Advisor service quota checks.
+ To use this solution’s Slack notification functionality, you must have an existing Slack channel.

**Important**
When deploying this solution across multiple account types (management, designated administrator for CloudFormation StackSets, and spoke accounts), ensure that the opted-in Regions overlap across all involved accounts. If the hub account has [opt-in Regions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-considerations) that are not enabled in the spoke accounts, the solution will attempt to deploy in those Regions. This will cause deployment failures in the spoke accounts and might prevent successful deployment in the common Regions. Ensuring this Region overlap is crucial for the successful deployment and operation of the solution across your organization.

## Deployment overview
<a name="deployment-overview"></a>

To deploy this solution, follow these steps:

 [Step 1: Choose your deployment scenario](step-1.-choose-your-deployment-scenario.md)

Choose the deployment scenario that meets your needs: AWS Organizations, hybrid, or AWS accounts that are not part of an AWS Organization.

 [Step 2a: Launch the prerequisite stack (optional)](step-2a.-launch-the-prerequisite-stack-optional)

Launch the prerequisite template in an Organizations management account to invoke a Lambda function that:
+ Checks that the Organizations **All Features** is activated.
+ Adds a member account as the designated administrator for CloudFormation StackSets.

  --Or--

 [Step 2b: Fulfill the prerequisites manually (optional)](step-2b.-achieve-prerequisites-manually-optional.md)
+ Fulfill the prerequisites needed for monitoring quotas across Organizations manually.

 [Step 3a. Launch the hub stack for AWS Organizations](step-3a.-launch-the-hub-stack-for-aws-organizations.md)

--Or--

 [Step 3b: Launch the hub stack for single account deployment](step-3b.-launch-the-hub-stack-for-single-account-deployment.md)
+ Launch the AWS CloudFormation template into an AWS account that is [registered as a delegated administrator for StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in your organization.
+ Enter values for the required parameters: **Deployment Configuration.**
+ Review the other template parameters and adjust if necessary.

 [Step 4a: Update the Systems Manager Parameter Store (Regions List)](step-4a.-update-systems-manager-parameter-store-regions-list.md)
+ Update Parameter Store with the `RegionToDeploy`.

 [Step 4b: Update the Systems Manager Parameter Store (OUs)](step-4b.-update-systems-manager-parameter-store-ous.md)
+ Update Parameter Store with the `OUs`.
+ Review StackSets instances.

 [Step 5: Launch the spoke notifications stacks (optional)](step-5.-launch-the-spoke-sns-stacks-when-not-using-aws-organizations-or-hybrid-environments.md)
+ Launch the components necessary to add decentralized notification into each account.

 [Step 6: Launch the spoke stacks (optional)](step-6.-launch-the-spoke-stacks-optional.md)
+ Launch the components necessary to monitor quotas in secondary accounts. Review the other template parameters and adjust if necessary.

 [Step 7: Configure notifications (optional)](step-7.-configure-notifications-optional.md)
+ Configure notification filtering.

 [Step 8. Configure Slack notifications (optional)](step-8.-configure-slack-notifications-optional.md)
+ Configure Slack for notifications.
+ Add the Slack webhook URL to the Systems Manager Parameter Store.

**Important**
This solution includes data collection. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
