---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/content-moderation-contentmoderation.html
---

# Content moderation (`contentModeration`)
<a name="content-moderation-contentmoderation"></a>

The `contentModeration` transformation accepts `true` (defaults) or an object:

```
{
  "transformation": "contentModeration",
  "value": {
    "minConfidence": 75,
    "blur": 50,
    "moderationLabels": ["Violence", "Gambling"]
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
|  `minConfidence`  | number (0-100) | Minimum confidence for a detected moderation label to trigger blurring. Default `75`. |
|  `blur`  | number (0.3-1000) | Gaussian blur strength applied to flagged images. Default `50`. |
|  `moderationLabels`  | string array | Specific moderation labels to act on. When omitted or empty, any detected moderation label above the confidence threshold triggers blurring. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
