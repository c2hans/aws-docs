---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

If you have previously deployed the solution, follow this procedure to update the solution’s CloudFormation stack to get the latest features and enhancements. There are three parts to the upgrade process:
+  [Step 1: Update Deployment dashboard](#update-deployment-dashboard)
+  [Step 2: Migrate use case configurations](#migrate-use-case-configurations)
+  [Step 3: Update use cases](#update-use-cases)

**Note**
In v2.0.0, integration with Anthropic and Hugging Face was deprecated in favor of Amazon Bedrock and Amazon SageMaker AI. You can deploy models available through Hugging Face through SageMaker JumpStart. Refer to [Use Hugging Face with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/hugging-face.html) for more details.
Ensure you test the update process in a non-production environment before running these steps.

## Step 1: Update Deployment dashboard
<a name="update-deployment-dashboard"></a>

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing CloudFormation stack, and select **Update**.

1. Select **Replace current template**.

1. Under Specify template:

   1. Select **Amazon S3 URL**.

   1. Copy the latest [CloudFormation template](https://solutions-reference.s3.amazonaws.com/generative-ai-application-builder-on-aws/latest/generative-ai-application-builder-on-aws.template) link.

   1. Paste the link in the **Amazon S3 URL** box.

   1. Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. For details about the parameters, see [Step 1: Launch the Deployment dashboard stack](step-1-launch-the-deployment-dashboard-stack.md).

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create IAM resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive an UPDATE\_COMPLETE status in approximately 10 minutes.

If the existing Solution version was prior to v2.0.0, updating will create a web UI stack (which replaces the `amplify-ui` implementation of the login screen with a Cognito hosted UI) and a new CloudFront URL, which can be obtained from the Output section of the CloudFormation console once the stack status is UPDATE\_COMPLETE.

**Note**
Existing use cases created using versions prior to v2.0.0 will NOT be displayed until you complete the steps outlined below.

## Step 2: Migrate use case configurations (Only updates from versions below 2.0.0)
<a name="migrate-use-case-configurations"></a>

The schema for storing and the AWS service to store use case configuration has changed in version 2.0.0. Follow the steps described in [GAAB v2 Migration User Guide](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/tree/main/docs/migration/migration.md) using the [gaab\_v2\_migration.py](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/blob/main/source/scripts/v2_migration/gaab_v2_migration.py) script. After you run the script, you can access the Deployment dashboard to view the deployed use cases.

**Note**
You must follow the steps below to complete migrating the use cases.

## Step 3: Update use cases
<a name="update-use-cases"></a>

You can edit the deployed use cases with new features available in the latest versions of GAAB. See [Use the solution](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/use-the-solution.html) for information about how to use the features in this solution.

To update use cases to the latest version, you must complete the `Edit`use case steps in the Deployment dashboard (although you might not make any changes). This action triggers a CloudFormation stack update with the latest template version.

**Note**
Use cases created with 1.x or 2.x versions of the solution might not work with later versions. Hence, we recommend cloning existing use cases created with versions prior to v3.0.0 through the Deployment dashboard. Then, gradually migrate and replace with new use cases created using v3.0.0 or later.
