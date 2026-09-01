---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/smart-crop-smartcrop.html
---

# Smart crop (`smartCrop`)
<a name="smart-crop-smartcrop"></a>

The `smartCrop` transformation accepts one of three value forms:
+  `true`: face-based cropping with default shaping (shorthand).
+ A legacy object `{ "index": <0-15>, "padding": <pixels> }`, interpreted as face cropping.
+ An expanded object combining one or more detection methods with optional shaping constraints.

At least one detection method (`faces`, `faceIndex`, `labels`, `customModelArn`, `retainText`, or `retainLogo`) must be present in the expanded form.

```
{
  "transformation": "smartCrop",
  "value": {
    "faces": true,
    "faceIndex": 0,
    "labels": ["Person", "Car"],
    "customModelArn": "arn:aws:rekognition:<region>:<account>:project/<name>/version/<name>/<timestamp>",
    "aspectRatio": "16:9",
    "padding": "10%",
    "gravity": "center",
    "priorities": ["aspectRatio", "padding"],
    "retainText": true,
    "retainLogo": true,
    "fallback": "cover",
    "minConfidence": 80
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
|  `faces`  | boolean | Detect faces (DetectFaces). |
|  `faceIndex`  | integer (0-15) | Crop around a specific detected face by index. Implies face detection. |
|  `labels`  | string array | Object or subject labels to detect (DetectLabels), for example `["Person", "Car"]`. |
|  `customModelArn`  | string | ARN of an Amazon Rekognition Custom Labels model version. The model must be running and the ECS task role must be permitted to call it. |
|  `aspectRatio`  | string (`w:h`) | Target ratio, with width and height each between 1 and 100. Orientation is preserved. |
|  `padding`  | integer or string | Breathing room around the targets, applied symmetrically on all sides. An integer is pixels; a string is `10%` or `50px`. Default `3%`. |
|  `gravity`  | string | Crop anchor: a directional position (`top-left`, `top-center`, `top-right`, `center-left`, `center`, `center-right`, `bottom-left`, `bottom-center`, `bottom-right`) or a label name from `labels`. Default `center`. |
|  `priorities`  | string array | Order in which `aspectRatio` and `padding` are satisfied when they conflict (first listed wins). Only `aspectRatio` and `padding` are accepted; target inclusion is always resolved first and gravity always last. Default `["aspectRatio", "padding"]`. |
|  `retainText`  | boolean | Include detected text regions (DetectText) in the crop. |
|  `retainLogo`  | boolean | Include detected brand logos in the crop. |
|  `fallback`  | string | Strategy when no targets are detected: `cover`, `contain`, `fill`, `inside`, `outside`, or `no-crop`. Default `cover`. |
|  `minConfidence`  | number (0-100) | Minimum Amazon Rekognition confidence for a detection to be used as a target. Default `80`. |

**Note**
 `padding` is symmetric only; a single value applies to all four sides. Per-axis padding values (such as `10%,20%`) are not supported. Listing `targetInclusion` or `gravity` in `priorities` is rejected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
