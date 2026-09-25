---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-2-launch-the-organization-role-stack-optional.html
---

# Step 2: Launch the organization role stack (optional)
<a name="step-2-launch-the-organization-role-stack-optional"></a>

Follow the step-by-step instructions in this section to configure and deploy the organization role stack into your Organizations management account. This optional step helps you add a OU path and VPC name in the attachment tags for tracking and auditing.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home) with your AWS Organizations management account.

1. Choose **Create stack**, then choose **With new resources (standard)**.

1. On the **Create stack** page, select **Upload a template file**, choose **Choose file**, and upload `network-orchestration-organization-role.template` from `./deployment/global-s3-assets/`.

1. Choose **Next**.

1. Launch this template in the same Region as you plan to launch the hub and spoke templates.

1. On the **Specify stack details** page, assign a name to your stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. For **Parameters**, review the parameters for the template and modify them as necessary. This stack uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>HubAccount</td><td> {{&lt;Requires input&gt;}} </td><td>The account ID for the hub account.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should see a status of **CREATE\_COMPLETE** in approximately three to four minutes.

**Note**
After the stack deploys, record the ARN for the role from the **Outputs** tab of the stack. You need this ARN as input for the **Account List or AWS Organizations ARN** parameter in the hub template.
