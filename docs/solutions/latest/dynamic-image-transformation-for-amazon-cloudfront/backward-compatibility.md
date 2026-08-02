---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/backward-compatibility.html
---

# Backward compatibility
<a name="backward-compatibility"></a>

**Note**
 **Lambda Architecture Only**: The backward compatibility features described in this section only apply to the Lambda architecture template. The ECS architecture uses a different request format and does not support legacy Thumbor or custom request formats.

This solution is compatible with legacy image request formats, including the Thumbor and Custom (with rewrite function) formats from previous versions of this solution. If you are using a previous version of this solution (version 3.x and earlier) and have image requests formatted for use with that version, review the following note to ensure minimal breaking changes or parities.

**Note**
Legacy requests (Thumbor and custom) will source images from the ﬁrst bucket in the `SOURCE_BUCKETS` environment variable by default. To use a different bucket, you can use the `s3:BucketName` tag in your request or you can adjust which bucket is first in the environment variables section of your image handler Lambda function. See [Using AWS Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html) in the *AWS Lambda Developer Guide* for more information.
