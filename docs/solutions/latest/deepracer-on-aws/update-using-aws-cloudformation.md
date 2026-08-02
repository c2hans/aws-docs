---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/update-using-aws-cloudformation.html
---

# Update using AWS CloudFormation
<a name="update-using-aws-cloudformation"></a>

If you have previously deployed the solution, follow this procedure to update the CloudFormation stack to the latest version.

1. Sign in to the AWS CloudFormation console, select your existing DeepRacer on AWS CloudFormation stack, and choose **Update**.

1. Select **Replace current template**.

1. Enter the appropriate Amazon S3 URL:
   + If using the default main template: `https://solutions-reference.s3.amazonaws.com/deepracer-on-aws/latest/deepracer-on-aws-main.template`

1. Under **Parameters**, review the parameters for the template and modify them as necessary.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Be sure to check the box acknowledging that the template might create AWS Identity and Access Management (IAM) resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a status in approximately 30 minutes.
