---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

If you have previously deployed the solution, follow this procedure to update the solution’s CloudFormation stack to get the latest version of the solution’s framework.

1. From the main account where the solution is deployed, sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Video on Demand on AWS CloudFormation stack, and select **Update**.

1. Select **Replace current template**.

1. Under Specify template:

   1. Select **Amazon S3 URL**.

   1. Copy the link of the `video-on-demand-on-aws.template` [AWS CloudFormation template](aws-cloudformation-template.md) .

   1. Paste the link in the **Amazon S3 URL** box.

   1. Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. For details about the parameters, see [Launch the Stack](launch-the-stack.md).

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a UPDATE\_COMPLETE status in approximately 20 minutes.
