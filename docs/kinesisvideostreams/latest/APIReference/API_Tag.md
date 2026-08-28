---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A key and value pair that is associated with the specified signaling channel.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="KinesisVideo-Type-Tag-Key"></a>
The key of the tag that is associated with the specified signaling channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Value **   <a name="KinesisVideo-Type-Tag-Value"></a>
The value of the tag that is associated with the specified signaling channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
