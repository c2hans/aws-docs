---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_NdiMediaInfo.html
---

# NdiMediaInfo
<a name="API_NdiMediaInfo"></a>

 Metadata about the audio and video media that is part of the NDI® source content. This includes details about the individual media streams.

## Contents
<a name="API_NdiMediaInfo_Contents"></a>

 ** streams **   <a name="mediaconnect-Type-NdiMediaInfo-streams"></a>
 A list of the individual media streams that make up the NDI source. This includes details about each stream's codec, resolution, frame rate, audio channels, and other parameters.
Type: Array of [NdiMediaStreamInfo](API_NdiMediaStreamInfo.md) objects
Required: Yes

## See Also
<a name="API_NdiMediaInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/NdiMediaInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/NdiMediaInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/NdiMediaInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
