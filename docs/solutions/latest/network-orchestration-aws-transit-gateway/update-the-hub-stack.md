---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/update-the-hub-stack.html
---

# Update the hub stack(s)
<a name="update-the-hub-stack"></a>

Follow the step-by-step instructions in this section to update the hub stack(s).

## Hub stack
<a name="hub-stack-update"></a>

**Important**
To mitigate the `AlreadyExists` error code for the service-linked role (**AWSServiceRoleForResourceAccessManager**) in the hub stack, we moved the role to a separate stack for v3.3.1. This way, you can upgrade the hub stack in multiple Regions. You must deploy the service-linked role for AWS RAM hub stack *after* updating the hub stack.

Follow the step-by-step instructions in this section to update the hub stack.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Network Orchestration for AWS Transit Gateway CloudFormation stack, and select **Update**.
**Note**
This Guidance was previously called Serverless Transit Network Orchestrator.

1. Select **Replace current template**.

1. Under **Specify template**:

   1. Select **Upload a template file**.

   1. Choose **Choose file** and upload the `network-orchestration-hub.template` from `./deployment/global-s3-assets/`. To build the templates from source, see [Step 1: Build deployment assets](step-1-build-deployment-assets.md).

   1. Choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. For details about the parameters, see [Step 4: Launch the hub stack](step-4-launch-the-hub-stack.md).
**Important**
To successfully upgrade from an earlier version to version 3.3.0 or later, provide input for the two required parameters for the hub stack: **Cognito Domain Prefix** and **Allow Listed Ranges**.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a UPDATE\_COMPLETE status in approximately 25 minutes.

## Service-linked role for AWS RAM hub stack
<a name="service-linked-role-for-hub-stack-update"></a>

The hub stack deletes the **AWSServiceRoleForResourceAccessManager** service-linked role. Re-deploy the service-linked role using [Step 3](step-3-launch-the-service-linked-role-hub-stack-optional.md) of **Deploy the Guidance**.
