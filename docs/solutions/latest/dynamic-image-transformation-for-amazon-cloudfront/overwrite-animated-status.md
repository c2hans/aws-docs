---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/overwrite-animated-status.html
---

# Overwrite animated status
<a name="overwrite-animated-status"></a>

This solution assumes that GIF files with multiple pages should be animated. If you’d like to indicate that a GIF should not be animated, or that another file type should be animated, include the animated property in the edits property in the image request.
+  **animated (optional, boolean)** - Overwrites the initial animated status of the image. If the value is `true` , the solution will attempt to process the image as animated. For example:

  ```
  const imageRequest = JSON.stringify({
      bucket: "<myImageBucket>",
      key: "<myImage.webp>",
      edits: {
          animated: true
      }
  })
  ```

  If it is `false`, the solution will process the image as a still image. For example:

  ```
  const imageRequest = JSON.stringify({
      bucket: "<myImageBucket>",
      key: "<myImage.gif>",
      edits: {
          animated: false
      }
  })
  ```

**Note**
If an image does not have multiple pages, it will always be processed as still, regardless of the **edits.animated** property. The following filters are not supported for images that are animated: **rotate**, **smartCrop**, **roundCrop**, and **contentModeration**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
