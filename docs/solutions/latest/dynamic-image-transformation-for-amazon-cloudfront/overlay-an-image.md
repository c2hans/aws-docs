---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/overlay-an-image.html
---

# Overlay an image
<a name="overlay-an-image"></a>

This solution can overlay images on top of others, for cases like watermarking a copyrighted image. To overlay an image, add the **overlayWith** property to the **edits** property in the [image request](use-the-solution-with-a-frontend-application.md).

 **overlayWith(optional, object)** - Overlays an image on top of the original. For example:

```
const imageRequest = JSON.stringify({
    bucket: "<myImageBucket>",
    key: "<myImage.jpeg>",
    edits: {
    overlayWith: {
        bucket: "<myImageBucket>",
        key: "<myOverlayImage.jpeg>",
        alpha: 0-100, // Opaque (0) to Transparent (100)
        wRatio: 0-100, // Ratio of the underlying image that the overlay width should be
        hRatio: 0-100, // Ratio of the underlying image that the overlay height should be
        options: {
                top: "-10p",
                left: 150
            }
        }
    }
})
```

The following **overlayWith** variables are shown in the previous code sample:
+  **overlayWith.bucket (required, string)** - Specifies the bucket that the overlay image should be retrieved from. This bucket must be present in the `SOURCE_BUCKETS` parameter.
+  **overlayWith.key (required, string)** - Specifies the object key that is used for the overlay image.
+  **overlayWith.alpha (optional, number)** - Specifies the opacity that should be used for the overlay image. This can be set from 0 (fully opaque) and 100 (fully transparent).
+  **overlayWith.wRatio (required, number)** - Specifies the percentage of the width of underlying image that the overlay image should be sized to. This can be set from 0 and 100, where 100 indicates that the overlay image has the same width as the underlying image.
+  **overlayWith.hRatio (required, number)** - Specifies the percentage of the height of underlying image that the overlay image should be sized to. This can be set from 0 and 100, where 100 indicates that the overlay image has the same height as the underlying image.
+  **overlayWith.options.top (optional, number \| string)** - Specifies the distance in pixels from the top edge of the underlying photo that the overlay should be placed. A number formatted as a string with a `p` at the end is treated as a percentage.
+  **overlayWith.options.left (optional, number \| string)** - Specifies the distance in pixels from the left edge of the underlying photo that the overlay should be placed. A number formatted as a string with a `p` at the end is treated as a percentage.

**Note**
 **overlayWith** is not fully supported for animated (such as, GIF) images. Instead, only the first frame will receive an overlay.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
