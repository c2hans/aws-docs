---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Video.html
---

# Video
<a name="API_Video"></a>

Video file stored in an Amazon S3 bucket. Amazon Rekognition video start operations such as [StartLabelDetection](API_StartLabelDetection.md) use `Video` to specify a video for analysis. The supported file formats are .mp4, .mov and .avi.

## Contents
<a name="API_Video_Contents"></a>

 ** S3Object **   <a name="rekognition-Type-Video-S3Object"></a>
The Amazon S3 bucket name and file name for the video.
Type: [S3Object](API_S3Object.md) object
Required: No

## See Also
<a name="API_Video_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Video)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/Video)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/Video)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
