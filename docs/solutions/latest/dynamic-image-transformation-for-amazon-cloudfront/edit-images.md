---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/edit-images.html
---

# Edit images
<a name="edit-images"></a>

You can use this solution to edit your images, such as rotating them or changing the coloring to negative. Refer to the [sharp documentation](https://sharp.pixelplumbing.com/api-operation) for a description of each operation. For example, to produce a negative of an image, enter the following:

```
const imageRequest = JSON.stringify({
    bucket: "<myImageBucket>",
    key: "<myImage.jpeg>",
    edits: {
        negate: true
    }
})
```
