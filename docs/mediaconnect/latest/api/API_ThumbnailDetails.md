---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ThumbnailDetails.html
---

# ThumbnailDetails
<a name="API_ThumbnailDetails"></a>

 The details of the thumbnail, including thumbnail base64 string, timecode and the time when thumbnail was generated.

## Contents
<a name="API_ThumbnailDetails_Contents"></a>

 ** flowArn **   <a name="mediaconnect-Type-ThumbnailDetails-flowArn"></a>
 The ARN of the flow that DescribeFlowSourceThumbnail was performed on.
Type: String
Required: Yes

 ** thumbnailMessages **   <a name="mediaconnect-Type-ThumbnailDetails-thumbnailMessages"></a>
 Status code and messages about the flow source thumbnail.
Type: Array of [MessageDetail](API_MessageDetail.md) objects
Required: Yes

 ** thumbnail **   <a name="mediaconnect-Type-ThumbnailDetails-thumbnail"></a>
Thumbnail Base64 string.
Type: String
Required: No

 ** timecode **   <a name="mediaconnect-Type-ThumbnailDetails-timecode"></a>
 Timecode of thumbnail.
Type: String
Required: No

 ** timestamp **   <a name="mediaconnect-Type-ThumbnailDetails-timestamp"></a>
 The timestamp of when thumbnail was generated.
Type: Timestamp
Required: No

## See Also
<a name="API_ThumbnailDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ThumbnailDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ThumbnailDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ThumbnailDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
