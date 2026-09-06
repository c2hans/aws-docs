---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-content-moderation-parameters.html
---

# Content moderation parameters
<a name="ecs-content-moderation-parameters"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

Content moderation analyzes an image with Amazon Rekognition DetectModerationLabels and applies a Gaussian blur to images whose detected content matches your criteria. Enable it with `contentModeration=true` for defaults, or configure the following `contentModeration.*` parameters.

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
|  `contentModeration.minConfidence`  | number (0-100) | Minimum confidence for a detected moderation label to trigger blurring. Default `75`. |  `contentModeration.minConfidence=75`  |
|  `contentModeration.blur`  | number (0.3-1000) | Gaussian blur strength applied to flagged images. Default `50`. |  `contentModeration.blur=50`  |
|  `contentModeration.moderationLabels`  | string list | Specific moderation labels to act on. When omitted, any detected moderation label above the confidence threshold triggers blurring. |  `contentModeration.moderationLabels=Violence,Gambling`  |
