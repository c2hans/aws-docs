---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/rekognition-cost-exposure.html
---

# Smart cropping cost exposure (ECS architecture)
<a name="rekognition-cost-exposure"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

Smart cropping calls Amazon Rekognition, a billable, usage-based service. The solution calls Amazon Rekognition once per *unique source image*: the first request for an image invokes the detection APIs, and the result is stored in a content-addressed Amazon Rekognition result cache so later requests for the same image reuse the stored analysis instead of calling Amazon Rekognition again (see [Amazon Rekognition costs (ECS architecture)](cost-considerations.md#ecs-rekognition-costs)). Because the cache is keyed by the contents of the source image, your Amazon Rekognition cost scales with the number of *unique* images you transform, not with total request volume. Repeat traffic against images you have already analyzed is served from the cache and is significantly cheaper.

Because the image endpoint is unauthenticated by default, the solution applies no application-layer limit on the rate at which unique images are processed. A flood of requests spanning many distinct source images bypasses the cache and converts directly into Amazon Rekognition charges, with no built-in per-client quota to stop it. To bound this exposure, we strongly recommend associating an AWS WAF rate-based rule with the distribution that serves your images (see [AWS WAF and rate-based rules](amazon-waf.md)), and monitoring Amazon Rekognition usage with Service Quotas and Amazon CloudWatch alarms so unexpected spend is detected early.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
