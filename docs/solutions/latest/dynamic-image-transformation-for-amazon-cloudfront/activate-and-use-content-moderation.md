---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/activate-and-use-content-moderation.html
---

# Activate and use content moderation
<a name="activate-and-use-content-moderation"></a>

This solution can detect inappropriate content using Amazon Rekognition. To activate content moderation, add the **contentModeration** property to the **edits** property in the [image request](use-the-solution-with-a-frontend-application.md).
+  **contentModeration (optional, boolean \|\| object)** - Activates the content moderation feature for an original image. If the value is true, then the feature detects inappropriate content using Amazon Rekognition with a minimum confidence that’s set higher than 75%. If Amazon Rekognition finds inappropriate content, the solution blurs the image. For example:

  ```
  const imageRequest = JSON.stringify({
      bucket: "<myImageBucket>",
      key: "<myImage.jpeg>",
      edits: {
          contentModeration: true
      }
  })
  ```

  The following **contentModeration** variables are shown in the following code sample:
+  **contentModeration.minConfidence (optional, number)** - Specifies the minimum confidence level for Amazon Rekognition to use. Amazon Rekognition only returns detected content that’s higher than the minimum confidence. If a value isn’t provided, the default value is set to 75%.
+  **contentModeration.blur (optional, number**) - Specifies the intensity level that an image is blurred if inappropriate content is found. The number represents the sigma of the Gaussian mask, where *sigma = 1 \+ radius /2*. For more information, refer to the [sharp](https://sharp.pixelplumbing.com/api-operation#blur) documentation. If a value isn’t provided, the default value is set to 50.
+  **contentModeration.moderationLabels (optional, array)** - Identifies the specific content to search for. The image is blurred only if Amazon Rekognition locates the content specified in the **smartCrop.moderationLabels** provided. You can use either a top-level category or a second-level category. Top-level categories include its associated second-level categories. For more information about moderation label options, refer to [Content moderation](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html) in the *Amazon Rekognition Developer Guide*.

  ```
  const imageRequest = JSON.stringify({
      bucket: "<myImageBucket>",
      key: "<myImage.jpeg>",
      edits: {
          contentModeration: {
              minConfidence: 90,  // minimum confidence level for inappropriate content
              blur: 80,           // amount to blur image
              moderationLabels: [ // labels to search for
                 "Hate Symbols",
                 "Smoking"
               ]
          }
      }
  })
  ```

**Note**
 **contentModeration** is not supported for animated (such as, GIF) images.
