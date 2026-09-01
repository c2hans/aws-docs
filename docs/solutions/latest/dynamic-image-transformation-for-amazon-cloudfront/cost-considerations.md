---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/cost-considerations.html
---

# Cost considerations
<a name="cost-considerations"></a>

 **Cost Considerations:** Lambda architecture incurs AWS Secrets Manager costs only when image URL signature feature is activated, and operational dashboard usage may fall under CloudWatch free tier. ECS architecture costs reflect continuous operation with minimum task counts, with auto-scaling increasing costs during high-traffic periods, and DynamoDB costs based on typical usage patterns. Additional costs may include Amazon S3 PUT/GET requests depending on caching effectiveness, Amazon Rekognition charges for smart cropping or content moderation features, external origin data transfer costs, and negligible Cognito costs for Admin UI authentication (typically under $1/month for single-user operation).

 *The operational dashboard included with the solution may fall under the free tier, refer to [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) for the most up to date pricing information. For information on how to disable the deployment of the operational dashboard, refer to [Optional Mappings](optional-mappings.md).*

<a name="demo-ui-1"></a> **Demo UI**

If you choose to deploy the demo UI, the solution automatically deploys an additional CloudFront distribution and S3 bucket for storing the static website assets in your account. You are responsible for the incurred variable charges from these services. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

<a name="image-modification-and-analysis"></a> **Image modification and analysis**

This cost estimate doesn’t account for Amazon S3 `PUT` and `GET` requests, which can vary because modified images are cached in CloudFront, and because certain use cases require special-use capabilities such as smart cropping and content moderation with Amazon Rekognition. Using Amazon Rekognition features may incur additional charges. For more information, see [Amazon Rekognition pricing](https://aws.amazon.com/rekognition/pricing/).

There is no additional cost for using `sharp`, which is an open source library.

<a name="ecs-rekognition-costs"></a> **Amazon Rekognition costs (ECS architecture)**

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

In the ECS architecture, smart cropping and content moderation call Amazon Rekognition only on a CloudFront cache miss. Plan for these costs based on the detection methods you enable:
+  **Standard detection APIs** (`DetectFaces`, `DetectLabels`, `DetectText`, `DetectModerationLabels`) are billed at $0.001 per image. A single smart crop request can invoke more than one of these APIs: for example, combining faces and labels invokes two APIs, so a single uncached request costs $0.002. Logo detection adds no extra API call because it reads from the labels response. At higher monthly volumes, the Amazon Rekognition volume-tier pricing reduces the per-image rate below $0.001.
+  **Custom Labels models** are billed differently: $4.00 per inference hour per inference unit, charged continuously while the model is running regardless of request volume (an always-on model is about $2,920/month per inference unit). There is no per-image charge for `DetectCustomLabels`. To control this cost, start the model only when needed; see [Amazon Rekognition Custom Labels access and lifecycle](custom-labels-access.md).

The number of standard detection APIs a smart crop request invokes depends on which detection methods you enable. The following table shows the cost of a single uncached request at the flat $0.001 rate (the conservative worst case, before volume-tier discounts):

| Detection methods enabled | Amazon Rekognition APIs called | Cost per uncached request |
| --- | --- | --- |
| Faces only |  `DetectFaces`  | $0.001 |
| Faces and labels (logos included) |  `DetectFaces`, `DetectLabels`  | $0.002 |
| Faces, labels, and text |  `DetectFaces`, `DetectLabels`, `DetectText`  | $0.003 |

**Note**
Logo detection reads from the `DetectLabels` response, so it adds no separate API call. Content moderation invokes `DetectModerationLabels`, which is one additional $0.001 call when enabled alongside smart cropping.

The solution reduces standard detection costs with an Amazon Rekognition result cache (a DynamoDB table). The first cache miss for a source image calls Amazon Rekognition and stores the result; later requests for the same image, across different policies, device sizes, formats, and aspect ratios, reuse the cached result instead of calling Amazon Rekognition again. The DynamoDB cost of a cache hit is a small fraction of the Amazon Rekognition call it replaces (a single eventually-consistent read is roughly 2,000 times cheaper than the Amazon Rekognition call it avoids), so the cache pays for itself at every workload size.

Your actual savings depend on the **variant multiplier** — how many distinct CloudFront variants (policies, device sizes, formats, and aspect ratios) share each source image. Because only the first miss per source image calls Amazon Rekognition, the cache eliminates roughly `1 − (1 ÷ variant multiplier)` of the calls. Deployments with more policies and richer smart crop configurations share each source image across more variants and therefore save the most:

| Variant multiplier (variants per source image) | Approximate reduction in Amazon Rekognition calls |
| --- | --- |
| 3 (simple: one policy, mobile and desktop) | \~67% |
| 5 (typical: two policies, mixed devices) | \~80% |
| 10 (complex: several policies, full optimization) | \~90% |
| 20 (heavy: many policies, rich configurations) | \~95% |

**Note**
These reductions are illustrative and assume source images are shared evenly across variants; a variant multiplier of 5 is a modeling assumption, not a measured value. Your results depend on your traffic and configuration.

For current rates, including volume-tier pricing, see [Amazon Rekognition pricing](https://aws.amazon.com/rekognition/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
