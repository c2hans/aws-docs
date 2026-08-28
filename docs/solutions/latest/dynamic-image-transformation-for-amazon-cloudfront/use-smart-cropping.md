---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/use-smart-cropping.html
---

# Use smart cropping
<a name="use-smart-cropping"></a>

This solution uses Amazon Rekognition for face detection in images submitted for smart cropping. To activate smart cropping on an image, add the **smartCrop** property to the **edits** property in the [image request](use-the-solution-with-a-frontend-application.md).
+  **smartCrop(optional, boolean \|\| object)** - Activates the smart cropping feature for an original image. If the value is `true`, then the feature returns the first face detected from the original image with no additional options. For example:

  ```
  const imageRequest = JSON.stringify({
      bucket: "<myImageBucket>",
      key: "<myImage.jpeg>",
      edits: {
          smartCrop: true
      }
  })
  ```

  The following **smartCrop** variables are shown in the following code sample:

   **smartCrop.faceIndex(optional, number)** - Specifies which face to focus on if multiple are present within an original image. The solution indexes detected faces in a zero-based array from the largest detected face to the smallest. If this value isn’t specified, Amazon Rekognition returns the largest face detected from the original image. **smartCrop.padding(optional, number)** - Specifies an amount of padding in pixels to add around the cropped image. The solution applies the padding value to all sides of the cropped image.

  ```
  const imageRequest = JSON.stringify({
      bucket: "<myImageBucket>",
      key: "<myImage.jpeg>",
      edits: {
          smartCrop: {
              faceIndex: 1,  // zero-based index of detected faces
              padding: 40,   // padding expressed in pixels, applied to all sides
          }
      }
  })
  ```

**Note**
 **smartCrop** is not supported for animated (such as, GIF) images.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
