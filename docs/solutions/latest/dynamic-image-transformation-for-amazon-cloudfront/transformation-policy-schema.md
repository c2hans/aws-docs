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
