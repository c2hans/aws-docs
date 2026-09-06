---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

If you have previously deployed the solution, follow this procedure to update the Cost Optimizer for Amazon WorkSpaces on AWS CloudFormation stack to get the latest version of the solution’s framework.

1. Log in to [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home), select your existing `workspaces-cost-optimizer `CloudFormation stack, and select Update. stack, and choose **Update**.

1. Select **Replace current template**.

1. Under **Specify template:**
   + Select Amazon S3 URL
   + Copy the link of the `cost-optimizer-for-amazon-workspaces.template` [AWS CloudFormation](templates.md) template.
   + Paste the link in the **Amazon S3 URL** box.
   + Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. Refer to [Step 1: Launch the stack](deploy-the-solution.md) for details about the parameters.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Be sure to check the box acknowledging that the template might create (IAM) resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a `UPDATE COMPLETE` status in approximately 15 minutes.
