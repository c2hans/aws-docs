---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_MediaExtractionConfiguration.html
---

# MediaExtractionConfiguration
<a name="API_MediaExtractionConfiguration"></a>

The configuration for extracting information from media in documents.

## Contents
<a name="API_MediaExtractionConfiguration_Contents"></a>

 ** audioExtractionConfiguration **   <a name="qbusiness-Type-MediaExtractionConfiguration-audioExtractionConfiguration"></a>
Configuration settings for extracting and processing audio content from media files.
Type: [AudioExtractionConfiguration](API_AudioExtractionConfiguration.md) object
Required: No

 ** imageExtractionConfiguration **   <a name="qbusiness-Type-MediaExtractionConfiguration-imageExtractionConfiguration"></a>
The configuration for extracting semantic meaning from images in documents. For more information, see [Extracting semantic meaning from images and visuals](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html).
Type: [ImageExtractionConfiguration](API_ImageExtractionConfiguration.md) object
Required: No

 ** videoExtractionConfiguration **   <a name="qbusiness-Type-MediaExtractionConfiguration-videoExtractionConfiguration"></a>
Configuration settings for extracting and processing video content from media files.
Type: [VideoExtractionConfiguration](API_VideoExtractionConfiguration.md) object
Required: No

## See Also
<a name="API_MediaExtractionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/MediaExtractionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/MediaExtractionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/MediaExtractionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
