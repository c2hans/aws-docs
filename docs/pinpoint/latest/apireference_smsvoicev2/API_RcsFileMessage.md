---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsFileMessage.html
---

# RcsFileMessage
<a name="API_RcsFileMessage"></a>

A file message containing a media file (image, video, audio, or PDF) with an optional thumbnail.

## Contents
<a name="API_RcsFileMessage_Contents"></a>

 ** FileUrl **   <a name="pinpoint-Type-RcsFileMessage-FileUrl"></a>
The S3 URI of the media file to send, in the format `s3://bucket-name/key`. The service downloads the file from your S3 bucket, rehosts it, and generates a presigned URL for the aggregator. Maximum 2000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(https://|s3://).+`
Required: Yes

 ** ThumbnailUrl **   <a name="pinpoint-Type-RcsFileMessage-ThumbnailUrl"></a>
The S3 URI of an optional thumbnail image for the media file, in the format `s3://bucket-name/key`. Maximum 2000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(https://|s3://).+`
Required: No

## See Also
<a name="API_RcsFileMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsFileMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsFileMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsFileMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
