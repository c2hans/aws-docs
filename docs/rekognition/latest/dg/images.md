---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/images.html
---

# Working with images
<a name="images"></a>

This section covers the types of analysis that Amazon Rekognition Image can perform on images.
+ [Object and scene detection](labels.md)
+ [Face detection and comparison](faces.md)
+ [Searching faces in a collection](collections.md)
+ [Celebrity recognition](celebrities.md)
+ [Image moderation](moderation.md)
+ [Text in image detection](text-detection.md)

These are performed by non-storage API operations where Amazon Rekognition Image doesn't persist any information discovered by the operation. No input image bytes are persisted by non-storage API operations. For more information, see [Understanding non-storage and storage API operations](how-it-works-storage-non-storage.md).

Amazon Rekognition Image can also store facial metadata in collections for later retrieval. For more information, see [Searching faces in a collection](collections.md).

In this section, you use the Amazon Rekognition Image API operations to analyze images stored in an Amazon S3 bucket and image bytes loaded from the local file system. This section also covers getting image orientation information from a .jpg image.

 Rekognition only uses RGB channels to perform inference. AWS recommends users remove the Alpha Channel before using a Display to visually (manually by a human) inspect the comparison.

**Topics**
+ [Image specifications](images-information.md)
+ [Analyzing images stored in an Amazon S3 bucket](images-s3.md)
+ [Analyzing an image loaded from a local file system](images-bytes.md)
+ [Displaying bounding boxes](images-displaying-bounding-boxes.md)
+ [Getting image orientation and bounding box coordinates](images-orientation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
