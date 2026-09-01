---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-smart-crop-parameters.html
---

# Smart crop parameters
<a name="ecs-smart-crop-parameters"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

Smart cropping identifies the important content in an image and crops around it. You combine one or more detection methods with optional shaping constraints, all expressed as `smartCrop.*` query parameters (or as a `smartCrop` transformation in a policy). At least one detection method (`faces`, `faceIndex`, `labels`, `customModelArn`, `retainText`, or `retainLogo`) must be present for content-aware cropping; `smartCrop=true` is a shorthand that enables face detection with default values.

**Note**
Parameter names are case-sensitive and use the casing shown below. List parameters (`labels`, `priorities`) are supplied as a single comma-separated value, for example `smartCrop.labels=Person,Car`.

 **Detection methods**

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
|  `smartCrop.faces`  | boolean | Detect faces using Amazon Rekognition DetectFaces. |  `smartCrop.faces=true`  |
|  `smartCrop.faceIndex`  | integer (0-15) | Crop around a specific detected face by index. Implies face detection. |  `smartCrop.faceIndex=0`  |
|  `smartCrop.labels`  | string list | Object or subject labels to detect using DetectLabels (for example `Person`, `Car`, `Shoe`). |  `smartCrop.labels=Person,Car`  |
|  `smartCrop.customModelArn`  | string | ARN of a Rekognition Custom Labels model version for domain-specific detection. The model must be running and the ECS task role must be permitted to call it. For details, see the Custom Labels access and lifecycle guidance in the deployment guide. |  `smartCrop.customModelArn=arn:aws:rekognition:…​`  |
|  `smartCrop.retainText`  | boolean | Include detected text regions (DetectText) in the crop, preserving overlays, price tags, and signage. |  `smartCrop.retainText=true`  |
|  `smartCrop.retainLogo`  | boolean | Include detected brand logos in the crop. |  `smartCrop.retainLogo=true`  |

 **Crop shaping**

When multiple targets are detected, DIT computes a single bounding box that encloses all of them, then shapes the crop using the following constraints.

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
|  `smartCrop.aspectRatio`  | string (`w:h`) | Target aspect ratio, width and height each 1-100. Orientation is preserved (`16:9` is landscape, `9:16` is portrait). |  `smartCrop.aspectRatio=16:9`  |
|  `smartCrop.padding`  | integer or string | Breathing room around the targets, applied symmetrically on all sides. An integer is pixels; a string is `10%` or `50px`. Default `3%`. |  `smartCrop.padding=10%`  |
|  `smartCrop.gravity`  | string | Crop anchor. Either a directional position (`top-left`, `top-center`, `top-right`, `center-left`, `center`, `center-right`, `bottom-left`, `bottom-center`, `bottom-right`) or a label name from `labels` to center the crop on that label. Default `center`. |  `smartCrop.gravity=center`  |
|  `smartCrop.priorities`  | string list | Order in which `aspectRatio` and `padding` are satisfied when they conflict (first listed wins). Only these two are configurable; target inclusion is always resolved first and gravity last. Default `aspectRatio,padding`. |  `smartCrop.priorities=aspectRatio,padding`  |
|  `smartCrop.minConfidence`  | number (0-100) | Minimum Rekognition confidence for a detection to be used as a target. Default `80`. |  `smartCrop.minConfidence=80`  |
|  `smartCrop.fallback`  | string | Strategy when no targets are detected: `cover`, `contain`, `fill`, `inside`, `outside`, or `no-crop`. Default `cover`. |  `smartCrop.fallback=cover`  |

**Note**
Only `aspectRatio` and `padding` are orderable through `priorities`. Target inclusion (keeping all detected targets visible) is always applied first, and gravity is always applied last. Listing `targetInclusion` or `gravity` in `priorities` is rejected.

 **Legacy parameters**

The original face-cropping parameters remain valid and are interpreted as face-based smart crop requests.

| Legacy parameter | Equivalent |
| --- | --- |
|  `smartCrop=true`  |  `smartCrop.faces=true` with default shaping. |
|  `smartCrop.index=<n>`  |  `smartCrop.faceIndex=<n>` (enables face detection). |
|  `smartCrop.padding=<n>`  |  `smartCrop.padding=<n>` in pixels. Applies to any smart crop mode. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
