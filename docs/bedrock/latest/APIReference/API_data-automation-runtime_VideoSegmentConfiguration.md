---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_VideoSegmentConfiguration.html
---

# VideoSegmentConfiguration
<a name="API_data-automation-runtime_VideoSegmentConfiguration"></a>

Used to set your start and end timestamp for what portion of a video you'd like to detect. The minimum segement length is 5 minutes.

## Contents
<a name="API_data-automation-runtime_VideoSegmentConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** timestampSegment **   <a name="bedrock-Type-data-automation-runtime_VideoSegmentConfiguration-timestampSegment"></a>
Holds the timestamps for the beginning and end of your video segment.
Type: [TimestampSegment](API_data-automation-runtime_TimestampSegment.md) object
Required: No

## See Also
<a name="API_data-automation-runtime_VideoSegmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/VideoSegmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/VideoSegmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/VideoSegmentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
