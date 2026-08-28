---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/dynamically-resize-photos.html
---

# Dynamically resize photos
<a name="dynamically-resize-photos"></a>

This solution offers the following **fit** options to dynamically resize an image: `cover`, `contain`, `fill`, `inside`, and `outside`. Refer to the [sharp documentation](https://sharp.pixelplumbing.com/api-resize) for a description of each fit. For example:

```
const imageRequest = JSON.stringify({
    bucket: "<myImageBucket>",
    key: "<myImage.jpeg>",
    edits: {
        resize: {
            width: 200,
            height: 250,
            fit: "cover"
        }
    }
})
```

If you use `contain` as the resize **fit** mode, you can specify the color of the fill by providing the hex code of the color you want to use. For example:

```
const imageRequest = JSON.stringify({
    bucket: "<myImageBucket>",
    key: "<myImage.jpeg>",
    edits: {
        resize: {
            width: 200,
            height: 250,
            fit: "contain",
            background: {
                r: 255,
                g: 0,
                b: 0,
                alpha: 1
            }
        }
    }
})
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
