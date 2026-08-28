---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_HorizontalLayoutConfiguration.html
---

# HorizontalLayoutConfiguration
<a name="API_media-pipelines-chime_HorizontalLayoutConfiguration"></a>

Defines the configuration settings for the horizontal layout.

## Contents
<a name="API_media-pipelines-chime_HorizontalLayoutConfiguration_Contents"></a>

 ** TileAspectRatio **   <a name="chimesdk-Type-media-pipelines-chime_HorizontalLayoutConfiguration-TileAspectRatio"></a>
Specifies the aspect ratio of all video tiles.
Type: String
Pattern: `^\d{1,2}\/\d{1,2}$`
Required: No

 ** TileCount **   <a name="chimesdk-Type-media-pipelines-chime_HorizontalLayoutConfiguration-TileCount"></a>
The maximum number of video tiles to display.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** TileOrder **   <a name="chimesdk-Type-media-pipelines-chime_HorizontalLayoutConfiguration-TileOrder"></a>
Sets the automatic ordering of the video tiles.
Type: String
Valid Values: `JoinSequence | SpeakerSequence`
Required: No

 ** TilePosition **   <a name="chimesdk-Type-media-pipelines-chime_HorizontalLayoutConfiguration-TilePosition"></a>
Sets the position of horizontal tiles.
Type: String
Valid Values: `Top | Bottom`
Required: No

## See Also
<a name="API_media-pipelines-chime_HorizontalLayoutConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/HorizontalLayoutConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/HorizontalLayoutConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/HorizontalLayoutConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
