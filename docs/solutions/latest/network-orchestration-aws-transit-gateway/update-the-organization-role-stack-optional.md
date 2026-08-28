---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/update-the-organization-role-stack-optional.html
---

# Update the organization role stack (optional)
<a name="update-the-organization-role-stack-optional"></a>

Follow the step-by-step instructions in this section to update the organization role stack for your Organizations management account.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Network Orchestration for AWS Transit Gateway CloudFormation stack, and select **Update**.
**Note**
This solution was previously called Serverless Transit Network Orchestrator.

1. Select **Replace current template**.

1. Under **Specify template**:

   1. Select **Amazon S3 URL**.

   1. Copy the link of the `network-orchestration-organization-role.template` [CloudFormation template](aws-cloudformation-templates.md).

   1. Paste the link in the **Amazon S3 URL** box.

   1. Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. For details about the parameters, see [Step 1: Launch the organization role stack (optional)](step-1-launch-the-organization-role-stack-optional.md).

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a UPDATE\_COMPLETE status in approximately three to four minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
