---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/update-the-organization-role-stack-optional.html
---

# Update the organization role stack (optional)
<a name="update-the-organization-role-stack-optional"></a>

Follow the step-by-step instructions in this section to update the organization role stack for your Organizations management account.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Network Orchestration for AWS Transit Gateway CloudFormation stack, and select **Update**.
**Note**
This Guidance was previously called Serverless Transit Network Orchestrator.

1. Select **Replace current template**.

1. Under **Specify template**:

   1. Select **Upload a template file**.

   1. Choose **Choose file** and upload the `network-orchestration-organization-role.template` from `./deployment/global-s3-assets/`. To build the templates from source, see [Step 1: Build deployment assets](step-1-build-deployment-assets.md).

   1. Choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. For details about the parameters, see [Step 2: Launch the organization role stack (optional)](step-2-launch-the-organization-role-stack-optional.md).

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a UPDATE\_COMPLETE status in approximately three to four minutes.
