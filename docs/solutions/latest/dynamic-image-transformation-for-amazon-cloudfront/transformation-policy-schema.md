---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/transformation-policy-schema.html
---

# Transformation policy schema reference
<a name="transformation-policy-schema"></a>

**Note**
 **Supported in:** ECS architecture only.

A transformation policy is JSON with two optional top-level arrays: `transformations` (operations applied to the image) and `outputs` (auto-optimization settings for quality, format, and size). A policy must contain at least one of the two. The sections that follow document the smart cropping, content moderation, and output-optimization portions of the schema introduced for content-aware cropping and multi-tier device detection. For the other transformations (resize, blur, watermark, and so on), see [Apply transformations using URL query parameters](transformation-filter-reference.md).

**Note**
Field names are case-sensitive. Use the exact casing shown below (for example, `smartCrop`, `customModelArn`, `minConfidence`). Unknown fields are rejected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
