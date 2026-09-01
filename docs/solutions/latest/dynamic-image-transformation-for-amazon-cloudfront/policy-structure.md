---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/policy-structure.html
---

# Policy structure
<a name="policy-structure"></a>

A policy is a single JSON object containing the `transformations` array, the `outputs` array, or both. The following skeleton shows the overall shape; the detailed sections below define the `smartCrop`, `contentModeration`, and `outputs` values.

```
{
  "transformations": [
    {
      "transformation": "resize",
      "value": { "width": 800, "fit": "contain" },
      "condition": { "field": "x-device", "value": "mobile" }
    }
  ],
  "outputs": [
    { "type": "format", "value": "auto", "fallback": { "format": "jpeg" } }
  ]
}
```

 **Top-level fields**

| Field | Type | Description |
| --- | --- | --- |
|  `transformations`  | array (optional) | Ordered list of operations applied to the image. Each item is a transformation object (see below). A policy can define up to 100 transformations. |
|  `outputs`  | array (optional) | Device-aware auto-optimization settings. Each `type` (`quality`, `format`, `autosize`) can appear at most once. See [Output optimizations](output-optimizations-outputs.md). |

A policy must contain at least one entry across `transformations` and `outputs`, and the serialized policy cannot exceed 10 KB.

 **Transformation object**

Each entry in `transformations` has the following fields:

| Field | Type | Description |
| --- | --- | --- |
|  `transformation`  | string | The operation to apply (for example, `resize`, `blur`, `smartCrop`, `watermark`). For the full list of operations and their `value` formats, see [Apply transformations using URL query parameters](transformation-filter-reference.md); `smartCrop` and `contentModeration` are detailed below. |
|  `value`  | varies | The configuration for the operation. The accepted shape depends on `transformation` (for example, a boolean for `flip`, an object for `resize`). |
|  `condition`  | object (optional) | Applies the transformation only when a request header matches. Contains `field` (the request header name) and `value` (a string, number, or array of either; an array matches if any element matches). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
