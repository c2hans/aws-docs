---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/use-filters.html
---

# Use filters
<a name="use-filters"></a>

To use filters, specify a filter from the following table. For example, to blur a JPEG image, enter the following:

```
https://<ApiEndpoint>/filters:blur(7)/<image.jpeg>
```

**Note**
Some Thumbor filters aren’t supported in the current version of this solution. This might affect legacy users with advanced image request configurations. For notes about Thumbor compatibility and source image storage limitations, see [Backward compatibility](backward-compatibility.md). For examples of filter usage, refer to the [Thumbor documentation](http://thumbor.readthedocs.io/en/latest/filters.html).

| Filter name | Filter syntax |
| --- | --- |
|  **Animated**  |  `/filters:animated(true/false)/`  |
|  **Autojpg**  |  `/filters:autojpg()/`  |
|  **Background color**  |  `/filters:background_color(color)/`  |
|  **Blur**  |  `/filters:blur(7)/`  |
|  **Color fill**  |  `/filters:fill(color)/`  |
|  **Convolution**  |  `/filters:convolution(1;2;1;2;4;2;1;2;1,3,false)/`  |
|  **Crop**  |  `/10x10:100x100/`  |
|  **Equalize**  |  `/filters:equalize()/`  |
|  **Grayscale**  |  `/filters:grayscale()/`  |
|  **Image format** `(.gif, .jpeg, .png, .avif, .webp, .tiff, .raw, .heif)`  |  `/filters:format(image_format)`  |
|  **No upscale**  |  `/filters:no_upscale()/`  |
|  **Proportion**  |  `/filters:proportion(0.0-1.0)/`, |
|  ** Quality**  |  `/filters:quality(0-100)/`  |
|  **Resize**  |  `/fit-in/800x1000/`  |
|  **RGB**  |  `/filters:rgb(20,-20,40)/`  |
|  **Rotate**  |  `/filters:rotate(90)/`  |
|  **Sharpen**  |  `/filters:sharpen(0.0-10.0, 0.0-2.0, true/false)/`  |
|  **Smart Crop**  |  `/filters:smart_crop(faceIndex, facePadding)/`  |
|  **Stretch**  |  `/filters:stretch()/`  |
|  **Strip Exif**  |  `/filters:strip_exif()/`  |
|  **Strip ICC**  |  `/filters:strip_icc()/`  |
|  **Upscale**  |  `/filters:upscale()/`  |
|  **Watermark**  |  `/filters:watermark(bucket,key,x,y,alpha[,w_ratio[,h_ratio]])`  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
