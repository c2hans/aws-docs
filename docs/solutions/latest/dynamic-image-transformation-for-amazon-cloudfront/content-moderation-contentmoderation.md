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
