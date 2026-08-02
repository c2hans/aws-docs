---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/step-3-launch-the-orgmanagement-stack.html
---

# Step 3: Launch the Org-Management stack
<a name="step-3-launch-the-orgmanagement-stack"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your Organizations management account.

 **Time to deploy:** Approximately 5 minutes

1. Sign in to the AWS Management Console and select the button to launch the `account-assessment-for-aws-organizations-org-management.template` CloudFormation template.

    [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/account-assessment-for-aws-organizations/latest/account-assessment-for-aws-organizations-org-management.template&redirectId=ImplementationGuide](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/account-assessment-for-aws-organizations/latest/account-assessment-for-aws-organizations-org-management.template&redirectId=ImplementationGuide)

1. Launch in the same region as the Hub stack.

| Parameter | Default | Description |
| --- | --- | --- |
|  **Solution Setup**  |  |  |
| Enter the namespace value you chose for the Hub stack. |  {{<Requires input>}}  | Unique string used as prefix for resource names. NOTE: Use the same namespace in the Hub stack and Spoke stack. |
| Provide the Hub Account Id |  {{<Requires input>}}  | ID of the AWS account where the Hub stack of this solution is deployed. |
|  **Application Manager Configuration**  |  |  |
| Create Resource Association |  `Yes`  | Select `No` if you did not provide Application Manager Configuration details in the Hub stack. |

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the CloudFormation console in the **Status** column. You should receive a `CREATE_COMPLETE` status in approximately five minutes.
