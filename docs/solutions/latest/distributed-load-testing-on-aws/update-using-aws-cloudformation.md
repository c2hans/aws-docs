---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/update-using-aws-cloudformation.html
---

# Update using AWS CloudFormation
<a name="update-using-aws-cloudformation"></a>

If you have previously deployed the solution, follow this procedure to update the CloudFormation stack to the latest version.

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing CloudFormation stack, and select **Update stack**.

1. Select **Make a direct update**.

1. Select **Replace existing template**.

1. Under **Specify template**:

   1. Select **Amazon S3 URL**.

   1. Copy the link of the [latest template](https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template).

   1. Paste the link in the **Amazon S3 URL** box.

   1. Verify that the correct template URL shows in the **Amazon S3 URL** text box.

   1. Choose **Next**.

   1. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. Refer to [Launch the stack](launch-the-stack.md) for details about the parameters.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings.

1. Select the box acknowledging that the template might create IAM resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a `UPDATE_COMPLETE` status in approximately 15 minutes.

**Note**
If you experience Amazon Cognito authentication issues while logging in from your browser after stack upgrade, please refresh your browser (Ctrl\+Shift\+R on Windows/Linux or Cmd\+Shift\+R on Mac) to clear cached data and try again.
