---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/cost-considerations.html
---

# Cost considerations
<a name="cost-considerations"></a>

 **Cost Considerations:** Lambda architecture incurs AWS Secrets Manager costs only when image URL signature feature is activated, and operational dashboard usage may fall under CloudWatch free tier. ECS architecture costs reflect continuous operation with minimum task counts, with auto-scaling increasing costs during high-traffic periods, and DynamoDB costs based on typical usage patterns. Additional costs may include Amazon S3 PUT/GET requests depending on caching effectiveness, Amazon Rekognition charges for smart cropping or content moderation features, external origin data transfer costs, and negligible Cognito costs for Admin UI authentication (typically under $1/month for single-user operation).

 *The operational dashboard included with the solution may fall under the free tier, refer to [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) for the most up to date pricing information. For information on how to disable the deployment of the operational dashboard, refer to .*

<a name="demo-ui-1"></a> **Demo UI**

If you choose to deploy the demo UI, the solution automatically deploys an additional CloudFront distribution and S3 bucket for storing the static website assets in your account. You are responsible for the incurred variable charges from these services. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

<a name="image-modification-and-analysis"></a> **Image modification and analysis**

This cost estimate doesn’t account for Amazon S3 `PUT` and `GET` requests, which can vary because modified images are cached in CloudFront, and because certain use cases require special-use capabilities such as smart cropping and content moderation with Amazon Rekognition. Using Amazon Rekognition features may incur additional charges. For more information, see [Amazon Rekognition pricing](https://aws.amazon.com/rekognition/pricing/).

There is no additional cost for using `sharp`, which is an open source library.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
