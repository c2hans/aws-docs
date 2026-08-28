---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/create-and-use-image-requests.html
---

# Create and use image requests
<a name="create-and-use-image-requests"></a>

This solution generates a CloudFront domain name that gives you access to both original and modified images through the image handler API. You can specify parameters such as the image’s location and edits to be made in a JSON object on the frontend.

Follow these step-by-step instructions to create image requests:

**Note**
The following image formats are supported for modifications: JPG/JPEG, PNG, TIFF/TIF, WEBP, GIF and 8-bit AVIF. For retrieval, the following formats are supported: All those listed previously, as well as AVIF (all bit depths) and SVG. Edited SVG files will be converted to .png by default.

1. Retrieve your API endpoint for the solution. Refer to [Use the solution with a frontend application](use-the-solution-with-a-frontend-application.md) for instructions.

1. In a code sandbox, or in your frontend application, create a new `imageRequest` JSON object. This object contains the key-value pairs needed to successfully retrieve and perform edits on your images. Using the following code sample and the [sharp](https://sharp.pixelplumbing.com/) documentation, adjust the following properties to meet your image editing requirements.
   +  **Bucket** - Specify the S3 bucket containing your original image file. This is the name that’s specified in the **SourceBuckets** template parameter. You can update the image location by adding it into the SOURCE\_BUCKETS environment variable of your image handler Lambda function. See [Using AWS Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html) in the *AWS Lambda Developer Guide* for more information.
   +  **Key** - Specify the filename of your original image. This name should include the file extension and subfolders between its location and the root of the bucket. For example, `folder1/folder2/image.jpeg`.
   +  **Edits** - Specify image edits as key-value pairs. If you don’t specify image edits, the original image returns with no changes made.

   For example, the following code block specifies the image location as `myImageBucket` and specifies edits of `grayscale: true` to change the image to grayscale:

```
const imageRequest = JSON.stringify({
    bucket: "<myImageBucket>",
    key: "<myImage.jpeg>",
    edits: {
        grayscale: true
    }
})
```

1. Stringify the JSON request object. For example:

   ```
   const stringifiedObject = JSON.stringify(<myObject>);
   ```

1. Base64 encode the JSON string. For example:

   ```
   const encodedObject = btoa(<stringifiedObject>);
   ```

1. Append the encoded string onto the CloudFront URL. For example:

   ```
   const url = '${<ApiEndpoint>}/${<encodedObject>}';
   ```

1. Use that URL either in the JavaScript as part of a `GET` request, or in the frontend as part of an HTML `img` tag’s `src` property.

For information regarding how to use additional features in an image request, refer to [Dynamically resize photos](dynamically-resize-photos.md), [Use smart cropping](use-smart-cropping.md), [Use round cropping](use-round-cropping.md), and [Activate and use content moderation](activate-and-use-content-moderation.md). For additional features supported by `sharp`, refer to the [sharp](https://sharp.pixelplumbing.com/) documentation.

**Note**
The following filters are not supported for multi-page GIF images due to limitations in the underlying libraries: **rotate**, **smartCrop**, **roundCrop**, and **contentModeration**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
