---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/transformation-filter-reference.html
---

# Transformation filter reference
<a name="transformation-filter-reference"></a>

The ECS architecture supports a comprehensive set of image transformation filters using a simplified syntax. The following table provides the complete filter reference:

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
|  **Smart Crop**  |  `smartCrop=true` or `smartCrop.index=1` `smartCrop.padding=200`  | Accepts either boolean or index \+ padding parameters. Boolean will automatically perform cropping. |
|  **Strip ICC**  |  `stripIcc=true`  | Strip ICC and enforces sRGB color space |
|  **Strip EXIF**  |  `stripExif=true`  | Removes image metadata |
|  **Tint**  |  `tint=aliceblue` `tint=[0,0,255,1]`  | Accepts color names or RGBA tuples |
|  **Watermark**  |  `watermark=https://example.com/overlayImage.png,[15,15,0.1,0.4,0.4]`  | Expects a format of: [watermarkURL, [x, y, alpha, widthRatio, heightRatio]] Note: For security reasons, the origin the watermark image is hosted at must be configured as an origin within DIT. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
