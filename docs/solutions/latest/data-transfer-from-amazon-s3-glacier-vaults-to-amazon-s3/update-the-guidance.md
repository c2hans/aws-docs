---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/update-the-guidance.html
---

# Update the Guidance
<a name="update-the-guidance"></a>

 If you have previously deployed the Guidance, follow this procedure to update the CloudFormation stack to get the latest version of the Guidance’s framework.

1.  Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Data Transfer from Amazon Glacier Vaults to Amazon S3 CloudFormation stack, and select **Update**.

1.  Select **Replace current template**.

1.  Under **Specify template**:

   1.  Select **Amazon S3 URL**.

   1.  Copy the link of the [latest template](https://solutions-reference.s3.amazonaws.com/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3.template).

   1.  Paste the link in the **Amazon S3 URL** box.

   1.  Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1.  Under **Parameters**, review the parameters for the template and modify them as necessary. For details about the parameters, see [Step 1: Launch the stack](step-1-launch-the-stack.md).

1.  Choose **Next**.

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review** page, review and confirm the settings. Select the box acknowledging that the template creates IAM resources.

1.  Choose **View change set** and verify the changes.

1.  Choose **Update stack** to deploy the stack.

 You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive an `UPDATE_COMPLETE` status in approximately 5-10 minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
