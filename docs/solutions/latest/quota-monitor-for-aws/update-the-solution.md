---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

If you previously deployed the solution, follow these procedures to get the latest version of the solution’s framework.

## Update to v6.1.0 or later
<a name="update-to-v6.1.0"></a>

Starting from version 6.1.0 of the solution, we used [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) on the spoke stacks, which previously used [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk). The hub stacks still use customer managed keys. This helps your cost because AWS managed keys don’t incur the monthly storage fee that customer managed keys incur.

Updating the stack and the StackSet instances, or deleting them, won’t delete the customer managed keys. You must manually delete the following customer managed keys after updating the solution from a version that uses customer managed keys, or after deleting the solution:
+ One customer managed key for the hub stack.
+ One customer managed key per account, per AWS Region, for the spoke stack.

## Update the hub stack
<a name="update-the-hub-stack"></a>

Use the following procedure to update your main AWS CloudFormation stack to the current version.

1. From your main account where the Quota Monitor for AWS hub template deployed, sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. From the **Stacks** page, select your Quota Monitor for AWS hub stack and choose **Update**.
**Note**
Take a note of the parameter **Account List**. You’ll need this later to complete the update process.

1. On the **Update stack** page, verify that **Replace current template** is selected.
   + In the **Specify template section, select \*Amazon S3 URL**.
   + Copy the link of the [latest template](aws-cloudformation-templates.md) for `quota-monitor-hub.template`.
   + Paste the link in the **Amazon S3 URL** box.
   + Verify that the correct template URL shows in the **Amazon S3 URL** box, and choose **Next**.

1. On the **Specify stack details** page, under **Parameters**, review the parameters for the template and modify them as necessary. Refer to [Step 4a. Update the Systems Manager Parameter Store (Regions list)](step-4a.-update-systems-manager-parameter-store-regions-list.md) for details about the parameters.
**Note**
When updating the SNS Spoke Region parameter:
   + Specify only one Region. If you provide multiple Regions, StackSet instances won’t deploy, and you’ll see warnings in the deployment manager logs.
   + Changing this parameter doesn’t initiate an immediate deployment or redeployment of the SNS spoke stack.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should see a status of **UPDATE\_COMPLETE** in approximately five minutes.

Once the stack status is **UPDATE\_COMPLETE**, follow these additional steps:

1. Update the `/QuotaMonitor/Accounts` Systems Manager Parameter Store with the **Account List** value copied earlier.

1. If you opted-in for Amazon SNS email notifications, you should receive email to confirm subscription.

After updating the hub stack, especially when changing the SNS Spoke Region, follow these steps:

1. Open the AWS Systems Manager console.

1. Go to Parameter Store.

1. Locate and update (or resave without making changes) the parameter for OUs (/QuotaMonitor/OUs) or Accounts (/QuotaMonitor/Accounts), depending on your deployment model. This action triggers the deployment manager to:
   + Deploy the SNS spoke stack in the new Region.
   + Remove the SNS spoke stack from the old Region (if applicable).

## Impact on SageMaker AI and Amazon Connect monitoring during stack updates
<a name="impact-on-sagemaker-and-connect-monitoring-during-stack-updates"></a>

In the Hybrid/OU model, when you update the hub stack, changes to the **SageMaker AI Monitoring** and **Connect Monitoring** parameters affect your deployment as follows:

1. If you modify the SageMaker AI Monitoring or Connect Monitoring parameters during the update, the new settings will apply to all spoke accounts.

1. If you leave these parameters unchanged during the update:
   + Existing spoke accounts will retain their current SageMaker AI and Amazon Connect monitoring settings.
   + New spoke accounts added after the update will inherit the current stack-level monitoring settings.

1. If you change the **SageMaker AI Monitoring** and **Connect Monitoring** parameters during the update, any spoke account-specific monitoring changes made for the two services in the Service DynamoDB table will be overwritten.

To preserve account-specific monitoring settings while updating other aspects of the stack, leave the SageMaker AI Monitoring and Connect Monitoring parameters unchanged during the update.

## Update the spoke stack if you aren’t using Organizations
<a name="update-the-spoke-stack"></a>

The solution previously did not support Organizations. If you are continuing with that model where your hub account is an independent account and not part of an organization, then follow instructions in this section. If you decide to use Organizations, then follow the launch steps in [Step 1. Choose your deployment scenario](step-1.-choose-your-deployment-scenario.md).

This section provides instructions for updating the hub and spoke CloudFormation stacks if you don’t use Organizations.

**Note**
When deleting a stack, your information in DynamoDB will not be deleted, and you will continue to incur costs until you delete the DynamoDB tables.

When you deploy the solution without Organizations, use the following procedure to update the spoke CloudFormation stack in your secondary accounts to the current version of `quota-monitor-ta-spoke.template` or `quota-monitor-sq-spoke.template`.

1. From your secondary account where the Quota Monitor for AWS spoke template is deployed, sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. From the **Stacks** page, select your primary Quota Monitor for AWS stack and choose **Update**.

1. On the **Update stack** page, verify that **Replace current template** is selected.

1. In the **Specify template** section, select **Amazon S3 URL**.

1. Copy the link of the [latest template](aws-cloudformation-templates.md) for `quota-monitor-ta-spoke.template` or `quota-monitor-sq-spoke.template`.

1. Paste the link in the **Amazon S3 URL** box.

1. Verify that the correct template URL shows in the **Amazon S3 URL** box and choose **Next**.

1. On the **Specify stack details** page, under **Parameters**, review the parameters for the template and modify them as necessary. Refer to [Step 6. Launch the spoke stacks](step-6.-launch-the-spoke-stacks-optional.md) for details about the parameters.
**Note**
You can copy the EventBridge bus ARN from the **Outputs** section of the hub stack.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **View** **change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

Repeat these steps to update additional secondary accounts containing the spoke template.

## Update or edit the spoke StackSets if you are using Organizations
<a name="update-if-you-are-using-organizations"></a>

When you deploy the solution in an organization, edit the StackSet details to update the spoke stacks in one operation. With the v6.0.0 release, there are two spoke templates; previous release had one spoke template. The two spoke templates individually own and provision resources needed to support Trusted Advisor and Service Quotas checks.

Use the following procedure to update the spoke AWS CloudFormation stack in your secondary accounts to the current version of `quota-monitor-ta-spoke.template` or `quota-monitor-sq-spoke.template`.

1. From your monitoring account where the Quota Monitor for AWS spoke template is deployed, sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. From the **StackSets** page, select your primary Quota Monitor for AWS stack and choose **Edit StackSet details**.

1. On the **Update stack** page, verify that **Replace current template** is selected.
   + In the **Specify template** section, select **Amazon S3 URL**.
   + Copy the link of the [latest template](aws-cloudformation-templates.md) for `quota-monitor-ta-spoke.template` or `quota-monitor-sq-spoke.template`.
   + Paste the link in the **Amazon S3 URL** box.
   + Verify that the correct template URL shows in the **Amazon S3 URL** box, and choose **Next**.

1. On the **Specify stack details** page, under **Parameters**, review the parameters for the template and modify them as necessary.
**Note**
You can copy the EventBridge bus ARN from the **Outputs** section of the hub stack.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Set deployment options** page:
   + Specify organization unit ID(s)
   + Specify AWS Regions
   + Specify deployment options

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the update.

You can update stacks in secondary accounts directly within those accounts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
