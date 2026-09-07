---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/update-the-spoke-stacks.html
---

# Update the spoke stack(s)
<a name="update-the-spoke-stacks"></a>

Follow the step-by-step instructions in this section to update the spoke stacks.

## Spoke stack
<a name="spoke-stack-update"></a>

**Important**
The service-linked role for Transit Gateway (`AWSServiceRoleForVPCTransitGateway`) has been consolidated into the spoke stack. During the stack update, a custom resource checks whether the role already exists. If the role exists, creation is skipped. If the role does not exist, it is created automatically.

Follow the step-by-step instructions in this section to update the spoke stack(s) for your spoke account(s).

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Network Orchestration for AWS Transit Gateway CloudFormation stack, and select **Update**.
**Note**
This solution was previously called Serverless Transit Network Orchestrator.

1. Select **Replace current template**.

1. Under **Specify template**:

   1. Select **Amazon S3 URL**.

   1. Copy the link of the `network-orchestration-spoke.template` [CloudFormation template](aws-cloudformation-templates.md).

   1. Paste the link in the **Amazon S3 URL** box.

   1. Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. For details about the parameters, see [Step 4: Launch the spoke stack(s)](step-4-launch-the-spoke-stacks.md).

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a UPDATE\_COMPLETE status in approximately three to four.

## Upgrade from nested stack to consolidated spoke stack.
<a name="upgrade-nested-to-consolidated-spoke"></a>

If you are upgrading to the latest version from any version between 3.3.11 and 3.3.22, follow these steps to migrate the spoke template from a nested stack to a consolidated spoke stack.

1. Delete the spoke stack.
   + If the role is in use, the deletion fails. Select **Retain resource** for `TransitGatewayServiceLinkedRole` and delete the stack.
![DELETE_FAILED state for TransitGatewayServiceLinkedRole](https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/delete-failed.png)
   + If the role is not in use, the stack deletion cleans up the role.

1. Deploy the spoke template with the latest version. For details, see [Step 4: Launch the spoke stack(s)](step-4-launch-the-spoke-stacks.md).
