---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/use-the-demo-ui.html
---

# Use the demo UI
<a name="use-the-demo-ui"></a>

The solution provides an optional demo UI that you can deploy into your AWS account to display basic capability and functionality. With this UI, you can interact directly with the new image handler using images from the specified Amazon S3 buckets in your account.

 **Screenshot of demo UI showing image source, original image, editing options, preview, code, and encoded URL.**

![Screenshot of the demo UI showing an example image transformation](http://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/demo-ui-example.png)

Follow this procedure to experiment with the supported image editing features, preview the results, and create example URLs that you can use in your applications:

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Select the solution’s installation stack.

1. Choose the **Outputs** tab, and then select value for the **DemoUrl** key. The Dynamic Image Transformation for Amazon CloudFront Demo UI opens in your browser.

1. In the **Image Source** card, perform the following actions:

   1. Specify a bucket name to use for the demo. The bucket you specify must be listed in the `SOURCE_BUCKETS` environment variable of the AWS Lambda function.

   1. Specify an image key to use for the demo. You must include the file extension in the key.

1. Select **Import**. The original image appears in the **Original Image** card.

1. In the **Editor** card, adjust the image settings, and select **Preview** to generate the modified image. You can select **Reset** to revert the settings back to their original values.

**Note**
The Dynamic Image Transformation for Amazon CloudFront demo UI offers a limited set of image edits and doesn’t include the full scope of capabilities offered by the Image Handler API and the image URL signature. We recommend using your own [frontend application](use-the-solution-with-a-frontend-application.md) for image modification.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
