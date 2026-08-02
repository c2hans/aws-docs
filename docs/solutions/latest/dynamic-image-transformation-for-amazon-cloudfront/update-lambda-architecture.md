---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/update-lambda-architecture.html
---

# Update Lambda architecture
<a name="update-lambda-architecture"></a>

Follow these steps to update an existing Lambda architecture deployment to the latest version:

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Dynamic Image Transformation for Amazon CloudFront CloudFormation stack, and select **Update**.

1. Select **Replace current template**.

1. Under **Specify template**:

   1. Select **Amazon S3 URL**.

   1. Copy the link of the `dynamic-image-transformation-for-amazon-cloudfront-lambda.template` [AWS CloudFormation template](aws-cloudformation-template.md).

   1. Paste the link in the **Amazon S3 URL** box.

   1. This link will point to the latest template by default, to modify which version you update to, replace the word `latest` with the desired version.

      1. For example: `https://solutions-reference.s3.amazonaws.com/dynamic-image-transformation-for-amazon-cloudfront/latest/dynamic-image-transformation-for-amazon-cloudfront-lambda.template` would become `https://solutions-reference.s3.amazonaws.com/dynamic-image-transformation-for-amazon-cloudfront/v8.0.0/dynamic-image-transformation-for-amazon-cloudfront-lambda.template`

**Note**
Alongside the rename in v7.0.0 from Serverless Image Handler to Dynamic Image Transformation for Amazon CloudFront, the location of the cloudformation template has changed, if you’d like to follow the above instructions for a version before v7.0.0, use the following template URL as a baseline: https://solutions-reference.s3.amazonaws.com/serverless-image-handler/latest/serverless-image-handler.template

1. Verify that the correct template URL shows in the *\*Amazon S3 URL\** text box, and choose **Next**. Choose **Next** again.

   1. Under **Parameters**, review the parameters for the template and modify them as necessary. For details about the parameters, see [Lambda architecture template parameters](lambda-parameters.md).

   1. Choose **Next**.

   1. On the **Configure stack options** page, choose **Next**.

   1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template creates IAM resources.

   1. Choose **View change set** and verify the changes.

   1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive an `UPDATE_COMPLETE` status in approximately 15 minutes.
