---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/option-2-deploy-on-new-aws-govcloud-us-accounts.html
---

# Option 2: Deploy on new AWS GovCloud (US) accounts
<a name="option-2-deploy-on-new-aws-govcloud-us-accounts"></a>

Deploying the solution in this pattern allows users to have workloads in AWS GovCloud (US) Regions only. The standard Region on the left is used to create AWS GovCloud (US) using Service Catalog.

**Note**
This deployment assumes that you want to limit your use of standard AWS Regions, and it includes steps to incorporate AWS Organizations SCPs that limit what the AWS standard accounts can do. If you also want to use standard AWS Regions (such as a US DoD customer that wants to run IL2 workloads in AWS US East/West Regions and IL4/IL5 workloads in AWS GovCloud [US] Regions through a shared AWS standard Management billing account), AWS recommends that you create new AWS standard accounts specifically for AWS standard Region usage.

 **Architecture diagram depicting AWS GovCloud (US) account deployment.**

![image11](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/image11.png)

## Step 1. Launch the stack
<a name="step-1.-launch-the-stack-1"></a>

1. Ensure that all [prerequisites](prerequisites.md) are complete. Ensure that you’ve set up AWS Organizations and that the account where the stack is launched can run the `CreateGovCloudAccount` API. See For AWS Organizations based installation (without AWS Control Tower) for more information.

1. Sign in to the AWS Management Console of your organization’s management account and select the following button to launch the `AWSAccelerator-GovCloudAccountVending` AWS CloudFormation template.

    [![View Template](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/view-template.png)](https://s3.amazonaws.com/solutions-reference/landing-zone-accelerator-on-aws/latest/AWSAccelerator-GovCloudAccountVending.template) **AWSAccelerator-GovCloudAccountVending.template** - Use this template to launch the AWS GovCloud (US) account vending component.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. We recommend you name your stack `AWSAccelerator-GovCloudAccountVending` to match the naming convention used for additional stacks that the solution creates. For information about naming character limitations, refer to [IAM and STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *AWS Identity and Access Management User Guide*.

1. Choose **Next**.

1. On the Configure stack options page, choose Next.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create stack** to deploy the stack.

## Step 2. Use Service Catalog to launch the product
<a name="step-2-use-aws-service-catalog-to-launch-the-product"></a>

1. In the AWS Management Console upper left section, select **Services** and then select **Service Catalog**.

1. Ensure that the in-use IAM resource that has permissions to access the portfolio **Landing Zone Accelerator on AWS**. Refer to [Grant Access to Users](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html) in Service Catalog Administrator Guide.

1. In the left-hand navigation menu, under **Provisioning**, choose **Products**.

1. In **Products**, choose a Landing Zone Accelerator on AWS - GovCloud Account Vending product and then **Launch product**.

1. In **Provisioned product name**, enter or generate a name (for example, `Landing_Zone_Accelerator_GovCloud_Account_LogArchive`).

1. In **Product versions**, choose a version of the product (for example, v1.0.0).

1. In **Parameters**, specify the following parameters:
   +  **Account Name** - Name of account (for example, `Accelerator Log Archive` Account)
   +  **Account Email** - Valid email address (for example, `example+log-archive@amazon.com`)
   +  **Organization Role Name** - Name of the IAM role that AWS Organizations automatically pre-configures in the new member accounts in both the AWS GovCloud (US) Regions and in the standard Region (for example, `OrganizationAccountAccessRole`)

1. Choose **Launch product**.

1. On the **Review** page, review the configuration information, and select **LAUNCH**. This creates a CloudFormation stack. The initial status of the product is shown as **Under change**. Wait for about ten minutes, and then refresh the screen until the status changes to **AVAILABLE**.

## Step 3. Get account IDs
<a name="step-3.-get-account-ids"></a>

1. In the AWS Management Console upper left section, select **Services** and then select **Service Catalog**.

1. In the left-hand navigation menu, under **Provisioning**, choose **Provisioned products**.

1. In **Provisioned Products**, choose the product that you created in step 3.8.

1. Choose **Events**.

1. Under the **Provisioned products** output, get the `GovCloudAccountId` and `AccountId`, which correspond to the AWS GovCloud (US) account ID and standard account ID, respectively.

## Step 4. Deploy the solution in your AWS GovCloud (US) Management account
<a name="step-4.-deploy-the-solution-in-your-aws-govcloud-us-management-account"></a>

**Important**
Ensure that the [prerequisites](prerequisites-1.md) have been completed.

1. Log in to the AWS GovCloud (US) Management account.

1. Deploy the solution by following [Step 2 of Option 1](option-1-deploy-to-new-standard-and-aws-govcloud-us-accounts.md#step-2.-deploy-the-solution-in-your-aws-govcloud-us-management-account).

1. To add more accounts:

   1. Follow [Step 2](#step-2-use-aws-service-catalog-to-launch-the-product) and [Step 3](#step-3.-get-account-ids) of [Option 2](#option-2-deploy-on-new-aws-govcloud-us-accounts).

   1. Follow [Step 4 ](option-1-deploy-to-new-standard-and-aws-govcloud-us-accounts.md#step-4.-configure-solution-in-aws-govcloud-us-regions-to-manage-new-accounts)of [Option 1](option-1-deploy-to-new-standard-and-aws-govcloud-us-accounts.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
