---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/transformation-filter-reference.html
---

# Apply transformations using URL query parameters
<a name="transformation-filter-reference"></a>

You apply transformations on demand by adding query parameters to the request URL sent to the CloudFront distribution. This is the per-request alternative to defining transformations in a transformation policy: any transformation in the following reference can be requested directly in the URL’s query string, and multiple transformations are combined with `&`. For example:

```
https://<cloudfront-domain>/<image-path>?format=webp&resize.width=200&blur=30
```

Grouped (dotted) parameters such as `resize.width` and `convolve.kernel` configure the sub-options of a single transformation.

**Note**
Query parameters are case-sensitive. Use the exact name and casing shown in the reference (for example, `smartCrop.faces`, not `smartcrop.faces` or `smartCrop.Faces`).

Explicit transformations requested in query parameters take precedence over transformations defined in a transformation policy. For the full precedence order, see **Policy application precedence** in the architecture details. The following table provides the complete filter reference:

| Filter Name | Filter Syntax | Notes |
| --- | --- | --- |
|  **Blur**  |  `blur=30`  | Integer from 0.3 to 1000 |
|  **Convolve**  |  `convolve.width=3` `convolve.height=3` `convolve.kernel=[1,0,-1,0,0,0,-1,0,1]`  | Requires 3 parameters: width, height, kernel |
|  **Extract**  |  `extract=[10,10,200,200]`  | Array of 4 non-negative integers |
|  **Flatten**  |  `flatten=aliceblue` `flatten=[0,0,255,1]`  | Accepts color names or RGBA tuples |
|  **Flip**  |  `flip=true`  | Boolean |
|  **Flop**  |  `flop=true`  | Boolean |
|  **Format**  |  `format=webp`  | Accepts: jpg, jpeg, png, tiff, webp, gif, avif |
|  **Greyscale**  |  `greyscale=true`  | Boolean |
|  **Normalize**  |  `normalize=true`  | Boolean |
|  **Quality**  |  `quality=0.5`  | Integer from 0 to 1 |
|  **Resize**  |  `resize.width=200` `resize.ratio=0.5` `resize.fit=contain` `resize.withoutEnlargement=true` `resize.background=blue`  | Must specify: height, width, or ratio |
|  **Rotate**  |  `rotate=90`  | Integer |
|  **Sharpen**  |  `sharpen=true` or `sharpen=sigma=5` `sharpen.m1=2` `sharpen.m2=1` `sharpen.x1=2` `sharpen.y2=20` `sharpen.y3=20`  | Accepts either boolean to perform a fast mild sharpen, or additional parameters for a slower but more accurate sharpen. See [Sharp docs](https://sharp.pixelplumbing.com/api-operation/#sharpen) for more information. |
|  **Smart Crop**  |  `smartCrop=true` or one or more of: `smartCrop.faces=true` `smartCrop.faceIndex=0` `smartCrop.labels=Person,Car` `smartCrop.customModelArn=arn:aws:…​` `smartCrop.retainText=true` `smartCrop.retainLogo=true` `smartCrop.aspectRatio=16:9` `smartCrop.padding=10%` `smartCrop.gravity=center` `smartCrop.priorities=aspectRatio,padding` `smartCrop.fallback=cover` `smartCrop.minConfidence=80`  | Content-aware cropping. `smartCrop=true` enables face-based cropping with defaults. To use other detection methods, specify at least one of `faces`, `faceIndex`, `labels`, `customModelArn`, `retainText`, or `retainLogo`. For full parameter details, see [Smart crop parameters](ecs-smart-crop-parameters.md). |
|  **Content Moderation**  |  `contentModeration=true` or `contentModeration.minConfidence=75` `contentModeration.blur=50` `contentModeration.moderationLabels=Violence,Gambling`  | Detects inappropriate content with Amazon Rekognition and applies a Gaussian blur to matching images. `contentModeration=true` uses defaults. See [Content moderation parameters](ecs-content-moderation-parameters.md). |
|  **Strip ICC**  |  `stripIcc=true`  | Strip ICC and enforces sRGB color space |
|  **Strip EXIF**  |  `stripExif=true`  | Removes image metadata |
|  **Tint**  |  `tint=aliceblue` `tint=[0,0,255,1]`  | Accepts color names or RGBA tuples |
|  **Watermark**  |  `watermark=https://example.com/overlayImage.png,[15,15,0.1,0.4,0.4]`  | Expects a format of: [watermarkURL, [x, y, alpha, widthRatio, heightRatio]] Note: For security reasons, the origin the watermark image is hosted at must be configured as an origin within DIT. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
