---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputThumbnailDetails.html
---

# RouterInputThumbnailDetails
<a name="API_RouterInputThumbnailDetails"></a>

The details of a thumbnail associated with a router input, including the thumbnail messages, the thumbnail image, the timecode, and the timestamp.

## Contents
<a name="API_RouterInputThumbnailDetails_Contents"></a>

 ** thumbnailMessages **   <a name="mediaconnect-Type-RouterInputThumbnailDetails-thumbnailMessages"></a>
The messages associated with the router input thumbnail.
Type: Array of [RouterInputMessage](API_RouterInputMessage.md) objects
Required: Yes

 ** thumbnail **   <a name="mediaconnect-Type-RouterInputThumbnailDetails-thumbnail"></a>
The thumbnail image, encoded as a Base64-encoded binary data object.
Type: Base64-encoded binary data object
Required: No

 ** timecode **   <a name="mediaconnect-Type-RouterInputThumbnailDetails-timecode"></a>
The timecode associated with the thumbnail.
Type: String
Required: No

 ** timestamp **   <a name="mediaconnect-Type-RouterInputThumbnailDetails-timestamp"></a>
The timestamp associated with the thumbnail.
Type: Timestamp
Required: No

## See Also
<a name="API_RouterInputThumbnailDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputThumbnailDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputThumbnailDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputThumbnailDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
