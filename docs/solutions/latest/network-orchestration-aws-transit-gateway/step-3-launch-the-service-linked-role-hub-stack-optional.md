---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-3-launch-the-service-linked-role-hub-stack-optional.html
---

# Step 3: (Optional) Launch the service-linked role for AWS RAM hub stack
<a name="step-3-launch-the-service-linked-role-hub-stack-optional"></a>

Follow the step-by-step instructions in this section to configure and deploy the optional service-linked role for AWS RAM hub stack into your hub account.

**Important**
This stack deploys the service-linked role for AWS RAM. AWS RAM uses the service-linked role named `AWSServiceRoleForResourceAccessManager` when you enable sharing with AWS Organizations. This role grants permissions to the AWS RAM service to view organization details, such as the list of member accounts and which organizational units each account is in.
This stack is optional because it fails if the role already exists in the hub account. You can validate if this roles exists by signing in to the IAM console, selecting **Roles** from the navigation menu, and entering `AWSServiceRoleForResourceAccessManager` in the search box. If this role already exists, skip this step.
The stack deployment will fail with following details in the CloudFormation events if it already exists.
Error Code: `AlreadyExists`
Message: `Service role name AWSServiceRoleForResourceAccessManager has been taken in this account.`

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home) with your AWS network hub account.

1. Choose **Create stack**, then choose **With new resources (standard)**.

1. On the **Create stack** page, select **Upload a template file**, choose **Choose file**, and upload `network-orchestration-hub-service-linked-roles.template` from `./deployment/global-s3-assets/`.

1. Choose **Next**.

1. Launch this template in the same Region as the hub template.

1. On the **Specify stack details** page, assign a name to your stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should see a status of **CREATE\_COMPLETE** in approximately three to four minutes.
