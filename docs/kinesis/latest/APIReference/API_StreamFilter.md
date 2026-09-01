---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StreamFilter.html
---

# StreamFilter
<a name="API_StreamFilter"></a>

Filters [ListChannels](API_ListChannels.md) results by source stream.

## Contents
<a name="API_StreamFilter_Contents"></a>

 ** StreamARN **   <a name="Streams-Type-StreamFilter-StreamARN"></a>
The Amazon Resource Name (ARN) of the source stream to filter by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** StreamCreationTimestamp **   <a name="Streams-Type-StreamFilter-StreamCreationTimestamp"></a>
The creation timestamp of the source stream.
Type: Timestamp
Required: No

## See Also
<a name="API_StreamFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/StreamFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/StreamFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/StreamFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
