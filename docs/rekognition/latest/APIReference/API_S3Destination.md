---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_S3Destination.html
---

# S3Destination
<a name="API_S3Destination"></a>

 The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation. These results include the name of the stream processor resource, the session ID of the stream processing session, and labeled timestamps and bounding boxes for detected labels.

## Contents
<a name="API_S3Destination_Contents"></a>

 ** Bucket **   <a name="rekognition-Type-S3Destination-Bucket"></a>
 The name of the Amazon S3 bucket you want to associate with the streaming video project. You must be the owner of the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[0-9A-Za-z\.\-_]*`
Required: No

 ** KeyPrefix **   <a name="rekognition-Type-S3Destination-KeyPrefix"></a>
 The prefix value of the location within the bucket that you want the information to be published to. For more information, see [Using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html).
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_S3Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/S3Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/S3Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/S3Destination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
