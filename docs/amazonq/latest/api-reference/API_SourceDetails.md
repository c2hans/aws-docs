---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SourceDetails.html
---

# SourceDetails
<a name="API_SourceDetails"></a>

Container for details about different types of media sources (image, audio, or video).

## Contents
<a name="API_SourceDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** audioSourceDetails **   <a name="qbusiness-Type-SourceDetails-audioSourceDetails"></a>
Details specific to audio content within the source.
Type: [AudioSourceDetails](API_AudioSourceDetails.md) object
Required: No

 ** imageSourceDetails **   <a name="qbusiness-Type-SourceDetails-imageSourceDetails"></a>
Details specific to image content within the source.
Type: [ImageSourceDetails](API_ImageSourceDetails.md) object
Required: No

 ** videoSourceDetails **   <a name="qbusiness-Type-SourceDetails-videoSourceDetails"></a>
Details specific to video content within the source.
Type: [VideoSourceDetails](API_VideoSourceDetails.md) object
Required: No

## See Also
<a name="API_SourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/SourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/SourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/SourceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
