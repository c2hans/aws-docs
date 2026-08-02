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
