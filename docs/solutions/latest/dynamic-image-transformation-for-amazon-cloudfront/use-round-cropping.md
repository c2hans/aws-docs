---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/use-round-cropping.html
---

# Use round cropping
<a name="use-round-cropping"></a>

This solution can crop images in a circular pattern. To activate round cropping on an image, add the **roundCrop** property to the **edits** property in the [image request](use-the-solution-with-a-frontend-application.md).
+  **roundCrop(optional, boolean \|\| object)** - Activates the round cropping feature for an original image. If the value is true, then the feature returns a circular cropped image that’s centered from the original image and has a diameter of the smallest edge of the original image. For example:

  ```
  const imageRequest = JSON.stringify({
      bucket: "<myImageBucket>",
      key: "<myImage.jpeg>",
      edits: {
          roundCrop: true
      }
  })
  ```

  The following **roundCrop** variables are shown in the following code sample:

   **roundCrop.rx (optional, number)** - Specifies the radius along the x-axis of the ellipse. If a value isn’t provided, the image handler defaults to a value that’s half the length of the smallest edge. **roundCrop.ry (optional, number)** - Specifies the radius along the y-axis of the ellipse. If a value isn’t provided, the image handler defaults to a value that’s half the length of the smallest edge. **roundCrop.top(optional, number)** - Specifies the offset from the top of the original image to place the center of the ellipse. If a value isn’t provided, the image handler defaults to a value that’s half of the height. **roundCrop.left (optional, number)** - Specifies the offset from the left-most edge of the original image to place the center of the ellipse. If a value isn’t provided, the image handler defaults to a value that’s half of the width.

  ```
  const imageRequest = JSON.stringify({
      bucket: "<myImageBucket>",
      key: "<myImage.jpeg>",
      edits: {
          roundCrop: {
              rx: 30,   // x-axis radius
              ry: 20,   // y-axis radius
              top: 300, // offset from top edge of original image
              left: 500 // offset from left edge of original image
          }
      }
  })
  ```

**Note**
 **roundCrop** is not supported for animated (such as, GIF) images.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
